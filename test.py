from fastapi.testclient import TestClient
from main import app
from utils import (
    welcome,
    simple_calculation
    )

class UtilsEndpointsTestCase():
    
    def setUp(self):
        self.client = TestClient(app)
        self.message = None
        self.result = None
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_welcome_message(self):
        pass
    
    def test_simple_calculation(self):
        pass

    def test_index_endpoint(self):
        pass

    def test_welcome_endpoint(self):
        pass

    def test_simple_calculation_endpoint(self):
        pass


if __name__ == '__main__':
    unittest.main()