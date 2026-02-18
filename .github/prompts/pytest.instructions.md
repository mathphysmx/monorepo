---
name: pytest generation instructions
description: This file describes the instructions for generating pytest test cases for the project.
applyTo: **/tests/**/*.py
---

When generating pytest test cases, please follow these guidelines:
1. Use descriptive test function names that clearly indicate what is being tested.
2. Use fixtures to set up any necessary test data or state.
3. Use assertions to verify the expected outcomes of the tests.
4. Group related tests into classes or modules for better organization.
5. Avoid using print statements in test cases; instead, rely on assertions to provide feedback on test results.
6. Ensure that test cases are independent and can be run in any order without affecting each other.
7. Use parameterized tests to cover multiple input scenarios for the same test logic.
8. Follow the Arrange-Act-Assert-Cleanup (AAAC) pattern to structure your test cases for clarity and maintainability.
9. Include docstrings in your test functions to explain the purpose of the test and any important details.
10. Keep test cases focused and concise, testing only one aspect of the functionality at a time.


