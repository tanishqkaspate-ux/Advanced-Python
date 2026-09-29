import random

durations = [random.randint(2, 8) for _ in range(50)]

print("Track Durations:")
print(durations)

time_limit = 60

memo = {}

def max_tracks(i, remaining_time):
    if i >= 50 or remaining_time <= 0:
        return 0
    if (i, remaining_time) in memo:
        return memo[(i, remaining_time)]

    skip = max_tracks(i + 1, remaining_time)

    take = 0

    if durations[i] <= remaining_time:
        take = 1 + max_tracks(i + 2, remaining_time - durations[i])

    memo[(i, remaining_time)] = max(skip, take)

    return memo[(i, remaining_time)]


result = max_tracks(0, time_limit)

print("\nTime Constraint:", time_limit, "minutes")
print("Maximum number of non-adjacent tracks:", result)

print("\nNumber of memoized subproblems:", len(memo))
