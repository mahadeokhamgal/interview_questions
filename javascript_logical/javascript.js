//String anagram
function stringAnagram(str1, str2) {
    let freqArray = new Array(26).fill(0);
    for(let ch of str1) 
        freqArray[ch.charCodeAt(0)-'a'.charCodeAt(0)] += 1
    for(let ch of str2) 
        freqArray[ch.charCodeAt(0)-'a'.charCodeAt(0)] -= 1
    return freqArray.every(el => el === 0);
}
console.log(stringAnagram("abccg", "bagccc"));

//Find min and max element in array
function getMinMax(arr) {
    return arr.reduce(([minE, maxE], el) => {
        return [Math.min(minE, el), Math.max(maxE, el)]
    }, [Infinity, -Infinity])
};

console.log(getMinMax([1, 2, 3, 4, 5, 6, 5, 4, 9, 7, 12, 23, 4, 3, 2, 15, 6]));

//Find the string in JavaScript sentence which has longest length
function getLongestWord(str) {
    return str.split(' ').reduce((acc, word) => {
        return acc.length > word.length ? acc : word;//this will give latest string with longest length;
    })
}

console.log(getLongestWord("Find out the longest string in this"));

//Find object with given id.
function getObjWithId(arr, id) {
    return arr.find(el => el.id === id);
}

console.log(getObjWithId([{id:1, name: 'John'}, {id: 4, name: "Shane"}], 4));
