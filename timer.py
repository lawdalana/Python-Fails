#Gay and barebones Timer.#
import time
def timre(x,y=1):
   while x>=0:
      time.sleep(y)
      print(x," Seconds left...")
      x-=1
  
#I know its misspelled btw#   
def delay(X,y=1):
   while x>0:
      time.sleep(y)
      x-=1
      
def onesec():
   time.sleep(1)
   print("done")

def rep(func,x):
   def reprep():
      for i in range(x):
         func()
   return reprep
#don't know why but last function doesn't #
#pls help#
      
# You can call rep function like this
func_reprep = rep(onesec, 10)
func_reprep()  # use () for call function work

# Or call function on funciton rep 
# def rep(func,x):
#    def reprep():
#       for i in range(x):
#          func()
#    return reprep()