## Functions

A function is defined like this:

````python
def makePerson(<arg1>,<arg2>,<arg3>, ...):

    name=<arg1>
    independent = False
    age=<arg3>
    if age >= 18:
        independent = True
    height=<arg2> 
    person = list(independent,age,name,height)
    return person
````

## Main points there:

+ A function definition is needed to create your own function
+ a function definition starts with `def <function_name>()`
+ A function does not require input values, but if you want take in input values, put them separated by a comma inside the `()`.
+ Indent 4 spaces to start. Indent 4 more spaces for each inner loop.
+ type lines of code

````python
people = []
names = ['make','bobby','zan','beatrice','markus']:
for first_name in names:
    age = random.randrange(4,100)
    feet = random.randrange(4,8)
    inches = random.randrange(0,11) 
    height_string = '{}ft, {}in'.format(feet,inches)

    # And here we call the makePerson function.

    people.append(makePerson(first_name,age,height_string))
````

Question:

We didn't need the function makePerson to make Mike.  Why did we use the function?

Your Challenge:

Write a program that doubles the square of a third of the reverse of the max of this list: [01,94,30,3.0,53]. It should have five functions that do the work of accepting arguments and calling them, plus a main function that 'wraps' the program.

Please try any approach you like but don't do this: 

def main():

    return func5(func4(func3(func2(func1()))))

main()

# variations:
# while loop f[num]()
# for loop num()
'''
