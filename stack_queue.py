#---------- stack ---------# 

# CREATION
s = []   # empty stack initialized
s.append('a')
s.append('b')
s.append('c')

print('initial stack is: \n \t',s)

# POPING
print(s.pop())
print(s.pop())
print(s.pop())

print("stack after elements are popped: \n \t", s)

#---------- queue ----------#

# CREATION
q = [] # empty queue initialized
q.append('a')
q.append('b')
q.append('c')

print("initial queue is: \n \t", q)

# DEQUEING
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print("queue after elements are Dequeued: \n \t", q)