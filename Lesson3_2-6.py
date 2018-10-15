s = input()
a = input()
b = input()
result = ""
if a in s:
    if a in b :
        result = "Impossible"
    else:
        result =0
        while a in s:
            s = s.replace(a, b)
            result = result +1
            if result > 1000:
                result = "Impossible"
                break

else:
    result = 0

print(result)
