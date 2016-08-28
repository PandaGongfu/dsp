# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are basically lists that are cannot be modified. Only tuples can be keys in dictionaries because of their immutability. Dictionaries hash their keys and the contents of the keys cannot be changing, otherwise hashing does not work. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered lists with unique elements, and they can only contain hashable items.  
   Unlike a list,  
   ``` 
   set([6,2,4,4]) == set([2,4,6])
   ```
   Like a list, a set also supports comprehension.  
   ```
   set(x for x in 'abrcdra' if x not in 'abc')
   ```
   Sets are much faster for lookup because they use hash table so it's O(1) time versus O(n) of lists.
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A `lambda` function is basically a function without a name. Because python supports functional programming, lambda functions can be combined other functions and therefore, extremely useful.   
   ```
   sorted(list(range(3,15)), key = lambda x: x/(math.log(x)**2))
   ``` 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions provide a succinct and elegant syntax for tranforming lists.   
   ```
   odd_power = [n**2 for n in nums if n%2]
   odd_power = map(lambda x: x**2, filter(lambda x: x%2, nums))
   ```
   The above two lines produce duplicate results.
   However, map and filter can handle more complicated conditions with the assistance of lambda functions, for instance, if the condition is expressed in if..elif..else, list comprehension may not be able to handle it.  
   Set comprehension has been demonstrated in Q2.   
   Dict comprehension is shown below:
   ```
   dict((k, k) for k in nums)
   ```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 917

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





