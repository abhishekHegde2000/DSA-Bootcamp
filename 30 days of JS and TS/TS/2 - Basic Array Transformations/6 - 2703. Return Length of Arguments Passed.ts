/*

https://leetcode.com/problems/return-length-of-arguments-passed/?envType=study-plan-v2&envId=30-days-of-javascript


2703. Return Length of Arguments Passed

Write a function argumentsLength that returns the count of arguments passed to it.
 

Example 1:

Input: args = [5]
Output: 1
Explanation:
argumentsLength(5); // 1

One value was passed to the function so it should return 1.
Example 2:

Input: args = [{}, null, "3"]
Output: 3
Explanation: 
argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.
 

Constraints:

args is a valid JSON array
0 <= args.length <= 100
*/

type JSONValue =
    | null
    | boolean
    | number
    | string
    | JSONValue[]
    | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    return args.length;
}

function argumentsLength2(...args: JSONValue[]): number {
    let count = 0;

    for (let i = 0; i < args.length; i++) {
        count++;
    }
}

function argumentsLength3(...args: JSONValue[]): number {
    return args.reduce((count: number) => count + 1, 0);
}

/**
 * argumentsLength(1, 2, 3); // 3
 */
