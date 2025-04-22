import unittest
from app.models import Internship, Application

class TestModels(unittest.TestCase):

    def test_create_internship(self):
        internship = Internship(title="Software Intern", description="Learn real dev skills.")
        self.assertEqual(internship.title, "Software Intern")
        self.assertEqual(internship.description, "Learn real dev skills.")

    def test_create_application(self):
        application = Application(student_name="John Doe", internship_id=1)
        self.assertEqual(application.student_name, "John Doe")
        self.assertEqual(application.internship_id, 1)

if __name__ == '__main__':
    unittest.main()
