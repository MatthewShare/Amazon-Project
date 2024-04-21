import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

URL = "https://www.amazon.co.uk/Wireless-Charger-CHGeek-Charging-Clamping/dp/B08D5XJTJS/ref=sr_1_5?crid=1R5I4DZSL2WL8&dib=eyJ2IjoiMSJ9.XAgjGBdZU5D8a8ayzpSDMaBFI8uNwd2I5YUCvF3qe3t8iTI8MnUIjZKK_ACrYwK-UKQi0H2E6yc8ggkdcA0c7eKwhPLRAdWixq9z_3pkDGnHbrlxRX7rqwTlOn0YAlLDJ0ajw-_-XUCP_dV8uPFPD6pXqEnhVXSfFQdX2dm8KJBw8NcntCZ8GVvmBelK2Cd4MJcdtM06___nQQ23Vf0Pcud0ix67lAmS3GOjaD_2jI8.dCkaL1wWQA2pRTbY6OXw5477wccKhcQ3T86T6TFettk&dib_tag=se&keywords=wireless+car+charger+iphone&qid=1713528358&quartzVehicle=29-10519&replacementKeywords=wireless+car+iphone&sprefix=wireless+car%2Caps%2C78&sr=8-5"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
MY_EMAIL = os.environ["ENVIRONEMAIL"]
MY_PASSWORD = os.environ["ENVIRONPASSWORD"]

user_headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}
response = requests.get(URL, headers=user_headers)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")

title_data = soup.select(selector="div div div div h1 span")[0]
title = title_data.getText().strip()
price_data = soup.select(selector="div div span")
price = float(soup.find("span", class_="aok-offscreen").getText().strip().split("£")[1])


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    if price < 15:
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Car Charger Price Drop\n\n{title} is now £{price}\n{URL}".encode("utf-8")
        )