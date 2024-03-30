/* 

https://leetcode.com/problems/sleep/?envType=study-plan-v2&envId=30-days-of-javascript

2621. Sleep

Given a positive integer millis, write an asynchronous function that sleeps for millis milliseconds. It can resolve any value.

 

Example 1:

Input: millis = 100
Output: 100
Explanation: It should return a promise that resolves after 100ms.
let t = Date.now();
sleep(100).then(() => {
  console.log(Date.now() - t); // 100
});
Example 2:

Input: millis = 200
Output: 200
Explanation: It should return a promise that resolves after 200ms.
 

Constraints:

1 <= millis <= 1000

*/

async function sleep(millis: number): Promise<void> {
    return new Promise((resolve) => {
        setTimeout(resolve, millis);
    });
}

async function sleep1(millis: number): Promise<void> {
    return new Promise((res, rej) => setTimeout(res, millis));
}

//  additional information

function delayPromise(
    promise: Promise<number>,
    millis: number
): Promise<number> {
    // Create a new promise that resolves after the specified delay time
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // After the delay time, resolve the new promise with the result of the original promise
            promise.then(resolve).catch(reject);
        }, millis);
    });
}

// Usage example:

let promise = new Promise<number>((resolve, reject) => {
    resolve(42);
});

delayPromise(promise, 2000).then(console.log); // 42 (after 2 seconds)
/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

const myPromise: Promise<number> = new Promise((resolve, reject) => {
    // Perform an asynchronous operation
    if (Math.random() > 0.5) {
        resolve(42);
    } else {
        reject(new Error("Operation failed"));
    }
});

myPromise
    .then((result) => {
        // result is inferred as number
        console.log("Result:", result);
    })
    .catch((error) => {
        console.error("Error:", error);
    });
