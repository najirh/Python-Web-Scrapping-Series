# This app scrap product data from amazon website

# BeautifulSoup4
# requests
# lxml


from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7S59D/ref=sr_1_4?crid=RBARZ970AYJI&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGlx8v2Sx78yzGgsFfSLyufaCZhsU6s-KsHLVTWzO21l030BNAPdSwF1uvk-xP2xiYHOrOsuJoyUXTbtnLlKohg0PDfeDV2ow3KJTID02CZHFHe8BElHxz0Qx9AFS7cgOtkIB0SiGqovUlX53vpFMVfDlFCxKDYYyYS0xwojJ1zvN8J-uZuRvzI8Bf-RrBv58giQ5qGy-67sptz4v75mHE4Wo.tSxthxJx5H1i4-8rVzEb4sSrmXDaiOyiNDov_Gs8y5U&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax&nsdOptOutParam=true&qid=1736429886&sprefix=%2Caps%2C209&sr=8-4&th=1"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # print(response.status_code)
    html_content = response.text
    
else:
    print("fetching error", response.status_code)
    
soup = BeautifulSoup(html_content, 'lxml')

# print(soup.prettify())

product_title = soup.find("span", id="productTitle").text.strip()
product_price = soup.find("span", class_="a-price-whole").text.strip()
product_rating = soup.find("span", id="acrPopover").text.strip()
product_bp = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
product_description = soup.find("div", id="productDescription").text.strip()
reviews = soup.find("ul", id="cm-cr-dp-review-list").text.strip()


print(reviews)
# find, find_all

# saving the data
with open("amazon_airpod pro max.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title", "product_price", "product_rating", "product_bp", "product_description", "reviews"])

    writer.writerow([product_title, product_price, product_rating, product_bp, product_description, reviews])

print("data saved!")


