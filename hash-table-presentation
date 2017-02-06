# Explain and provide an example of the average case and worst case time complexity for insertion and deletion in a hash table.

an associative array...
a hash table is a specific way to implement a python dictionary, can also implement sets.

Key:Value pairs. Index Key : Data pairs.

A data structure in which insertion and search operations are very fast irrespective of the size of the data. Hash Table uses an array as a storage medium and uses a Hash Function to generate an index where an element is to be located from. You can then insert or delete the element.

Hashing is a technique to convert a range of key values into a range of indexes of an array.

This allows us to search for key values in constant, O(1), time. We simply use the hash function to compute the slot name for the item and then check the hash table to see if it is present. A constant amount of time is required to compute the hash value and then index the hash table at that location. If everything is where it should be, we have found a constant time search algorithm.

However, due to collisions, instances where the hashing technique did not result in a unique location and wants to put an item in a location that is already occupied, a search for a location would take longer and depends on the probing method used. Some hashing techniques use a linear search function to find the next empty, some use chaining with linked lists. Both would mean the search would take closer to O(n) time. (Chaining can make it O(n) or O(log N) depending on the data structure used.)

If the hash table does not have a fixed size but can shrink and grow as more keys are added and deleted, then every now and then the hash table needs to be resized, which takes a lot of time. So in those cases, insertion and deletion can sometimes take very long. This would be the worst case scenario. Although on average the time complexity is still O(1)- this is called amortized O(1).
 
 
Insert
Whenever an element is to be inserted, compute the hash code of the key passed and locate the index using that hash code as an index in the array. If an element is found at the computed hash code, use a method to find an empty location. linear probing for example.

Delete
Whenever an element is to be deleted, compute the hash code of the key passed and locate the index using that hash code as an index in the array. Use linear probing to get the element ahead if an element is not found at the computed hash code. When found, store a dummy item there to keep the performance of the hash table intact.


However, this does not take into account the hashing technique time- the function would most probably have a complexity of its own, but can be very simple.


References:
- https://www.tutorialspoint.com/data_structures_algorithms/hash_data_structure.htm
- http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
- https://www.quora.com/What-is-the-time-complexity-of-hash-table-O-1
- http://www.cs.rmit.edu.au/online/blackboard/chapter/05/documents/contribute/chapter/05/linear-probing.html
- http://stackoverflow.com/questions/9214353/hash-table-runtime-complexity-insert-search-and-delete



Question:
Why is this faster than referring to an object by its direct memory location?

Hash tables allow the program to Always store the data in the same exact location each time. Memory location changes when the program is executed again. Hashing ensures that the data is always being stored in the same way every time.
