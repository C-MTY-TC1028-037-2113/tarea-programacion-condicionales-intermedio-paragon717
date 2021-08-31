import math

def main():
    r = float(input("Introduce el radio: ")) 
    x1 = float(input("Introduce x1: ")) 
    y1 = float(input("Introduce y1: ")) 
    x2 = float(input("Introduce x2: ")) 
    y2 = float(input("Introduce y2: ")) 
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    if d>r:
        print("FUERA")
    elif d==r:
        print("SOBRE")
    else:
        print("DENTRO")

if __name__ == '__main__':
    main()
