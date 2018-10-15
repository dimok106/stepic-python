s = input()
t = input()

result = 0;
for i in range( len(s)):
    if s.startswith(t,i):
        result= result+1
print(result)
