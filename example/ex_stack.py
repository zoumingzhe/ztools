from ztools import stack

s = stack()
s.Version(isShow = True)

print(s.get())
s.put(1)
print(s.get())
s.put(2)
s.put(3)
s.put(4)
print(s.get())
s.put(5)
print(s.get())
print(s.get())
print(s.get())
print(s.get())
print(s.get())


input()
