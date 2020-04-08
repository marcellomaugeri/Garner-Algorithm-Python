'''
Copyright (c) 2020 Marcello Maugeri <maugeri.marcello@studium.unict.it>
This software is distributed under GNU GPL v3
More info at <https://github.com/Maray97/Garner-Algorithm-Python>
'''

import re
import math
system=[]

def modInverse(a, n): 
    a=a%n
    for x in range(1, n): 
        if ((a*x)%n == 1): 
            return x 
    return None

def eqToString(eq):
    if(eq[0]==1): 
        return "x = "+str(eq[1])+" mod "+str(eq[2])
    return str(eq[0])+"x = "+str(eq[1])+" mod "+str(eq[2])

def stringToEq(eq):
    eq=eq.split()
    if(eq[0]=="x"):
        a=int(1)
    else:
        a=int(eq[0].strip('x'))
    b=int(eq[2])
    c=int(eq[4])
    eq=[a,b,c]
    return eq

def checkCoprime(system):
    for i in range(len(system)):
        for j in range(i+1, len(system)):
            if math.gcd(system[i][2],system[j][2]) != 1:
                return False
    return True

def garner(system):
    if(checkCoprime(system)):
        N=1
        h=[0]*len(system)
        for x,a,n in system:
            N=N*n
            
        for i in range(1, len(system)):
            h[i]=1
            for j in range(0, i-1):
                t=modInverse(system[j][2], system[i][2]) 
                h[i]=(t*h[i])%system[i][2]

        t=system[0][1]
        x=t
        for i in range(1, len(system)):
            t=((system[i][1]-x)*h[i])%system[i][2]
            mul=1
            for j in range(0, i):
                mul=mul*system[j][2]
            x=x+t*mul
        return [x,N]
    return None

print("Enter '[a]x = [b] mod [n]' equations one at a time, when you're ready enter 'go' ")
while True:
    ins=input()
    if ins == "stop" or ins == "Stop" or ins == "go":
        break
    match = re.compile(r'\d{0,100}x = \d{1,100} mod \d{1,100}') 
    result = match.search(ins)
    if result is not None:
        system.append(stringToEq(result.group()))
res=garner(system)
if res is not None:
    print("x="+str(res[0])+" mod "+str(res[1]))