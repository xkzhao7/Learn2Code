class Vector:
	def __init__(self):
		self.size = 1
		self.data = [None]
		self.count = 0
	def add(self, value):
		if self.count < self.size:
			self.data[self.count] = value
			self.count += 1
		else:
			self._resize()
			self.data[self.count] = value
			self.count += 1
	def remove(self, pos):
		for i in range(pos, self.size-1):
			self.data[i] = self.data[i+1]
		self.count -= 1
	def deleteValue(self, value):
		counter = 0
		for i in range(self.count):
			if self.data[i] == value:
				counter += 1
			else:
				self.data[i-counter] = self.data[i]	
		self.count -= counter
	def _resize(self):
		new_data = [None] * (self.size * 2)
		for i in range(self.size):
			new_data[i] = self.data[i]

		self.data = new_data
		self.size *= 2

	def getValue(self, pos):
		if pos < self.count:
			return self.data[pos]
		else:
			return "invalid"

	def setValue(self, pos, value):
		self.data[pos] = value

	def getArray(self):
		return self.data[:self.count]

	def getSize(self):
		return self.count

if __name__ == "__main__":
	v = Vector()
	for i in range(1, 11):
		v.add(i)
	print(v.getArray())

	for i in range(v.getSize()):
		if v.getValue(i) % 2 == 1:
			v.setValue(i, 50)
	print(v.getArray())

	v.deleteValue(50)
	print(v.getArray())

	v.add(100)
	print(v.getArray())
	
	v.remove(2)
	print(v.getArray())