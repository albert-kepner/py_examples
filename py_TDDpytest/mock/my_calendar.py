from datetime import datetime
from unittest.mock import Mock

tuesday = datetime(year=2019, month=1, day=1)
saturday = datetime(year=2019, month=1, day=5)

datetime = Mock()

def is_weekday():
    today = datetime.today()
    day_of_week = today.weekday()
    # 0 Monday, 6 Sunday
    return (0 <= day_of_week < 5)


datetime.today.return_value = tuesday


assert is_weekday()

import requests
import unittest
from requests.exceptions import ConnectionError

requests = Mock()

def get_holidays():
    r = requests.get('http://xxxlocalhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestGetHolidays(unittest.TestCase):
    def test_get_holidays_connection(self):
        requests.get.side_effect = ConnectionError
        with self.assertRaises(ConnectionError):
            get_holidays()


if __name__ == '__main__':
    unittest.main()

