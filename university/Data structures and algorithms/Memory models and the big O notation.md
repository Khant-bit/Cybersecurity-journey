The memory models i made myself farmilar with today are two:
 - Heap 
 - Stack
## Stack
Is a memory function used to manage function execution.
Information is organized in a cell called frame.
A frame contain:
1. Function parameters
2. Local variable bindings
3. Information needed to resume execution
4. References to objects

It uses the principle of Last In First Out
To run a function the function is PUSH() to the top of the frame and to return the function the function is POP() from the frame.

## Heap
Is an area of memory used to dynamically allocate the objects.
Used to store objects that are managed lifetime.

![[Screenshot 2026-11-13 105446.png]]

## Memory management in python
When programs create objects they are stored in memory and what happpens if the object is no longer needed.
Python has two ways of dealing with this situation:
- Reference counting
- Garbage collection

## Reference counting
Objects maintain a count reference to them. When the reference count reaches zero the objects memory can be reclaimed immediately

## Garbage collection
Reference counting cannot alone cannot handle every situation 
Consider two objects that refer to each other, even if nothing outside can reach the cycle their reference number will still not get to zero
CPython has a cyclic garbage collector that can detect and reclaim certain unreachable reference cycles.

## Big-O notation
Big-O notation describes how an algorithm's resource requirements grow with increase in input size.
It has two common analysis
 -Time complexity
 -Space complexity


| Big-O      | Name         | Explanation                                                                      | Example                                     | Practical application                        |
| ---------- | ------------ | -------------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------- |
| O(1)       | Constant     | Execution work remains approximately the same regardless of input size.          | Accessing an array element using its index. | Retrieving a specific record by index.       |
| O(log n)   | Logarithmic  | The problem size is reduced by approximately half at each step.                  | Binary search.                              | Searching **sorted** security records.       |
| O(n)       | Linear       | Every element may need to be examined once.                                      | Linear search.                              | Scanning security logs for a suspicious IP.  |
| O(n log n) | Linearithmic | The algorithm performs approximately n operations across log n levels.           | Merge sort and average-case heap sort.      | Sorting large security datasets efficiently. |
| O(n²)      | Quadratic    | Each element is compared or processed against approximately every other element. | Nested loops over the same collection.      | Pairwise comparison of network events.       |
| O(2ⁿ)      | Exponential  | The number of operations doubles with each additional input element.             | Generating all binary combinations.         | Exhaustive combinatorial searches.           |
| O(n!)      | Factorial    | The algorithm explores permutations of the input elements.                       | Generating every possible ordering.         | Exhaustive permutation problems.             |

## IMPORTANT DISTINCTIONS

1. O(1) does not mean zero execution time. It means constant growth.
    
2. O(n) means work grows proportionally to the input size.
    
3. O(n²) commonly occurs when a loop is nested inside another loop over the same collection.
    
4. O(log n) is associated with repeatedly reducing the search space.
    
5. Binary search requires sorted data.
    
6. Hash tables provide average-case O(1) lookup, but worst-case lookup can be O(n).
    

## EXAMPLE: QUADRATIC COMPLEXITY

If n = 10,000:

n² = 10,000 × 10,000

n² = 100,000,000 operations.

This explains why quadratic algorithms become expensive when processing large datasets.

## BEST, AVERAGE AND WORST CASES

|Case|Meaning|
|---|---|
|Best case|Minimum work required for an input.|
|Average case|Expected work across typical inputs, under an assumed input distribution.|
|Worst case|Maximum work required for an input of a given size.|

Example: Linear search.

|Case|Time complexity|
|---|---|
|Best|O(1)|
|Average|O(n)|
|Worst|O(n)|

## SPACE COMPLEXITY

Space complexity describes how memory requirements grow with input size.

Examples:

|Complexity|Example|
|---|---|
|O(1)|Using a fixed number of additional variables.|
|O(n)|Creating a new list containing n elements.|
|O(n²)|Creating an n × n matrix.|

## GENERAL GROWTH ORDER

From slower growth to faster growth:

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

## WHY BIG-O MATTERS IN CYBERSECURITY

- Efficient processing of security logs.
    
- Searching threat intelligence databases.
    
- Network traffic analysis.
    
- Malware analysis.
    
- Resource management.
    
- Preventing algorithmic Denial-of-Service vulnerabilities.
    
- Building scalable security tools.