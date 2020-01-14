## Arrays

### Introduction

You are new to programming and you came across a situation where you need to store some values in a list. So, to achieve this you can declare `N` variables and store each value in it. Somehow it fixed your problem, but in the long run i guess it will not be the optimal choice. So, the best choice you have is `arrays`.

An Array is a `linear data structure` that can be used to store a group of values of similar type.

Here is the syntax of array

```
datatype array_name[size]
```

```c
int array[10];
array[0] = 10;
array[1] = 100;
array[2] = 1000;
```

Array are _index-based_, that means you use an index to access i<sup>th</sup> element of an array. Imagine array as your text book and you can access any page with its page number and arrays are also similair to that.

Arrays are _zero-based_, that means it will start with zero and end with `N-1`, where `N` is the size of an array.

When it comes to arrays, we can access any element of array in the constant unit of time. This is the huge perk of using arrays. It does not mean that it does not have any limitations. Any data structure has its own advantages and disadvantages, we cannot compare any of them.

```c
int array[5] = {1, 2, 3, 4, 5};
```

This is the one line declaration and initialization of an array.

### Safety

A code is said to be safe, if its does not raise any exception during its execution.

Arrays are fixed and bounded, that means accessing any element beyond the bounds of an array will cause exception.

```c
int array[5] = {1, 2, 3, 4, 5};
a[5] = 6; //this will cause exception
a[-1] = 0; //this will cause exception
```

When the first line of this code execute, the array will have 5 elements and they are fixed and bounded to 5. It's lower bound is `0` and upper bound is `4`. When you tried to access 5<sup>th</sup> index i.e 6<sup>th</sup> element of an array, the exception raises. It's like asking 6<sup>th</sup> chocolate when you only has 5 chocolates. So, we need to be cautious while accessing the elements of an array.

### Memory Allocation

You might be wondering how the array is stored and how all the values are stored in a single variable. Actually not, for better understanding, lets see how a single variable is allocated.<br/>
In the process of allocation of a single variable, its value is stored in a _word_, which is an unit of storage in the memory and an unique address is assigned to the memory location where it is stored.
So, when allocating a group of values, it is not possible to store all the values in a single _word_, which is limited to say 32 or 64 bit size.

![Frame 1](https://user-images.githubusercontent.com/21126965/72368671-8cdf0d80-3724-11ea-8e5d-895cefa4e6ae.png)

Instead all the values are allocated successively, one after another in a sequence to each _word_ and the starting memory location is used as reference to access every element in the array.

```c
int a[7] = {2, 3, 5, 7, 9, 1, 0};
printf("%d", a); //it prints the starting location of the array i.e RAND0
```

In this way, the memory allocation of array happens. When, you say `a[0]` that means the value in the first location (i.e location = RAND0, value = 2)

### Updates

I'll be adding more content to this article, i hope you like this and all of your doubts are clarified and if you have any queries feel free to reach me.If you find any corrections, please let me know.

Thanking you,<br/>
Mohan
