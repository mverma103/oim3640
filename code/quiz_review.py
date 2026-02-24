### Going over quiz 0 - mistakes I made:


def calculate_tip(amount):
    """Calculate Tip"""
    tip = amount * 0.2
    print(tip)
    return(tip)         # this was the problem - we need to return the value back, without it we get an error

price = 50
my_tip = calculate_tip(price)
total = price + my_tip
print(total)

# Draw a triangle from right to left

def draw_triangle(n):
    for i in range(n):
        spaces = " " * (n - i)
        letters = "L" * (i+1)
        print(spaces, letters)

draw_triangle(5)

# reverse triangle frm the other one

def draw_reverse_triangle(symbol, n):
    for i in range(n):
        spaces = " " * (i + 1)
        letters = symbol * (n - i)      # we use n - i to get from 5 to 1
        print(spaces, letters)

draw_reverse_triangle("#", 5)