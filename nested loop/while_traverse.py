s = "MISSISSIPPI"

target = input("Enter character: ")

count = 0

for ch in s:
    if ch == target:
        count += 1

print(count)