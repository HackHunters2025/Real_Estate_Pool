import unittest
from backend.services.occupancy_service import OccupancyService 

class TestOccupancyService(unittest.TestCase):
    def setUp(self):
        self.service = OccupancyService("property_A")

    def test_forecast_output(self):
        forecast = self.service.forecast_occupancy(3)
        self.assertEqual(len(forecast), 3)
        for val in forecast:
            self.assertTrue(0.0 <= val <= 1.0)

    def test_type_consistency(self):
        forecast = self.service.forecast_occupancy()
        self.assertTrue(all(isinstance(val, float) for val in forecast))
