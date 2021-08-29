### Problem

Given an array of integers with the pattern: strictly increasing then strictly decreasing, find the maximum number.

### Idea

Let's call the array `arr`.  
The traight forward solution should be looping throught `arr` from start to finish and looking for the number at position `i` where `arr[i + 1] < arr[i] > arr[i - 1]`.
This solution would have `O(n)` run time with `n` is the length of `arr.` We can do better by using binary search:
- Start with the search range: `l = 0` and `r = n - 1`
- Let middle pivot be`m = (l + r) // 2`
- If `m` is in the increasing part of the array, set `l = m + 1`
- If `m` is in the decreasing part of the array, set `r = m - 1`
- Stop when we find `m` is the largest number.


### Complexity

let `n` be the length of the array:
- time: `O(log(n))`
- space: `O(1)`

### Code

The solution can be found in `solution.py`. I also provided some tests to validate the solution. To run the test:
```
❯ python test.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
