import ast, json, requests

spoonacular_lst = []
fread = open('epicurious-cache.txt', 'r')
for line in fread:
	(name, nutrients, ingredients) = ast.literal_eval(line)
	d = dict()
	d['Source'] = 'Epicurious'
	d['Recipe'] = name
	for (k, v) in nutrients:
		if k == 'Calories':
			d[k] = v
		else:
			d[k] = v.split()[0]

	base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"
	r = requests.get(base_url, headers = {"X-Mashape-Key": "9SU23pBJVmmshVvR0rEHeV1Bo7dip1EHArPjsn72hzCCLWlgqU", "Accept": "application/json"}, params = {'fillIngredients' : True, 'ingredients' : ','.join(ingredients), 'limitLicense' : False, 'number' : 1, 'ranking' : 1})
	recipe_id = json.loads(r.text)[0]['id']
	base_url = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/" + str(recipe_id) + "/information"
	r = requests.get(base_url, headers = {"X-Mashape-Key": "9SU23pBJVmmshVvR0rEHeV1Bo7dip1EHArPjsn72hzCCLWlgqU", "Accept": "application/json"}, params = {'includeNutrition' : True})
	try:
		spoonacular_lst.append(json.loads(r.text))
	except ValueError:
		print str(recipe_id), 'failed'
fread.close()

fwrite = open('spoonacular-cache.txt', 'w')
for each_spoonacular in spoonacular_lst:
	fwrite.write(json.dumps(each_spoonacular) + "\n")
fwrite.close()
