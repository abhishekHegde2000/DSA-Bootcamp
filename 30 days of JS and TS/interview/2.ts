let sentence = " heya what u doing???";

let ans = (sentence: string): string => {
  let res: string = "";

  // Split the sentence into words and trim each word
  let arr: string[] = sentence.split(" ").map((word) => word.trim());

  // Iterate through the words to find the longest one
  for (let word of arr) {
    if (word.length > res.length) {
      res = word;
    }
  }

  return res;
};

console.log(ans(sentence)); // Output: "doing???"

let check_pal = function (word: string): boolean {
  // Convert the string to lowercase and remove non-alphanumeric characters
  let cleanedWord = word.toLowerCase().replace(/[^a-z0-9]/g, "");

  // Reverse the cleaned string
  let reversedWord = cleanedWord.split("").reverse().join("");

  // Compare the original cleaned string with the reversed string
  return cleanedWord === reversedWord;
};

// Example usage
console.log(check_pal("A man, a plan, a canal, Panama")); // Output: true
console.log(check_pal("hello")); // Output: false

let check_pal_two_ptr = (word: string): boolean => {
  // Convert the string to lowercase and remove non-alphanumeric characters
  let cleanedWord = word.toLowerCase().replace(/[^a-z0-9]/g, "");

  // Initialize two pointers
  let left = 0;
  let right = cleanedWord.length - 1;

  // Compare characters while moving towards the center
  while (left < right) {
    if (cleanedWord[left] !== cleanedWord[right]) {
      return false; // Characters do not match
    }
    left++;
    right--;
  }

  return true; // All characters match
};

// Example usage
console.log(check_pal_two_ptr("A man, a plan, a canal, Panama")); // Output: true
console.log(check_pal_two_ptr("hello")); // Output: false

// 3. Write a program to remove duplicates from an array ?

let removeDuplicates = (arr: any[]): any[] => {
  // Convert the array to a Set to remove duplicates
  let uniqueSet = new Set(arr);

  // Convert the Set back to an array
  return [...uniqueSet];
};

// Example usage
let arrayWithDuplicates = [1, 2, 2, 3, 4, 4, 5];
let uniqueArray = removeDuplicates(arrayWithDuplicates);
console.log(uniqueArray); // Output: [1, 2, 3, 4, 5]

/*
The `...uniqueSet` syntax is the **spread operator**. It is used to expand an iterable (like an array or a set) into individual elements.

### Explanation

- **Spread Operator**: Expands an iterable into individual elements.
  ```typescript
  let uniqueArray = [...uniqueSet];
  ```
  - Here, [`uniqueSet`](command:_github.copilot.openSymbolFromReferences?%5B%22uniqueSet%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5Ccode%5C%5Cinterview-prep%5C%5CDSA-Bootcamp%5C%5C30%20days%20of%20JS%20and%20TS%5C%5Cinterview%5C%5C2.ts%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2Fcode%2Finterview-prep%2FDSA-Bootcamp%2F30%2520days%2520of%2520JS%2520and%2520TS%2Finterview%2F2.ts%22%2C%22path%22%3A%22%2FC%3A%2Fcode%2Finterview-prep%2FDSA-Bootcamp%2F30%20days%20of%20JS%20and%20TS%2Finterview%2F2.ts%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A67%2C%22character%22%3A13%7D%7D%5D%5D "Go to definition") is a `Set` containing unique values.
  - The spread operator `...` expands the `Set` into individual elements.
  - These elements are then placed into a new array.

### Example

```typescript
let uniqueSet = new Set([1, 2, 3, 4, 5]);
let uniqueArray = [...uniqueSet]; // [1, 2, 3, 4, 5]
```

- **Rest Operator**: Collects multiple elements into a single array or object.
  ```typescript
  function sum(...numbers: number[]): number {
    return numbers.reduce((acc, curr) => acc + curr, 0);
  }
  ```
  - Here, the rest operator `...` collects all arguments passed to the function into an array called `numbers`.

### Summary

- **Spread Operator**: Expands an iterable into individual elements.
- **Rest Operator**: Collects multiple elements into a single array or object.

In your code, `...uniqueSet` is the spread operator.
*/

// 4. Program to find Reverse of a string without using built-in method ?
let reverseString = (str: string): string => {
  let reversedStr = "";

  // Iterate through the string from the end to the beginning
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr += str[i];
  }

  return reversedStr;
};

// Example usage
let originalString = "hello";
let reversed = reverseString(originalString);
console.log(reversed); // Output: "olleh"

// 5. Find the max count of consecutive 1’s in an array ?

let findMaxConsecutiveOnes = (arr: number[]): number => {
  let maxCount = 0;
  let currentCount = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1) {
      currentCount++;
    } else {
      if (currentCount > maxCount) {
        maxCount = currentCount;
      }
      currentCount = 0;
    }
  }

  // Final check to update maxCount if the array ends with 1's
  if (currentCount > maxCount) {
    maxCount = currentCount;
  }

  return maxCount;
};

// Example usage
let array = [1, 1, 0, 1, 1, 1, 0, 1, 1];
let maxConsecutiveOnes = findMaxConsecutiveOnes(array);
console.log(maxConsecutiveOnes); // Output: 3

let fact = (n: number): number => {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) return 1;

  // Recursive case: n * factorial of (n - 1)
  return n * fact(n - 1);
};

// Example usage
console.log(fact(5)); // Output: 120
console.log(fact(0)); // Output: 1
console.log(fact(1)); // Output: 1

// 7. Given 2 arrays that are sorted [0,3,4,31] and [4,6,30]. Merge them and sort [0,3,4,4,6,30,31] ?

let mergeSortedArrays = (arr1: number[], arr2: number[]): number[] => {
  let mergedArray: number[] = [];
  let i = 0; // Pointer for arr1
  let j = 0; // Pointer for arr2

  // Iterate through both arrays
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      mergedArray.push(arr1[i]);
      i++;
    } else {
      mergedArray.push(arr2[j]);
      j++;
    }
  }

  // Add remaining elements from arr1
  while (i < arr1.length) {
    mergedArray.push(arr1[i]);
    i++;
  }

  // Add remaining elements from arr2
  while (j < arr2.length) {
    mergedArray.push(arr2[j]);
    j++;
  }

  return mergedArray;
};

// Example usage
let array1 = [0, 3, 4, 31];
let array2 = [4, 6, 30];
let mergedAndSortedArray = mergeSortedArrays(array1, array2);
console.log(mergedAndSortedArray); // Output: [0, 3, 4, 4, 6, 30, 31]

// 8. Create a function which will accepts two arrays arr1 and arr2. The function should return true if every value in arr1 has its corresponding value squared in array2. The frequency of values must be same.

// 9. Given two strings. Find if one string can be formed by rearranging the letters of other string.
// 10. Write logic to get unique objects from below array ?
//     I/P: [{name: "sai"},{name:"Nang"},{name: "sai"},{name:"Nang"},{name: "111111"}];
//     O/P: [{name: "sai"},{name:"Nang"}{name: "111111"}
// 11. Write a JavaScript program to find the maximum number in an array.
// 12. Write a JavaScript function that takes an array of numbers and returns a new array with only the even numbers.
// 13. Write a JavaScript function to check if a given number is prime.
// 14. Write a JavaScript program to find the largest element in a nested array.
//     [[3, 4, 58], [709, 8, 9, [10, 11]], [111, 2]]
// 15. Write a JavaScript function that returns the Fibonacci sequence up to a given number of terms.
// 16. Given a string, write a javascript function to count the occurrences of each character in the string.
// 17. Write a javascript function that sorts an array of numbers in ascending order.
// 18. Write a javascript function that sorts an array of numbers in descending order.
// 19. Write a javascript function that reverses the order of words in a sentence without using the built-in reverse() method.
// 20. Implement a javascript function that flattens a nested array into a single-dimensional array.

// Keep learning and sharing!

// Follow[](https://www.linkedin.com/in/ACoAAB0s4O8BKVirCr1CjADQBeXWfJ5oI34nuFY)[Alpna P.](https://www.linkedin.com/in/alpnap/)for more related content!
