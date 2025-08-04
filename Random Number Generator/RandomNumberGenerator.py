import random
n=int(input("Enter the number of random numbers to generate: "))

l=[random.randint(1,100) for i in range(n)]
for i in l:
    if i>90:
        print(i, "---> It is your lucky day!")
    else:
        print(i, "---> Better luck next time!")
