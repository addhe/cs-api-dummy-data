import os
import unittest
from src.main import app
from unittest.mock import patch, MagicMock

class NasabahApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.api_key = os.environ.get("API_KEY")


    @patch("main.supabase")
    def test_get_nasabah_by_email(self, mock_supabase):
        # Mock chaining: select().filter().filter()...execute()
        mock_query = MagicMock()
        # Chaining select/filter
        mock_query.select.return_value = mock_query
        mock_query.filter.return_value = mock_query
        mock_query.execute.return_value = MagicMock(data=[{
            "id": 1,
            "nama": "Addhe Warman Putra",
            "email": "addhe.warman@outlook.co.id",
            "status": "aktif",
            "created_at": "2025-08-05T00:00:00Z"
        }])
        mock_supabase.table.return_value = mock_query

        response = self.app.get(
            "/nasabah?email=addhe.warman@outlook.co.id",
            headers={"x-api-key": self.api_key}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("data", data)
        self.assertEqual(data["data"][0]["email"], "addhe.warman@outlook.co.id")

    def test_unauthorized(self):
        response = self.app.get("/nasabah?email=addhe.warman@outlook.co.id")
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()
