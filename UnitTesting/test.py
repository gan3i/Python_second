

# strint = ["BA","CB","AA"]
# d = []
# for i in strint:
#     d.insert()

# print(strint = strint[::-1])

# print(sorted(d))

dictionary = {6: ['monday', 'coffee', 'strong'], 5: ['short'], 3: ['may', 'and']}

def print_keys_values_inorder(dictionary):
    for key in sorted(dictionary):
        # print(key, ' '.join(map(str, sorted(dictionary[key]))))
        print(key, *sorted(dictionary[key])) # "*" is used to print list elements in single line with space.

print_keys_values_inorder(dictionary)
