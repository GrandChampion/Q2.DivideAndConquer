def divide(L,k)->int:
    pivot = L[0]
    Lesser = [i for i in L if i<L[0]]
    Greater = [i for i in L if i>L[0]]

    if len(Lesser) == k-1:
        return pivot
    elif len(Lesser) > k-1:
        return divide(Lesser,k)
    else:
        return divide(Greater,k-(len(Lesser)+1))
    
print(divide([3,2,5,6,1,26],2))