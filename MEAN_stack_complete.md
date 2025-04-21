# 📚 Web Development Interview Questions (Grouped & Formatted)

---

## 🌐 JavaScript Basics

- What is hoisting?
- Difference between `let`, `const`, and `var`?
- What are callbacks?
- How do you avoid callback hell in JavaScript?
- What is a callback in JavaScript?
- Call, apply and bind methods
- What is a first-class function?
- What is a closure? Any disadvantages?
- Currying function in JavaScript
- Optional chaining
- Difference between `for...of` and `for...in`
- `map` vs `reduce`
- Prototype in JavaScript
- Arrow function vs normal function
- What is the event loop?
- Is Node.js single-threaded or multi-threaded?
- How do we make Node.js multi-threaded?
- What is scope in JavaScript?
- What is a promise? How to resolve one?
- Promises vs async/await
- What is a WeakMap and WeakSet?
- Features of ES6
- Difference between ES5 and ES6
- JS vs TS (TypeScript)
- What is CORS?

### JavaScript Programming Questions

```js
// 1. Variable shadowing and hoisting
let a =10;
{
  let a = 20;
  {
    console.log(a);
    let a = 30;
    console.log(a);
  }
  console.log(a);
}

// 2. Function and arrow function hoisting
console.log("z");
a();
b();
function a() { console.log("a"); }
console.log("c");
var b = () => { console.log("b"); }
console.log("d");

// 3. Asynchronous setTimeout
for (var x = 0; x <= 5; x++) {
  printVal(x);
}
let printVal = (z) => {
  setTimeout(() => {
    console.log(z);
  }, 0);
};

// 4. Object property confusion
const arr = ["name"];
const obj = { name: "hi" };
obj.name = "Hi";
obj[arr] = "how?";
console.log(obj.name); // Output?

// 5. Comparison
let a = [1,2,3];
let b = [1,2,3];
let c = "1,2,3";
console.log(a == c); // true
console.log(b == c); // true
console.log(a == b); // false

// 6. Sparse array
let a = [1,2,3,4,5];
a[10] = 10;
console.log(a.length); // 11

// 7. Async/Await vs Promise
async function async1() {
  console.log('async1 start');
  await async2();
  console.log('async1 end');
}
async function async2() {
  console.log('async2');
}
console.log('script start');
setTimeout(() => { console.log('setTimeout'); }, 0);
async1();
new Promise(function(resolve) {
  console.log('promise1');
  resolve();
}).then(function() {
  console.log('promise2');
});
new Promise(function(resolve) {
  console.log('promise3');
  resolve();
}).then(function() {
  console.log('promise4');
});
console.log('script end');


🧠 Logical & Coding Exercises
Write a program to remove duplicates and return unique values only:
Input: [1,2,3,3,4,4,5] → Output: [1,2,5]

Program to print count of each alphabet in a string

Write a program to find mid based on weightage

💻 Node.js Concepts
Event loop

Middleware in Node.js

Authentication and Authorization

JWT Token

REST API - PUT vs PATCH

Cluster vs Worker Threads

How clusters work in Node.js?

What is a fork?

Optimizing Node.js applications (asynchronous programming, caching, async/await)

What is REPL in Node.js?

What is the usage of the buffer class?

EventEmitter vs EventListener

What is a callback in Node.js?

What is a single-threaded architecture?

When should Node.js NOT be used?

What is the child process module?

🌿 MongoDB / Database
What is indexing in MongoDB?

Can we do multiple indexing on the same collection?

Aggregation, pipeline, and chaining in MongoDB

Joins in MongoDB ($lookup)

Data modeling

Difference between session and cookies

Difference between localStorage, sessionStorage, and cookies

Left Join vs Right Join in MySQL

Indexing and how it improves performance

🧰 DevOps & Tooling
What is Docker? What is a container?

What is a Redis server?

Jenkins, PM2, Kubernetes – what are they?

Explain deployment process on the server

What is containerization?

Popular DevOps tools: Jenkins, Docker, Git, Ansible, Selenium, Nagios

🧩 Angular & Frontend
Angular Core Concepts
What is binding in Angular?

What is a guard? Types of route guards

What is an interceptor in Angular?

Return type of interceptor

View Encapsulation

What is a singleton component?

What is a provider?

Angular Lifecycle Hooks

Angular CLI

Dependency Injection

Two-way Data Binding

Directives

EventEmitter

@ViewChild and @ContentChild

Pure vs Impure Pipes

Angular Optimization – Build Size, Performance

Angular Coding Task – Progress Bar Component
Component to show progress bar:

Starts at 0% on page load

Increments by 10% every second

Stops when it reaches 100% width

🔁 RxJS
What is RxJS?

Observable

Subject vs BehaviorSubject

🛡️ Authentication
Difference between authentication and authorization

What is JWT?

Authentication packages in Node.js/Angular

🏗️ MEAN Stack Overview
MongoDB: Stores and retrieves data

ExpressJS: Connects database and frontend, manages routes

Angular: Frontend, handles UI and SPA

NodeJS: Server-side, handles requests

🛠️ TypeScript
Decorators in TypeScript

Classes vs Interfaces

How TypeScript supports OOP principles (Inheritance, Encapsulation, Abstraction, Polymorphism)

TypeScript as optionally statically typed language

🔐 Security
Cross-site Scripting (XSS)

CORS policy

🧭 Version Control & Workflows
Centralized Workflow

Git basics

🔎 Other Common Questions
Your role in the project

Describe a full-stack project you designed

Are you comfortable explaining code logic?

Able to solve logical problems?

✅ Self-Rating Checklist
JavaScript
 Hoisting

 ES6 features

 Promises & Promise.all

 Resolve promises

 Closures

 Promises vs Async/Await

 JS vs TS

Angular
 Lifecycle methods

 Directives

 Pipes & Filters

 Services and Constructors

 Event Handling

 Optimization

Node.js
 Middleware

 Authentication & Authorization

 Event Emitter

 Web Socket

 Queue

 REST API

 Security

 Optimization

Other
 Express

 MongoDB

 Aggregation

 TypeORM

 Docker / Containers

 PM2 / Jenkins

 Able to explain code

 Cloud (AWS)

