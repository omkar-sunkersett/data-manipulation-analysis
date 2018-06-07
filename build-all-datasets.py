import ast, json

epicurious =[]
fread = open('epicurious-cache.txt', 'r')
for line in fread:
	(name, nutrients, ingredients) = ast.literal_eval(line)
	if nutrients[0][1] != 'NaN':
		d = dict()
		d['Source'] = 'Epicurious'
		d['Recipe'] = name.replace(',', ' ').replace('#', '')
		for (k, v) in nutrients:
			if k == 'Calories':
				d[k] = float(v)
			else:
				d[k] = float(v.split()[0])
			if 'Calories' not in d.keys():
				d['Calories'] = 0.0
			if 'Protein' not in d.keys():
				d['Protein'] = 0.0
			if 'Carbohydrates' not in d.keys():
				d['Carbohydrates'] = 0.0
			if 'Fat' not in d.keys():
				d['Fat'] = 0.0
			if 'Saturated Fat' not in d.keys():
				d['Saturated Fat'] = 0.0
			if 'Cholesterol' not in d.keys():
				d['Cholesterol'] = 0.0
			if 'Fiber' not in d.keys():
				d['Fiber'] = 0.0
			if 'Sodium' not in d.keys():
				d['Sodium'] = 0.0
		epicurious.append(d)
fread.close()

epicurious = sorted(epicurious, key = lambda x: x['Saturated Fat'] + (x['Cholesterol'] / 1000) + (x['Sodium'] / 1000))


spoonacular = []
fread = open('spoonacular-cache.txt', 'r')
for line in fread:
	spoon_d = json.loads(line)
	if spoon_d['title'] != 'Mini Chorizo Corn Dogs' and spoon_d['title'] != 'Steak Rancheros':
		d = dict()
		d['Source'] = 'Spoonacular'
		d['Recipe'] = spoon_d['title'].replace(',',' ').replace('#', '')
		for nutrient in spoon_d['nutrition']['nutrients']:
			if nutrient['title'] == 'Calories':
				d['Calories'] = nutrient['amount']
			elif nutrient['title'] == 'Protein':
				d['Protein'] = nutrient['amount']
			elif nutrient['title'] == 'Carbohydrates':
				d['Carbohydrates'] = nutrient['amount']
			elif nutrient['title'] == 'Fat':
				d['Fat'] = nutrient['amount']
			elif nutrient['title'] == 'Saturated Fat':
				d['Saturated Fat'] = nutrient['amount']
			elif nutrient['title'] == 'Cholesterol':
				d['Cholesterol'] = nutrient['amount']
			elif nutrient['title'] == 'Fiber':
				d['Fiber'] = nutrient['amount']
			elif nutrient['title'] == 'Sodium':
				d['Sodium'] = nutrient['amount']
		if 'Calories' not in d.keys():
			d['Calories'] = 0.0
		if 'Protein' not in d.keys():
			d['Protein'] = 0.0
		if 'Carbohydrates' not in d.keys():
			d['Carbohydrates'] = 0.0
		if 'Fat' not in d.keys():
			d['Fat'] = 0.0
		if 'Saturated Fat' not in d.keys():
			d['Saturated Fat'] = 0.0
		if 'Cholesterol' not in d.keys():
			d['Cholesterol'] = 0.0
		if 'Fiber' not in d.keys():
			d['Fiber'] = 0.0
		if 'Sodium' not in d.keys():
			d['Sodium'] = 0.0
		spoonacular.append(d)
fread.close()

spoonacular = sorted(spoonacular, key = lambda x: x['Saturated Fat'] + (x['Cholesterol'] / 1000) + (x['Sodium'] / 1000))


fwrite = open('dataset-epicurious.tsv', 'w')
fwrite.write("Recipe\tSource\tCalories (cal)\tProtein (g)\tCarbohydrates (g)\tFat (g)\tSaturated Fat (g)\tCholesterol (mg)\tFiber (g)\tSodium (mg)\n")
for recipe in epicurious:
	fwrite.write(recipe['Recipe']+"\t"+str(recipe['Source'])+"\t"+str(recipe['Calories'])+"\t"+str(recipe['Protein'])+"\t"+str(recipe['Carbohydrates'])+"\t"+str(recipe['Fat'])+"\t"+str(recipe['Saturated Fat'])+"\t"+str(recipe['Cholesterol'])+"\t"+str(recipe['Fiber'])+"\t"+str(recipe['Sodium'])+"\n")
fwrite.close()

fwrite = open('dataset-spoonacular.tsv', 'w')
fwrite.write("Recipe\tSource\tCalories (cal)\tProtein (g)\tCarbohydrates (g)\tFat (g)\tSaturated Fat (g)\tCholesterol (mg)\tFiber (g)\tSodium (mg)\n")
for recipe in spoonacular:
	fwrite.write(recipe['Recipe'].encode('utf-8')+"\t"+str(recipe['Source'])+"\t"+str(recipe['Calories'])+"\t"+str(recipe['Protein'])+"\t"+str(recipe['Carbohydrates'])+"\t"+str(recipe['Fat'])+"\t"+str(recipe['Saturated Fat'])+"\t"+str(recipe['Cholesterol'])+"\t"+str(recipe['Fiber'])+"\t"+str(recipe['Sodium'])+"\n")
fwrite.close()

fwrite = open('dataset-combined.tsv', 'w')
fwrite.write("Recipe\tSource\tCalories (cal)\tProtein (g)\tCarbohydrates (g)\tFat (g)\tSaturated Fat (g)\tCholesterol (mg)\tFiber (g)\tSodium (mg)\n")
for recipe in epicurious:
	fwrite.write(recipe['Recipe']+"\t"+str(recipe['Source'])+"\t"+str(recipe['Calories'])+"\t"+str(recipe['Protein'])+"\t"+str(recipe['Carbohydrates'])+"\t"+str(recipe['Fat'])+"\t"+str(recipe['Saturated Fat'])+"\t"+str(recipe['Cholesterol'])+"\t"+str(recipe['Fiber'])+"\t"+str(recipe['Sodium'])+"\n")
for recipe in spoonacular:
	fwrite.write(recipe['Recipe'].encode('utf-8')+"\t"+str(recipe['Source'])+"\t"+str(recipe['Calories'])+"\t"+str(recipe['Protein'])+"\t"+str(recipe['Carbohydrates'])+"\t"+str(recipe['Fat'])+"\t"+str(recipe['Saturated Fat'])+"\t"+str(recipe['Cholesterol'])+"\t"+str(recipe['Fiber'])+"\t"+str(recipe['Sodium'])+"\n")
fwrite.close()
