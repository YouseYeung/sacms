from django.db import models

class aaa():
	name = 
	def edit(self, name = NONE):
		self.name = name

	def __str__(self):
		return self.name

a = aaa()
print (a)
a.edit("ss")
print (a)