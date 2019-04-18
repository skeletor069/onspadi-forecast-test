import random

class Sensor:
	def __init__(self, sensor_id, simulator):
		self.sensor_id = sensor_id
		self.simulator = simulator
		self.checkCount = 0
		self.state = 0
		self.maxNextArriveDelay = 180 / self.simulator.minutesPerTick
		self.maxStayTime = 240 / self.simulator.minutesPerTick
		self.decideNextArrival()

	def decideNextArrival(self):
		ticksToPickHour = self.simulator.getTicksToPickHour();
		self.nextArrival = random.randint(ticksToPickHour + self.checkCount , ticksToPickHour + self.checkCount + self.maxNextArriveDelay)
		self.stayTime = random.randint(1, self.maxStayTime)
		# print("next arrival on ", self.nextArrival, ", stayTime ", self.stayTime)

	def checkState(self):
		if self.checkCount < self.nextArrival:
			self.simulator.setSensorResponse(0, self.sensor_id)
		else:
			self.stayTime = self.stayTime - 1
			if self.stayTime == 0:
				self.decideNextArrival()
			self.simulator.setSensorResponse(1, self.sensor_id)
		self.checkCount = self.checkCount + 1
