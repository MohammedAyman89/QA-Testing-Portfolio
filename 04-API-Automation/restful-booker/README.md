# RESTful-Booker — API Automation Testing Project

Automated testing of the [RESTful-Booker](https://restful-booker.herokuapp.com) API using Python, Requests, and Pytest. Covers full CRUD operations, authentication, and negative scenarios with intentional bug detection.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Programming language |
| Requests | HTTP client for API calls |
| Pytest | Test framework |
| pytest-html | HTML report generation |

---

## Project Structure

```
restful-booker/
├── tests/
│   ├── conftest.py                # Pytest fixtures (auth, booking creation, failure logging)
│   ├── test_health.py             # Health check (1 test)
│   ├── test_get_booking.py        # GET endpoints (2 tests)
│   ├── test_create_booking.py     # POST endpoint (3 tests)
│   ├── test_update_booking.py     # PUT endpoint (2 tests)
│   ├── test_partial_update_booking.py # PATCH endpoint (3 tests)
│   ├── test_delete_booking.py     # DELETE endpoint (2 tests)
│   └── test_negative.py          # Negative & bug tests (9 tests)
├── config.py                      # Base URL, auth credentials, sample payload
├── pytest.ini                     # Pytest markers (smoke, regression, negative)
├── requirements.txt               # Project dependencies
└── README.md
```

---

## Test Coverage

### Health Check (1 test)
| Test Case | Type |
|-----------|------|
| API ping returns 201 | Smoke |

### GET Booking (2 tests)
| Test Case | Type |
|-----------|------|
| Get all booking IDs returns list with bookingid | Regression |
| Get single booking returns all fields | Regression |

### Create Booking (3 tests)
| Test Case | Type |
|-----------|------|
| Create booking with full payload, verify all fields | Smoke |
| Create booking without optional field (additionalneeds) | Regression |
| Create booking dates match input | Regression |

### Update Booking — PUT (2 tests)
| Test Case | Type |
|-----------|------|
| Full update changes reflected in response | Regression |
| Full update returns all 6 fields | Regression |

### Partial Update Booking — PATCH (3 tests)
| Test Case | Type |
|-----------|------|
| Update only firstname | Regression |
| Update only additionalneeds | Regression |
| Update only totalprice | Regression |

### Delete Booking (2 tests)
| Test Case | Type |
|-----------|------|
| Delete booking returns 201 | Smoke |
| Deleted booking returns 404 on GET | Regression |

### Negative Tests & Bug Detection (9 tests)
| Test Case | Expected | Actual | Bug |
|-----------|----------|--------|-----|
| Get booking with invalid ID | 404 | 404 | — |
| Create without firstname | 400 | 500 | Server crash |
| Create without lastname | 400 | 500 | Server crash |
| Create without totalprice | 400 | 500 | Server crash |
| Create without bookingdates | 400 | 500 | Server crash |
| PUT/PATCH/DELETE without auth | 403 | 403 | — |
| Update non-existent booking | 404 | 405 | Wrong error code |
| Delete non-existent booking | 404 | 405 | Wrong error code |
| Auth with wrong credentials | 401 | 200 | Success code for failure |
| Auth with wrong username | 401 | 200 | Success code for failure |

**Total: 22 test cases | 3 bugs identified**

---

## Bugs Found

### Bug 1: Missing Required Fields Return 500 Instead of 400
- **Endpoint:** POST `/booking`
- **Expected:** 400 Bad Request when required fields (firstname, lastname, totalprice, bookingdates) are missing
- **Actual:** 500 Internal Server Error — the server crashes instead of validating input
- **Severity:** Medium

### Bug 2: Invalid Credentials Return 200 Instead of 401
- **Endpoint:** POST `/auth`
- **Expected:** 401 Unauthorized when username or password is incorrect
- **Actual:** 200 OK with `"reason": "Bad credentials"` in the response body
- **Severity:** High — a success status code for a failed operation can mislead clients and monitoring tools

### Bug 3: Non-Existent Booking Returns 405 Instead of 404
- **Endpoint:** PUT/DELETE `/booking/999999`
- **Expected:** 404 Not Found when the booking doesn't exist
- **Actual:** 405 Method Not Allowed
- **Severity:** Low — incorrect error code but still blocks the operation

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest tests/ -v
```

### Run by marker
```bash
pytest -m smoke -v          # Critical tests only
pytest -m regression -v     # Full test suite
pytest -m negative -v       # Error/edge case tests only
```

### Generate HTML report
```bash
pytest tests/ -v --html=report.html
```

---

## Key Features

- **Centralized Configuration** — base URL, credentials, and payload in `config.py`
- **Pytest Fixtures** — `auth_token`, `auth_headers`, and `create_booking` with automatic teardown
- **Parametrized Tests** — missing fields, auth methods, and invalid credentials use `@pytest.mark.parametrize`
- **Failure Logging** — automatically saves request/response details to `failure_logs/` when tests fail
- **Test Markers** — `smoke`, `regression`, and `negative` markers for flexible test execution
- **Bug Documentation** — negative tests assert correct HTTP behavior, failures prove bugs exist

---

## Skills Demonstrated

- REST API testing with Python Requests
- Pytest fixtures, markers, and parametrize
- HTTP status code validation (200, 201, 400, 401, 403, 404, 405, 500)
- Positive and negative test scenario design
- Authentication token management
- Bug detection and documentation
- HTML test reporting
