import os
import sys
from shutil import copy2

'''
The following imports are imported inline because they need to be imported
after the venv is initialized.
'''
# import time
# import uuid
# import requests

# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

FRONTEND_HOST = "http://localhost:3000"
BACKEND_HOST = "http://localhost:8000"
REGISTRATION_CODE = "woo_teacher"

def copy_file(original_path, new_path):
    if sys.platform.startswith('win'):
        copy2(original_path, new_path)
    else:
        os.system('cp %s %s' % (original_path, new_path))


def wait_for_server(url, timeout, label):
    import time
    import requests

    num_retries = 0
    while True:
        try:
            response = requests.get(url, timeout=1)
            response.raise_for_status()
            break
        except Exception as e:
            pass
        print('Waiting for %s to load...' % label)
        time.sleep(1)
        num_retries += 1
        if num_retries > timeout:
            raise Exception('Timeout waiting for %s server to start' % label)


def setup_driver(headless=False, use_firefox=False):
    import uuid

    import requests

    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait

    if use_firefox:
        options = webdriver.firefox.options.Options()
        options.set_headless(headless)
        driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(chrome_options=options)

    if headless:
        driver.set_window_size(1200, 800)
    driver.implicitly_wait(0)

    wait_for_server(BACKEND_HOST + '/admin', 30, 'backend')

    # Create user to test with
    username = str(uuid.uuid4())[:12]
    password = str(uuid.uuid4())[:12]
    print('username %s password %s' % (username, password))
    data = {
        "username": username,
        "password": password,
        "registration_code": REGISTRATION_CODE
    }
    r = requests.post(BACKEND_HOST + '/api/v0/users/register/', json=data)
    assert r.status_code == 200

    wait_for_server(FRONTEND_HOST, 60, 'frontend')

    # Load login page
    driver.get(FRONTEND_HOST + '/login')

    # Login
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, 'username')))
    username_field = driver.find_element_by_id('username')
    password_field = driver.find_element_by_id('password')
    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button = driver.find_element_by_css_selector(
        '.login-page-container .btn-success')
    submit_button.click()

    # Agree to terms
    wait = WebDriverWait(driver, 10)
    selector = '.license-page-content .button'
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    # Chromium on Docker fails unless we scroll the window down before
    # trying to click on the continue button.
    driver.execute_script('window.scrollBy(0, 5000)')
    driver.find_element_by_css_selector(selector).click()

    return driver
