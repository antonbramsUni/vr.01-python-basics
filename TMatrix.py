
import math
from Vector4 import Vector4

identity = [
	1,0,0,0, 
	0,1,0,0, 
	0,0,1,0, 
	0,0,0,1
]

class TMatrix:

	value = []

	def __init__(self, *args):
		self.value = identity if len(args) == 0 else list(args)
		# print('matrix is initialized', self.value)
	
	def log(self):
		print(self.value)

	def mult(self, other_matrix):
		a = other_matrix if isinstance(other_matrix, list) else other_matrix.value
		b = self.value
		return TMatrix(
			a[ 0]*b[0] + a[ 1]*b[4] + a[ 2]*b[ 8] + a[ 3]*b[12],
			a[ 0]*b[1] + a[ 1]*b[5] + a[ 2]*b[ 9] + a[ 3]*b[13],
			a[ 0]*b[2] + a[ 1]*b[6] + a[ 2]*b[10] + a[ 3]*b[14],
			a[ 0]*b[3] + a[ 1]*b[7] + a[ 2]*b[11] + a[ 3]*b[15],
			a[ 4]*b[0] + a[ 5]*b[4] + a[ 6]*b[ 8] + a[ 7]*b[12],
			a[ 4]*b[1] + a[ 5]*b[5] + a[ 6]*b[ 9] + a[ 7]*b[13],
			a[ 4]*b[2] + a[ 5]*b[6] + a[ 6]*b[10] + a[ 7]*b[14],
			a[ 4]*b[3] + a[ 5]*b[7] + a[ 6]*b[11] + a[ 7]*b[15],
			a[ 8]*b[0] + a[ 9]*b[4] + a[10]*b[ 8] + a[11]*b[12],
			a[ 8]*b[1] + a[ 9]*b[5] + a[10]*b[ 9] + a[11]*b[13],
			a[ 8]*b[2] + a[ 9]*b[6] + a[10]*b[10] + a[11]*b[14],
			a[ 8]*b[3] + a[ 9]*b[7] + a[10]*b[11] + a[11]*b[15],
			a[12]*b[0] + a[13]*b[4] + a[14]*b[ 8] + a[15]*b[12],
			a[12]*b[1] + a[13]*b[5] + a[14]*b[ 9] + a[15]*b[13],
			a[12]*b[2] + a[13]*b[6] + a[14]*b[10] + a[15]*b[14],
			a[12]*b[3] + a[13]*b[7] + a[14]*b[11] + a[15]*b[15]
		)
	
	def make_trans_mat(self, x = 0, y = 0, z = 0):
		return self.mult([
			1, 0, 0, 0, 
			0, 1, 0, 0,
			0, 0, 1, 0,
			x, y, z, 1
		])

	# def make_rot_around_axis(self, d, v):
	# 	s  = math.sin(t)
	# 	c  = math.cos(t)
	# 	c1 = 1 - c
	# 	return self.mult([
	# 		c + math.pow(v.x, 2) * c1,
	# 		v.x * v.y * c1 - v.z * s,
	# 		v.x * v.z * c1 + v.y * s, 0,
	# 		v.x * v.y * c1 + v.z * s,
	# 		c + math.pow(v.y, 2) * c1,
	# 		v.y * v.z * c1 - v.x * s, 0,
	# 		v.x * v.z * c1 - v.y * s,
	# 		v.y * v.z * c1 + v.x * s,
	# 		c + math.pow(v.z, 2) * c1, 0,
	# 		0, 0, 1
	# 	])

	def make_rot_mat(self, d, axis):
		r = d * math.pi / 180
		s = math.sin(r)
		c = math.cos(r)
		m = identity
		if axis == 'x':
			m = [
				1, 0, 0, 0, 
				0, c,-s, 0,
				0, s, c, 0, 
				0, 0, 0, 1
			]
		elif axis == 'y':
			m = [
				 c, 0, s, 0, 
				 0, 1, 0, 0,
				-s, 0, c, 0, 
				 0, 0, 0, 1
			]
		elif axis == 'z':
			m = [			
				c,-s, 0, 0, 
				s, c, 0, 0,
				0, 0, 1, 0, 
				0, 0, 0, 1
			]
		return self.mult(m)

	def make_scale_mat(self, x = 1, y = 1, z = 1):
		return self.mult([
			x, 0, 0, 0, 
			0, y, 0, 0,
			0, 0, z, 0, 
			0, 0, 0, 1
		])

	def mult_vec(self, v):
		a = self.value
		b = v.value
		return Vector4(
			a[ 0]*b[0] + a[ 4]*b[1] + a[ 8]*b[2] + a[12]*b[3],
			a[ 1]*b[0] + a[ 5]*b[1] + a[ 9]*b[2] + a[13]*b[3],
			a[ 2]*b[0] + a[ 6]*b[1] + a[10]*b[2] + a[14]*b[3],
			a[ 3]*b[0] + a[ 7]*b[1] + a[11]*b[2] + a[15]*b[3])

