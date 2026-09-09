from array import array

# 1. Initialize an array for floating-point (decimal) numbers
scores = array('f', [])

# 2. Get 5 scores from the user
print("Enter 5 test scores:")
for i in range(5):
    score = float(input(f"Score {i + 1}: "))
    scores.append(score)

# 3. Calculate total and average
total = 0.0
for s in scores:
    total += s

average = total / len(scores)

# 4. Count scores above average using conditional logic
above_average_count = 0
for s in scores:
    if s > average:
        above_average_count += 1

# 5. Output results
print("\n--- Results ---")
print(f"All Scores: {list(scores)}")
print(f"Average Score: {average:.2f}")
print(f"Scores Above Average: {above_average_count}")