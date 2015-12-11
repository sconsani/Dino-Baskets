class Dino(object):
	def __init__(self, name, color, height):
		self.name = name
		self.color = color
		self.height = height

	def paint(self,body_color):
		self.color = body_color

	def display(self):
		print self.name
		print self.color
		print self.height


Freddy = Dino("Freddy", ["black","green"], 240)

Georgie = Dino("Georgie", ["blue","gold"], 140)

Freddy.display()



Freddy.paint("red")

Freddy.display()
