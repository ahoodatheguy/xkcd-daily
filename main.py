import requests, bs4
from requests.api import request
from notify import sendComic

def getComic(url):
	site = requests.get(url)
	site.raise_for_status()  # Crash program if something goes wrong.
	soup = bs4.BeautifulSoup(site.text, 'html.parser')
	images = soup.find_all('img')

	# Get title of Comic
	global title
	title = soup.find(id='ctitle').text


	for image in images:
		imagesrc = 'https://' + image['src'][2:]
		# Images are saved under the comics directory on xkcd. Tells python to ignore other images (e.g header)
		if '/comics/' in imagesrc:
			print(imagesrc)
			with open('comic.png', 'wb') as f:
				im = requests.get(imagesrc)
				f.write(im.content)


if __name__ == '__main__':
	getComic('https://c.xkcd.com/random/comic/')
	sendComic('from_email_adress@gmail.com', 'fromEmailPassword', 'recipientEmail@vzwpix.com', title)
	