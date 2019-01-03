print "This is init file"
# Why is the need of of __Init__ file if we are not doing anyhting in __init__
# init can be used for the sequence of execution of files 
#__init__ will creatr Mod 1 stack and f1 and f2 in Stack
import f1
import f2
#from f1 import fun1 # importing only function from f1, this will create fun1() in stack
#from f1 import fun1()

## Conclusion: Never Import files in Init file## See notes 14h oct