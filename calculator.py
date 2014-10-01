def divition (a , b):
    c = float(a) / float(b)
    return c

def Plus(a, b):
    c = a + b
    return c

def Minus(a, b):
    c = a - b
    return c

def multiplikation(a, b):
    c = a * b
    return c

def pow(a,x):
    b = a**x
    return b

def Summan( *MyList ):
    c = sum(MyList)
    return c

def Medeltal( *MyList ):
    for i in MyList:
        c = sum(MyList)/len(MyList)
    return c

def Median(*MyList):
    i = len(MyList)
    if not i%2:
        return (MyList[(i/2)-1]+MyList[i/2])/2
    return MyList[i/2]
