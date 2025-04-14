const fruits = ['apple', 'orange', 'banana'];
const colors = ['red', 'orange', 'yellow'];
const fruitColors = fruits.map((fruit, index) => {
    return `${fruit} is ${colors[index]}`;
});
console.log(fruitColors);