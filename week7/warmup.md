## Warmup

The List Comprehension

## if I want to construct a list of odd numbers under 100, I can do it like this:

odds = []
for i in range(100):
    if i%2 == 1:
        odds.append(i)
print odds
      

I can do this in at least two other ways:

#### 1

odds = [i for i in range(100) if i%2 == 1]
print odds

#### 2

def isOdd(num):
    return num%2 == 1

odds = filter(isOdd,range(100))
print odds
