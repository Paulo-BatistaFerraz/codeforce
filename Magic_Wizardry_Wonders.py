def reconstruct_cards(n, d, l):
    # Initialize the array with all elements as 1
    a = [1] * n

    # Calculate initial sums for odd and even indexed positions
    sum_odd = (n + 1) // 2  # Number of odd positions
    sum_even = n // 2       # Number of even positions

    # Determine starting position based on the sign of d
    if d > 0:
        i = 0  # Start adjusting odd indices
    elif d < 0:
        i = 1  # Start adjusting even indices
    else:
        if n % 2 == 1:  # For n odd, start from the last odd index
            i = n - 1
        else:
            i = 0  # For n even, start from the first odd index

    # Adjust values to balance the sums to achieve d
    while i < n:
        if sum_odd - sum_even == d:
            break  # Target difference achieved
        while a[i] < l and sum_odd - sum_even != d:
            a[i] += 1
            if i % 2 == 0:
                sum_odd += 1  # Adjusting an odd position
            else:
                sum_even += 1  # Adjusting an even position
        i += 2  # Move to the next odd/even index

    # If it's not possible to achieve the desired difference
    if sum_odd - sum_even != d:
        return -1

    # Return the resulting array
    return a


# Input handling
if __name__ == "__main__":
    while True:
        try:
            n, d, l = map(int, input().split())
            result = reconstruct_cards(n, d, l)
            if result == -1:
                print(-1)
            else:
                print(" ".join(map(str, result)))
        except EOFError:
            break


