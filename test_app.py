import unittest
import app

class TestApp(unittest.TestCase):
    def test_output(self):
        self.assertIsNone(app.main())  # Verifica que main() no retorne nada

if __name__ == '__main__':
    unittest.main()
