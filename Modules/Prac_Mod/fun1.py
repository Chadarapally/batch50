print "name:",__name__
def fun():
	print "This is calling function1"
if __name__=="main":
	print "This is Main function"
else:
	fun()