# What is mutability?
 
Mutability means that the data in the data structure can be modified (added, deleted, or changed) after creation. Mutability is an important factor to consider when choosing your data structure. 
If you know that you won’t need to change the internal state, consider using an immutable object to ensure that it is thread-safe and that nothing can overwrite your data.
 
Mutability bermakna data pada DS dapat dimodifikasi(added, deleted, changed) saat sudah dibuat.
Mutability adalah faktor penting untuk diperhatikan ketika memilih tipe DS.
Jika anda tahu bahwa anda tidak akan merubah state internal, pertimbangkan untuk menggunakan immutable object untuk memastikan bahwa ini thread-safe dan tak ada yang bisa overwrite datamu.

## Lists
To represent a sequence of items indexed by their integer position, one data structure you can use is a list. 
Lists contain zero or more elements and can contain elements of different types (even objects!). 

This makes lists powerful because they allow you to create deep and complex data structures.
Lists are mutable, meaning that you can add, delete, or change elements in a flexible manner. 

List masuk dalam jenis DS yang mutable, yang berarti sangat fleksibel untuk merubah nilainya (add, delete, update).

Another sequential data structure is a tuple; the difference between these two is that tuples are immutable.

Contoh sequential DS lainnya adalah tuple. Berbeda dengan List, tuple memiliki sifat immutable.

Karena lists memiliki sequential element: jika kamu hanya 


Because lists have a sequential element: if you only want to keep track of unique values and don’t care about the order, use a Python set.

Create lists using [] or list(). 

`Typecast using list().`

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

`Tuples`
Tuples are also a sequenced data structure, just like lists. 
However, tuples are immutable; you cannot add, delete, or change items after a tuple is created. 


Tuples differ from lists by having many fewer functions because they can’t be modified after being defined. Tuples contain zero or more elements and can contain elements of different, immutable types.


Advantages to tuples over lists:
Tuples use less space
Immutability prevents changing tuple items by mistake
Tuples can be used as dictionary keys
Function arguments are passed as tuples
Create tuples using () or a comma-separated list of elements with no surrounding brackets or braces. Typecast using tuple().
Some notable methods & tips
count() returns the number of times an element is found in the tuple
index() returns the index position of an element
Dictionaries
Instead of using an offset, dictionaries use keys to associate with each value. This means that order is not tracked and should not matter if you plan to use a dictionary. Dictionary keys are immutable and unique, however, dictionaries are mutable; the key-value elements can be added, deleted, or changed. In short, dictionaries are very similar to hashmaps.
Create dictionaries using {}. Typecast using dict().
Some notable methods & tips
my_dict[‘key’] gets an item by its key
my_dict['key'] = ‘value' uses a key to add (or change if it already exists) a value.
update() merges the keys and values of one dictionary into another.
del deletes an item by the provided key. del is a Python statement, not a dictionary method.
keys() returns all the dictionary keys. values() returns all the values in the dictionary. items() returns all the dictionary key-value pairs.

Sets
A set is like a dictionary with only the keys, not the values. This means that sets are unique and not sequential (stored unordered). Sets are also mutable. Sets contain zero or more elements and can contain elements of different, immutable types.
Essentially, sets are used when you want to know if something exists and nothing else about it. If it matters to track value order or store multiple of the same value, consider using a space-friendly tuple instead.
Create sets using set(). Typecast using set().
Some notable methods & tips
add() adds an item to the set if it doesn’t already exist
clear() removes all items from the set
intersect() returns an intersection of two sets
union() returns a union of two sets
In summary
If you need to keep track of sequencing, use a list or tuple
If you only want to keep track of unique values and don’t care about the order, use a Python set
If you don’t need to make changes once you define your object, use a tuple to save space and ensure that nothing can overwrite your data
If you need to keep track and modify data structured in key-value pairs, use a dictionary
