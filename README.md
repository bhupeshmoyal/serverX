# serverX

A lightweight Flask-based mock server for testing API integrations without relying on external services.

## Features

- **Easy Mock Configuration**: Define mocks using simple JSON files
- **Flexible Matching**: Support for URL matching, HTTP methods, query parameters, and request bodies
- **Regex Support**: Use regular expressions for URL pattern matching
- **Custom Responses**: Define custom status codes, headers, and response bodies
- **Request Delays**: Simulate network latency with configurable delays

## Project Structure

```
.
├── server.py                 # Main Flask application
├── controllers/
│   └── mock_controller.py   # Request handling and routing
├── services/
│   ├── mock_engine.py       # Mock matching logic
│   └── mock_repository.py   # Mock data loading
└── mock_data/               # Mock definitions (JSON files)
    ├── getTemperature.json
    ├── getUser.json
    ├── login.json
    └── userRegisteration.json
```

## Installation

1. Clone or download this project
2. Install Flask:
   ```bash
   pip install flask
   ```

## Usage

### Starting the Server

```bash
python server.py
```

The server will start on `http://0.0.0.0:5002` and accept requests on all routes.

### Defining Mocks

Create a JSON file in the `mock_data/` directory with the following structure:

```json
{
    "url": "/api/example",
    "method": "GET",
    "match_method": false,
    "use_regex": false,
    "match_query": false,
    "match_body": false,
    "status_code": 200,
    "headers": {
        "Content-Type": "application/json"
    },
    "response": {
        "message": "success"
    },
    "delay": 0.5
}
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `url` | string | - | The endpoint URL to match |
| `method` | string | - | HTTP method (GET, POST, PUT, DELETE, PATCH) |
| `match_method` | boolean | true | Whether to match the HTTP method |
| `use_regex` | boolean | false | Use regex for URL matching |
| `match_query` | boolean | false | Match query parameters exactly |
| `match_body` | boolean | false | Match request body exactly |
| `status_code` | number | 200 | HTTP response status code |
| `headers` | object | {} | Custom response headers |
| `response` | object/string | - | Response body |
| `delay` | number | - | Delay in seconds before responding |

### Examples

**Simple GET endpoint:**
```json
{
    "url": "/api/getUser",
    "method": "GET",
    "match_method": false,
    "status_code": 200,
    "headers": {"Content-Type": "application/json"},
    "response": {"id": 101, "name": "Bhupesh"}
}
```

**With regex pattern matching:**
```json
{
    "url": "/api/users/.*",
    "method": "GET",
    "use_regex": true,
    "status_code": 200,
    "response": {"user": "data"}
}
```

**With simulated delay:**
```json
{
    "url": "/api/slow-endpoint",
    "method": "POST",
    "delay": 2.5,
    "status_code": 201,
    "response": {"status": "created"}
}
```

## Testing

Make requests to the mock server:

```bash
# GET request
curl http://localhost:5002/api/getUser

# POST request
curl -X POST http://localhost:5002/api/login

# GET with query parameters
curl http://localhost:5002/api/search?query=test
```

## How It Works

1. **Server** ([server.py](server.py)) - Receives all incoming requests
2. **Controller** ([controllers/mock_controller.py](controllers/mock_controller.py)) - Routes requests to the matching handler
3. **Engine** ([services/mock_engine.py](services/mock_engine.py)) - Matches requests against defined mocks
4. **Repository** ([services/mock_repository.py](services/mock_repository.py)) - Loads and caches mock definitions from JSON files

## Troubleshooting

- **No mock matched**: Ensure your mock URL and configuration match the incoming request
- **Port already in use**: Change the port in [server.py](server.py) line 9
- **JSON parsing error**: Validate your mock JSON files for syntax errors
