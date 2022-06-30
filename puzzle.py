#WAP to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def count(head=35,leg=94):
    flag=0
    for i in range(0,head+1):
        chic=i
        if head-chic==(leg-2*chic)/4:
            flag=1
            print("Chickens:",chic,"Rabbits:",head-chic)
    if(flag==0):
        print("No Solution")
    return

a,b=input("Enter no. of heads and legs seperated by space: ").split()
a,b=int(a),int(b)
count(a,b)

