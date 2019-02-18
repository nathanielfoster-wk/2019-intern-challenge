import unittest

from challenge import generate_efficiency_report

users = [
    {
    'id': 1111,
    'region_id': 1,
    'tasks_completed': 10,
    'time_taken': 500
    },
    {
    'id': 1112,
    'region_id': 1,
    'tasks_completed': 15,
    'time_taken': 200
    },
    {
    'id': 1113,
    'region_id': 2,
    'tasks_completed': 5,
    'time_taken': 300
    },
    {
    'id': 1114,
    'region_id': 2,
    'tasks_completed': 20,
    'time_taken': 600
    },
    {
    'id': 1115,
    'region_id': 3,
    'tasks_completed': 12,
    'time_taken': 300
    },
    {
    'id': 1116,
    'region_id': 3,
    'tasks_completed': 18,
    'time_taken': 650
    }
]


class ChallengeTest(unittest.TestCase):
    def test_region(self):
        region = generate_efficiency_report(users)
        self.assertEquals(region['region'], 'East')