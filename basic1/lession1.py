programming_languages = "Python", "C++", "Java", "C#" # this is a tuple

print(type(programming_languages)) # prints of the object type

# iteration with for loop
for language in programming_languages:
    print(language)

######## Extended tuple reading ########
t = 12345, 54321, 'hello'
print(t[0]) # indexing a tuple

print(t) # print out all members of the tuple

# nesting a tuple
u = t, (1, 2, 3, 4, 5) # u is a tuple containning another tuple

print(u) 

# index value of a tuple cannot be changed (immutablity)
try:
    t[0] = 8888 # not possible
except Exception:
    # this is meant to catch the TraceBack error message
    print("Tuple value ",t[0], " can't be changed to ", 8888)


