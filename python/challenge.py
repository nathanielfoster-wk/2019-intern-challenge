import csv


def load_users(filepath):
    users = []

    with open(filepath, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)

    return users


def generate_efficiency_report(users):
    region_efficiency = {}

    for user in users:
        if user['region_id'] == 1:
            user['region'] = 'East'

        if user['region_id'] == 2:
            user['region'] = 'Central'

        if user['region_id'] == 3:
            user['region'] = 'West'

        if user['region_id'] in region_efficiency:
            region_efficiency[user['region_id']]['region'] = user['region']
            region_efficiency[user['region_id']]['user_count'] += 1
            region_efficiency[user['region_id']]['time_taken'] += user['time_taken']
            region_efficiency[user['region_id']]['tasks_completed'] += user['tasks_completed']
            region_efficiency[user['region_id']]['efficiency'] += user['time_taken'] / user['tasks_completed']
        else:
            region_efficiency[user['region_id']] = {}
            region_efficiency[user['region_id']]['region'] = user['region']
            region_efficiency[user['region_id']]['usrr_count'] = 1
            region_efficiency[user['region_id']]['time_taken'] = user['time_taken']
            region_efficiency[user['region_id']]['tasks_completed'] = user['tasks_completed']
            region_efficiency[user['region_id']]['efficiency'] = user['time_taken'] / user['tasks_completed']

    for region in region_efficiency:
        region_efficiency[region]['efficiency'] = (region_efficiency[region]['efficiency']
                                                   / region_efficiency[region]['user_count'])

    most_efficient_region = None
    least_efficient_region = None

    for region in region_efficiency:
        if most_efficient_region is None:
            most_efficient_region = region_efficiency[region]
        else:
            if region_efficiency[region]['efficiency'] < most_efficient_region['efficiency']:
                most_efficient_region = region_efficiency[region]

        if least_efficient_region is None:
            least_efficient_region = region_efficiency[region]
        else:
            if region_efficiency[region]['efficiency'] > least_efficient_region['efficiency']:
                least_efficient_region = region_efficiency[region]

    return most_efficient_region, least_efficient_region
