from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
#print(articles)
article_links = []
article_texts = []
for tags in articles:
    a_tags = soup.find_all("a")
    for refs in a_tags:
        link = refs.get("href")
        article_links.append(link)
        text = refs.getText()
        article_texts.append(text)
#print(article_links)
#print(article_texts)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# print(article_links)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# largest_number = max(article_upvotes) - 1
# largest_index = article_upvotes.index(largest_number) - 1
#
# print(article_texts[largest_index])
#print(article_links[largest_index])