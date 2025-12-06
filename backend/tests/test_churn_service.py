# tests/test_churn_service.py

import unittest
from backend.services.churn_service import ChurnService


class TestChurnService(unittest.TestCase):
    def setUp(self):
        self.service = ChurnService("property_A")

    def test_model_runs(self):
        result = self.service.run()
        self.assertIn("churn_score", result)
        self.assertIn("risk_level", result)
        self.assertIn("top_factors", result)
        self.assertGreaterEqual(result["churn_score"], 0.0)
        self.assertLessEqual(result["churn_score"], 1.0)

    def test_predict_churn_range(self):
        scores = self.service.predict_churn()
        self.assertEqual(len(scores), len(self.service.data))
        for score in scores:
            self.assertTrue(0.0 <= score <= 1.0)
