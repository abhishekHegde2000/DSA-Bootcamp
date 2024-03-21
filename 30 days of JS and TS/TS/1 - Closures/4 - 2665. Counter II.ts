/*

https://leetcode.com/problems/counter-ii/description/?envType=study-plan-v2&envId=30-days-of-javascript

2665. Counter II

Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.

The three functions are:

increment() increases the current value by 1 and then returns it.
decrement() reduces the current value by 1 and then returns it.
reset() sets the current value to init and then returns it.
 

Example 1:

Input: init = 5, calls = ["increment","reset","decrement"]
Output: [6,5,4]
Explanation:
const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4
Example 2:

Input: init = 0, calls = ["increment","increment","decrement","reset","reset"]
Output: [1,2,1,0,0]
Explanation:
const counter = createCounter(0);
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
counter.reset(); // 0
counter.reset(); // 0
 

Constraints:

-1000 <= init <= 1000
0 <= calls.length <= 1000
calls[i] is one of "increment", "decrement" and "reset"

*/

type Counter = {
    increment: () => number;
    decrement: () => number;
    reset: () => number;
};

// using function expression
const createCounter = function createCounter(init: number): Counter {
    let temp = init;
    return {
        increment: () => {
            return (temp = temp + 1);
        },
        decrement: () => {
            return (temp = temp - 1);
        },
        reset: () => {
            return (temp = init);
        },
    };
};

// with return type arrwo function
const createCounter2 = function createCounter(init: number): Counter {
    let temp = init;
    return {
        increment: () => temp + 1,
        decrement: () => temp - 1,
        reset: () => init,
    };
};

// with return type function
const createCounter3 = function createCounter(init: number): Counter {
    let temp = init;
    return {
        increment: function () {
            return (temp = temp + 1);
        },
        decrement: function () {
            return (temp = temp - 1);
        },
        reset: function () {
            return (temp = init);
        },
    };
};

const counter = createCounter(5);

counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4
