# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scrapping using some tools like bs4

#Step 0: To install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib


import requests
from bs4 import BeautifulSoup
import html5lib
url = "https://www.codewithharry.com/"

import requests

# Make an HTTP GET request to a URL
response = requests.get(url)

# Check if the request was successful
# if response.status_code == 200:
#     # Access the content of the response
#     htmlContent = response.content
#     # ... continue with your code ...
# else:
#     print('Request failed with status code:', response.status_code)


# Step 1: Get the html
content = requests.get(url)
htmlContent = response.content
#print(htmlContent)

# Step 2: Parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

# Step 3: HTML tree traversal

#Commonly used type of objects:
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment

#title = soup.title
# print(type(title)) # Tag
# print(type(soup)) # BeautifulSoup
# print(type(title.string)) # NavigableString

#Get the title of HTML page
title = soup.title

# Get all the paragraph from the page
paras = soup.find_all('p')
#print(paras)

# get all the anchor tag 
anchors = soup.find_all('a')
#Get all the link on th epage

#print(anchors)

print(soup.find('p')) # Get first element in the html page
print(soup.find('p')['class']) # Get the clasess of any elements
 
#  Find all the element with class lead
print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup

# print(soup.find('p').get_text())
# print(soup.get_text)

# get all the anchor tag 
anchors = soup.find_all('a')
all_link = set()
#Get all the link on th epage
for link in anchors:
    if(link != '#'):
        link = "https://www.codewithharry.com/" +link.get('href')
        all_link.add(link)
        print(link)

# Content
ul = soup.find("ul")
print(ul.contents)

# Childrens, parent, next sibling and previous_Sibling

# 1. Children
ul = soup.find("ul")
for i in ul.children:
    print(i)

# 2. Parent:
ul = soup.find("ul")
print(ul.parent)

print(ul.parent.parent)

# 3. next_sibling and previuos_sibling
ul = soup.find(id = "li")
print(ul.next_sibling.next_sibling)

ul = soup.find(id="li")

for j in ul.next_siblings:
    print(j)

    for i in ul.previous_siblings:
     print(i)

     print(ul.previous_sibling.previous_sibling)

# stripped_string
ul = soup.find(id="li")
elem = ul.next_sibling.next_sibling
print(elem)
for i in elem.stripped_strings:
    print(i)