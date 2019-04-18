
import json
import random

month = 4
training_data = {}
training_data['training_data'] = []

for day in range(7):
	for time in range(48):
		for location_id in range(3):
			data = {}
			data['location_id'] = location_id
			data['time'] = time
			data['day'] = day
			data['date'] = day + 1
			data['month'] = month
			data['traffic'] = random.randint(0,3)
			data['free'] = random.randint(0,4)
			if time < 24:
				data['free'] = 4
			data['is_raining'] = random.randint(0,1)
			data['is_event'] = random.randint(0,1)
			data['is_snowing'] = random.randint(0,1)
			training_data['training_data'].append(data)
with open("training_data.json", "w") as file:
	json.dump(training_data, file)
