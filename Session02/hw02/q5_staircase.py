def climbCount(n):
    # Base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # Recursively calculate the number of ways to climb the staircase
        return climbCount(n - 1) + climbCount(n - 2) + climbCount(n - 3)


# Testing the function
if __name__ == "__main__":
    n = 4
    print(f"Number of ways to climb {n} steps: {climbCount(n)}")