import unittest

from challenge import load_users, generate_efficiency_report


class ChallengeTest(unittest.TestCase):
    def test_load_users(self):
        users = load_users('../input.csv')
        self.assertEquals(users[0]['id'], 1111)

    def test_region(self):
        users = load_users('../input.csv')
        most_efficient, least_efficient = generate_efficiency_report(users)

        most_efficient_expected = {
            'efficiency': 14,
            'region': 'East',
            'user_count': 2,
            'time_taken': 700,
            'tasks_completed': 25
        }
        self.assertEquals(most_efficient, most_efficient_expected)

        least_efficient_expected = {
            'efficiency': 18,
            'region': 'Central',
            'tasks_completed': 25,
            'time_taken': 900,
            'user_count': 2
        }
        self.assertEquals(least_efficient, least_efficient_expected)
