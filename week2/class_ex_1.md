## 1: which line in list 2 causes it to differ from list 1 ?

````python
l = [num for num in range(4)]
l.append('four')
l.extend([5.0,6])
l += ['7',16/2,[9,10]]
print l
````

````python
y = []
y.extend(range(3))
y.append(['four',5.0])
y += [6,'7',8,[9,10]]
print y
````

## 2: find the sum of all even numbers under 100 that contain a '4' or a '2'

