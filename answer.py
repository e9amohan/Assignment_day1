def answer():
    li = []
    for i in range(1000):
        if i % 3 == 0:
            li.append(i)
        elif i % 5 == 0:
            if i not in li:
                li.append(i)
    return sum(li)

print(answer())