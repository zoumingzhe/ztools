from ztools import queue

q = queue()
q.Version(isShow = True)

print(q.get())
q.put(1)
print(q.get())
q.put(2)
q.put(3)
q.put(4)
print(q.get())
q.put(5)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())


input()
