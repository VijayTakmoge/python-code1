a=121
if str(a)==str(a)[::-1]:
     print(a,"its palandrom")
else:
     print(a,"its not palandrom")


positive = []
negative = []
zero = []

a1 = list(range(-25, 26))

for i in a1:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        zero.append(i)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
