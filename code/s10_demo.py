count = 0
for letter in 'Babson College':
    count += 1
print(count)

print(len('Babson College'))



def uses_any(word, letters):
    if letter in letters:
        return True
    else:
        return False

print(uses_any('aurora', 'aeiou'))
