'''Base ball scores  '''
def points_calculator(scores):
    stacker = []
    for entry in scores:
        if entry=='C':
            stacker.pop()
        if entry=='D':  
            stacker.append(stacker[-1]*2)
        if entry=='+':
            stacker.append(stacker[-1]+stacker[-2])    
        else:
            stacker.append(entry)
    return sum(stacker)        

'''Next closest time '''
def nextClosestTime(time):
    times=time.split(':')
    digits=[int(y) for x in times for y in x] 
    hh,mm=times[0],times[1]
    while True:
        if int(mm)+1 > 59:
            hh,mm = str(int(hh)+1),'00'
        else:
            hh,mm = hh,str(int(mm)+1)
        if int(hh) > 23:
            hh ='00'
        if len(hh) == 1:
            hh = '0' + hh
        if len(mm) == 1:
            mm = '0'+ mm
        if all([int(x) in digits for x in hh+mm]):
            return hh+':'+mm    



