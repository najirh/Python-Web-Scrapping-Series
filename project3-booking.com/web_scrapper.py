# This app scrap data from booking.com

# library installed
# 1. beautifulsoup4
# 2. requests


"""
give the url, file name
greetings
start scrapping
hotel_name,
price
location
ratings
reviews
link
save the file

"""

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random


# url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=New+Delhi&ssne=New+Delhi&ssne_untouched=New+Delhi&highlighted_hotels=1591538&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AueF3b0GwAIB0gIkMjFkYTVhYTMtZWM5ZC00ZmYyLTkzMDktZjUxN2IxMzVjZTdk2AIF4AIB&sid=e926d54c76bc20f9416c4f573131702a&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=hotel&dest_id=-2106102&dest_type=city&checkin=2025-04-01&checkout=2025-04-02&group_adults=2&no_rooms=1&group_children=0'
mumbai = 'https://www.booking.com/searchresults.en-gb.html?ss=Mumbai&ssne=New+Delhi&ssne_untouched=New+Delhi&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4AueF3b0GwAIB0gIkMjFkYTVhYTMtZWM5ZC00ZmYyLTkzMDktZjUxN2IxMzVjZTdk2AIF4AIB&sid=e926d54c76bc20f9416c4f573131702a&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2092174&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=bb7575c39e5206d2&ac_meta=GhBiYjc1NzVjMzllNTIwNmQyIAAoATICZW46Bk11bWJhaUAASgBQAA%3D%3D&checkin=2025-04-01&checkout=2025-04-02&group_adults=2&no_rooms=1&group_children=0&flex_window=1'

def web_scrapper2(web_url, f_name):
    
    # greetings
    print("Thank you sharing the url and file name!\n⏳\nReading the content!")
    
    num = random.randint(3, 7)
    
    # processing
    time.sleep(num)

    
    header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}


    response = requests.get(web_url, headers=header)
    

    if response.status_code == 200:
        print("Connected to the website")
        html_content = response.text
        
        
        # creating soup
        soup =  BeautifulSoup(html_content, 'lxml')
        
        # print(soup.prettify())
        
        # main containers
        hotel_divs = soup.find_all('div', role="listitem")
        
        with open(f'{f_name}.csv', 'w', encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)
            
            # adding header
            writer.writerow(['hotel_name', 'locality', 'price', 'rating', 'score', 'review', 'link'])
        
            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_="f6431b446c a15b38c233").text.strip()
                hotel_name if hotel_name else "NA"
                
                location = hotel.find('span', class_="aee5343fdb def9bc142a").text.strip()
                location if location else "NA"
                
                # price
                price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f").text.replace('₹ ', '')
                if price:
                    price
                else:
                    "NA"
                
                rating = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb").text
                rating if rating else "NA"
            
            
                score = hotel.find('div', class_="a3b8729ab1 d86cee9b25").text.strip().split(' ')[-1]
                score if score else "NA"
                
                review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47").text.strip()
                review if review else 'NA'
                
                
                # getting link
                link = hotel.find('a', href=True).get('href')
                link if link else 'NA'
                

                # saving the file into csv
                writer.writerow([hotel_name, location, price, rating, score, review, link])
    
            
            # print(hotel_name)
            # print(location)
            # print(price)
            # print(rating)
            # print(score)
            # print(review)
            # print(link)
            # print('')
        print("Web Scrapped done")
        # print(hotel_divs)
        
        

    else:
        print(f"Connection Failed!{response.status_code}")



# if using this script directly than below task will be executed
if __name__ == '__main__':

    url = input("Please enter url! :")
    fn = input('Please give file name! :')

    # calling the function
    web_scrapper2(url, fn)
