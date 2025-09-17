def print_figure(N, current=1):
    """Recursive function to print a figure of size N."""
    if current > N:
        return
    print('X' * current)
    print_figure(N, current + 1)

# Example usage
if __name__ == "__main__":
    N = 5
    print_figure(N)