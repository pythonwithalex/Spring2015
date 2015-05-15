## Python Sorted function explored in some depth

The core principle at work in sorting is the comparison of two values.  

#### Sorting a List of Tuples

If we sort a list of tuples, Python compares the first item in each.  If there is a tie, it compares the second items in the sequences being compared:

````
mylist = [ (0, 'z'), (0,'a') ]
print sorted(mylist)
# prints [(0, 'a'), (0, 'z')]
````

The zeros tied, so the secondary keys 'z' and 'a' were compared to determine the order of the overall sequence. 
You will remember from yesterday that the conceptual idea behind how sorting is achieved is the transformation of each value in a sequence into something that is then sortable.  Usually a comparison ultimately involves two numeric values. 
When comparing 'alpha' and 'zebra', this might be a sketch of the internal representation of what's going on:

(97, 108, 112, 104, 97, 122) -> alphaz

(97, 108, 112, 104, 97, 115) -> alphas ** WINNER **

In the case of 'alphaz' and 'alphas' above, the items are compared one element at a time until one of their elements differ, at which point the original value to which the smaller one belongs is inserted first into the final sorted list (assuming we are using the default 'ascending' order).



## Sorting with a Custom Function using two Keys

The examples above didn't involve using a custom function, so let's do that.  We could write a redundant function that gets the same exact results that sorted gets by default:

````
def custom(item):
    return item
````

This is useless right? Well, no. It's great, because we can generate the same default sorted behavior ourselves.  When would this be appropriate? 

What if we wanted to sort by length, but if two items have the same length, sort them by alphabetical order.  What we want to make use of is the 'fallback' logic above where the next element is compared in the case of a tie.  Let's write a custom function that produces two values, not just one.  This way, the transformed values are tuples and are compared in the same way that mylist above is compared. There are no parenthesis in the return statement from custom, but understand that it's returning a tuple containing first the integer length of the word and second, a tuple of ascii values that represent each letter in the word. 

````
def custom(item):
    return len(item), item
````

Here's my conceptual representation of what python is doing:

( 6, (97, 108, 112, 104, 97, 122) ) -> alphaz

( 6, (97, 108, 112, 104, 97, 115) ) -> alphas



Here's a sort to show the end result conforms with the representation above.

````
sorted(['alphaz','alphas','mint','mine'] ,key=custom)

['mine', 'mint', 'alphas', 'alphaz']
````
