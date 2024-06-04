class Node {
    value: number;
    next: Node | null;
    prev: Node | null;

    constructor(value: number) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class Deque {
    head: Node;
    tail: Node;

    constructor() {
        // Create two dummy nodes and link them
        this.head = new Node(-1);
        this.tail = new Node(-1);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    isEmpty(): boolean {
        return this.head.next === this.tail;
    }

    append(value: number): void {
        const newNode = new Node(value);
        const lastNode = this.tail.prev;

        if (lastNode) {
            lastNode.next = newNode;
            newNode.prev = lastNode;
            newNode.next = this.tail;
            this.tail.prev = newNode;
        }
    }

    appendLeft(value: number): void {
        const newNode = new Node(value);
        const firstNode = this.head.next;

        if (firstNode) {
            this.head.next = newNode;
            newNode.prev = this.head;
            newNode.next = firstNode;
            firstNode.prev = newNode;
        }
    }

    pop(): number {
        if (this.isEmpty()) {
            return -1;
        }

        const lastNode = this.tail.prev;
        if (lastNode && lastNode.prev) {
            const value = lastNode.value;
            const prevNode = lastNode.prev;

            prevNode.next = this.tail;
            this.tail.prev = prevNode;

            return value;
        }

        return -1;
    }

    popLeft(): number {
        if (this.isEmpty()) {
            return -1;
        }

        const firstNode = this.head.next;
        if (firstNode && firstNode.next) {
            const value = firstNode.value;
            const nextNode = firstNode.next;

            this.head.next = nextNode;
            nextNode.prev = this.head;

            return value;
        }

        return -1;
    }
}
