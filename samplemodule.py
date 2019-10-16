def module_funt(arg1, arg2 ='default val', *args):
	localvar = arg1*3
	return locallvar

class X(object):
	def __init__(self, name):
		self.name = name
	def getname(self):
		return self.name

xobj = X("objectx")

class Y(X):
	def funct1(self):
		pass

	def funct2(self):
		return "Y("+self.name+")"

