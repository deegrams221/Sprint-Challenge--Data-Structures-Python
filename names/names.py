import time
# import BinarySearchTree
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# set bstree to BinarySearchTree containing 'names'
bstree = BinarySearchTree('names')
# for names in names_1, use insert (from bst.py) to insert names into bstree
for names in names_1:
    bstree.insert(names)
# for name in names_2, if bstree contains (from bst.py) name, append the duplicate names
for name in names_2:
    if bstree.contains(name):
        duplicates.append(name)
# Runtime will be O(n) I think
# runtime: 0.09803485870361328 seconds, 64 duplicates


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# Runtime O(n^2)
# runtime: 5.4339165687561035 seconds, 64 duplicates

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
