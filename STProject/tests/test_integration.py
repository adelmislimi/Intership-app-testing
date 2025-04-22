import unittest
from app import create_app, db
from app.models import Internship

class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Setup a test app with in-memory SQLite
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_post_and_fetch_internship(self):
        # Post a new internship
        response = self.client.post('/internships', json={
            'title': 'Backend Intern',
            'description': 'Work with Flask APIs.'
        })
        self.assertEqual(response.status_code, 201)

        # Get internships
        response = self.client.get('/internships')
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Backend Intern')

if __name__ == '__main__':
    unittest.main()
