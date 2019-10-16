import samplemodule
import inspect

x = samplemodule.X('new obj of X')
for name, data in inspect.getmembers(x,inspect.isfunction):
	# if name.startswith('__'):
		# continue
	print(f"{name} : {data}")
print(samplemodule.X.__doc__)
print(inspect.getdoc(samplemodule.X))

print(inspect.getsource(samplemodule.X))