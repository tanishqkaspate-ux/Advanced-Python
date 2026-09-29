import random

expenses = [random.randint(0, 1000) for _ in range(30)]

print("Daily Expenses for 30 Days:")
print(expenses)

week1 = expenses[0:7]
week4 = expenses[21:28]

print("\nWeek 1 Expenses:")
print(week1)

print("\nWeek 4 Expenses:")
print(week4)

print("\nWeekly Summary:")

for i in range(0, 28, 7):
    week = expenses[i:i+7]
    total = sum(week)
    average = total / 7

    print("Week", i // 7 + 1)
    print("Total:", total)
    print("Average:", round(average, 2))

no_spend_days = []

for i in range(30):
    if expenses[i] == 0:
        no_spend_days.append(i + 1)

print("\nNo-Spend Days:")
if no_spend_days:
    print(no_spend_days)
else:
    print("No no-spend days")

streaks = []
current_streak = 0
start_day = 0

for i in range(30):
    if expenses[i] == 0:
        if current_streak == 0:
            start_day = i + 1

        current_streak += 1
    else:
        if current_streak > 0:
            streaks.append((start_day, i, current_streak))
            current_streak = 0

if current_streak > 0:
    streaks.append((start_day, 30, current_streak))

print("\nNo-Spend Streaks:")

if streaks:
    for start, end, length in streaks:
        print("Day", start, "to Day", end, "=", length, "days")
else:
    print("No no-spend streaks found")
