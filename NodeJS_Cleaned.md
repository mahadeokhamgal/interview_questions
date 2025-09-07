1. JavaScript: Core Concepts & GTO / Logical Questions
`Core JS Concepts`
# What is JavaScript? How is it different from Java?
# Difference between var, let, and const
# Primitive vs non-primitive data types
# Type coercion in JavaScript
# Difference between == and ===
# setTimeout vs setInterval
# Closures and examples
# Hoisting in JavaScript
# Callback functions and usage
# this keyword and arrow vs normal functions
# Different types of scopes
# Event loop
# Promises and async/await
# setTimeout vs setInterval
# null vs undefined vs undeclared
# Prototypes and prototypal inheritance
# Synchronous vs asynchronous execution
# IIFE (Immediately Invoked Function Expressions)
# call(), apply(), bind()
# Arrays: map(), filter(), reduce(), iteration
# Error handling: try-catch
# typeof operator
# Default parameters
# Template literals
# Modules and import/export

`Advanced / ES6 JS`
# ES6 Classes vs prototypes
# Promise.all() and Promise.race() usage
# Destructuring assignment
# Rest and spread operators
# let block scope
# Generator functions
# Symbol type
# Default and named imports
# Sets, WeakSets, WeakMaps
# Computed property names
# for…of vs for…in
# Object.assign(), Object.entries(), Object.values()
# Promise chains
# Iterable objects
# Higher-order functions
# Currying
# WeakRef
# Garbage collection, memory leaks, and performance optimization
# Service workers
# Module pattern

`JS Logical / GTO`
```js
typeof null, undefined, NaN, Symbol, BigInt

0.1 + 0.2 === 0.3

1 < 2 < 3, 3 > 2 > 1

[] + {}, {} + []

null + 1, [] == false, {} == false, [] == ![]

[1,2,3].map(parseInt), [1,2,3].reduce()
```
# Async/Await, setTimeout, setImmediate, process.nextTick execution
# Array behavior: sparse arrays, length, map/reduce/filter
# Closure, hoisting, scope errors
# Function vs arrow function behavior
# Coding / Logical Challenges
# Flatten nested object
# Convert 2D array with operators to 1D array
# Reverse strings / capitalize words / count vowels / anagrams
# Remove duplicates in array, find intersection, most frequent element
# Min and max element in array
# GCD, Fibonacci, factorial, prime checking
# Convert object key-value format (e.g., {id:123} → {123:'id'})
# String manipulations (palindrome, longest word in sentence)

2. NodeJS & ExpressJS
`NodeJS Core`
# Node.js overview vs traditional server-side technologies
# Event-driven architecture
# Event loop, microtasks vs macrotasks
# Worker threads, clusters, fork, process spawn
# Streams: types, usage
# REPL in Node.js
# Buffer class usage
# libuv in Node.js
# Handling file uploads
# Global error handling
# Deep copy vs shallow copy
# Garbage collection
# NodeJS callbacks: error-first style
# NodeJS Networking & Server
# HTTP server creation
# process object
# EventEmitter class
# setImmediate() vs setTimeout()
# Handling increased traffic
# Securing cookies
# DDOS protection
# JWT creation, validation, and content
# Middleware usage
# Authorization and authentication
# Connecting to MongoDB / SQL databases

`ExpressJS`
# Express overview vs other NodeJS frameworks
# Setting up an Express app
# Middleware concepts, usage, and route-specific middleware
# Handling routes (GET, POST)
# app.use() and express.Router()
# Sending responses and error handling
# next() function
# Serving static files
# Using template engines (EJS)
# CORS handling
# Validating request data
# Authorization methods

3. Specific Coding / Guess-the-Output Examples
Scope / Hoisting / Closure
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

# Async / Event Loop
```js
let printVal = (z) => {
    setTimeout(() => { console.log(z) }, 0);
}
for (var x = 0; x <= 5; x++) {
    printVal(x);
}

async function async1() { 
    console.log('async1 start');
    await async2();
    console.log('async1 end'); 
}
async function async2() {
    console.log('async2');
}
new Promise(resolve => { 
    console.log('promise1');
    resolve();
    }).then(() => console.log('promise2'));
new Promise(resolve => {
    console.log('promise3'); resolve();
    }).then(() => console.log('promise4'));
console.log('script start');
setTimeout(() => console.log('setTimeout'), 0);
async1();
console.log('script end');
```

# Object / Array Behavior
```js
 const arr=["name"];
 const obj={name:"hi"};
 obj.name="Hi";
 obj[arr]="how?";
 console.log(obj.name);
 
 let a=[1,2,3], b=[1,2,3], c="1,2,3";
 console.log(a==c, b===c, a==b);
 let a=[1,2,3,4,5];
 a[10]=10;
 console.log(a.length);
```

String / Object Transformations
# Convert "India is my country" → "India Is My Country"
# Convert { id: 123, name: 'John', email: 'john@email.com' } → { 123:'id', John:'name', 'john@email.com':'email' }