const { assert } = require('chai');
const { loadUsers, generateEfficiencyReport } = require('./challenge.js')

describe('challenge functionality', function() {
    it('should load users from csv file', function() {
        const users = loadUsers('./input.csv');

        assert.equal(users[0].id, 1111)
    })

    it('should generate a report of most efficient and least efficient regions', function () {
        const users = loadUsers('./input.csv');
        const report = generateEfficiencyReport(users);

        mostEfficientExpected = {
            'efficiency': 14,
            'region': 'East',
            'user_count': 2,
            'time_taken': 700,
            'tasks_completed': 25
        }

        assert.deepEqual(report.mostEfficientRegion, mostEfficientExpected);

        leastEfficientExpected = {
            'efficiency': 18,
            'region': 'Central',
            'tasks_completed': 25,
            'time_taken': 900,
            'user_count': 2
        }
        assert.deepEqual(report.leastEfficientRegion, leastEfficientExpected);
    })
})