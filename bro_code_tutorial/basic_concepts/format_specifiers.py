# format specifiers = {value:flags} format a value based on what flags are inserted (used in the context of an string interpolation)
# format specifiers can be mixed and matched

# ADDING DECIMAL POINT PRECISION --> round to that many decimal places (fixed point)
# .(number)f

# ALLOCATING SPACE TO DISPLAY A VALUE --> enter a number to allocate that many spaces
# :(number)

# ALLOCATING SPACE AND ZERO PADDING --> enter a number preceeded by 0  to allocate and zero pad that many spaces
# :(0number)

# LEFT JUSTIFY A VALUE
# :<

# RIGHT JUSTIFY A VALUE
# :>

# CENTER ALIGN A VALUE
# :^

# INDICATING POSITIVE VALUES --> use a plus sign to indicate positive value
# :+

# ??? probably added from a different video, let's see...
# := = place sign to leftmost position

# INDICATING POSITIVE VALUES --> it can also be done using a space
# : = insert a space before positive numbers

# COMMA (THOUSANDS) SEPARATOR --> use a comma to separate each thousands place
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# ADDING DECIMAL POINT PRECISION
# print(f"Price 1 is ${price1:.2f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.3f}")

# ALLOCATING SPACE TO DISPLAY A VALUE
# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")

# ALLOCATING SPACE AND ZERO PADDING
# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")

# LEFT JUSTIFY A VALUE (with space allocation)
# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:<10}")

# RIGHT JUSTIFY A VALUE (with space allocation); it's the default?
# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")

# CENTER ALIGN A VALUE
# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")

# INDICATING POSITIVE VALUES (using a + sign)
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")

# INDICATING POSITIVE VALUES (using a space)
# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")

# COMMA (THOUSANDS) SEPARATOR
# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")

# MIXING AND MATCHING FLAGS
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
