import re

class MockEngine:

    def match_mock(self, mock, endpoint, flask_request):

        mock_url = mock["url"]

        if mock.get("use_regex", False):
            if not re.fullmatch(mock_url, endpoint):
                return False
        else:
            if mock_url != endpoint:
                return False

        if mock.get("match_method", True):
            if mock["method"] != flask_request.method:
                return False

        if mock.get("match_query", False):
            if mock.get("query_params") != flask_request.args.to_dict():
                return False

        if mock.get("match_body", False):
            if mock.get("body") != flask_request.get_json(silent=True):
                return False

        return True
