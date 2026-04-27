# Saucedemo — Selenium Automation Testing Project

Automated testing of the [Swag Labs](https://www.saucedemo.com) e-commerce application using Python, Selenium WebDriver, and Pytest. Covers the full user flow from login to checkout with positive and negative test scenarios.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML report generation |
| Page Object Model | Design pattern |

---

## Project Structure

```
saucedemo/
├── pages/
│   ├── login_page.py          # Login page object
│   ├── Inventory_Page.py      # Inventory page object
│   ├── cart_page.py           # Cart page object
│   └── checkout_page.py       # Checkout page object
├── tests/
│   ├── conftest.py            # Pytest fixtures & screenshot hook
│   ├── test_login.py          # Login tests (8 scenarios)
│   ├── test_inventory.py      # Inventory tests (3 scenarios)
│   ├── test_cart.py           # Cart tests (3 scenarios)
│   └── test_checkout.py       # Checkout tests (4 scenarios)
├── utils/
│   └── driver_factory.py      # Browser setup & configuration
├── pytest.ini                 # Pytest configuration & markers
├── requirements.txt           # Project dependencies
└── README.md
```

---

## Test Coverage

### Login (8 tests)
| Test Case | Type |
|-----------|------|
| Valid login with standard_user | Smoke |
| Wrong password | Negative |
| Wrong username | Negative |
| Empty username | Negative |
| Empty password | Negative |
| Locked out user | Negative |
| Username with trailing space | Negative |
| SQL injection attempt | Negative |

### Inventory (3 tests)
| Test Case | Type |
|-----------|------|
| Verify all 6 product names | Regression |
| Add 2 products to cart | Regression |
| Open cart and verify title | Regression |

### Cart (3 tests)
| Test Case | Type |
|-----------|------|
| Verify item appears in cart | Regression |
| Remove one item from cart | Regression |
| Proceed to checkout | Regression |

### Checkout (4 tests)
| Test Case | Type |
|-----------|------|
| Full checkout flow (login to order complete) | Smoke |
| All fields empty | Negative |
| Last name empty | Negative |
| Postal code empty | Negative |

**Total: 18 test cases**

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

- **Page Object Model** — each page has its own class with locators and methods, keeping tests clean and maintainable
- **Explicit Waits** — uses `WebDriverWait` instead of `time.sleep` for reliable test execution
- **Parameterized Tests** — login and checkout negative tests use `@pytest.mark.parametrize` to reduce duplication
- **Pytest Fixtures** — shared setup/teardown via `conftest.py` with a `logged_in_driver` fixture
- **Screenshot on Failure** — automatically captures a screenshot when any test fails
- **HTML Reports** — generates a visual test report with pass/fail status
- **Test Markers** — `smoke`, `regression`, and `negative` markers for flexible test execution
- **Driver Factory** — browser configuration separated into its own module

---

## Skills Demonstrated

- Selenium WebDriver automation
- Page Object Model design pattern
- Pytest fixtures, markers, and parametrize
- Explicit waits and expected conditions
- Positive and negative test scenario design
- Input validation testing (empty fields, SQL injection, trailing spaces)
- Test reporting and documentation
