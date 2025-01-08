function minOperations(boxes: string): number[] {
  const n = boxes.length;
  const answer = new Array(n).fill(0);

  // Left to right pass
  let leftCount = 0; // Number of balls to the left
  let leftOperations = 0; // Cumulative operations from the left
  for (let i = 0; i < n; i++) {
    answer[i] += leftOperations;
    if (boxes[i] === "1") {
      leftCount += 1;
    }
    leftOperations += leftCount; // Add the cost of moving left balls to box i
  }

  // Right to left pass
  let rightCount = 0; // Number of balls to the right
  let rightOperations = 0; // Cumulative operations from the right
  for (let i = n - 1; i >= 0; i--) {
    answer[i] += rightOperations;
    if (boxes[i] === "1") {
      rightCount += 1;
    }
    rightOperations += rightCount; // Add the cost of moving right balls to box i
  }

  return answer;
}

// Example usage
console.log(minOperations("110")); // [1,1,3]
console.log(minOperations("001011")); // [11,8,5,4,3,4]
