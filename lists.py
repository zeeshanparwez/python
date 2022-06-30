#Take two lists of input and generate a list of tuples that are combo of the numbers such that the two numbers in the pair are not equal

x=list(map(int,input("Enter a list of nos. seperated by spaces: ").split()))
y=list(map(int,input("Enter another list of nos. seperated by spaces: ").split()))
print([(i,j) for i in x for j in y if i!=j])



