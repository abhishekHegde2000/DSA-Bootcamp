/*
https://leetcode.com/problems/function-composition/?envType=study-plan-v2&envId=30-days-of-javascript

2629. Function Composition

Given an array of functions [f1, f2, f3, ..., fn], return a new function fn that is the function composition of the array of functions.

The function composition of [f(x), g(x), h(x)] is fn(x) = f(g(h(x))).

The function composition of an empty list of functions is the identity function f(x) = x.

You may assume each function in the array accepts one integer as input and returns one integer as output.

 

Example 1:

Input: functions = [x => x + 1, x => x * x, x => 2 * x], x = 4
Output: 65
Explanation:
Evaluating from right to left ...
Starting with x = 4.
2 * (4) = 8
(8) * (8) = 64
(64) + 1 = 65
Example 2:

Input: functions = [x => 10 * x, x => 10 * x, x => 10 * x], x = 1
Output: 1000
Explanation:
Evaluating from right to left ...
10 * (1) = 10
10 * (10) = 100
10 * (100) = 1000
Example 3:

Input: functions = [], x = 42
Output: 42
Explanation:
The composition of zero functions is the identity function
 

Constraints:

-1000 <= x <= 1000
0 <= functions.length <= 1000
all functions accept and return a single integer

*/

type F = (x: number) => number;

function compose(functions: F[]): F {
    return function (x) {
        return functions.reduceRight((acc, fn) => fn(acc), x);
    };
}

function compose1(functions: F[]): F {
    return function (x) {
        // Start with the initial value
        let result = x;

        // Iterate over the array in reverse order
        for (let i = functions.length - 1; i >= 0; i--) {
            // Apply the current function to the result
            result = functions[i](result);
        }

        // Return the final result
        return result;
    };
}

const fn = compose([(x) => x + 1, (x) => 2 * x]);
console.log(fn(4)); // 9

const fn1 = compose1([(x) => x + 1, (x) => 2 * x]);
console.log(fn1(4)); // 9

// ---------------------------------------------------

type F = (x: number) => number;

function compose(functionsArray: F[]): F {
    return function (x) {
        console.log("Initial value: ", x);
        return functionsArray.reduceRight((accumulator, currentFunction) => {
            console.log("Current accumulator: ", accumulator);
            let result = currentFunction(accumulator);
            console.log("Result after applying current function: ", result);
            return result;
        }, x);
    };
}

function composeWithForLoop(functionsArray: F[]): F {
    return function (x) {
        console.log("Initial value: ", x);
        let result = x;
        for (let i = functionsArray.length - 1; i >= 0; i--) {
            console.log("Current result: ", result);
            result = functionsArray[i](result);
            console.log("Result after applying current function: ", result);
        }
        return result;
    };
}

const composedFunction = compose([(x) => x + 1, (x) => 2 * x]);
console.log("Result of composed function: ", composedFunction(4)); // 9

const composedFunctionWithForLoop = composeWithForLoop([
    (x) => x + 1,
    (x) => 2 * x,
]);
console.log(
    "Result of composed function with for loop: ",
    composedFunctionWithForLoop(4)
); // 9

/*


Sure, let's start with a simple example of using `reduce` to sum up an array of numbers.

```javascript
let numbers = [1, 2, 3, 4, 5];

let sum = numbers.reduce((accumulator, currentValue) => {
    console.log(`Accumulator: ${accumulator}, Current Value: ${currentValue}`);
    return accumulator + currentValue;
}, 0);

console.log(`Sum: ${sum}`); // Sum: 15
```

Here's a step-by-step explanation:

1. `reduce` is called on the `numbers` array. The function `(accumulator, currentValue) => accumulator + currentValue` is the reducer function, and `0` is the initial value for the accumulator.

2. On the first call to the reducer function, `accumulator` is `0` (the initial value), and `currentValue` is `1` (the first element in the array). The reducer function returns `0 + 1 = 1`.

3. On the second call, `accumulator` is `1` (the result of the previous call), and `currentValue` is `2` (the second element in the array). The reducer function returns `1 + 2 = 3`.

4. This process continues for each element in the array. On each call, `accumulator` is the result of the previous call, and `currentValue` is the next element in the array.

5. After all elements in the array have been processed, `reduce` returns the final value of the accumulator, which is the sum of all numbers in the array.

The `console.log` statements inside the reducer function and after the `reduce` call show the value of the accumulator and the current value on each call, and the final sum, respectively.



-------------------------------------------

The `reduceRight` function in JavaScript is used to apply a function against an accumulator and each value of the array (from right-to-left) to reduce it to a single value.

In this case, `functions.reduceRight((acc, fn) => fn(acc), x)` is applying each function in the `functions` array to a value, starting with `x` and then the result of each subsequent function call.

Here's a dry run of how it works:

1. `reduceRight` starts from the last function in the `functions` array.
2. It calls this function with `x` as the argument, and the return value of this function call becomes the new accumulator (`acc`).
3. It then moves to the second last function in the `functions` array, and calls this function with the new accumulator as the argument. The return value of this function call becomes the new accumulator.
4. This process continues until `reduceRight` has called every function in the `functions` array.
5. The final value of the accumulator is the result of the `reduceRight` call.

For example, if `functions` is an array of two functions `[f, g]` where `f(x) = x + 1` and `g(x) = x * 2`, and `x` is `5`, then `functions.reduceRight((acc, fn) => fn(acc), x)` would be equivalent to `f(g(5))`, which would be `f(10)`, which would be `11`.



Sure, let's break down how `reduceRight` works with a dry run. 

Let's assume we have an array of functions `functions = [f, g, h]` where `f(x) = x + 1`, `g(x) = x * 2`, and `h(x) = x / 2`, and we call `reduceRight` with `x = 4`.

Here's how `reduceRight` would process this array:

1. `reduceRight` starts from the last function in the array, which is `h`. It calls `h` with `x` as the argument. So, `acc = h(4) = 4 / 2 = 2`. This is the new accumulator (`acc`).

2. It then moves to the second last function in the array, which is `g`. It calls `g` with the new accumulator as the argument. So, `acc = g(2) = 2 * 2 = 4`. This is the new accumulator.

3. Finally, it moves to the first function in the array, which is `f`. It calls `f` with the new accumulator as the argument. So, `acc = f(4) = 4 + 1 = 5`. This is the new accumulator.

4. Now, all functions in the array have been processed, so `reduceRight` returns the final value of the accumulator, which is `5`.

So, in this example, `functions.reduceRight((acc, fn) => fn(acc), x)` would return `5`.

The accumulator (`acc`) is used to keep track of the intermediate results as `reduceRight` processes the array. It starts as the initial value `x`, and for each function in the array, it's updated to the return value of calling that function with the current accumulator as the argument.


----------------------


The `x` in `functions.reduceRight((acc, fn) => fn(acc), x)` is the initial value for the accumulator (`acc`) in the `reduceRight` function.

When you call `reduceRight` (or `reduce`), you can provide an initial value for the accumulator. This value is used as the first accumulator value when the `reduceRight` function starts processing the array.

In the context of function composition, `x` is the initial input to the composition of functions. When `reduceRight` starts, it calls the last function in the `functions` array with `x` as the argument. The return value of this function call then becomes the new accumulator value, and `reduceRight` continues to the next function in the array.

So, in short, `x` is used as the initial input to the composition of functions.


-----------------------

Sure, let's start with a simple example of using `reduce` to sum up an array of numbers.

```javascript
let numbers = [1, 2, 3, 4, 5];

let sum = numbers.reduce((accumulator, currentValue) => {
    console.log(`Accumulator: ${accumulator}, Current Value: ${currentValue}`);
    return accumulator + currentValue;
}, 0);

console.log(`Sum: ${sum}`); // Sum: 15
```

Here's a step-by-step explanation:

1. `reduce` is called on the `numbers` array. The function `(accumulator, currentValue) => accumulator + currentValue` is the reducer function, and `0` is the initial value for the accumulator.

2. On the first call to the reducer function, `accumulator` is `0` (the initial value), and `currentValue` is `1` (the first element in the array). The reducer function returns `0 + 1 = 1`.

3. On the second call, `accumulator` is `1` (the result of the previous call), and `currentValue` is `2` (the second element in the array). The reducer function returns `1 + 2 = 3`.

4. This process continues for each element in the array. On each call, `accumulator` is the result of the previous call, and `currentValue` is the next element in the array.

5. After all elements in the array have been processed, `reduce` returns the final value of the accumulator, which is the sum of all numbers in the array.

The `console.log` statements inside the reducer function and after the `reduce` call show the value of the accumulator and the current value on each call, and the final sum, respectively.


*/
