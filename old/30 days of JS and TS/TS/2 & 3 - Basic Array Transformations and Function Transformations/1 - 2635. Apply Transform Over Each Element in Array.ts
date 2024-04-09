/*
https://leetcode.com/problems/apply-transform-over-each-element-in-array/?envType=study-plan-v2&envId=30-days-of-javascript

2635. Apply Transform Over Each Element in Array

Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

The returned array should be created such that returnedArray[i] = fn(arr[i], i).

Please solve it without the built-in Array.map method.

 

Example 1:

Input: arr = [1,2,3], fn = function plusone(n) { return n + 1; }
Output: [2,3,4]
Explanation:
const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one. 
Example 2:

Input: arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
Output: [1,3,5]
Explanation: The function increases each value by the index it resides in.
Example 3:

Input: arr = [10,20,30], fn = function constant() { return 42; }
Output: [42,42,42]
Explanation: The function always returns 42.
 

Constraints:

0 <= arr.length <= 1000
-109 <= arr[i] <= 109
fn returns a number
*/

let map = function map(
    arr: number[],
    fn: (n: number, i: number) => number
): number[] {
    const res = [];

    for (let i = 0; i < arr.length; i++) {
        res.push(fn(arr[i], i));
    }

    return res;
};

const arr = [1, 2, 3];
const plusone = (n: number) => n + 1;

console.log(map(arr, plusone)); // [2, 3, 4]

// ---------------------------------------------------

let mapWithArrayMap = function map(
    arr: number[],
    fn: (n: number, i: number) => number
): number[] {
    // Use the built-in map method to apply fn to each element in arr
    return arr.map(fn);
};

// Sure, let's go through each of them:

// 1. `for` loop: This is the most basic type of loop in JavaScript. It's great when you know exactly how many times you want to loop.

for (let i = 0; i < 5; i++) {
    console.log(i); // prints 0, 1, 2, 3, 4
}

// 2. `forEach` loop: This is an array method that executes a provided function once for each array element. It's great when you want to do something with each item in an array and you don't need to break out of the loop.

let arr = [1, 2, 3, 4, 5];
arr.forEach((value, index) => {
    console.log(value); // prints 1, 2, 3, 4, 5
});

// 3. `for...of` loop: This is a modern loop in JavaScript that works not only with arrays, but also with other iterable objects like strings, maps, sets, etc. It's great when you want to do something with each item in an iterable and you might need to break out of the loop.

let arr = [1, 2, 3, 4, 5];
for (let value of arr) {
    console.log(value); // prints 1, 2, 3, 4, 5
}

// 4. `for...in` loop: This loop is used to iterate over the enumerable properties of an object, in an arbitrary order. It's great when you want to work with object properties.

let obj = { a: 1, b: 2, c: 3 };
for (let key in obj) {
    console.log(key, obj[key]); // prints 'a 1', 'b 2', 'c 3'
}

// Note: `for...in` should not be used to iterate over an Array where the index order is important, as it does not guarantee the order of properties. Use `for...of` or `forEach` for arrays.
