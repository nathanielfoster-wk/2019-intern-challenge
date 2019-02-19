const fs = require('fs');

module.exports = {
    loadUsers,
    generateEfficiencyReport
}

function loadUsers (filepath) {
    const text = fs.readFileSync(filepath, 'utf8'); 
    const lines = text.split('\r\n');
    const fields = lines.shift().split(',');
    const users = [];

    for (let i = 0; i < lines.length; i++) {
        let data = lines[i].split(',');
        let user = {};
        for (let j = 0; j < fields.length; j++) {
            user[fields[j]] = data[j];
        }
        users.push(user);
    }
    
    return users;
}

function generateEfficiencyReport (users) {
    const regionEfficiency = {};

    users.forEach

    for (let i = 0; i < users.length; i++) {
        let user = users[i];

        if (user.region_id === 1) {
            user.region = 'East'
        }

        if (user.region_id === 2) {
            user.region = 'Central'
        }

        if (user.region_id === 3) {
            user.region = 'West'
        }
        
        if (regionEfficiency.hasOwnProperty(user.region_id)) {
            regionEfficiency[user.region_id].region = user.region
            regionEfficiency[user.region_id].user_count += 1
            regionEfficiency[user.region_id].time_taken += user.time_taken
            regionEfficiency[user.region_id].tasks_completed += user.tasks_completed
            regionEfficiency[user.region_id].efficiency += user.time_taken / user.tasks_completed
        } else {
            regionEfficiency[user.region_id] = {}
            regionEfficiency[user.region_id].region = user.region
            regionEfficiency[user.region_id].usrr_count = 1
            regionEfficiency[user.region_id].time_taken = user.time_taken
            regionEfficiency[user.region_id].tasks_completed = user.tasks_completed
            regionEfficiency[user.region_id].efficiency = user.time_taken / user.tasks_completed
        }
    }

    console.log(regionEfficiency)
    const keys = Object.keys(regionEfficiency);

    for (let i = 0; i < keys.length; i++) {
        const region_id = keys[i];
        
        regionEfficiency[region_id].efficiency = regionEfficiency[region_id].efficiency /
                                                 regionEfficiency[region_id].user_count;
    }

    let mostEfficientRegion = null;
    let leastEfficientRegion = null;

    for (let i = 0; i < keys.length; i++) {
        const region_id = keys[i];

        if (mostEfficientRegion === null) {
            mostEfficientRegion = regionEfficiency[region_id];
        } else {
            if (regionEfficiency[region_id].efficiency < mostEfficientRegion.efficiency) {
                mostEfficientRegion = regionEfficiency[region_id];
            }
        }

        if (leastEfficientRegion === null) {
            leastEfficientRegion = regionEfficiency[region_id];
        } else {
            if (regionEfficiency[region_id].efficiency > leastEfficientRegion.efficiency) {
                leastEfficientRegion = regionEfficiency[region_id];
            }
        }
    }

    return {
        leastEfficientRegion,
        mostEfficientRegion
    }
}