import unittest
from unittest.mock import patch, MagicMock
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch("app.routes.Internship.query")
    def test_get_internships(self, mock_query):
        mock_internship = MagicMock()
        mock_internship.id = 1
        mock_internship.title = "Backend Dev"
        mock_internship.description = "Build APIs"
        mock_query.all.return_value = [mock_internship]

        response = self.client.get('/internships')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Backend Dev', response.data)

    @patch("app.routes.db")
    def test_post_internship(self, mock_db):
        response = self.client.post('/internships', json={
            "title": "Frontend Dev",
            "description": "ReactJS and Tailwind"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Internship posted', response.data)

    @patch("app.routes.db")
    def test_apply(self, mock_db):
        response = self.client.post('/apply', json={
            "student_name": "Adel",
            "internship_id": 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Application submitted', response.data)

if __name__ == "__main__":
    unittest.main()
