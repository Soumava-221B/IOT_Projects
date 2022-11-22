import _thread
import utime

num = [2,3,4,5]

def calc_square():
    global num
    print("calculate square of numbers")
    for i in num:
        utime.sleep(1)
        print("square: ",i*i)
        
def calc_cube():
    global num
    print("calculate cube of numbers")
    for i in num:
        utime.sleep(1)
        print("cube: ",i*i*i)
        

t = utime.time()
_thread.start_new_thread(calc_square, ())

#calc_square()
calc_cube()

print(utime.time()-t)
print(t)