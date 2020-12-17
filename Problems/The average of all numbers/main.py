a = int(input())
b = int(input())
mod = []
for i in range(a, b + 1):
    if i % 3 == 0:
        mod.append(i)
print(sum(mod) / len(mod))