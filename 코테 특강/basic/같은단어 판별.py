str1 = input()
str2 = input()

if len(str1) != len(str2):
    print("No")
else:
    if "".join(sorted(str1)) == "".join(sorted(str2)):
        print("Yes")
    else:
        print("No")