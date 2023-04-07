try:
    from app import app
    import unittest
except Exception as e:
    print("Modules are missing.", e)


class Flask_tests(unittest.TestCase):

    def test_flask_endpoint_list_available_moves_code_200(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/rook/h1")
        status_code = response.status_code
        self.assertEqual(200, status_code)

    def test_flask_endpoint_list_available_moves_code_404(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/rookie/h1")
        status_code = response.status_code
        self.assertEqual(404, status_code)

    def test_flask_endpoint_list_available_moves_code_409(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/rook/h")
        status_code = response.status_code
        self.assertEqual(409, status_code)

    def test_flask_endpoint_validate_move_code_200(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/rook/h1/h2")
        status_code = response.status_code
        self.assertEqual(200, status_code)

    def test_flask_endpoint_validate_move_code_404(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/rookie/h1")
        status_code = response.status_code
        self.assertEqual(404, status_code)

    def test_flask_endpoint_list_validate_move_code_409(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/rook/h1/g")
        status_code = response.status_code
        self.assertEqual(409, status_code)


if __name__ == "__main__":
    unittest.main()
