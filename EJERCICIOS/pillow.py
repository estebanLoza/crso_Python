# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])

# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints,"r*")

# plt.show()



count = 1

for numeros in range(1, 101):
    if numeros % 3 == 0 and numeros % 5 == 0:
        print("fizzbuzz")
    elif numeros % 3 == 0:
        print("fizz")
    elif numeros % 5 == 0:
        print("buzz")
    else:
        print(f"{numeros}")

