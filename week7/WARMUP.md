## Warmup

## List Comprehensions and Filter

#### If I want to construct a list of odd numbers under 100, I can do it like this:

#### 1 : for loop with conditional
    odds = []
    for i in range(100):
        if i%2 == 1:
            odds.append(i)
    print odds
      

I can do this in at least two other ways:

#### 2 : List Comprehension

    odds = [i for i in range(100) if i%2 == 1]
    print odds

#### 3 : using filter()

filter() takes 2 arguments, a function and an iterable
ex. filter(isOdd,range(10))

    def isOdd(num):
        return num%2 == 1

    odds = filter(isOdd,range(100))
    print odds

## Warm-up Exercise

#### Now try this out in two separate ways (using 2 and 3 as examples)

sentence = 'A kilogram weights 2.2 pounds and 1 pound is .45 kilograms'

#### problem : use a list comprehension and then filter() to generate a list 'longEnough' that holds words in the string 'sentence' that are longer than 2 characters.
