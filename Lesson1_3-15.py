def foo (n,k):
    if(k == 0):
        return 1
    if(k>n):
        return 0

    result = foo(n-1,k)+ foo(n-1,k-1)



    return result



n, k = map(int, input().split())


print(foo(n,k))
