import unittest
from backend.services.forecasting_service import ForecastingService
class TestForecastingService(unittest.TestCase):
    def setUp(self):
        self.service = ForecastingService("property_A")

    def test_forecast_lengths(self):
        months = 6
        self.assertEqual(len(self.service.forecast_revenue(months)), months)
        self.assertEqual(len(self.service.forecast_expenses(months)), months)
        self.assertEqual(len(self.service.forecast_noi(months)), months)

    def test_forecast_non_negative(self):
        rev = self.service.forecast_revenue()
        exp = self.service.forecast_expenses()
        noi = self.service.forecast_noi()
        for val in rev + exp + noi:
            self.assertGreaterEqual(val, 0)
