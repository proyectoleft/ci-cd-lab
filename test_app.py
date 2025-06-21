import unittest
import app

class TestApp(unittest.TestCase):
    def test_output(self):
        self.assertEqual(app.main(), "Hola desde la app de CI/CD")

if __name__ == '__main__':
    unittest.main()
