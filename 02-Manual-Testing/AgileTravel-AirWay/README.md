# Agile Travel — Manual Testing Project

Manual testing of the [Agile Travel](https://travel.agileway.net) web application, a flight booking platform. Covers the full booking flow with positive and negative test scenarios, managed via JIRA and Zephyr Scale.

---

## Project Info

| Item | Details |
|------|---------|
| **Application** | Agile Travel — Flight Booking Platform |
| **URL** | https://travel.agileway.net |
| **Testing Type** | Manual Testing |
| **Test Management** | JIRA, Zephyr Scale |
| **Test Cycles** | 1 |
| **Total Test Cases** | 33 |
| **Bugs Found** | 10 |

---

## Test Coverage

### Test Cases Summary

| Category | Valid (Passed) | Invalid (Failed) | Total |
|----------|----------------|------------------|-------|
| Selecting Flight | 6 | 6 | 12 |
| Passenger Details | 5 | 5 | 10 |
| Payment Details | 5 | 6 | 11 |
| **Total** | **16** | **17** | **33** |

### Test Cycle Results — Valid Scenarios

![Valid Selecting Flight](./screenshots/Valid%20Selecting%20flight%20Scenarios.png)

![Valid Passenger Details](./screenshots/Valid%20Passengers%20Details.png)

![Valid Payment Details](./screenshots/Valid%20Payment%20Details.png)

### Test Cycle Results — Invalid Scenarios

![Invalid Selecting Flight](./screenshots/Invalid%20Selecting%20flight%20Scenarios.png)

![Invalid Passenger Details](./screenshots/Invalid%20Passengers%20Details.png)

![Invalid Payment Details](./screenshots/Invalid%20Payment%20Details.png)

---

## Bugs Found (10)

| ID | Summary | Priority | Area |
|----|---------|----------|------|
| MA-1 | User can't return back to Booking page after completing a booking | Highest | Booking |
| MA-2 | No error message when leaving 'From' or 'To' fields empty | High | Flight Selection |
| MA-3 | Last name field accepts numeric values instead of letters only | Medium | Passenger Details |
| MA-4 | Content aligned to top leaving excessive empty space (~80%) | Low | Responsive UI |
| MA-5 | Multiple flight selection allowed without validation | High | Flight Selection |
| MA-6 | Past departure date accepted without validation | Highest | Flight Booking |
| MA-7 | Same origin and destination allowed without validation | Highest | Flight Booking |
| MA-8 | Return date earlier than departure date accepted without validation | Medium | Flight Booking |
| MA-9 | Special characters accepted in card holder name | Low | Payment Details |
| MA-10 | Card number field accepts 24 digits (limit should be 16) | Medium | Payment Details |

### Bug Priority Breakdown

| Priority | Count |
|----------|-------|
| Highest | 3 |
| High | 2 |
| Medium | 3 |
| Low | 2 |

### Bug Area Distribution

| Area | Bugs |
|------|------|
| Flight Booking/Selection | 5 |
| Payment Details | 2 |
| Passenger Details | 1 |
| Responsive UI | 1 |
| Navigation | 1 |

---

## Files

| File | Description |
|------|-------------|
| `Cylce_AirWay.xlsx` | Test cycle — Test cases and results |
| `Bug_reports.csv` | Bug report export from JIRA (detailed) |
| `Bug_reports1.csv` | Bug report export from JIRA (summary) |
| `Bug_reports.html` | Bug report export from JIRA (HTML) |
| `screenshots/` | Test execution evidence (6 screenshots) |

---

## Key Techniques Demonstrated

- **Positive & Negative Testing** — 16 valid + 17 invalid test scenarios across the booking flow
- **Test Cycle Management** — Organized test execution using JIRA/Zephyr Scale
- **Bug Reporting** — 10 bugs with steps to reproduce, expected/actual results, and severity classification
- **Boundary Value Analysis** — Tested card number limits, date validation, and field constraints
- **Input Validation Testing** — Tested empty fields, special characters, and numeric input in text fields