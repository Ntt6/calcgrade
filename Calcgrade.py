total = 0
for i in range(1, 11):
    mark = float(input(f"Subject {i} mark: "))
    total += mark

avg = total / 10
level = 7 if avg>=80 else 6 if avg>=70 else 5 if avg>=60 else 4 if avg>=50 else 3 if avg>=40 else 2 if avg>=30 else 1
print(f"\nTotal: {total}/1000")
print(f"Average: {avg:.1f}%")
print(f"Level: {level}")
print("PASS" if avg>=30 else "FAIL")
