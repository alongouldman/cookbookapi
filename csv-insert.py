import csv
from cookbookapi.api.models import Ingredient

with open('ingeredients.csv', 'r') as f:
	reader = csv.reader(f)
	your_list = list(reader)

for lst in your_list:
	for i in range(2, len(lst)):
		try:
			lst[i] = float(lst[i])
		except Exception:
			print(i)
	ing = Ingredient(name=lst[0], type=lst[1], protein=float(lst[2]), carbohydrate=float(lst[3]), fat=float(lst[4]), calories=float(lst[5]), sugar=float(lst[6]),
					 vitamin_C=float(lst[7]), vitamin_B1=float(lst[8]), vitamin_B2=float(lst[9]),
					 vitamin_B3=float(lst[10]), vitamin_B6=float(lst[11]), sodium=float(lst[12]),
					 phosphorus=float(lst[13]), magnesium=float(lst[14]), iron=float(lst[15]), calcium=float(lst[16]), potassium=float(lst[17]), nutritional_fiber=float(lst[18]))
	ing.save()
