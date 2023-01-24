from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

MY_EMAIL = "##########"
MY_PASSWORD = "########"

url = "https://www.amazon.com/Lenovo-Ideapad-Touchscreen-i3-1005G1-Processor/dp/B08B6F1NNR/ref=nav_signin?qid=1674545188"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
amazon_webpage = response.text
#print(amazon_webpage)

soup = BeautifulSoup(amazon_webpage, "lxml")
price = soup.find(name="span", class_="a-offscreen").get_text()
price = float(price.split("$")[1])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 390

if price < BUY_PRICE:
    message = f"{title} is now {price}.Place your order now."

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
