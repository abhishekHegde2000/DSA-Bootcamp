/*
https://leetcode.com/problems/to-be-or-not-to-be/description/?envType=study-plan-v2&envId=30-days-of-javascript

2704. To Be Or Not To Be

Write a function expect that helps developers test their code. It should take in any value val and return an object with the following two functions.

toBe(val) accepts another value and returns true if the two values === each other. If they are not equal, it should throw an error "Not Equal".
notToBe(val) accepts another value and returns true if the two values !== each other. If they are equal, it should throw an error "Equal".
 

Example 1:

Input: func = () => expect(5).toBe(5)
Output: {"value": true}
Explanation: 5 === 5 so this expression returns true.
Example 2:

Input: func = () => expect(5).toBe(null)
Output: {"error": "Not Equal"}
Explanation: 5 !== null so this expression throw the error "Not Equal".
Example 3:

Input: func = () => expect(5).notToBe(null)
Output: {"value": true}
Explanation: 5 !== null so this expression returns true.

*/

// Define a type for an object that has two methods: toBe and notToBe
type ComparisonFunctions = {
    toBe: (comparisonValue: any) => boolean;
    notToBe: (comparisonValue: any) => boolean;
};

// Define a function that takes a value and returns an object with toBe and notToBe methods
function expect(inputValue: any): ComparisonFunctions {
    console.log("Creating comparison functions for input value: ", inputValue);
    return {
        toBe: (comparisonValue: any) => {
            console.log("toBe called with comparison value: ", comparisonValue);
            if (inputValue === comparisonValue) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: (comparisonValue: any) => {
            console.log(
                "notToBe called with comparison value: ",
                comparisonValue
            );
            if (inputValue !== comparisonValue) {
                return true;
            } else {
                throw new Error("Equal");
            }
        },
    };
}

// Call expect with the value 5 and call the toBe method with the value 5
console.log("expect(5).toBe(5) result: ", expect(5).toBe(5)); // true

// Call expect with the value 5 and call the notToBe method with the value 5
try {
    console.log("expect(5).notToBe(5) result: ", expect(5).notToBe(5)); // throws "Equal"
} catch (error) {
    console.log("expect(5).notToBe(5) error: ", error.message); // "Equal"
}
