numcalls = 0
def square(x):
    global numcalls
    numcalls=numcalls + 1
    return x*x

print square(5),numcalls
print square(2*5),numcalls
