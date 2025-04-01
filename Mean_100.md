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
    `Way of asynchronous programing in Javascript before Promises etc, this leverages feature of higher order functions in JS, executes a function asynchronously though callee fucntion after some block of code has been executed to emulate async nature.`
    - Callback hell is a challenge with callback functions which has been resolved in Promises.

6. What is the difference between `==` and `===` in JavaScript?
    **==** is loose comparison operator vs **===** is strong comparison operator,
    checks only values and not data type vs checks type as well.
    Performs coersion to compare vs no coersion.
    no recommended to use as much vs recommended as it's faster and safe as doesn't perform coersion.
    e.g.
        console.log(5 == "5");  // true (type coercion occurs)
        console.log(5 === "5"); // false (different types)

7. What is hoisting in JavaScript?
    `While compilation all variable, function declarions float to top of the scope(const and let are in TDZ till actual declaration), this phenomeon is called hoisting`, This means they can be referenced before they are declared in the code.
    e.g.
    1.  console.log(a); // undefined
        var a = 10;
    2.  console.log(hello()); // "Hello, world!"
        function hello() {
          return "Hello, world!";
        }

8. What is the difference between synchronous and asynchronous execution?
    **Synchronous** - Code executes line by line and next line waits till current line is executed.
    **Asynchronous** - if current line takes time to execute then it moves out of call stack to Event loop or background and next line is taken for execution in call stack allowing main thread not to be blocked.

9. Explain how `this` works in JavaScript, and it's difference in terms of an arrow and normal function in terms of object.
    `this refers to calling context/scope(class, function)`.
    normal functions have their own scope, whereas Arrow functions inherit lexographical scope.
    - normal functions rely on the caller for **this**.
    -  arrow functions are tied to the scope they were defined in.

    e.g.
    const object = {
      who: 'World',
      greet() {
        return `Hello, ${this.who}!`;
      },
      farewell: () => {
        return `Goodbye, ${this.who}!`;
      }
    };

console.log(object.greet()); // What is logged?
console.log(object.farewell()); // What is logged?

10. What are JavaScript modules, and how do you import/export them?
    `JavaScript modules are a way to organize and reuse code in smaller, independent files.     They enable developers to break their application into separate files, each with a  specific functionality, and share or import functionality across those files. This leads     to better maintainability and cleaner code architecture.`

11. What are arrow functions, and how are they different from regular functions?
    `An arrow function in JavaScript is a concise way to write functions using the => syntax. Arrow functions have a shorter syntax compared to traditional functions and behave differently in terms of how they handle the this keyword.`
    Diff - 
    1. Named vs Anonymous.
    2. Return manatory vs not mandatory.
    3. have their own scope vs inherit lexographical scope.


12. Explain the concept of prototype in JavaScript.
    `In JavaScript, prototypes are a fundamental concept that allows objects to inherit properties and methods from other objects. Every JavaScript object has an internal property called [[Prototype]] (often referred to as __proto__ in older code), which points to another object. This forms a chain known as the prototype chain, enabling inheritance.`
    1. Prototype Chain.
    2. Prototype and Constructor.
    e.g.
    function Animal(name) {
      this.name = name;
    }

    Animal.prototype.sayHello = function() {
      console.log(`${this.name} says hello!`);
    };

    const dog = new Animal('Buddy');
    dog.sayHello();  ` Output: Buddy says hello!`

13. What is event delegation in JavaScript?
    `Event delegation is a technique in JavaScript where a single event listener is attached to a parent element rather than individual child elements. The event listener takes advantage of event bubbling to catch events from child elements, allowing the parent to handle events for multiple children dynamically.`
    - This is to ensure that elements dying off page or coming to life later handle the event.
    e.g.
    list.addEventListener('click', function(event) {
      // Check if the clicked element is a list item (li)
      if (event.target.tagName === 'LI') {
        console.log(`You clicked on ${event.target.textContent}`);
      }
    })

14. What is the difference between `null` and `undefined`?
    `Null` is intentional absence of value whereas `undefined` is non initialised variable/referance.
    Null is explicitly assigned value.
    Undefined is variable declared but not initialised or function that doesn't return any value.
    - typeof null returns "object".
    - typeof undefined returns "undefined".

16. What is the `bind()` method in JavaScript?
    `returns a new instance of function that has "this" variable pointed to the  object passed in .bind(objName)`;
    - **this** variable remains intact for original function.
    - syntax - function.bind(thisArg, arg1, arg2, ...);

    function printSomething() {
        console.log(`this is ${this.name}`);
    }
    let obj = { name: "John" }
    let boundInstance = printSomething.bind(obj);
    boundInstance();

17. Explain how the `apply()` and `call()` methods differ in JavaScript.
    - call resembles .bind in sence that it dosen't return new function rather executes function with passed context directly.
    - apply acceps fucntion parameter in form of array after first object to bind.
    - call - Person.sayName.call(objToContext, arg1, arg2)
    - apply - Person.sayName.call(objToContext, [arg1, arg2]).

18. What are the different data types in JavaScript?
    JavaScript has the following data types:

    1. **Primitive Types**:
       - **Number**: Used for all numeric values (both integers and floating-point numbers).
       - **String**: Represents a sequence of characters (text).
       - **Boolean**: Represents `true` or `false` values.
       - **Undefined**: A variable that has been declared but not assigned a value has the value `undefined`.
       - **Null**: Represents the intentional absence of a value or object.
       - **Symbol**: A unique and immutable data type often used as keys in objects.
       - **BigInt**: Represents large integers beyond the limit of the `Number` type.

    2. **Objects**:
       - **Object**: The base data type for key-value pairs and used to store more complex data structures.
       - **Array**: A special type of object used for ordered collections of values.
       - **Function**: Functions are also considered objects in JavaScript and can be assigned to variables.

19. How does garbage collection work in JavaScript?
    `Garbage collection (GC) in JavaScript is the automatic process of reclaiming memory that is no longer in use, helping to prevent memory leaks.`
    1. Reachability Analysis.
    2. Mark-and-Sweep Algorithm.
    3. Generational Garbage Collection.

20. What is the `setTimeout()` function in JavaScript?
    `inbuilt function that takes callback and number/time in milliseconds as parameters and executes the callback function after number time is comepleted.`
    - it returns an id, which can be used to cancel the timeout later.

## TypeScript (15 Questions)

1. What are the advantages of using TypeScript over JavaScript?
    - IntelliSense and Enhanced IDE Support.
    - Compile-time Error Handling.
    - Enums and Interfaces for More Modular Code.
    - Type Safety.
    - Tooling and Ecosystem.

2. What is the difference between `interface` and `type` in TypeScript?
    **Interfaces**
    - Can be extended using the extends keyword.
    - can be merged(`When you declare an interface with the same name multiple times, TypeScript automatically merges them together`).
    **type**
    - Cannot be merged.
    - can extend other types using the & operator (intersection types).

    e.g.
    type Person = {
      name: string;
    };

    type Employee = Person & {
      jobTitle: string;
    };

3. Explain the concept of "Generics" in TypeScript.
    `Generics in TypeScript are a way to create reusable components (functions, classes, or interfaces) that can work with a variety of types rather than being restricted to a single one. By using generics, you can define a placeholder for the type that will be used, making your code more flexible and type-safe.`
    Why use generics.
    - Code Reusability.
    - Type Safety.
    - Improved Readability.
    e.g.
    function getFirstElement<T>(arr: T[]): T {
        return arr[0];
    }

    let numberArray = [1, 2, 3];
    let firstNumber = getFirstElement(numberArray);  // T is inferred as number

    let stringArray = ['apple', 'banana', 'cherry'];
    let firstString = getFirstElement(stringArray);  // T is inferred as string
    

4. What are "enums" in TypeScript?
    `Enums in TypeScript are a special type that allows you to define a set of named constants. These constants can be strings, numbers, or other values. Enums provide a way to handle a collection of related values with clear names, making code more readable and maintainabl.`
    - this helps with uniformity and needs minimal changes to update an option value everywhere in application.
    e.g.
    enum CountryCode {
        US = 'US',
        CA = 'CA',
        MX = 'MX'
    }

5. How does TypeScript handle type checking and inference?
    `TypeScript handles type checking and inference through a combination of explicit type annotations and automatic type inference. This system ensures that your code is type-safe while allowing for flexibility and reducing the need for explicit type annotations in many cases.`
    1. Type Checking.
    2. Type Inference.
    3. Explicit Type Annotations.
    4. Type Inference in Functions.
    5. Contextual Typing.
    6. Type Assertions.
    7. Union and Intersection Types.

6. What are "tuples" in TypeScript, and how are they used?
    `A tuple is a special type of array in TypeScript that allows you to store a fixed number of elements of different types. Unlike regular arrays, where all elements are typically of the same type, tuples allow for a more flexible structure with mixed types. Tuples maintain their specific type order, which means each element in the tuple can be of a different type, and TypeScript keeps track of the types and their positions.`
    - Fixed Length.
    - Element Types.
    - Preserved Order.
    e.g. 
    let person: [string, number, boolean] = ['Alice', 30, true];

7. How do you define optional parameters in TypeScript functions?
    `In TypeScript, you can define optional parameters in functions by appending a ? to the parameter name. This tells TypeScript that the parameter is not required when calling the function. If the parameter is not provided, it will be undefined by default.`
    - Optional parameters must be placed after required parameters.
    - Can also combine optional parameters with default values.
    - Optional Parameters with Rest Parameters.

8. What is the `any` type in TypeScript, and when should it be used?
    `Type that allows any type, compiler ignores the errors in its case and errors will be caught at runtime.`
    - TypeScript essentially disables type checking for that variable.
    When to use?
    1. When Migrating to TypeScript.
    2. Working with Dynamic Data.
    3. Handling Unknown or Uncertain Types.
    4. Dynamic Object Structures.

9. What are `never` and `unknown` types in TypeScript?
    **never**
    `The never type represents values that never occur. It is used in situations where a function or expression cannot possibly return a value or complete its execution. Essentially, never is used to represent unreachable code or functions that never return (e.g., functions that always throw errors or enter infinite loops).`
    - Common use cases for never
    - Functions that throw errors: A function that always throws an error will never return a value.
    - Functions with infinite loops.
    - Exhaustive checking in switch statements.
    **unknown**
    `The unknown type is similar to any in that it can hold any value. However, the key difference between unknown and any is that you cannot perform operations on an unknown value directly without first checking its type. This makes unknown a safer alternative to any because it forces you to perform type checks before interacting with the value.`
    - More restrictive than any.
    - Unknown API responses.

10. What is the purpose of `readonly` in TypeScript?
    `In TypeScript, the readonly modifier is used to define properties or variables that cannot be modified after initialization. It enforces **immutability** by making sure that once a value is assigned to a readonly variable or property, it cannot be changed throughout the lifecycle of that variable or object.`
    e.g.
    interface Person {
        readonly name: string;
        readonly age: number;
    }

    const person: Person = { name: 'Alice', age: 25 };

    // person.name = 'Bob';  // Error: Cannot assign to 'name' because it is a read-only property.
    **Common Use Cases:**
        1. Prevent modification of object properties.
        2. Prevent modification of arrays and tuples.
        3. Enforce immutability in class properties.

    **Key Benefits:**
        1. Ensures data integrity and prevents unintended changes.
        2. Helps achieve immutability in data structures.
        3. Enhances type safety by preventing mutations.

11. What is type assertion in TypeScript?
    `Type assertion is a way to tell TypeScript the type of a value when TypeScript is unable to infer it correctly, but you, as the developer, are confident about the type. It allows you to override the inferred type of a value.`
    - Angle Bracket (<type>) Syntax (This syntax is typically used in TypeScript files with .ts extension).
    let value: any = "Hello, World!";
    let length: number = (<string>value).length;
    - as Syntax (This is the recommended syntax, especially in JSX/React code, where angle brackets can interfere with JSX syntax)
    let value: any = "Hello, World!";
    let length: number = (value as string).length;

12. How do you define a class in TypeScript?
    - Class Declaration.
    - Properties.
    - Constructor.
    - Method.
    -- Creating an Instance of a Class.
    -- Adding Access Modifiers.
    -- Class Inheritance.
    -- Static Members.
    -- Readonly Properties.

13. What is the purpose of the `as` keyword in TypeScript?
    `In TypeScript, the as keyword is primarily used for type assertion, which is a way to tell the TypeScript compiler the specific type of a variable, especially when TypeScript's type inference doesn't have enough information to determine it.`
    - Type Assertion.
    - Type Narrowing.

14. How do you handle modules in TypeScript?
    `In TypeScript, modules are a way to organize and structure your code by splitting it into separate files. Modules help in encapsulating functionality and keeping your codebase clean and manageable.`
    1. Exporting and Importing in TypeScript.
    - Named Exports.
    - Default Export.
    - Importing Named Exports.
    - Importing Default Export.
    - Importing Everything as an Object
    2. Module Resolution in TypeScript.
    - Relative Import.
    - Non-relative Import. (from node_modules.)
    3. Handling Third-party Modules.
    - Install the library.
    - Import the library.
    - Install Type Definitions.
    4. Using tsconfig.json for Module Configuration.


15. What are "decorators" in TypeScript?
    `decorators are a special kind of declaration that can be attached to classes, methods, properties, or parameters. They are used to modify or enhance the behavior of the element they are applied to.`
    - Class Decorators.
    - Method Decorators.
    - Property Decorators.
    - Parameter Decorators.

## Node.js (20 Questions)

1. What is Node.js, and how is it different from traditional server-side technologies?
    `Node.js is a runtime environment that allows you to run JavaScript code outside of a web browser, typically on the server side. It is built on Google Chrome's V8 JavaScript engine and enables developers to build scalable and high-performance applications using JavaScript on both the client-side and server-side.`
    Features.
    - Event-driven, Non-blocking I/O.
    - Single threaded.
    - Built on chrome v8 engine.
    - JavaScript.
    - npm (Node Package Manager).
    - Cross-platform.
    How Node.js Differs from Traditional Server-side Technologies.
    - Concurrency Model.
    - Blocking vs Non-blocking I/O.
    - Single vs Multi-threaded.
    - Scalability.
    - Real-time Applications.


2. What is the event-driven architecture in Node.js?
    `Event-driven architecture (EDA) in Node.js is a design pattern where the flow of the program is determined by events or    messages. In this architecture, an application reacts to different types of events (like user input, system updates, or external service responses) rather than following a strict sequence of commands.`

    Key Concepts of Event-Driven Architecture in Node.js:
    **Event Loop:**
    **Event Emitter:**
    **Callbacks**
    **Non-Blocking I/O:**
    **Asynchronous Programming:**

    Advantages of Event-Driven Architecture in Node.js:
    **Scalability**
    **Performance**
    **Real-time Applications**

3. What is the role of the `package.json` file in a Node.js project?
    - The **package.json** file holds important metadata and configuration for a Node.js project when using `npm` as the package manager. It includes project details such as the name, version, scripts, dependencies, and devDependencies. When you run npm install, npm reads the dependencies from package.json and installs the required packages.
    - this file is accompanied by **package-lock.json**, which locks the exact versions of every package and its dependencies. This ensures consistency across environments, meaning the exact same versions of dependencies are installed each time, which helps prevent potential issues caused by version mismatches.

4. Explain the concept of callbacks in Node.js.
    `Callbacks are functions that allow asynchronous execution in JavaScript. This is achieved through JavaScript's "higher-order function" feature, where a function is passed as an argument to another function. The callee function then calls the callback function when the task is completed, effectively simulating asynchronous behavior.`
    - this is used in case code is supposed to be executed in order, especially when dealing with I/O operations like reading files.


5. What is the `require()` function in Node.js?
    `The require() function in Node.js is a built-in function used to import modules into a Node.js application. It is essential for modularizing your code and including various libraries, packages, or built-in Node.js modules.`
    Key Points about require() in Node.js :-
    1. Importing Modules.
    2. Importing Custom Modules.
    3. Caching.
    4. Module Resolution.
    5. JSON Files. -const data = require('./data.json');

6. How does Node.js handle asynchronous operations?
    `NodeJS handles asynchronous operations though Event driven architecture, this includes Event loop, Event Emitters, callbacks, etc.`
    **Event Loop**: The event loop is at the core of Node.js's ability to handle asynchronous operations. It allows Node.js to process multiple requests concurrently on a single thread by constantly checking the event queue and executing callbacks when the associated tasks are completed.

    **Event Emitters**: Node.js uses the EventEmitter class to allow objects to emit events and have listeners react to them. This is useful for managing asynchronous events like HTTP requests, file reading, or user input.

    **Callbacks**: In asynchronous operations, Node.js often uses callbacks. When an asynchronous task (like reading a file or querying a database) completes, a callback function is called to process the result. This prevents blocking the main thread while waiting for I/O tasks to finish.
    **Worker Threads:**
    For CPU-bound tasks that could block the event loop, Node.js introduced Worker Threads(available in `Node.js 10.x` and later). These allow parallel processing of heavy computational tasks while keeping the event loop free, ensuring responsiveness in the application.

7. What are streams in Node.js, and how are they useful?
    `Stream is powerfull concept in nodejs used to handle data that is transferred in chunks rather than single whole block, Streams allow data to be read or written in a continuous, efficient, and non-blocking manner. They provide an efficient way to process large amounts of data that may not fit into memory all at once, such as reading from files, receiving data over the network, or interacting with databases.`
    Types of Streams in Node.js.
    1. Readable Streams.
    2. Writable Streams.
    3. Duplex Streams.
    4. Transform Streams.

8. What are the different types of streams in Node.js?
    Types of Streams in Node.js.
    1. Readable Streams.
    2. Writable Streams.
    3. Duplex Streams.
    4. Transform Streams.
9. Explain the concept of middleware in Express.js.
    `middleware is a function that has access to req, res, and next object, it can modify req, res object and can decide when and if to pass the control to next handler.`
    - middleware get's executed based on where they are put in code(before which route handlers it is put).
    - middleware can be put on specific route handler to make it specific to that handler only.
    - error handling middlewares get called if any unhandler error is thown and there is an error handling middleware attched after the route where error was thown, this middleware has access to err, req, res, next object.

10. What is the `process` object in Node.js, and how do you use it?
    `The process object in Node.js is a global object that provides information and control over the current Node.js process. It is a part of Node.js's built-in APIs and is accessible from anywhere in the application without requiring the use of require()`
    1. process.argv
    2. process.env
    3. process.exit([code])
    4. process.stdout
    5. process.stdin
    6. process.pid
    
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
21. How do you upload large sized file from Angular to NodeJS to MongoDB, give me design for this.

## Angular (20 Questions)

1. What is Angular, and how does it differ from other JavaScript frameworks like React or Vue?
    `Angular is a platform and framework for building single-page applications (SPAs) using TypeScript and JavaScript. Developed and maintained by Google, Angular is a full-featured framework for building web applications.`
    - Component-based architecture.
    - Two-way data binding.
    - Dependency Injection.
    - Directives.
    - Routing.
    - RxJS.
    - Angular is often considered a **complete solution** for building complex, large-scale web applications, offering a lot of built-in functionality and structure.
    **How Angular Differs from Other JavaScript Frameworks Like React and Vue**
    Angular - Full Framework, Two-way binding, Opinionated, MVC/MVVM, Good with optimizations, Large, enterprise-focused
    React -	Library for UI, One-way binding, Unopinionated, Component-based, Very good (Virtual DOM), Largest, very active
    Vue - Progressive Framework, Two-way binding, Flexible, Component-based, Very good (Virtual DOM), Growing, developer-friendly

2. What are components in Angular?
    `In Angular, components are the fundamental building blocks of an application. A component is a self-contained unit that controls a part of the UI (User Interface).`
    - Template.
    - Class.
    - Styles.
    metadata.
    - Selector.
    - Template.
    - Class.
    - Styles.
    **Why Are Components Important in Angular?**
    - Modularity.
    - Separation of Concerns.
    - Reusability.
    - Testability.
    - Maintainability.

3. How does two-way data binding work in Angular?
    `Two-way data binding in Angular enables synchronization between the model (component class) and the view (UI). This means that any changes made in the input field on the UI are automatically reflected in the component's data, and any changes made to the data in the component are instantly updated in the input field on the UI.`
    - done usign ngModel directive.
    - view to model to view.
    e.g. <input [(ngModel)]="username" />.

4. What is dependency injection in Angular?
    `Dependency Injection (DI) in Angular is a design pattern used to implement inversion of control (IoC). It allows Angular to manage the creation and injection of dependencies (such as services) into components, directives, or other services`
    How it works.
    - Service Creation and Provision.
    - Constructor Injection.
    Benefits.
    - Loose Coupling.
    - Reusability.
    - Easier Testing.
    - Singleton Pattern.

5. What are Angular services, and how do you create one?
    `Angular services are typescript classes decorated with @injectable decorator, they contain buisness logic and shared functionality needed for components.`
    - to create use -> ng generate service
    - 

6. What is the purpose of the `ngOnInit` lifecycle hook in Angular?
    `Hook that gets called called after Angular has initialized all data-bound properties of a component or directive.`
    Used to.
    - Initialization of Component Data.
    - Access to Input Properties.
    - Avoiding Logic in Constructors.

7. What is the purpose of the `ngFor` directive in Angular?
    `A structural directive, it changes structure of dom by repeating elements for each element in an array`.
    - Used to create dynamic repeated elements on UI side based on Array like data.
    - Dynamic List of elements in html is ideal situation to use ngFor.
    e.g.
    
    <ul>
      <li *ngFor="let user of users; trackBy: trackByUserId">{{ user.name }}</li>
    </ul>

    trackByUserId(index: number, user: any): number {
      return user.id; // Use the unique 'id' of the user to track changes
    }

8. How does routing work in Angular?
    `Routing in Angular refers to the mechanism that allows navigation between different views or components within a single-page application (SPA). It enables you to control the flow of the application based on URL changes without reloading the entire page, allowing for a seamless user experience.`
    - routes are defined in an array, which decides which route renders which component.
    - The active route is rendered within a router-outlet directive in the template, which acts as a placeholder for the matched component.
    - routes are registered in a module as RouterModule.forRoot(routes)
    - Can manually route in component using route.navigate(), where route is instance of Router.
    - If you're dealing with lazy-loaded modules, you would use RouterModule.forChild(routes).

9. What are pipes in Angular, and how do you create one?
    `Pipes are used to transform data on template before it is rendered, they are similar to filter in angularJS. typically used to format data, e.g. dates, numbers or texts.`
    Built-in pipes -
    1. DatePipe
    2. CurrencyPipe
    - To create use -> ng generate pipe <pipe-name> -> then Implement the Pipe in transform method in ts file.
    - register pipe in declarations.

10. What are directives in Angular, and how are they different from components?
    `Directives are classes in Angular decorated with @Directive() that are used to manipulate the DOM. They can either change the appearance, behavior, or structure of DOM elements. Directives don’t have their own templates but instead work by modifying existing DOM elements, such as adding event listeners or changing CSS styles.`
    How are they different from component.
    - Component vs Directive.
    - By definition components are special type of directives which have their view vs where directives don't have their own view but they update behavior of existing DOM element.
    - @Component vs @Directive
    - have template metadata vs doens't have template metadata.

11. What is RxJS, and how is it used in Angular?
    `RxJS is a library for reactive programming using observables, It allows you to compose asynchronous and event-based programs with operators such as map, filter, merge, and more. RxJS makes it easier to work with data streams, such as user inputs, HTTP requests, or WebSocket messages, by treating them as streams that can be transformed, combined, and manipulated over time.`
    - Observable - An Observable is like a stream of values that can be observed (subscribed to).
    - Observer - An object that subscribes to an Observable.
    - Operators - Functions that allow you to transform, combine, or filter values from an Observable(map, filter).
    - Subscription - The act of observing an Observable.
    How RxJS is used in angular?
    - HTTP Requests.
    - Reactive Forms.
    - Event Handling.
    - Pipes and Async Pipe.
    e.g.
    - debaunceTime comes from rxjs that is used to implement debauncing.

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
