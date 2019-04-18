from Sensor import Sensor

class Simulator:
	def __init__(self):
		self.sensors = []
		self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		self.dayInWeek = 4
		self.date = 28
		self.month = 2
		self.year = 2019
		self.hour = 7
		self.minute = 0;
		self.minutesPerTick = 30

	def addSensor(self, sensor_id):
		self.sensors.append(Sensor(sensor_id, self))

	def status(self):
		for sensor in self.sensors:
			print(sensor.sensor_id)

	def simulate(self, count):
		while count >= 0:
			for sensor in self.sensors:
				sensor.checkState()
			count = count - 1
			self.updateTime();

	def getDaysOfMonth(self):
		if self.month in [1,3,5,6,8,10,12]:
			return 31
		elif self.month in [4,7,9,11]:
			return 30
		elif self.year % 4 != 0 and self.month == 2:
			return 28
		else:
			return 29

	def updateTime(self):
		self.minute = self.minute + self.minutesPerTick
		if self.minute == 60:
			self.hour = self.hour + 1
			self.minute = 0
			if self.hour == 24:
				self.dayInWeek = (self.dayInWeek + 1) % 7
				self.date = self.date + 1
				self.hour = 0
				if self.date > self.getDaysOfMonth():
					self.month = self.month + 1
					self.date = 1
					if self.month > 12:
						self.year = self.year + 1
						self.month = 1

	def getDate(self):
		minuteText = str(self.minute)
		if self.minute < 10:
			minuteText = "0"+minuteText;
		hourText = str(self.hour)
		if self.hour < 10:
			hourText = "0" + hourText
		return str(str(self.date) + "-"+ str(self.month) + "-"+ str(self.year)+ ", " + self.days[self.dayInWeek] + " (" + hourText+":"+minuteText+")")

	def getTicksToPickHour(self):
		if self.hour > 18:
			if self.dayInWeek == 5:
				return (24 - self.hour + 7 + 48) * 60 / self.minutesPerTick
			return (24 - self.hour + 7) * 60 / self.minutesPerTick
		elif self.hour < 7:
			if self.dayInWeek == 6:
				return (7 - self.hour + 48) * 60 / self.minutesPerTick
			return (7 - self.hour) * 60 / self.minutesPerTick
		else:
			return 0;

	def setSensorResponse(self, state, sensor_id):
		print(self.getDate(), " ", sensor_id, ": ", state )


simulator = Simulator()
simulator.addSensor('s1')
# simulator.addSensor('s2')
# simulator.addSensor('s4')
# simulator.addSensor('s3')
# simulator.status();
simulator.simulate(800)