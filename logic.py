import random
import blockshapes

class Board:
	def __init__(self,width=10,height=20):
		self.grid=[[' ' for i in range(10)] for j in range(20)]
		self.width=width
		self.height=height
	def collision(self,block):
		shape=Block.blockShapes[block.blockType][block.rotation]
		for dy,line in enumerate(shape):
			for dx,pixel in enumerate(line):
				pos=Pos(dx,dy)+block.pos
				if pixel!=' ':
					if pos.x < 0 or pos.x >= self.width or pos.y < 0 or pos.y >= self.height:
						print(str(pos))
						return True
					if self.grid[pos.y][pos.x] != ' ':
						return True
		return False
					
class Pos:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(self,other):
		return Pos(self.x+other.x,self.y+other.y)
	def __str__(self):
		return '({0},{1})'.format(self.x,self.y)
	def __repr__(self):
		return str(self)

class Block:
	blockShapes={
		'l':blockshapes.l,
		'j':blockshapes.j,
		'o':blockshapes.o,
		's':blockshapes.s,
		'z':blockshapes.z,
		'i':blockshapes.i,
		't':blockshapes.t
	}
	def __init__(self,blockType='r',pos=Pos(5,0),rotation=0):
		self.pos=pos

		if (blockType == 'r'):
			self.blockType=random.choice(list(Block.blockShapes.keys()))
		else:
			self.blockType=blockType

		if rotation not in [0,1,2,3]:
			self.rotation=random.choice([0,1,2,3])
		else:
			self.rotation=rotation

	def __add__(self,shift: tuple):
		return Block(self.blockType,self.pos+shift,self.rotation)
		


