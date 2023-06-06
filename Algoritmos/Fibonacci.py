n = 3
f0 = 0
f1 = 1
print(f0)
print(f1)
for i in range(n):
    fn = f0 + f1
    f0 = f1
    f1 = fn
    print(fn)