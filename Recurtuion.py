def fun(k):
    if(k>0):
        result=k+fun(k-1)
        print(result)
    else:
        result=0
    return result
print("The number is")
fun(6)