# arithmetic operators 

x= 10
y= 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

#comparison operators 

print(x==y) #false
print(x<y) #false
print(x>y) #true

# logical operators 

print("AND Operator Result ", x>y and x<y) #false
print("OR Operator Result ", x>y or x<y) #true
print("Not Operator Result", not(x>y)) #false

# Assignment operator 

a= 2
b= 3

a= a+6
a+=6


a= a-1
a-=1

a=a/10
a/=10

a=a*10
a*=10


#Bitwise operators
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)


# Bitwise <<(left shift) operator shifts the bits of the number to the left by specified number of positions.
a = 5 # 5 in binary is 0101
print("Left shift by 1:", a << 1) # 0101 becomes 01010 which is 10 in decimal
print("Left shift by 2:", a << 2) # 0101 becomes 010100 which is 20 in decimal

# Bitwise >> (right shift) operator shifts the bits of the number to the right by specified number of positions.
b = 20 # 20 in binary is 10100
print("Right shift by 1:", b >> 1) # 10100 becomes 1010 which is 10 in decimal
print("Right shift by 2:", b >> 2) # 10100 becomes 101 which is 5 in decimal

#Bitwise ^ (XOR) operator compares each bit of the two numbers and returns 1 if the bits are different, otherwise returns 0.
c = 5 # 5 in binary is 0101
d = 3 # 3 in binary is 0011
print("XOR of 5 and 3:", c ^ d) # 0101 XOR 0011 gives 0110 which is 6 in decimal

# Swap numbers without temp variable using ^ XOR operator:
a=5
b=3

print(f"Print a, b --> {a}, {b}") #a=5 (0101) and b=3 (0011)

a=a^b
print(f"Print a, b --> {a}, {b}") #a=6 (0110) and b=3 (0011)

b=a^b
print(f"Print a, b --> {a}, {b}") #a=6 (0110) and b=5 (0101)

a=a^b
print(f"Print a, b --> {a}, {b}") #a=5 (0101) and b=6 (0110)

