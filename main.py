# https://github.com/rileypredum/East-Bay-Housing-Web-Scrape/blob/master/EB_Room_Prices.ipynb
import sms
import threading
import os
from requests import get
from bs4 import BeautifulSoup


all_posts = {} #timestamps of all the posts the query has ever seen
all_posts_length = 0
query = os.getenv("QUERY")


def main_loop():
    print("checking craigslist...")
    global all_posts
    global all_posts_length
    global query

    response = get(query)

    #grab the HTML as a BS4 soup object
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)

    #get the macro-container for the housing posts
    posts = html_soup.find_all('li', class_= 'result-row')
    #print(type(posts)) #to double check that I got a ResultSet
    #print(len(posts)) #to double check I got 50 (elements/page)

    for post in posts:
        all_posts[ post.find('time', class_= 'result-date')['datetime'] ] = True

    print("posts found so far: " + str(len(all_posts)))

    if len(all_posts) > all_posts_length: #new post found

        print("a new post was found!")

        #update all posts length
        all_posts_length = len(all_posts)

        #send sms
        sms.send("new posting foor your query: " + query)

    threading.Timer(30 * 60, main_loop).start() # check every 30 min

if __name__ == "__main__":
    main_loop()

