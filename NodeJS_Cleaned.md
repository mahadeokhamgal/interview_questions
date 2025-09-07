What is event delegation and event bubbling?

What will be the output of the following code? (Counter with setCount twice)

How do you conditionally apply a CSS class in React? (JSX-based condition)

How does React handle events? Explain event delegation in React.

Promise.resolve().then(()=>console.log('Promise 1')) … setTimeout … console.log('End') → What is the order of execution?

What is monkey-patching?

What is AbortController?

What is Intersection Observer?

Does useEffect propagate from parent to child or child to parent?

Apply and bind in JS/TS.

What are ways to update an event from one Microservice to another Microservice?

When will you recommend using NodeJS server, and when will you not recommend it?

How to create a JWT and how to validate a JWT?

How to make my NodeJS handle increased traffic?

How to configure my NodeJS app against DDOS attacks?

What is the event loop in NodeJS?

What is Event loop?

Microtasks and Macrotasks in Event loop.

What is a worker thread in NodeJS?

Is multithreading possible in NodeJS?

What are streams in NodeJS?

How to handle file uploads in NodeJS?

Closure.

Hoisting.

How to perform global error handling in NodeJS?

What is CORS?

How to create API documentation using swagger.js in express.js?

What is order of execution in process.nextTick and setImmediate?

Guess the output of given event loop + promise + setTimeout examples.

What if I had setImmediate in the above code? Can the order switch with setTimeout(…, 0)?

What are challenges with Closure?

What is currying function in JavaScript?

What is optional chaining in JS?

What is difference between for of and for in?

What is difference between map vs reduce?

Why are JS functions called First-class Functions?

What is WeakSet and WeakMap in JS?

What is fork method in JS?

What is worker thread in JS?

How many event loops are there if used Quad core CPU and forked all cores by Node.js?

What is difference between worker threads and clusters fork in NodeJS?

Explain life cycle of request process in Backend (Express.js).

What is the usage of a buffer class in NodeJS?

What is REPL in NodeJS?

Guess the output (multiple code snippets provided).

Write a JS function to flatten the object.

Explain scenarios when you’d recommend NOT using Node.js.

# JavaScript Logical Ability Questions

1. **Write a function that converts the following input 2D array into a 1D array by solving the basic operations within each array.**  
   **Input:**  
   `[['1','*','40'], ['14', '/', '2'], ['7','+','-4']]`  
   **Output:**  
   `[40, 7, 3]`

   function solve(arr) {
    return arr.map(([a, op, b]) => {
        a = +a;
        b = +b;
        switch(op) {
            case "+": return a+b;
            case "-": return a-b;
            case "*": return a*b;
            case "/": return b == 0 ? "Cannot divide by zero Error" : a/b;
        }
    })
   }

2. **Write a function that takes an array of strings and returns a new array where each string has been reversed.**  
   **Input:**  
   `['apple', 'banana', 'cherry']`  
   **Output:**  
   `['elppa', 'ananab', 'yrrehc']`
    function reverseWords(array) {
       return array.map(el => el.split().reverse().join(''))
    }
3. **Write a function that finds the smallest number in an array of numbers.**  
   **Input:**  
   `[4, 2, 7, 1, 9]`  
   **Output:**  
   `1`
    function smallest(array) {
        return array.reduce((acc, el) => Math.min(acc, el))
    }

4. **Write a function that returns the sum of all even numbers in an array.**  
   **Input:**  
   `[1, 2, 3, 4, 5, 6]`  
   **Output:**  
   `12`
    function getSum(array) {
        return array.reduce((acc, el) => acc+el)
    }
5. **Write a function that checks if a string is a palindrome.**  
   **Input:**  
   `'racecar'`  
   **Output:**  
   `true`
    function isPalindrome(str) {
        function helper(l, r) {
            if(l > r) return true;
            else if(str[l] != str[r]) return false;
            else return helper(l+1, r-1);
        }
        return helper(0, str.length-1)
    }

6. **Write a function that returns the number of vowels in a given string.**  
   **Input:**  
   `'hello'`  
   **Output:**  
   `2`
    function getWovels(str) {
        let vowels = new Set("aeiou".split(''));
        return str.split('').reduce((acc, c) => {
            if(vowels.has(c)) {
                return acc + 1;
            } else {
                return acc;
            }
        } ,0)
    }

7. **Write a function that removes all duplicates from an array.**  
   **Input:**  
   `[1, 2, 2, 3, 4, 4, 5]`  
   **Output:**  
   `[1, 2, 3, 4, 5]`
    function removeDuplicates(str) {
        return [...new Set(arr)];
    }

8. **Write a function that returns the longest word in a given sentence.**  
   **Input:**  
   `'The quick brown fox jumped over the lazy dog'`  
   **Output:**  
   `'jumped'`
    function longestWord(str) {
        return str.split(' ').reduce((acc, word) => {
            return word.length > acc.length ? word : acc;
        })
    }

9. **Write a function that converts a number from Celsius to Fahrenheit.**  
   **Input:**  
   `0`  
   **Output:**  
   `32`

10. **Write a function that checks if a number is prime.**  
    **Input:**  
    `7`  
    **Output:**  
    `true`

11. **Write a function that capitalizes the first letter of each word in a sentence.**  
    **Input:**  
    `'hello world'`  
    **Output:**  
    `'Hello World'`
    function capitalize(str) {
        return str.split(' ').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')
    }

12. **Write a function that returns an array of all even numbers from a given range.**  
    **Input:**  
    `1, 10`  
    **Output:**  
    `[2, 4, 6, 8, 10]`
    function getEven(start, end) {
        if(start%2 != 0) start++;
        ans = [];
        for(let i = start; i <= end; i += 2) {
            ans.push(i);
        }
        return ans;
    }

13. **Write a function that removes all occurrences of a given element from an array.**  
    **Input:**  
    `[1, 2, 3, 4, 5], 3`  
    **Output:**  
    `[1, 2, 4, 5]`
    function removeElement(arr, target) {
        return arr.filter(e => e != target)
    }

14. **Write a function that returns the sum of digits in a number.**  
    **Input:**  
    `123`  
    **Output:**  
    `6`
    function getSumOfDigits(num) {
        if(num < 0) return -1;
        ans = 0;
        while(num > 0) {
            ans = ans + (num % 10);
            num = Math.floor(num / 10);
        }
        return ans;
    }

15. **Write a function that returns the nth Fibonacci number.**  
    **Input:**  
    `5`  
    **Output:**  
    `5`
    function nThFibo(num) {
       if(num<=1){
           return num;
       }
       return nThFibo(num-1)+nThFibo(num-2);
}   

16. **Write a function that checks if a number is a perfect square.**  
    **Input:**  
    `16`  
    **Output:**  
    `true`

17. **Write a function that returns the factorial of a number.**  
    **Input:**  
    `5`  
    **Output:**  
    `120`

18. **Write a function that finds the second largest number in an array.**  
    **Input:**  
    `[4, 5, 7, 1, 9]`  
    **Output:**  
    `7`

19. **Write a function that converts a string to an array of words.**  
    **Input:**  
    `'hello world'`  
    **Output:**  
    `['hello', 'world']`

20. **Write a function that returns true if a number is a perfect number. A perfect number is a number that is equal to the sum of its proper divisors.**  
    **Input:**  
    `28`  
    **Output:**  
    `true`

21. **Write a function that returns the largest number in an array.**  
    **Input:**  
    `[5, 1, 9, 4, 7]`  
    **Output:**  
    `9`

22. **Write a function that checks whether a number is a multiple of 3 and 5.**  
    **Input:**  
    `15`  
    **Output:**  
    `true`

23. **Write a function that returns the number of characters in a string excluding spaces.**  
    **Input:**  
    `'Hello World'`  
    **Output:**  
    `10`

24. **Write a function that converts a number from Fahrenheit to Celsius.**  
    **Input:**  
    `32`  
    **Output:**  
    `0`

25. **Write a function that returns the common elements between two arrays.**  
    **Input:**  
    `[1, 2, 3], [2, 3, 4]`  
    **Output:**  
    `[2, 3]`

26. **Write a function that checks if two strings are anagrams.**  
    **Input:**  
    `'listen', 'silent'`  
    **Output:**  
    `true`

27. **Write a function that returns a number as a string with commas separating every three digits.**  
    **Input:**  
    `1234567`  
    **Output:**  
    `'1,234,567'`

28. **Write a function that removes all falsy values (false, null, 0, "", undefined, NaN) from an array.**  
    **Input:**  
    `[1, null, 0, 'hello', NaN, false, 3]`  
    **Output:**  
    `[1, 'hello', 3]`
    function removeFalsy(arr) {
        return arr.filter(e => e)
    }

29. **Write a function that finds the intersection of multiple arrays.**  
    **Input:**  
    `[[1, 2, 3], [2, 3, 4], [3, 4, 5]]`  
    **Output:**  
    `[3]`
    function interSectionOf(arr) {
        if(arr.length == 1) return arr[0];
        let set = new Set(arr[0]);
        for(let i = 1; i < arr.length; i++) {
            currArr = arr[i];
            tempSet = new Set();
            for(let el of currArr) {
                if(set.has(el)){
                    tempSet.add(el);
                }
            }
            set = tempSet;
        }
        return [...set];
    }

30. **Write a function that checks if a number is even or odd.**  
    **Input:**  
    `8`  
    **Output:**  
    `'Even'`

31. **Write a function that finds the most frequent element in an array.**  
    **Input:**  
    `[1, 2, 2, 3, 3, 3, 4]`  
    **Output:**  
    `3`

32. **Write a function that calculates the greatest common divisor (GCD) of two numbers.**  
    **Input:**  
    `24, 36`  
    **Output:**  
    `12`
    function gcd(a, b) {
        a = Math.abs(a);
        b = Math.abs(b);

        if(b == 0) return a;

        return gcd(b, a%b);
    }

33. **Write a function that counts the number of occurrences of a specific character in a string.**  
    **Input:**  
    `'banana', 'a'`  
    **Output:**  
    `3`

34. **Write a function that returns a string with each letter doubled.**  
    **Input:**  
    `'hello'`  
    **Output:**  
    `'hheelllloo'`
    function makeDouble(str) {
        return str.replace(/([\w])/g, "$1_");
    }

35. **Write a function that sorts an array of numbers in ascending order.**  
    **Input:**  
    `[9, 3, 7, 1, 5]`  
    **Output:**  
    `[1, 3, 5, 7, 9]`

36. **Write a function that returns the sum of all odd numbers in an array.**  
    **Input:**  
    `[1, 2, 3, 4, 5, 6]`  
    **Output:**  
    `9`

37. **Write a function that returns the total number of words in a sentence.**  
    **Input:**  
    `'This is a test sentence'`  
    **Output:**  
    `5`

38. **Write a function that returns the number of days between two dates.**  
    **Input:**  
    `'2025-03-01', '2025-03-23'`  
    **Output:**  
    `22`

39. **Write a function that returns the reverse of an array.**  
    **Input:**  
    `[1, 2, 3, 4, 5]`  
    **Output:**  
    `[5, 4, 3, 2, 1]`

40. **Write a function that checks if a given number is divisible by another number.**  
    **Input:**  
    `20, 4`  
    **Output:**  
    `true`

# 40 JavaScript Logic-Based Questions

### 1. **Even or Odd:**
Write a function that takes a number as an argument and returns `"Even"` if the number is even, or `"Odd"` if the number is odd.

---

### 2. **Reverse a String:**
Write a function that reverses a given string without using any built-in reverse methods.

---

### 3. **Find the Maximum Number:**
Write a function that takes an array of numbers and returns the maximum number in the array.

---

### 4. **Sum of Array Elements:**
Write a function that takes an array of numbers and returns the sum of all elements in the array.

---

### 5. **Count Vowels:**
Write a function that takes a string and returns the number of vowels (`a`, `e`, `i`, `o`, `u`) in the string.

---

### 6. **Check Prime Number:**
Write a function that checks if a number is prime.

---

### 7. **Check Palindrome:**
Write a function that checks if a given string is a palindrome (it reads the same forward and backward).

---

### 8. **Find Missing Number in Sequence:**
Given an array of numbers from `1` to `n`, with one number missing, write a function to find the missing number.

---

### 9. **Find Duplicate in Array:**
Write a function that takes an array and returns the first duplicate element it finds. If no duplicates exist, return `null`.

---

### 10. **Fibonacci Sequence:**
Write a function that prints the first `n` numbers of the Fibonacci sequence.

---

### 11. **Factorial:**
Write a function that calculates the factorial of a number using a loop.

---

### 12. **Find Second Largest Element:**
Write a function that takes an array of numbers and returns the second-largest number.

---

### 13. **Flatten Nested Array:**
Write a function that flattens a nested array (an array containing arrays) into a single array.

---

### 14. **Count Occurrences of an Element:**
Write a function that counts how many times a specific element appears in an array.

---

### 15. **Remove Falsy Values:**
Write a function that removes all falsy values (`null`, `undefined`, `false`, `0`, `NaN`, and empty strings) from an array.

---

### 16. **Find Longest Word:**
Write a function that finds the longest word in a string and returns it.

---

### 17. **Sorting an Array:**
Write a function that sorts an array of numbers in ascending order without using the built-in sort function.

---

### 18. **Sum of Digits:**
Write a function that returns the sum of the digits of a given number.

---

### 19. **Sum of Positive Numbers in Array:**
Write a function that sums only the positive numbers in an array and returns the result.

---

### 20. **Find the Missing Character in String:**
Write a function that finds the character missing from a string. The string is an alphabetical sequence with one letter missing.

---

### 21. **Find Index of Element in Array:**
Write a function that takes an array and an element as arguments and returns the index of the element, or `-1` if it’s not found.

---

### 22. **Check if an Array Contains a Subarray:**
Write a function that checks if an array contains a given subarray.

---

### 23. **Check for Anagram:**
Write a function that checks if two given strings are anagrams (they contain the same letters in any order).

---

### 24. **Find the Most Frequent Element:**
Write a function that returns the element that appears most frequently in an array.

---

### 25. **Find Missing Letter in Range:**
Given a range of letters (e.g., `"a"` to `"z"`), find the missing letter in the sequence.

---

### 26. **Merge Two Sorted Arrays:**
Write a function that merges two sorted arrays into one sorted array.

---

### 27. **Remove Duplicates from an Array:**
Write a function that removes all duplicates from an array and returns the resulting array.

---

### 28. **Check if a Number is a Power of Two:**
Write a function that checks if a given number is a power of two (e.g., 1, 2, 4, 8, 16, etc.).

---

### 29. **Sum of Array Except Itself:**
Write a function that for each element in an array, calculates the sum of the other elements in the array (without using the element itself).

---

### 30. **Find Common Elements in Two Arrays:**
Write a function that finds and returns all the common elements between two arrays.

---

### 31. **Sum of Even Numbers in Array:**
Write a function that sums only the even numbers in an array.

---

### 32. **Rotate an Array:**
Write a function that rotates an array by `n` positions (e.g., rotating `[1, 2, 3, 4]` by 2 positions gives `[3, 4, 1, 2]`).

---

### 33. **Calculate the Power of a Number:**
Write a function that calculates the power of a number, where `x` raised to the power of `y` is calculated as `x^y`.

---

### 34. **Find All Divisors of a Number:**
Write a function that returns all divisors of a given number.

---

### 35. **Find Missing Number in an Unsorted Array:**
Given an unsorted array of numbers from 1 to `n`, write a function to find the missing number.

---

### 36. **Count Elements that are Greater than a Specific Value:**
Write a function that counts how many numbers in an array are greater than a specific value.

---

### 37. **Find First Non-Repeated Character:**
Write a function that finds the first non-repeated character in a string.

---

### 38. **Matrix Multiplication:**
Write a function that multiplies two 2D matrices.

---

### 39. **Check if Two Arrays are Equal:**
Write a function that checks if two arrays are equal (contain the same elements in the same order).

---

### 40. **Find Missing Number in Range:**
Write a function that finds the missing number in an array where all numbers are between `1` and `n` except for one missing number.

41. **Write a function that takes a string as input, capitalizes the first letter of each word, and then returns the string with a "#" symbol prepended to it.**
    **input**
    `"hello world"`
    **output**
    `"#HelloWorld"`

42. **Write a javascript function that returns count of given character from given string(it should count both lowercase and uppercaqse characters)**.
    **input**
    `"MissIssippi", 'i'`
    **output**
    `4`

# JS GTO
```js

console.log(typeof null);
console.log(0.1+0.2 === 0.3);
console.log([1, 2, 3] + [4, 5, 6]);
console.log('5' + 6);
console.log([] == false);
console.log({} == false);
console.log([] + {});
console.log({} + []);
console.log(typeof NaN);
console.log(!!"");
console.log(!!"false");
console.log(1 < 2 < 3);
console.log(3 > 2 > 1);
console.log([] == ![]);
console.log(typeof undefined == typeof null);
console.log(typeof function(){} === 'function');
console.log(typeof (function(){}()));
console.log([1,2,3].map(num => num*2));
console.log([1,2,3].reduce((acc, num) => acc+num, 0));
console.log(typeof typeof 1);
console.log(1 + "1" - 1);
console.log("5" - 3);
console.log(null + 1);
console.log([] == 0);
console.log({} + {}); 
console.log([1] == true);
console.log(false == 'false');
console.log(new Array(5).toString());
console.log(parseInt("10e1"));
console.log(!![]);
console.log(+"");
console.log([1,2,3] == "1,2,3");
console.log(10 > 9 > 8);
console.log(typeof (1,2,3));
console.log((function() { return typeof arguments; })());
console.log(typeof (function() { return; }()));
console.log(Math.max() < Math.min());
console.log("5" + - "2");
console.log(undefined == null);
console.log(NaN == NaN);
console.log(Object.is(NaN, NaN));
console.log(!!NaN);
console.log({a:1} == {a:1});
console.log([,,].length);
console.log([1,,2].toString());
console.log(0 == -0);
console.log(Object.is(0, -0));
console.log([] instanceof Array);
console.log(function(){}.constructor === Function);
console.log(Array.isArray([]));
console.log([1,2,3].map(parseInt));
console.log(setTimeout(() => console.log("Timeout"), 0));
console.log(Promise.resolve(5).then(console.log));
console.log("a"["toUpperCase"]());
console.log(1..toString());
console.log(new Date(0));
console.log("b" + "a" + +"a" + "a");
console.log(typeof Symbol());
console.log(typeof BigInt(123456789));
console.log((true + false) > 1);
console.log(1 < 2 && 2 < 1);
console.log(Boolean([]));
console.log(Boolean({}));
console.log(" " == 0);
console.log(new Boolean(false) == false);
console.log([1,2,3].filter(x => x));
console.log([1,2,3].find(x => x > 1));
console.log([1,2,3].findIndex(x => x > 1));
console.log([...new Set([1,1,2,2,3,3])]);
```
# Core JavaScript

- **What is JavaScript? How is it different from Java?**
- **Explain the difference between var, let, and const.**
- **What are primitive and non-primitive data types in JavaScript?**
- **How does type coercion work in JavaScript?**
- **What are JavaScript closures? Provide an example.**
- **Explain the concept of "hoisting" in JavaScript.**
- **What is the difference between == and ===?**
- **What are callback functions? Why are they used?**
- **How does the `this` keyword work in JavaScript?**
- **What are the different types of scopes in JavaScript?**
- **What is an event loop in JavaScript?**
- **How are promises used in JavaScript?**
- **Explain `setTimeout` and `setInterval`.**
- **What is the difference between `null` and `undefined`?**
- **What are JavaScript prototypes?**
- **What is the difference between synchronous and asynchronous programming?**
- **Explain how arrays are handled in JavaScript.**
- **How can you iterate over an object in JavaScript?**
- **What is the difference between `map()`, `filter()`, and `reduce()`?**
- **What are Immediately Invoked Function Expressions (IIFEs)?**
- **Explain the difference between `call()`, `apply()`, and `bind()`.**
- **What are arrow functions? How are they different from regular functions?**
- **How does JavaScript handle errors? What are `try...catch` blocks?**
- **Explain the `typeof` operator in JavaScript.**
- **What are default parameters in functions?**
- **What is event bubbling and event delegation?**
- **How does debouncing and throttling work?**
- **What are template literals? Provide an example.**
- **How can you check if a variable is an array in JavaScript?**
- **What are modules in JavaScript?**

---

# ES6 Concepts

- **What are ES6 classes? How are they different from prototypes?**
- **Explain destructuring assignment with examples.**
- **What are rest and spread operators?**
- **How does the `let` keyword handle block scope?**
- **What is a generator function in JavaScript?**
- **Explain the concept of promises and `async/await` in ES6.**
- **What is the use of the `Symbol` type in JavaScript?**
- **What are default imports and named imports in ES6?**
- **How do you create and use a Set in ES6?**
- **What are WeakMap and WeakSet in JavaScript?**
- **What are computed property names in ES6?**
- **Explain how `for...of` is different from `for...in`.**
- **What is the purpose of `Object.assign()`?**
- **How does `Object.entries()` and `Object.values()` work?**
- **What is a promise chain?**
- **How can you create an iterable object in ES6?**

---

# Advanced JavaScript

- **What are higher-order functions? Provide examples.**
- **Explain currying in JavaScript with examples.**
- **What are web APIs? How are they accessed?**
- **What is the difference between shallow copy and deep copy in JavaScript?**
- **How does garbage collection work in JavaScript?**
- **Explain the concept of `async/await` with an example.**
- **What is event propagation in JavaScript?**
- **What is the purpose of the `WeakRef` object?**
- **How can you optimize performance in JavaScript?**
- **Explain how JavaScript engines like V8 work.**
- **What is a memory leak? How can it be prevented in JavaScript?**
- **How does a service worker work with JavaScript?**
- **What is the purpose of the `Intl` object in JavaScript?**
- **How does the module pattern work in JavaScript?**

What are closures in JavaScript?

Explain the difference between var, let, and const.

What is the event loop in JavaScript?

What is a promise in JavaScript, and how do you use it?

What is a callback function, and how does it work in JavaScript?

What is the difference between == and === in JavaScript?

What is hoisting in JavaScript?

What is the difference between synchronous and asynchronous execution?

Explain how this works in JavaScript, and its difference in arrow vs normal functions.

What are JavaScript modules, and how do you import/export them?

What are arrow functions, and how are they different from regular functions?

Explain the concept of prototype in JavaScript.

What is event delegation in JavaScript?

What is the difference between null and undefined?

What is the bind() method in JavaScript?

Explain how the apply() and call() methods differ in JavaScript.

What are the different data types in JavaScript?

How does garbage collection work in JavaScript?

What is the setTimeout() function in JavaScript?

What is Scope in JavaScript?

Explain XSS attack in Web page.

Describe WeakSet and WeakMap in JavaScript.

What is arguments keyword in JavaScript?

Difference between null, undefined, undeclared.

What is prototyping?

What is Node.js, and how is it different from traditional server-side technologies?

What is the event-driven architecture in Node.js?

What is the role of the package.json file in a Node.js project?

Explain the concept of callbacks in Node.js.

What is the require() function in Node.js?

How does Node.js handle asynchronous operations?

What are streams in Node.js, and how are they useful?

What are the different types of streams in Node.js?

Explain the concept of middleware in Express.js.

What is the process object in Node.js, and how do you use it?

How do you create a simple HTTP server in Node.js?

What is the eventEmitter class in Node.js?

What is the purpose of the fs module in Node.js?

How do you handle errors in Node.js?

What is the purpose of the setImmediate() function in Node.js?

What is the difference between setTimeout() and setImmediate() in Node.js?

How do you handle file uploads in Node.js?

What is clustering in Node.js, and how does it work?

Explain the concept of "callback hell" in Node.js and how to avoid it.

What is the Buffer class in Node.js?

What is NodeJS?

What is REPL in NodeJS?

What is libuv in Node.js?

What is cluster, fork, process spawn in Node.js?

Why are NodeJS callbacks error-first?

Explain the Node.js Event Emitter.

Express.js

What is Express.js, and how does it differ from other Node.js frameworks?

How do you set up an Express.js application?

What is the purpose of middleware in Express.js?

How do you handle routes in Express.js?

What is the role of app.use() in Express.js?

How do you send a response to the client in Express.js?

How do you handle errors in Express.js?

What is the next() function in Express.js?

How do you serve static files in Express.js?

What is the purpose of express.Router() in Express.js?

How do you handle POST requests in Express.js?

How do you use Express.js with a template engine (e.g., EJS)?

What is CORS, and how do you handle it in Express.js?

How do you validate request data in Express.js?

How do you implement authentication in Express.js?

How to make my Express server only accept requests from a specific server/host?

TypeScript

What are the advantages of using TypeScript over JavaScript?

What is the difference between interface and type in TypeScript?

Explain the concept of "Generics" in TypeScript.

What are "enums" in TypeScript?

How does TypeScript handle type checking and inference?

What are "tuples" in TypeScript, and how are they used?

How do you define optional parameters in TypeScript functions?

What is the any type in TypeScript, and when should it be used?

What are never and unknown types in TypeScript?

What is the purpose of readonly in TypeScript?

What is type assertion in TypeScript?

How do you define a class in TypeScript?

What is the purpose of the as keyword in TypeScript?

How do you handle modules in TypeScript?

What are "decorators" in TypeScript?


# **Asynchronous Execution Questions**
-----------------------------------------------------------------------------------

### What are the key differences between JavaScript's Promise and RxJS Observable?

### How do you use async/await in Angular services or components?

### How does Angular handle asynchronous data in templates using the async pipe?

### What is the difference between setTimeout and setInterval in JavaScript?

### Explain how Angular handles asynchronous operations during change detection.

### How do you use Promise.all() and Promise.race() in Angular?

### What is the event loop in JavaScript, and how does it affect asynchronous code in Angular?

### How can you trigger change detection manually in Angular?

### Explain the role of zone.js in managing asynchronous operations.

### What is the NgZone service in Angular? How can it be used?

### How do you handle race conditions in Angular while making HTTP calls?

### What is the difference between then() and catch() in Promises and subscribe() in Observables?

### What are microtasks and macrotasks in JavaScript? How do they impact Angular execution?

### How can you make an Angular component wait for multiple asynchronous operations to complete?

### What is the purpose of setImmediate()? How does it compare to setTimeout()?

### How do you handle asynchronous errors in Angular?

### What is the purpose of await with try-catch for handling errors in asynchronous functions?

### How do you debounce user input in Angular using both Observables and Promises?

### How do you combine asynchronous data with real-time updates in Angular?

### Explain the rxjs/ajax package and how it is used for asynchronous executions in Angular.


# **NodeJS**
-------------------------------------------------------------------------------

### 1. How to use Jwt in angular and at the expressjs side.

### 2. Validating data at serverside in expressjs.

### 3. Authorization methods.

### 4. Can one use get api to create records in db.

### 5. Rest Api packages at server side in express js.

### 6. Ways to make APIs at the server side.

### 7. How to connect to a databases(mongo and sql) in express.

### 8. What are middlewares in express.

### 9. What is Http interceptor in angular.

### 10. How to apply a middleware only to one route handler in expressJS.


- **What are ways to update an event from one Microservice to another Microservice?**
- **When will you recommend using NodeJS server, and when will you not recommend it?**
- **What information does a JWT token have?**
- **How to create a JWT and how to validate a JWT?**
- **How to make my NodeJS handle increased traffic?**
- **How to configure my NodeJS app against DDOS attacks?**
- **What is the event loop in NodeJS?**
- **How to make cookies as secure as possible?**
- **What is Event loop?**
- **Microtasks and Macrotasks in Event loop.**
- **What is a worker thread in NodeJS?**
- **Is multithreading possible in NodeJS?**


- What are streams in nodejs.
- How to handle file uploads in nodejs.
- Closure.
- Hoisting.
- How to perform global error handling in nodejs.
- what is deep copy vs shallow copy.
- What is cors.

What will you choose between customised package and readymade package from npm.

What is a closure?

What is the event loop?

What are types of streams in Node.js?

How many types of streams are there in Node.js?

What is cluster in Node.js?

How many event loops are in one process?

If I used cluster to fork all remaining cores of octa core CPU, how many event loops and processes will be there?

Guess the output of the following (event loop, promises, nextTick).

What if I had setImmediate in the above code? Can the order switch with setTimeout(…, 0)?

What are challenges with Closure?

What is currying function in JavaScript?

What is optional chaining in JS?

What is difference between for of and for in?

What is difference between map vs reduce?

Why are JS functions called First-class Functions?

What is WeakSet and WeakMap in JS?

What is fork method in JS?

What is worker thread in JS?

How many event loops are there if used Quad core CPU and forked all cores by Node.js?

What is difference between worker threads and clusters fork in NodeJS?

What is the usage of a buffer class in Node.js?

What is REPL in Node.js?

Write code to convert → Input: India is my country → Output: India Is My Country


**Guess the output**
1. Guess the output for below block and if any error, name the error you'll get and then provide fix for the error.
```js
{
  let a = 10;
  {
    let a = 20;
    {
      console.log(a);
      let a = 30;
      console.log(a);
    }
    console.log(a);
  }
}
```

2. Guess the output for below block and if any error, name the error you'll get and then provide fix for the error.
```js
console.log("z");
a();
b();
function a() {
    console.log("a");
}
console.log("c");
var b = () => {
    console.log("b");
}
console.log("d");
```

3. Guess the output for below block.
```js
let printVal = (z) => {
    setTimeout(() => {
        console.log(z)
    }, 0);
}

for (var x = 0; x <= 5; x++) {
    printVal(x);
}
```

4. Guess the output for below block.
```js
//1
const arr=["name"]; 
const obj={name:"hi"}; 
obj.name="Hi"; 
obj[arr]="how?"; 
console.log(obj.name);

//2
const arr=["n", "a", "m", "e"]; 
const obj={name:"hi"}; 
obj.name="Hi"; 
obj[arr]="how?"; 
console.log(obj.name);
```

5. Guess the output for below block.
```js
let a = [1,2,3];
let b = [1,2,3];
let c = "1,2,3";
console.log(a == c);
console.log(b === c);
console.log(a == b);
```

6. Guess the output for below block.
```js
let a = [1, 2, 3, 4, 5];
a[10] = 10;
console.log(a.length);
```

7. Guess the output for below block.
```js
async function async1() {
  console.log('async1 start');
  await async2();
  console.log('async1 end');
}
new Promise(function(resolve) {
  console.log('promise1');
  return resolve();
}).then(function() {
  console.log('promise2');
});
async function async2() {
  console.log('async2');
}
console.log('script start');
setTimeout(function() {
  console.log('setTimeout');
}, 0);
async1();
new Promise(function(resolve) {
  console.log('promise3');
  return resolve();
}).then(function() {
  console.log('promise4');
});
console.log('script end');
```

**Coding challenges**
`Q1. Create Angular  component which will have a progress bar.`
  1 It will initiate from 0% on page load.   
  2. It will increment after 1 secs by 10%.
  3. The progress bar will keep on incrementing till the width of the page is met.
  4. Create reset button which will start the progress bar from 0 again.

--------------------------------------------------------------------------------------------

`Q2. Write a JS function to Flatten the object.`
`Given below is input and output format.`
```js
IP = const data = {
  user: {
    id: 101,
    stats: {
      age: "30",
      score: 95
    }
  },
  settings: [
    {
      volume: "100",
      brightness: 70
    },
    {
      contrast: "85",
      sharpness: 90
    }
  ],
  logs: [
    { event1: "1", event2: "2" },
    { event3: 3, event4: "4" }
  ],
  metrics: {
    daily: [
      { day1: 10, day2: "20" },
      { day3: "30", day4: 40 }
    ],
    weekly: {
      week1: { views: "100", clicks: 50 },
      week2: { views: 200, clicks: "150" }
    }
  }
};

OP = [101, 30, 95, 100, 70, 85, 90, 1, 2, 3, 4, 10, 20, 30, 40, 100, 50, 200, 150];
```

//String anagram
//Find min and max element in array
//Find the string in JavaScript sentence which has longest length
//Find object with given id.
# Write function to convert:
Input:  { id: 123, name: 'John', email: 'john@email.com' }  
Output: { 123: 'id', John: 'name', 'john@email.com': 'email' }