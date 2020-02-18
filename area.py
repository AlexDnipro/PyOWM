from math import pow, pi
def rectsquare():
    height = float(input("Please enter height:"))
    width =  float(input("Please enter width:"))
    return height * width

def triangle():
    h = float(input("Please enter height:"))
    base = float(input("Please enter base:"))
    return  0.5 * h * base

def areacircle():
    #PI = 3.14
    radius = float(input("Please enter radius:"))
    return round(pi * pow(radius, 2), 2)

def squarefind():
    choice = float(input("choose 1 - Rectangle 2 - Triangle 3 - Circle:" ))
    if choice == 1:
        return rectsquare()
       
    elif choice == 2:
        return triangle()
        
    elif choice == 3:
        return areacircle()

print(squarefind())