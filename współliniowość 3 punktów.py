class Punkt:
    def __init__(self):
            self.x=0.0
            self.y=0.0
 
def det(a,b,c):
    d= a.x*b.y + b.x*c.y + b.x*a.y
    d-=a.x*c.y + b.x*a.y + c.x*b.y
    return d


a=Punkt()
c=Punkt()
b=Punkt()
print("podaj x1")
a.x=float(input())

print("podaj y1")
a.y=float(input())

print("podaj x2")
b.x=float(input())

print("podaj y2")
b.y=float(input())

print("podaj x3")
c.x=float(input())

print("podaj y3")
c.y=float(input())

if det(a,b,c):
    print("Punkty sa wspolliniowe")
else:
    print("Punkty nie sa wspolliniowe")
        

