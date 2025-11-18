from flask import make_response
from services.mock_repository import MockRepository
from services.mock_engine import MockEngine

class MockController:

    def __init__(self):
        self.repo = MockRepository()
        self.engine = MockEngine()

    def handle_request(self, endpoint, flask_request):
        endpoint = "/" + endpoint

        mocks = self.repo.list_mocks()

        for mock in mocks:
            if self.engine.match_mock(mock, endpoint, flask_request):
                return self._build_response(mock)

        return make_response({"error": "No mock matched"}, 404)

    def _build_response(self, mock):
        resp = make_response(mock.get("response"), mock.get("status_code", 200))

        for k, v in mock.get("headers", {}).items():
            resp.headers[k] = v

        if "delay" in mock:
            import time
            time.sleep(mock["delay"])

        return resp
