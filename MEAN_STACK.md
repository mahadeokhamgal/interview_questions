# Angular

- **MergeMap(Parallel Execution) vs Fork Join.**
- **ConcatMap(Serial Execution), SwitchMap(debauncing), exhaustMap(throttling)**
- **What is Debouncing and Throttling?**
- **Difference between AngularJS and Angular.**
- **Angular 16 Features:**
  - Standalone
  - Signal
- **What is JWT?**
- **Is it needed to use jwt on socket**
- **Where should Client store JWT?**
- **What all information a JWT token has?**
- **What is Profiling in Angular**
- **How to make routes/components protected in Angular?**
- **Alternative methods to JWT.**
- **Ways to pass data between unrelated components in Angular.**
- **Ways to pass data between related components.**
- **What is change detection in Angular and how it works?**
- **Change detection strategies**
- **What is Lazy loading?**
- **When to use forChild in angular.**
- **What are types of lazy loading in angular**
- **What is Content projection?**
- **List change detection strategies.**
- **What is role of Zone in angular**
- **What is the `Inject` keyword?**
- **What is `keyvalue` pipe, and its optional arguments? On what type of inputs can it be used?**
- **What are custom elements in Angular?**
- **How are custom elements different in terms of Standalone and non-standalone components?**
- **Are JS components possible in Angular?**
- **What is a decorator?**
- **Apply and bind in JS/TS.**
- **What is SSO (Single Sign-On)?**
- **What is PWA (Progressive Web App)?**
- **What is Angular Universal?**
- **What is a Service Worker in Angular?**
- **What is `Renderer2` in Angular?**
- **beforeEach vs beforeAll in Angular.**
- **When should one use MockServices and when to use Actual services?**
- **How to perform integration testing in Angular?**
- **`inject` vs `@Inject` vs `TestBed.inject` vs constructor injection in Angular.**
- **What is `tick` in Angular?**
- **What is `fakeAsync` in Angular?**
- **Is multithreading possible in Angular?**

---

# HTML

1. **Semantic elements** and features provided by semantics.
2. **How to make a password show and hide?**
3. **How to make my div resize and adjust to dynamic elements coming in?**
4. **How to create responsive web pages?**
5. **What does Less/Sass provide over CSS?**
6. **What is `em` and `rem`?**
7. **What are all relative units in CSS?**

---

---
# CSS
1. what is difference between flex-grow: 1; and flex: 1;
---

# NodeJS

- **What are ways to update an event from one Microservice to another Microservice?**
  - 1. Direct Apis to microservices are one of the ways.
  - 2. Can use Message broker like Kafka to make it more robust to handle messages.

- **When will you recommend using NodeJS server, and when will you not recommend it?**
  - 1. CPU-Intensive Tasks.
  - 2. High-Precision Financial Systems.
  - 3. Monolithic Enterprise Apps with Heavy Business Logic.
  - 4. Multi-threaded Background Processing.

- **What information does a JWT token have?**
  - Headers, payload, Signature.
  - Headers - type of token and algorithm used to sign it.
  - payload - iss, sub, aud, exp, nbf, exp, iat, jti + custom claims.
  - Signature - HMACSHA256(..., secret).

- **How to create a JWT and how to validate a JWT?**
  - create using jwt.sign(obj, key) #(import jwt from 'jsonwebtoken';)
  - validate using jwt.validate(token, key)

- **How to make my NodeJS handle increased traffic?**
  1. Optimize Your Node.js App First (Code Level)
    a. Avoid Blocking Operations
    b. Use Asynchronous Code Properly
    c. Limit Payload Size
  2. Use Clustering (Multi-core Support)
  3. Use a Reverse Proxy (e.g., NGINX or HAProxy)
  4. Horizontal Scaling (Multiple Machines/Containers)
  5. Use Caching Strategically
  - a. In-memory cache (per instance).
  - b. Distributed cache (shared between instances).
  6. Use a Database That Scales
  

- **How to configure my NodeJS app against DDOS attacks?**
- **What is the event loop in NodeJS?**
- **How to make cookies as secure as possible?**
- **What is Event loop?**
- **Microtasks and Macrotasks in Event loop.**
- **What is a worker thread in NodeJS?**
- **Is multithreading possible in NodeJS?**

---

# SQL

- **What is indexing?**
- **Is it advisable to add indexing to all columns of a table?**

---

# Cloud

- **What is an EC2 server?**

---

# System Design

- **What is Vertical and Horizontal scaling?**
- **Why is horizontal scaling needed if vertical scaling is available?**
- **What is Leader/(Master)-Follower architecture?**
- **What is Sharding and Partitioning?**
- **Can two partitions have identical data? Why?**
- **When to use sharding and when not to?**

**Addition**
1. Difference between deepCopy and ShallowCopy.
2. What is flex-box.
3. What re properties of flex-box.
4. Difference between forkJoin vs combineLatest.
5. What is standalone component?
6. What is difference between Promise and Observable.
7. List few ES6 features.
8. What is change detection in Angular.
9. When to use UpgradeModule and DownGrademodule in angular.
10. Difference between MergeMap and SwitchMap.
11. How to create simulteneus/parallel API calls?
12. Create a custom pipe.
13. write function to convert below input to output format.
-input - {'id': 123, 'name': 'John', 'email': 'john@email.com'}
output - {123:'id', 'John': 'name', 'john@email.com': 'email'}
14. Write a reactive form(component side only) as below.
- 3 input fields.
  1. name.
  2. date of birth.
  3. phone number.

- what are types of indexex in mongodb.
- how to use pagination in mongodb
- What should be order of queries in aggregation pipeline for optimised performance in mongodb.
- 
- What are streams in nodejs.
- How to handle file uploads in nodejs.
- Closure.
- Hoisting.
- How to perform global error handling in nodejs.
- what is deep copy vs shallow copy.
- What is cors.
**How to create api documentation using swagger.js in express.js?

- 
- What is content projection in angular.
- what is order of execution in process.nextTick and setimmediate.
- 
- What is purpose of ngOnChanges.
- What is purpose of viewchild.
- What does it mean b y bootstrapping in angular.
- What is view encapsulation in angular.
- How many type guards are there.
- What is pure and impure pipe
- patch vs put.


----------------------------------------------------------------------
- What are inline and block elements.
- How do you design your pages, mobile in mind or desktop screen in mind ?
- What are decorators Decorators.
- What will you choose between customised package and readymade package from npm.
- How is angular better than other frameworks ?
- Challenges migrating angularjs to angular.
- Routing in angular?
- How is Lazy loading better? / When will you recommend lazy loading ?
- How angular application starts?
- Bootstrap vs Angular material.
- What is Storages in browser.
- What are disadvantages of cookies.
- Which code review procedure do you follow.
- What is Your way of managing your respositories.
----------------------------------------------------------------------
1. How to optimise grid like data in angular.
2. How to optimise performance of API's only from frontend side.
3. How will you implement test framework in your project if there was not any testing being done before.
4. How to implement multistep angular form.
----------------------------------------------------------------------

1. Name me all sorting algorithms you know.
2. What is a closure?
3. Why is Angular an SPA?
4. What are micro-frontends in Angular?
5. What is SSR?
6. What is the event loop?
7. What is an auth guard?
8. How does lazy loading work in Angular?
9. What are types of streams in Node.js?
10. How many types of streams are there in Node.js?
11. What is cluster in nodejs.
12. How many event loops are in one process.
13. if I used cluster to fork all remaining cores of octa core cpu, how many event loops and processes will be there.
14. Write code for:
    ```
    Input:  India is my country
    Output: India Is My Country
    ```
15. Guess the output of the following:
    ```js
    console.log("Start");

    setTimeout(() => {
        console.log("setTimeout 1");
    }, 0);

    Promise.resolve().then(() => {
        console.log("Promise 1");
    });

    process.nextTick(() => {
        console.log("nextTick 1");
    });

    setTimeout(() => {
        console.log("setTimeout 2");
    }, 0);

    Promise.resolve().then(() => {
        console.log("Promise 2");
    });

    process.nextTick(() => {
        console.log("nextTick 2");
    });

    console.log("End");
    ```

16. What if I had `setImmediate` in the above code? Can the order switch with `setTimeout(…, 0)`?

-----------------------------------------------------------

1. What is Difference between sessions and cookie?
2. What are disadvantages of cookie?
3. What is indexing in mongodb?
4. Can we do multiple indexing of same collection?
5. What is a singleton component?
6. What is View encapsulation in Angular?
7. How to force you style to get applied in angular, irrespective of element heirarchy ? (What is ::ng-deep in angular?)
8. What if component A is emulated, component B is ShadowDom and component C is None. How will styles react in this case?
9. What is the return type of interceptor in angular?
10. What are challenges with Closure?
11. What is currying function in javascript?
12. What is optional chaining in js?
13. what is difference between `for of` and `for in`?
14. What is difference between `map` vs `reduce`.
15. Why are JS functions called `First-class Functions`?
16. What is `Weak set` and `Weak map` in JS?
17. what is fork method in JS?
18. what is worker thread in JS?
19. How many event loops are there if used Quad core CPU and forked all cores by Node.js?
20. What is difference between `ng-content` vs `ng-container`?
21. What is difference between `@ViewChild` and `@ContentChild`?
22. How we can reduce Angular Build Size?
23. What is difference between `worker threads` and `Clusters fork` in node?
24. Explain life cycle of request process in Backend(Express.js).
25. What is Left Join in SQL?
26. Is is possible to create join between two collections in mongoDB?
27. Do you think that `TypeScript` supports all object-oriented principles?
28. Explain how the Centralized Workflow works.
29. Explain the scenarios when you'll recommend not using Node.js.
30. What is the usage of a buffer class in Node.js?
31. What is REPL In Node.Js?
32. Define Dependency Injection.
33. Define Cross-site Scripting (XSS).
34. What is a Grid System in CSS?
35. Explain the main difference between REST and GraphQL.
36. What is docker? 
37. What is redis server?
38. Explain me Redux toolkit.
39. 

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