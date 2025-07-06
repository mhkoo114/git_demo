import random
total = 12000
for i in range(1,21):
    score = random.randint(1,10)
    if score < 5:
        print(f"Worker {i} scores {score}, not eligible.")
        continue
    if total >= 1000:
        total-=1000
        print(f"Worker {i} scores {score}, paid 1000, now total is {total}")
    else:
        print(f"Total is only {total}, not enough for next paid.")
        break