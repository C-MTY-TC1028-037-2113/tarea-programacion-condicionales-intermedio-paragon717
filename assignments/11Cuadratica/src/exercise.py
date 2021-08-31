import math

def main():
    a = int(input("Inserta a: "))
    b = int(input("Inserta b: "))
    c = int(input("Inserta c: "))

    if a==0 and b==0:
        print("No tiene solución")
    elif a==0 and b != 0:
        u = -c/b
        print(u)
    else: 
        dis = b**2 - 4 * a * c
        if dis <0:
            print("Raices complejas")
        elif dis >0:
            x1 = -b + math.sqrt(dis) / 2 * a
            x2 = -b + math.sqrt(dis) / 2 * a
            print(x1)
            print(x2)
        else:
            x = -b / 2 * a
            print(x)

