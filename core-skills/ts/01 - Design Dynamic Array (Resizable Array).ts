// https://neetcode.io/problems/dynamicArray

// Design Dynamic Array (Resizable Array)
// Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

// Your DynamicArray class should support the following operations:

// DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
// int get(int i) will return the element at index i. Assume that index i is valid.
// void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
// void pushback(int n) will push the element n to the end of the array.
// int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
// void resize() will double the capacity of the array.
// int getSize() will return the number of elements in the array.
// int getCapacity() will return the capacity of the array.
// If we call void pushback(int n) but the array is full, we should resize the array first.

// Example 1:

// Input:
// ["Array", 1, "getSize", "getCapacity"]

// Output:
// [null, 0, 1]
// Example 2:

// Input:
// ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

// Output:
// [null, null, 1, null, 2]
// Example 3:

// Input:
// ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

// Output:
// [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
// Note:

// The index i provided to get(int i) and set(int i) is guranteed to be greater than or equal to 0 and less than the number of elements in the array.

class DynamicArray {
    private capacity: number;
    private length: number;
    private arr: number[];

    constructor(capacity: number) {
        this.capacity = capacity;
        this.length = 0;
        this.arr = new Array<number>(this.capacity).fill(0);
    }

    // Get value at i-th index
    get(i: number): number {
        if (0 <= i && i < this.length) {
            return this.arr[i];
        } else {
            throw new Error("Index out of bounds");
        }
    }

    // Set n at i-th index
    set(i: number, n: number): void {
        if (0 <= i && i < this.length) {
            this.arr[i] = n;
        } else {
            throw new Error("Index out of bounds");
        }
    }

    // Insert n in the last position of the array
    pushback(n: number): void {
        if (this.length === this.capacity) {
            this.resize();
        }

        // insert at next empty position
        this.arr[this.length] = n;
        this.length++;
    }

    // Remove the last element in the array
    popback(): number {
        if (this.length > 0) {
            // soft delete the last element
            this.length--;
            // return the popped element
            return this.arr[this.length];
        } else {
            throw new Error("Array is empty");
        }
    }

    resize(): void {
        // Create new array of double capacity
        this.capacity *= 2;
        const newArr = new Array<number>(this.capacity).fill(0);

        // Copy elements to new_arr
        for (let i = 0; i < this.length; i++) {
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
    }

    getSize(): number {
        return this.length;
    }

    getCapacity(): number {
        return this.capacity;
    }
}

let sol = new DynamicArray(1);
console.log(sol.getSize());
console.log(sol.getCapacity());

sol.pushback(1);
console.log(sol.getCapacity());
