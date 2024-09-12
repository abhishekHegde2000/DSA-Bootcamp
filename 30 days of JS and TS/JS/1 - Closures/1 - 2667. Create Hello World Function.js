/*
https://leetcode.com/problems/create-hello-world-function/description/?envType=study-plan-v2&envId=30-days-of-javascript

2667. Create Hello World Function

Write a function createHelloWorld. It should return a new function that always returns "Hello World".
 

Example 1:

Input: args = []
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".
Example 2:

Input: args = [{},null,42]
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".
 

Constraints:

0 <= args.length <= 10

*/

var createHelloWorld = function () {
    return function (...args) {
        return "Hello World";
    };
};

var helloWorldFunction = createHelloWorld(); // This calls the outer function, which returns the inner function.

console.log(helloWorldFunction); // This logs the inner function.

console.log(helloWorldFunction(1000)); // This calls the inner function, which returns "Hello World".
