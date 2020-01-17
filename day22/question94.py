
def comput():
    for x in range(1, 36):
        for y in range(1, 36):
            if (x + y) == 35 and (2*x + 4*y) == 94:
                print((x, y))
                return


comput()
