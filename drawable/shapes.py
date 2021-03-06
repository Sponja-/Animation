from drawable import Drawable
from utils import ensureArray, isConvex

class Line(Drawable):
	def __init__(self, start, end, **kwargs):
		self.start = ensureArray(start)
		self.end = ensureArray(end)

		super().__init__(**kwargs)

		self.exposedProperties += ["start", "end"]

	def draw(self):
		self.canvas.drawLine(self.start, self.end, self.color)

class Arrow(Line):
	def __init__(self, start, end, **kwargs):
		super().__init__(start, end, **kwargs)

	def draw(self):
		self.canvas.drawArrow(self.start, self.end, self.color)

class Rectangle(Drawable):
	def __init__(self, start, width, height, **kwargs):
		self.start = ensureArray(start)
		self.width = width
		self.height = height

		super().__init__(**kwargs)

		self.exposedProperties += ["start", "width", "height"]

	def draw(self):
		self.canvas.drawRectangle(self.start, self.width, self.height, self.color)

class Circle(Drawable):
	def __init__(self, center, radius, **kwargs):
		self.center = ensureArray(center)
		self.radius = radius

		super().__init__(**kwargs)

		self.exposedProperties += ["center", "radius"]

	def draw(self):
		self.canvas.drawCircle(self.center, self.radius, self.color)

class Polygon(Drawable):
	def __init__(self, points, **kwargs):
		self.points = [ensureArray(p) for p in points]
		super().__init__(**kwargs)

		self.exposedProperties += ["points"]

	def draw(self):
		self.canvas.drawPolygon(self.points, self.color)

class ConvexPolygon(Polygon):
	def __init__(self, points, **kwargs):
		super().__init__(points, **kwargs)
		assert(isConvex(self.points))

	def draw(self):
		self.canvas.drawConvexPolygon(self.points, self.color)

class Arrow(Line):
	def __init__(self, start, end, **kwargs):
		super().__init__(start, end, **kwargs)

	def draw(self):
		self.canvas.drawArrow(self.start, self.end, self.color)