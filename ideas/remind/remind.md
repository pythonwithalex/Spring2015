## remind.py

#### topics
+ command line arguments
+ datetime library
+ string formatting
+ functions
+ default arguments
+ calendar.txt is a file that has a date and a task informatino separated by a comma

````
3/29/2015, interview
4/5/2015, sister's birthday
6/7/2015, going to western ma for the weekend 

````

+ running remind.py parses the calendar.txt file and outputs a sentence like 'Going to Western MA for the weekend in 13 days'

+ remind.py should have a default time window prior to each date to remind you of that event.   However, allow that to be overridden with command line arguments, 'e.g': `remind.py -d 2`, which would tell you the things you have scheduled that fall within 2 days of running the script. 

write a program that parses this information and ouputs a reminder 
