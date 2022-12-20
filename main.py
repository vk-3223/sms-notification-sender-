from selenium import webdriver
import time
from twilio.rest import Client
chrome_driver_path = "YOUR_CHROME_driver_path"

account_sid = "TWILLIO_ACCOUNT_SID"
auth_token = "TWILLIO_ACCOUNT_TOKEN"
client = Client(account_sid,auth_token)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options,executable_path=chrome_driver_path)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def main():
    while True:

        driver = get_driver()
        time.sleep(5)
        elemnt = driver.find_element(by="xpath",value="/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]")
        value,percantage = (elemnt.text.split(" "))
        float_value = float(value)
        if float_value < -0.1:
            message = client.messages.create(
                body=f"the stock value less than -0.10% {value}",
                from_="Here_twillio_account_PhNo",
                to="Sender_NO"
            )
            print(message.sid)


if __name__ == ("__main__"):
    main()