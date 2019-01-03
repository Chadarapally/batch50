print ("Calling File1:")
import File1
#import Mod1 # Error
#import Mod1.f1 # Error
#from Mod1 import f1 # Error
# Step:2 Remove f1 and f2 from Mod1 and add __init__.py
# now run app2
#import Mod1 # No Error
# now create f1 and f2 in Mod1
# run app2 again, still it runs only init file not f1 and f2 files
#import Mod1
#Mod1.f1.fun1() # Error
#from Mod1 import f1 # run only f1
#f1.fun1()
from Mod1 import f1,f2
f1.fun1()
f2.fun2()
print ("Thank you")
