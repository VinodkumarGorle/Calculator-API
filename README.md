# Calculator API

This is a FastAPI-based calculator API that supports basic arithmetic operations such as addition and subtraction.

## Features

- FastAPI application with built-in validation
- Handles CORS for cross-origin requests
- Custom error handling for invalid inputs
- Returns structured JSON responses

## Endpoint

### POST `/calculate`

**Request Body:**
```
{
  "num1": 10.5,
  "num2": 4.2,
  "process": "add"  // or "sub"
}
```

**Response (Success):**
```
{
  "Status": [{"MessageCode": "S", "MessageText": "OK"}],
  "ReturnData": [{"addition": 14.7}],
  "DevelopedBy": "Vinod Kumar"
}
```

**Response (Error):**
```
{
  "Status": [{"MessageCode": "E", "MessageText": "Invalid process type. Use 'add' or 'sub'."}],
  "ReturnData": [],
  "DevelopedBy ": "Vinod Kumar"
}
```

## Error Handling

Returns appropriate error responses for invalid data types or missing fields.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VinodkumarGorle/Calculator-API.git
cd Calculator-API
```

2. Install dependencies:
```bash
pip install fastapi uvicorn
```

3. Run the application:
```bash
uvicorn app:app --reload
```

## Developed By

**Vinod Kumar**
