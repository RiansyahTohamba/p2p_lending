mutasi.md

# What is mutability?
 
Mutability means that the data in the data structure can be modified (added, deleted, or changed) after creation. Mutability is an important factor to consider when choosing your data structure. 
If you know that you won’t need to change the internal state, consider using an immutable object to ensure that it is thread-safe and that nothing can overwrite your data.
 
Mutability bermakna data pada DS dapat dimodifikasi(added, deleted, changed) saat sudah dibuat.
Mutability adalah faktor penting untuk diperhatikan ketika memilih tipe DS.
Jika anda tahu bahwa anda tidak akan merubah state internal, pertimbangkan untuk menggunakan immutable object untuk memastikan bahwa ini thread-safe dan tak ada yang bisa overwrite datamu.

## Lists
To represent a sequence of items indexed by their integer position, one data structure you can use is a list. 
Lists contain zero or more elements and can contain elements of different types (even objects!). 

names = ['','','']


This makes lists powerful because they allow you to create deep and complex data structures.
Lists are mutable, meaning that you can add, delete, or change elements in a flexible manner. Another sequential data structure is a tuple; the difference between these two is that tuples are immutable.
Because lists have a sequential element: if you only want to keep track of unique values and don’t care about the order, use a Python set.
Create lists using [] or list(). Typecast using list().

Some notable methods & tips
Access list items:
my_list[0] gets a list item by offset. Like strings, negative indexes can be used to count backward from the end.
my_list[0] = ‘new item' changes a list item by offset.
my_list[0:2] slices to extract items by offset. This example returns the first 2 elements of my_list.
Add list items:
append() adds an item to the end of a list.
extend() or += merges one list into another.
insert() adds an item before any offset.
Remove list items:
remove() removes an item value from a list.
pop() removes the last (or specified) element while also returning the value.
del removes an item by its position in the list. del is a Python statement, not a list method.
join() returns a string of combined list items. The argument for join() is a string or any iterable sequence of strings.
len() returns the number of items in the list. count() returns the number of occurrences of a specified value.
Tuples
Tuples are also a sequenced data structure, just like lists. However, tuples are immutable; you cannot add, delete, or change items after a tuple is created. Tuples differ from lists by having many fewer functions because they can’t be modified after being defined. Tuples contain zero or more elements and can contain elements of different, immutable types.