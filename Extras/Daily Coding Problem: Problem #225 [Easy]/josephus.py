# This problem was asked by Bloomberg.

# There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

# Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

# For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

def last_survivor_position(N, k):
    if k == 1:
        return N

    def josephus(n, k):
        if n == 1:
            return 0
        else:
            return (josephus(n - 1, k) + k) % n

    return josephus(N, k) + 1

print(last_survivor_position(5, 2))  # Output: 3
print(last_survivor_position(10, 3))  # Output: 4