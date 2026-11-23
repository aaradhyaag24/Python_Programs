n = int(input("Enter number of terms: "))
s = "1"
for i in range(n):
    print(s)
    result = ""
    count = 1
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            count += 1
        else:
            result += str(count) + s[j]
            count = 1
    result += str(count) + s[-1]
    s = result