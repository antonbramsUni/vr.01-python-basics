
import math

identity = [0,0,0,0]

class Vector4:

	value = []

	def __init__(self, x = 0, y = 0, z = 0, w = 0):
		self.value = [x, y, z, w]
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		# print('vector is initialized', self.value)

def euclidean_distance(v1, v2):
	return math.sqrt(
		math.pow(v1.x - v2.x, 2) + 
		math.pow(v1.y - v2.y, 2) +
		math.pow(v1.z - v2.z, 2))