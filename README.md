# data-structures-and-algos

# Arrays
In most languages, arrays can hold up to a maximum length, specified at array creation, max_len, and the type of the elements is specified. The elements all have to be the same type. An array may not be full at creation, but the unassigned element positions will be defaulted to 0/null. 

An array needs to be able to perform the following operations:
    - Find
        takes a value and sees if the index meets that value
    - getItem
        takes index as input, checks whether index is valid 
    - Insert
        adds an element, moves the size/order up one if size < max_length
    - Delete
        takes out an element, moves the size/order down one if size > 0
    - Traverse
        loops over array

while able to keep track of the current length of the Array, not the max length. 
    - size (length)



Mimicing a C programming language array type_code: 

| Code | C analogue           | Signed? | Typical size\* | Rough numeric range (2’s-complement) |
| ---- | -------------------- | ------- | -------------- | ------------------------------------ |
| `b`  | `signed char`        | Yes     | 1 byte         | –128 … 127                           |
| `B`  | `unsigned char`      | No      | 1 byte         | 0 … 255                              |
| `u`  | “Unicode char”†      | N/A     | 2 bytes        | UTF-16 code unit                     |
| `h`  | `short`              | Yes     | ≥ 2 bytes      | –32 768 … 32 767 (if 16-bit)         |
| `H`  | `unsigned short`     | No      | ≥ 2 bytes      | 0 … 65 535                           |
| `i`  | `int`                | Yes     | ≥ 2 bytes      | platform-dependent                   |
| `I`  | `unsigned int`       | No      | ≥ 2 bytes      | platform-dependent                   |
| `l`  | `long`               | Yes     | ≥ 4 bytes      | platform-dependent                   |
| `L`  | `unsigned long`      | No      | ≥ 4 bytes      | platform-dependent                   |
| `q`  | `long long`          | Yes     | 8 bytes        | ±9.22 × 10¹⁸                         |
| `Q`  | `unsigned long long` | No      | 8 bytes        | 0 … 1.84 × 10¹⁹                      |
| `f`  | `float`              | —       | 4 bytes        | IEEE-754 single precision            |
| `d`  | `double`             | —       | 8 bytes        | IEEE-754 double precision            |



## unsorted-arrays

## sorted-arrays
