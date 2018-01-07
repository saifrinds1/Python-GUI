def frange(arg0, arg1=None, arg2=None):
    start = 0.0
    step = 1.0
    
    if arg2 is not None:
        start = arg0
        stop = arg1
        step = arg2

    elif arg1 is not None:
        start = arg0
        stop = arg1

    else:
        stop = arg0

    result = []
    while start < (stop - (step/2.0)):
        result.append(start) 
        start += step
    return result

for x in frange(10): 
    print("X is now  %d ",x)
