# MEAN Stack Interview Questions

## JavaScript (20 Questions)

1. What are closures in JavaScript?
    - `A closure is a feature in JavaScript where a function (child function) retains access to variables from its parent function, even after the parent function has finished executing.`
    e.g. 
    function parentFun() {
        let parentVar = 1;
        return () => {
            parentVar += 1;
            return parentVar;
        }
    }
    let childFun = parentFun();
    console.log(childFun());
    console.log(childFun());

2. Explain the difference between `var`, `let`, and `const`.
    `var` - 1. both redeclaration and reassignment is possible. 2.before ES6. 3. Doesn't enter TDZ. 4. function scope.
    `let` - 1. no redeclaration possible, reassignment is possible.2.  Introduced in ES6. 3. Enters TDZ. 4. Block scope.
    `const` - 1. no redeclaration or reassignment possible. 2. Introduced in ES6. 3. Enters TDZ. 4. Block scope.

3. What is the event loop in JavaScript?
    `Event loop is a fundamental part of JavaScript’s concurrency model, It checks for call stack and if it's empty, if it's empty it moves tasks from Task Queues(Macro and Micro) into call stack`
    - **Micro** - Promise callbacks, queueMicrotask.
    - **Macro** - I/O tasks, timers (setTimeout, setInterval), and events.

4. What is a promise in JavaScript, and how do you use it?
    `Introduced in ES6, are a better way of handling async operations which help overcoming callback hell issue in callback async programming, Promise is an object that provides eventual resolution or rejection to async task. Promise has 3 states named - Pending, resolved, Rejected`
    - Promises are handled using .then and .catch syntax.

5. What is a callback function, and how does it work in JavaScript?
    - 
6. What is the difference between `==` and `===` in JavaScript?
7. What is hoisting in JavaScript?
8. What is the difference between synchronous and asynchronous execution?
9. Explain how `this` works in JavaScript, and it's difference in terms of an arrow and normal function in terms of object.
10. What are JavaScript modules, and how do you import/export them?
11. What are arrow functions, and how are they different from regular functions?
12. Explain the concept of prototype in JavaScript.
13. What is event delegation in JavaScript?
14. What is the difference between `null` and `undefined`?
15. Explain the concept of closures in JavaScript with an example.
16. What is the `bind()` method in JavaScript?
17. Explain how the `apply()` and `call()` methods differ in JavaScript.
18. What are the different data types in JavaScript?
19. How does garbage collection work in JavaScript?
20. What is the `setTimeout()` function in JavaScript?

## TypeScript (15 Questions)

1. What are the advantages of using TypeScript over JavaScript?
2. What is the difference between `interface` and `type` in TypeScript?
3. Explain the concept of "Generics" in TypeScript.
4. What are "enums" in TypeScript?
5. How does TypeScript handle type checking and inference?
6. What are "tuples" in TypeScript, and how are they used?
7. How do you define optional parameters in TypeScript functions?
8. What is the `any` type in TypeScript, and when should it be used?
9. What are `never` and `unknown` types in TypeScript?
10. What is the purpose of `readonly` in TypeScript?
11. What is type assertion in TypeScript?
12. How do you define a class in TypeScript?
13. What is the purpose of the `as` keyword in TypeScript?
14. How do you handle modules in TypeScript?
15. What are "decorators" in TypeScript?

## Node.js (20 Questions)

1. What is Node.js, and how is it different from traditional server-side technologies?
2. What is the event-driven architecture in Node.js?
3. What is the role of the `package.json` file in a Node.js project?
4. Explain the concept of callbacks in Node.js.
5. What is the `require()` function in Node.js?
6. How does Node.js handle asynchronous operations?
7. What are streams in Node.js, and how are they useful?
8. What are the different types of streams in Node.js?
9. Explain the concept of middleware in Express.js.
10. What is the `process` object in Node.js, and how do you use it?
11. How do you create a simple HTTP server in Node.js?
12. What is the `eventEmitter` class in Node.js?
13. What is the purpose of the `fs` module in Node.js?
14. How do you handle errors in Node.js?
15. What is the purpose of the `setImmediate()` function in Node.js?
16. What is the difference between `setTimeout()` and `setImmediate()` in Node.js?
17. How do you handle file uploads in Node.js?
18. What is clustering in Node.js, and how does it work?
19. Explain the concept of "callback hell" in Node.js and how to avoid it.
20. What is the `Buffer` class in Node.js?

## Angular (20 Questions)

1. What is Angular, and how does it differ from other JavaScript frameworks like React or Vue?
2. What are components in Angular?
3. How does two-way data binding work in Angular?
4. What is dependency injection in Angular?
5. What are Angular services, and how do you create one?
6. What is the purpose of the `ngOnInit` lifecycle hook in Angular?
7. What is the purpose of the `ngFor` directive in Angular?
8. How does routing work in Angular?
9. What are pipes in Angular, and how do you create one?
10. What are directives in Angular, and how are they different from components?
11. What is RxJS, and how is it used in Angular?
12. How do you handle forms in Angular?
13. What is an observable, and how do you subscribe to it in Angular?
14. How do you create a custom directive in Angular?
15. What is Angular CLI, and how do you use it?
16. What are Angular modules, and why are they important?
17. What is lazy loading in Angular?
18. What are Angular guards, and how are they used in routing?
19. What is the role of `ngModel` in Angular?
20. What is change detection in Angular?

## Express.js (15 Questions)

1. What is Express.js, and how does it differ from other Node.js frameworks?
2. How do you set up an Express.js application?
3. What is the purpose of middleware in Express.js?
4. How do you handle routes in Express.js?
5. What is the role of `app.use()` in Express.js?
6. How do you send a response to the client in Express.js?
7. How do you handle errors in Express.js?
8. What is the `next()` function in Express.js?
9. How do you serve static files in Express.js?
10. What is the purpose of `express.Router()` in Express.js?
11. How do you handle POST requests in Express.js?
12. How do you use Express.js with a template engine (e.g., EJS)?
13. What is CORS, and how do you handle it in Express.js?
14. How do you validate request data in Express.js?
15. How do you implement authentication in Express.js?

## MongoDB (10 Questions)

1. What is MongoDB, and how does it differ from relational databases?
2. What are collections and documents in MongoDB?
3. How do you connect to a MongoDB database using Node.js?
4. What is a MongoDB query, and how do you use it?
5. What are indexes in MongoDB, and why are they important?
6. How do you perform CRUD operations in MongoDB?
7. What is the aggregation framework in MongoDB?
8. How does MongoDB handle schema design and validation?
9. What is replication in MongoDB?
10. What is the purpose of sharding in MongoDB?

---

I hope this helps! Let me know if you'd like to make any adjustments to the list. Would you like me to save it as a file for you?
