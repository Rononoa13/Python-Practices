num_strings = ['March', 'Jan', 'Feb', 'Dec']

print(f"The variable num_strings is a {type(num_strings)}.")
print(f"It contains elements: {num_strings}")
print(f"The element {num_strings[0]} is a {type(num_strings[0])}")

num_ints = [15, 100, 55, 42]

print(f"The variable num_strings is a {type(num_ints)}.")
print(f"It contains elements: {num_ints}")
print(f"The element {num_ints[0]} is a {type(num_ints[0])}")

num_floats = [2.2, 1.0025, 5.5, 0.1242]

print(f"The variable num_strings is a {type(num_floats)}.")
print(f"It contains elements: {num_floats}")
print(f"The element {num_floats[0]} is a {type(num_floats[0])}")

num_lists = [[1,2,3], [4,5,6], [7,8,9]]

print(f"The variable num_strings is a {type(num_lists)}.")
print(f"It contains elements: {num_lists}")
print(f"The element {num_lists[0]} is a {type(num_lists[0])}")

print("Now sorting num_strings and num ints...")
num_strings.sort()
num_ints.sort()
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")