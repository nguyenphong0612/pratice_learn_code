List = [5,4,3,2,1,0]
smallest = List[0]
for i in range(len(List)-1):
    smallest = List[i]
    for j in range(i+1, 6):
        if List[j] < smallest:
            smallest = List[j]
            List[j], List[i] = List[i], smallest
print(List)           
