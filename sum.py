#Create an add function that is agnosticto number of inputs.

def My_Custom_Add(a):
    sum=0
    for i in a:
        sum=sum+int(i)
    return sum

a=input("Enter the list of elements to be added seperated by spaces: ").split()
res=My_Custom_Add(a)
print("Resultant is",res)


