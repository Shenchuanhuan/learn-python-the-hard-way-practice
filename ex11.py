# raw_input is python2 function
# input is python3 function

print("how old are you?"),
age = input()
print("how tall are you?"),
height = input()
print("how much do you weight?"),
weight = input()

print("so, you're %r old, %r tall and %r heavy." % (
    age, height, weight
))
