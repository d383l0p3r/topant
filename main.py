from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://qiwi.com/")
WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/section/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/button/div/div/div[1]/div",
        )
    )
).click()

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div/input",
        )
    )
).send_keys(phone if len(phone) == 10 else phone[-10:])

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div[1]/div"
            "/div/img",
        )
    )
)

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            f"/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div"
            f"/div[1]/div[9]/div/div",
        )
    )
).click()

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div[2]/div/div/div[1]/button/div/div/div[1]/div",
        )
    )
).click()

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[2]/p/a",
        )
    )
).click()

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[1]/div[3]/div/div/div[2]/div/input",
        )
    )
).send_keys(8873)

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[1]/div[4]/div/div/div/button/div/div/div[1]/div",
        )
    )
).click()


WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[1]/div[2]/div/div/div[2]/div/input",
        )
    )
).send_keys('password')

WebDriverWait(driver, 20).until(
    presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[2]/div/div/form/div/div[2]/div[2]/div[1]/div/div/div/button/div/div/div[1]/div",
        )
    )
).click()
