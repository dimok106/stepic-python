ans = 0
parsed_objects = []
for obj in objects:
    add = True
    for parsed in parsed_objects:
        if obj is parsed :
            add = False

    if add ==True :
        parsed_objects.append(obj)
        ans += 1

print(ans)
