import sys
import tensorflow as tf
from tensorflow import keras
import numpy as np
import array as arr
import matplotlib.pyplot as plt
import json
# import tensorflowjs as tfjs

# days : sun = 1, mon = 2, tue = 3, wed = 4, thu = 5, fri = 6, sat = 7
# time : 12:00 - 01:00 = 0, 01:00 - 02:00 = 1,...
# parking location :  0,1,2,3,....
# isRaining : true = 1, false = 0
# traffic state : low = 0, moderate = 1, heavy = 2
# number of free spaces : 0 = 0, 1 - 3 = 1, 4 - 6 = 2, 7 - 10 = 3, more than 10 = 4

# data format = [day, time, location, isRaining, traffic]

def GetDataset(input_file):
	num_lines = sum(1 for line in open(input_file))
	data = np.random.random((num_lines, 5))
	labels = np.random.random((num_lines, 5))
	with open(input_file) as fin:
		i = 0
		for line in fin:
			splitted = line.split()
			data[i][0] = splitted[0]
			data[i][1] = splitted[1]
			data[i][2] = splitted[2]
			data[i][3] = splitted[3]
			data[i][4] = splitted[4]
			labels[i] = GetOutputValueByType(int(splitted[5]))
			i=i+1
	return data,labels

def GetJsonData(input_file):
	with open(input_file, "r") as file:
		obj = json.loads(file.read())
		raw_data_array = obj["training_data"];
		num_lines = len(raw_data_array)
		data = np.random.random((num_lines, 9))
		labels = np.random.random((num_lines, 5))


		for i in range(num_lines):
			data[i][0] = raw_data_array[i]["location_id"]
			data[i][1] = raw_data_array[i]["time"]
			data[i][2] = raw_data_array[i]["day"]
			data[i][3] = raw_data_array[i]["date"]
			data[i][4] = raw_data_array[i]["month"]
			data[i][5] = raw_data_array[i]["traffic"]
			data[i][6] = raw_data_array[i]["is_event"]
			data[i][7] = raw_data_array[i]["is_raining"]
			data[i][8] = raw_data_array[i]["is_snowing"]

			labels[i] = GetOutputValueByType(int(raw_data_array[i]["free"]))

		return data, labels

	return [],[]


def GetOutputValueByType(output_type):
	output = [1,0,0,0,0]
	if output_type == 1:
		output = [0,1,0,0,0]
	elif output_type == 2:
		output = [0,0,1,0,0]
	elif output_type == 3:
		output = [0,0,0,1,0]
	elif output_type == 4:
		output = [0,0,0,0,1]
	return output

def GetNumberOfFreeSpaces(inputs):
	outputs = np.random.random((len(inputs), 1))
	i = 0
	for values in inputs:

		max_val = 0
		max_pos = 0
		for pos in range(0,5):
			if values[pos] > max_val:
				max_val = values[pos]
				max_pos = pos
		outputs[i] = max_pos
		print(str(values), " -> " + str(max_pos))
		i = i + 1

	return outputs

if len(sys.argv) != 2:
	print("usage : TrainTest.py data_file_name");
	exit(0)

input_file = sys.argv[1]
data, labels = GetJsonData(input_file)


# data,labels = GetDataset(input_file)

# for line in range(0, len(data)):
# 	print(str(data[line]), " " + str(labels[line]))

model = keras.Sequential()
# # Adds a densely-connected layer with 5 units to the model:
model.add(keras.layers.Dense(25, input_dim = 9, activation='relu'))
# # Add another:
model.add(keras.layers.Dense(5, activation='relu'))
# # Add a softmax layer with 5 output units:
model.add(keras.layers.Dense(5, activation='softmax'))

# # model.compile(optimizer=tf.train.AdamOptimizer(0.001),
# #               loss='categorical_crossentropy',
# #               metrics=['accuracy'])

model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['accuracy'])


model.fit(data, labels, epochs=10)

# # sample_data = np.random.random((4, 5))
# # sample_data[0] = [1,1,1,1,1]
# # sample_data[1] = [4,1,1,0,0]
# # sample_data[2] = [3,10,1,1,0]
# # sample_data[3] = [3,3,1,0,1]

# # pred = model.predict(data, batch_size=4)
# # print("Prediction")
# # print(pred)
# # print(GetNumberOfFreeSpaces(data))

# # plt.plot(range(len(data)), GetNumberOfFreeSpaces(labels), label="actual")
# # plt.plot(range(len(data)), GetNumberOfFreeSpaces(pred), label="actual")
# # plt.show()

keras_file = "keras_model_2.h5"
tf.keras.models.save_model(model, keras_file)



# # converter = tf.contrib.lite.TocoConverter.from_keras_model_file(keras_file)
# # tflite_model = converter.convert()
# # open("converted_model.tflite", "wb").write(tflite_model)
# # tfjs_target_dir = "/build"
# # tfjs.converters.save_keras_model(model, tfjs_target_dir)