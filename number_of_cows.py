#!/user/bin/python3

""" This solves the problems of cows"""

for i in range(21):
    for j in range(34):
        for k in range(100):
            if i + j + k == 100:
                if 5*i + 3*j + k/5 == 100:
                    print(i,j,k)
