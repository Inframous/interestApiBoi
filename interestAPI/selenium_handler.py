from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# import chromedriver_autoinstallerxxxxxxxxxxxxxx
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

# Install and check the correct version of ChromeDriver
# chromedriver_autoinstaller.install()

def get_interest():
    url = "https://www.boi.org.il/"
    
    ## Set the driver to load headless (no screen)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=options)
    
    print("Connecting to server...")
    driver.get(url)

    ## Set the waitForElement time to 10 seconds.
    wait = WebDriverWait(driver, 10)
    print("Waiting for element...")
    interest = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "interestAndInflationValue")))
    next_date = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "interestAndInflationComment")))
    print("Data received successfully.")
    data = {"Interest": interest.text,
            "Next Decision Date": next_date[0].text.split(":")[1].strip()}
    return data

