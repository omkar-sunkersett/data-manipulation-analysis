import urllib2
from bs4 import BeautifulSoup

recipe_urls = []
for p in range(1, 140):
	epicurious_html = urllib2.urlopen("http://www.epicurious.com/search/?meal=lunch&sort=highestRated&content=recipe&page=" + str(p))
	soup = BeautifulSoup(epicurious_html, 'html.parser')
	urls = [("http://www.epicurious.com" + str(tag.find('a').get('href'))) for tag in soup.find_all('div') if tag.get('class') == ['recipe-panel','']]
	for each_url in urls:
		print each_url
		recipe_urls.append(each_url)

recipe_info = []
for each_url in recipe_urls:
	recipe_html = urllib2.urlopen(each_url)
	soup = BeautifulSoup(recipe_html, 'html.parser')
	recipe_name = [tag.get_text().encode('utf-8') for tag in soup.find_all('h1')][0].replace(',',' ')
	nutrients_name = [tag.get_text().encode('utf-8') for tag in soup.find_all('span') if tag.get('class') == ['nutri-label']]
	nutrients_value = [tag.get_text().encode('utf-8') for tag in soup.find_all('span') if tag.get('class') == ['nutri-data']]
	ingredients_name = [tag.get_text().encode('utf-8').replace(',','') for tag in soup.find_all('li') if tag.get('class') == ['ingredient']]
	print (recipe_name, zip(nutrients_name, nutrients_value), ingredients_name)
	recipe_info.append((recipe_name, zip(nutrients_name, nutrients_value), ingredients_name))

data_cleanup = [t for t in recipe_info if t[1] != []]
recipe_nutrition = []
for (name, nutrients, ingredients) in data_cleanup:
	recipe_nutrition.append((name, [x for x in nutrients if x[0] != ''], ingredients))

fwrite = open('epicurious-cache.txt', 'w')
for recipe_info in recipe_nutrition:
	fwrite.write(str(recipe_info) + "\n")
fwrite.close()
