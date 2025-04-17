// function flattenArray(arr) {
//     let ans = [];

//     function dfs(ar) {
//         for(let el of ar){
//             if(Array.isArray(el))
//                 dfs(el)
//             else
//                 ans.push(el);
//         }
//     }
//     dfs(arr);
//     return ans;
// }

function flattenArray(arr) {
    let ans = [];
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            ans = ans.concat(flattenArray(arr[i]));
        } else {
            ans.push(arr[i])
        }
    }
    return ans;
}

function flattenArray(arr) {
    let result = []; 
    arr.forEach(element => {
        if (Array.isArray(element)) {
            result = [...result, ...flattenArray(element)]; // Recursively flatten nested arrays
        } else {
            result.push(element);
        }
    });
    return result;
}



let arr = [1, 2, [3, 4, [5, 6], [7, 8]], [10]]
console.log(flattenArray(arr));



let a = [12,2,34,5,3,9,77];

let r = a.toSorted((a,b) => a-b);
console.log(r);
