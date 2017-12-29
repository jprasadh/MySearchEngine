# Defining the variables based on scalar "sand" doesn't permit aliasing
x = "sand"
y = x
x = "sandbox"
print(x, y)

# Now note that 1x1 array ["sand"] has two aliases, p and q
p = ["sand"]
q = p
p[0] = "sandbox"
print(p, q)
