import itertools

string = input("String to be permuted: ")
resullt = itertools.permutations(string, len(string))

for i in resullt:
    print(''.join(i))