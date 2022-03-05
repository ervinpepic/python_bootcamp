keys = ["a", "b", "c", "d", "e", "f", "g"]
keys_tuples = ["do", "re", "mi", "fa", "so", "la", "ti"]
slice_keys = keys[2:5]
slice_keys_2 = keys[:5]
slice_keys_3 = keys[2:]
slice_keys_4 = keys[2:5:2]
slice_keys_5 = keys[::-1]

print(slice_keys)
print(slice_keys_2)
print(slice_keys_3)
print(slice_keys_4)
print(slice_keys_5)

print(keys_tuples[2:5])