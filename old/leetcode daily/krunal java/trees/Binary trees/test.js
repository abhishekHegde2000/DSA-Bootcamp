// create a big pattern problem

function find(arr, target, index) {
    if (index === arr.length) {
        return false;
    }
    return arr[index] === target || find(arr, target, index + 1);
}

function findIndex(arr, target, index) {
    if (index === arr.length) {
        return -1;
    }
    if (arr[index] === target) {
        return index;
    } else {
        return findIndex(arr, target, index + 1);
    }
}

function findIndexLast(arr, target, index) {
    if (index === -1) {
        return -1;
    }
    if (arr[index] === target) {
        return index;
    } else {
        return findIndexLast(arr, target, index - 1);
    }
}

function findAllIndex(arr, target, index, list = []) {
    if (index === arr.length) {
        return list;
    }
    if (arr[index] === target) {
        list.push(index);
    }
    return findAllIndex(arr, target, index + 1, list);
}

function findAllIndex2(arr, target, index) {
    let list = [];
    if (index === arr.length) {
        return list;
    }
    if (arr[index] === target) {
        list.push(index);
    }
    let ansFromBelowCalls = findAllIndex2(arr, target, index + 1);
    list = list.concat(ansFromBelowCalls);
    return list;
}

let arr = [2, 3, 1, 4, 4, 5];
console.log(findAllIndex2(arr, 4, 0));
