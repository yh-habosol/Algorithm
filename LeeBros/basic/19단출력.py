for i in range(1, 20):
    for j in range(1, 20, 2):
        if j != 19:
            print(i, "*", j, "=", i*j , "/", i, "*", j+1, "=", i*(j+1))
        else:
            print(i, "*", j, "=", i*j)
