import numpy 
import matplotlib.pyplot as plt # our shortcut for matplotlib.pyplot

def example1():
    x = numpy.linspace(0,5,20)      #create our first array
    y = x**2    #this is how Python does exponents
    plt.plot(x,y)           #create the plot
    plt.show()              #show the plot

def example2():
    x = 5
    y = 5.0
    z = 'five'
    print type(x) # from standard library
    print type(y)
    print type(z)

def example3(): #to show i changes 
    i=3
    print i
    for i in range(6):
        print i
        a=2.5
    print 'i=',i,'a=',a

def example4():
    x = 5
    peanut = 7

    if x > peanut:
        print "x is greater than 7"
    
    elif x < peanut:        #note that Python contracts else if to elif
        print "x is less than 7"
    
    else:
        print "x is equal to 7"

def add_two_numbers(a,b):
    sum = a + b
    return sum
    
#print add_two_numbers(4,6)

def example5():
    my_array = numpy.array([1, 2, 3, 4, 5])
    print my_array[2]
    print my_array[:]
    print my_array[0:3]
    print my_array[3:]

def example6():
    print 1 == 1 #True
    print (1 == 1) == 1 #True
    print (1 == 1) == True #True
    print 1 != 1 #False
    print (1 != 1) == 0 #True
    print (1 != 1) == False #True
    print True == 1 #True
    print False == 0 #True
    print True == 5 #False
    print 1 and 1 #1
    print 1 and 0 #0
    print 1 or 0 #1

def example7(): # !!! assignments are pointers, they don't make copies
#in python a variable, array, string, etc are objects
#assignments give a name to that object, or that "points" to it.
#copy creates another object identical to the first one
    a = numpy.array([1, 2, 3])
    b = a
    c = a.copy()
    b[1] = 7 # this changes both a and b, because they are the same object!!
    c[1] = 4 # this changes only c
    print a #[1 7 3]
    print b #[1 7 3]
    print c #[1 4 3]


example6()
