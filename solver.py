def solver(factors, start, end):
    li = []
    for j in factors:
        for i in range(start,end):
            if i % j == 0:
                if i not in li:
                    li.append(i)
    return sum(li)         
       
# print(solver([3, 5, 12], 400, 1842))
print(solver([4, 7, 11], 8912, 40512))

# def test_solver():
#     assert solver.solver([4, 7, 11], 8912, 40512) == 340374916