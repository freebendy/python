def hello(x):
    helloStr = "hello,wolrd from helloworld.py."
    if x>0:
        print "x>0", helloStr
    elif x<0:
        print "x<0", helloStr
    else:
        print "x=",x, helloStr
        
def minus():
    x = 0;
    y = 0;
    while(x <= 9):
        while(y <= 9):
            if(y == 4):
                print x, "*", y, "=", x * y
            else:
                print x, "*", y, "=", x * y, ' ',
            y = y + 1
        print 
        x = x + 1
        y = 0