result = None

a = input("a > ")
b = input("b > ")

if all(map(str.isdigit, (a, b))):
    a = int(a)
    b = int(b)

    if a > 0 and b > 0:
        if a < b:
            result = a / b + 1
        elif a == b:
            result = -1
        else:
            result = (a * b - 5) / a

        print(result)
    else:
        print("Number should be more than 0...")
else:
    print(f"\nBad input...\n\tData: a = {a}\tb = {b}")

