from flask import Flask, request
from controllers.mock_controller import MockController

app = Flask(__name__)
controller = MockController()

@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def mock_handler(path):
    return controller.handle_request(path, request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True, threaded=True)
