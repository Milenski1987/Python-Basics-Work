while True:
    number = float(input())
    if number < 0:
        print("Negative number!")
        break

    result = number * 2
    print(f"Result: {result:.2f}")
