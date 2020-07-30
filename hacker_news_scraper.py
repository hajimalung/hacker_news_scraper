import requests
#use beautiful soup to parse the data
from bs4 import BeautifulSoup
import pprint

def get_custom_hacker_news(story_links,sub_texts):
	cutom_news = []
	if len(story_links) != len(sub_texts):
		print('oops not enough votes data for stories data')
	else:
		for idx,story in enumerate(story_links):
			title = story.getText()
			href = story.get('href',None)
			scores = sub_texts[idx].select('.score')
			if scores:
				votes = int(scores[0].getText().replace(' points',''))
				if votes > 99:
					cutom_news.append({
						'title' : title,
						'link' : href,
						'votes' : votes
						})
	return sort_custom_news(cutom_news)

def sort_custom_news(news_list):
	return sorted(news_list, key= lambda news:news['votes'])

def get_hacker_news_from(url_to_scrape):
	res =requests.get(url_to_scrape)
	#text returns entire html file
	#the html.parser will tell the BeautifulSoup that we want to parse html text
	hacker_news_page = BeautifulSoup(res.text,'html.parser')
	#select will return list of matching selectors from html
	story_links = hacker_news_page.select('.storylink')
	sub_texts = hacker_news_page.select('.subtext')
	return get_custom_hacker_news(story_links, sub_texts)[::-1]

pprint.pprint(get_hacker_news_from('https://news.ycombinator.com/news'))


