import random;

parking_id = 1
out_file = open("out_file.txt", "w")

for day in range(7):
	# print("day ", day)
	for time in range(0, 24):
		isRaining = random.randint(0,1)
		traffic = random.randint(0,2)
		free = random.randint(0, 4)
		if time < 5:
			free = 4
		print("day ", day, ", time ", time, ", free ", free)
		out_file.write(str(day) + " " + str(time) + " " + str(parking_id) + " " + str(isRaining) + " " + str(traffic) + " " + str(free) + "\n")

out_file.close()