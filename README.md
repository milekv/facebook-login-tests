# Facebook Login Tests

This repository contains automated tests for Facebook login functionality using Selenium WebDriver and Python.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* **Python:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
* **Selenium:** Install the Selenium library using pip:
    ```bash
    pip install selenium
    ```
* **ChromeDriver:** Download the ChromeDriver executable that matches your Chrome browser version from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads). 
    * Extract the downloaded file and place the `chromedriver` executable in a directory that is in your system's PATH environment variable.
* **pytest (optional):** Install pytest for running tests in a structured way:
    ```bash
    pip install pytest
    ```

### Running the Tests

1. **Clone the repository:**
    ```bash
    git clone https://github.com/milekv/facebook-login-tests.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd facebook-login-tests
    ```

3. **Update the test_login.py file:**
    * Open the `test_login.py` file and replace `"your_facebook_email"` and `"your_facebook_password"` with your actual Facebook credentials.

4. **Run the tests:**
    * To run the tests using pytest, execute the following command:
        ```bash
        pytest test_login.py
        ```
    * Alternatively, you can run the tests directly using Python:
        ```bash
        python test_login.py
        ```

## Test Scenarios

* `test_valid_login()`: Tests a successful login with valid credentials.
* `test_invalid_login()`: Tests an unsuccessful login with invalid credentials.


## Notes

* **Facebook may block automated logins.** If you encounter issues, try using a different test account or solve the CAPTCHA manually.
* This code is simplified and may require adjustments depending on changes to the Facebook website.
* Make sure to keep your ChromeDriver version updated to match your Chrome browser version.

## Contributing

Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvement.
