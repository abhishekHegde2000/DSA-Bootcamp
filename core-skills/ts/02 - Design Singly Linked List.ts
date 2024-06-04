/*
https://neetcode.io/problems/singlyLinkedList

Design Singly Linked List
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
int remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guranteed to be greater than or equal to 0.
*/

// Singly Linked List Node
class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val: number, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

// Implementation for Singly Linked List
class LinkedList {
    private head: ListNode;
    private tail: ListNode;

    constructor() {
        // Init the list with a 'dummy' node which makes
        // removing a node from the beginning of list easier.
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    get(index: number): number {
        let curr = this.head.next;
        let i = 0;
        while (curr) {
            if (i === index) {
                return curr.val;
            }
            i++;
            curr = curr.next;
        }
        return -1; // Index out of bounds or list is empty
    }

    insertHead(val: number): void {
        const new_node = new ListNode(val);
        new_node.next = this.head.next;
        this.head.next = new_node;
        if (!new_node.next) {
            // If list was empty before insertion
            this.tail = new_node;
        }
    }

    insertTail(val: number): void {
        this.tail.next = new ListNode(val);
        this.tail = this.tail.next!;
    }

    remove(index: number): boolean {
        let i = 0;
        let curr = this.head;
        while (i < index && curr) {
            i++;
            curr = curr.next!;
        }

        // Remove the node ahead of curr
        if (curr && curr.next) {
            if (curr.next === this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    getValues(): number[] {
        let curr = this.head.next;
        const res: number[] = [];
        while (curr) {
            res.push(curr.val);
            curr = curr.next;
        }
        return res;
    }
}
