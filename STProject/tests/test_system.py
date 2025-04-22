import unittest
from app import create_app, db
from app.models import Application

class TestSystem(unittest.TestCase):

    def setUp(self):
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

    def test_full_user_flow(self):
        # Step 1: Post internship
        post_res = self.client.post('/internships', json={
            'title': 'Frontend Intern',
            'description': 'React development'
        })
        self.assertEqual(post_res.status_code, 201)

        # Step 2: Get internship ID
        get_res = self.client.get('/internships')
        internship_id = get_res.get_json()[0]['id']

        # Step 3: Apply to internship
        apply_res = self.client.post('/apply', json={
            'student_name': 'Alice',
            'internship_id': internship_id
        })
        self.assertEqual(apply_res.status_code, 201)

        # Step 4: Check in DB directly (or you can add a GET /applications endpoint)
        with self.app.app_context():
            apps = Application.query.all()
            self.assertEqual(len(apps), 1)
            self.assertEqual(apps[0].student_name, 'Alice')

if __name__ == '__main__':
    unittest.main()
