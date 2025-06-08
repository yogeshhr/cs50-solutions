def check_input():
    while True:
        try:
            x = int(input("x : "))
            if x > 0 and x < 9:
                return x
            elif x > 8:
                print("please enter valid number (1-8)")

            else:
                print("please enter a positive number greater that 0 (1-8)")
        except ValueError:
            print("invalid input. Please enter a positive integer (1-8)")


x = check_input()
for i in range(x):
    print((x-i-1)*" ", end="")
    for j in range(i+1):
        print("#", end="")
    print()
