import math
ab=int(input())
bc=int(input())
ac=(ab*ab+bc*bc)**(1/2)
t=math.acos(bc/ac)
t=t*180/math.pi
t=round(t)
print(str(t)+u"\N{DEGREE SIGN}")
