#Check if a given input no. is a perfect square

num=int(input("Enter a number: "))
temp=num**0.5
if(num==(temp**2)):
    print("PERFECT SQUARE")
else:
    print("NOT A PERFECT SQUARE")
