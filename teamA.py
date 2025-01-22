# 3
# 1 1 0
# 1 1 1
# 1 0 0

#output

# 2
# 1 0 0
# 0 1 1

# Read the number of problems
n = int(input())

# Initialize a counter for the number of problems to solve
count = 0

# Process each problem
for _ in range(n):
    # Read the confidence levels of Petya, Vasya, and Tonya
    a, b, c = map(int, input().split())
    
    # Check if at least two friends are sure about the solution
    if a + b + c >= 2:
        count += 1

# Output the total count
print(count)



# first, read the total number of problems
# the n line of inputs of each line represents the confidence of the three friends
#
# https://codeforces.com/problemset/problem/231/A



