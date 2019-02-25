import math
#program for solving stiangles using the law of sines
sides = []
angles = []
anchor = 0
mode = 0
def getall():

    names = ["A","B","C"]
    sideNames=["a","b","c",]
    for i in names:
        e = input("what is side " + i + "? ")
        if e == 'x':
            sides.append('x')
        else:
            sides.append(int(e))
       
            
    for i in sideNames:
        d = input("what is angle " + i + "? ")
        if d == 'x':
            angles.append('x')
        else:
            angles.append(int(d))

def errorCheck():
    for i in sides:
        if i != 'x' and i < 0:
            print("Sorry, there can't be negative sides.")
    for i in angles:
        if  i != 'x' and ((i < 0) or (i > 180)):
            print("sorry, invalid angles.")
def findAnchor():
    getall()
    for i in range(4):
        if sides[i] != 'x' and angles[i] != 'x':
            anchor = i
            break
        else:
            mode = 'findanchor'
findAnchor()
print(sides[:])
print(angles[:])
print(anchor)
print(mode)
