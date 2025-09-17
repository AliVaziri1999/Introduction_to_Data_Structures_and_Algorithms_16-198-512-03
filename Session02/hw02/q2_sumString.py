def sumString(N):
    # Base case
    if N == 1:
        return "1"
    else:
        return sumString(N - 1) + "+" + str(N)

# Testing the sumString function
if __name__ == "__main__":
    test_value = 5
    result = sumString(test_value)
    print(f"The sum expression from 1 to {test_value} is: {result}")