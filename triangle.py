#TRIANGLE

def is_valid(a,b,c):
    if(a+b>c and b+c>a and c+a>b):
        return True
    else:
        return False

def triangle_class(a,b,c):
    if is_valid(a,b,c)=='Triangle is Valid':
        if a==b and b==c:
            return 'Equilateral Triangle'
        elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
            return 'Right-Angled Triangle'
        elif a==b or b==c or c==a:
            return 'Isosceles Triangle'
        else:
            return 'Scalene Triangle'
    else:
        return -1

def circumradius(a,b,c):
    if triangle_class(a,b,c)=='Right-Angled Triangle':
        return max(a,b,c)/2
    else:
        return -1
    
def main():
    a,b,c=input("Enter sides of triangle seperated by spaces: ").split()
    a,b,c=int(a),int(b),int(c)
    print(is_valid(a,b,c))
    print(triangle_class(a,b,c))
    print(circumradius(a,b,c))

main()
    
