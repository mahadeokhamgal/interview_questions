# Angular

- **MergeMap(Parallel Execution) vs Fork Join.**
    - MergeMap doesn't wait for all observables to complete/emit a value 
    - vs
    - Formjoin waits for all observables to emit atleast one value.
    - MergeMap is good in case response is needed for every subject if any comes in irrespective of any other      observable.
    - vs
    - Forkjoin is good in case processing should happen after all observables resolve.
    - Both MergeMap and forkJoin execute all observables parallely/simultanuesly.

-**ConcatMap(Serial Execution), SwitchMap(debauncing), exhaustMap(throttling)**
    - `ConcatMap` - Each observable is executed serially, ideal when order of execution is dependant on previous observable.
    - SwitchMap(debauncing), exhaustMap(throttling) - work on `Higher order observables`.
    - `SwitchMap` - Cancels previos observable in stream if new one comes in while previos one was in progress.
    - `exhaustMap` - Ignores all coming observables in stream if current one is in progress.

- **What is Debouncing and Throttling?**
    - Techniques used to handle and keep page more responsive in case of rapid input which could have hampered application performance.
    - Debauncing cancels previous event and starts timer for new one if next input/event was fired within timer.
    - vs
    - Throttling ignores subsequent events till timer for an active event is completed.
    - Debauncing is ideal when latest event is important.
    - Throttling is ideal when first event is important.

- **Difference between AngularJS and Angular.**
    - Change detection systems Digest cycle vs Change detection.
    - MVC archetecture vs Conponent based archetecture.
    - JS based, TS based.
    - All errors caught at runtime vs due to strong typing compile time errors are caught early.
    - Don't support Standalone components vs Does support.
    - Not able to use ENUMS and Interfaces vs able to use.
    - AngularJs supports Jest test framework vs Angular used to provide Jasmine framework.
- 
- **Angular 16 Features:**
  - Standalone
  - Signal

- **What is JWT?**
    - Stands for json-web-token, used to provide security via token based session.
    - This secures application by refershing tokens every few minutes.
    - Created at login time and refreshed on timeouts.
    - Validated for each resource request on server side.

- **Is it needed to use jwt on socket**
    - Not for each data transfer, but advisable to use and validate on initial connection.

- **Where should Client store JWT?**
    - Possible to store on Localstorage/sessionstorage, Cookies.
    - Advisable to store in application cookies with HttpOnly flag=true, secure=true flag for https only and sameorigin if possible to keep client and server on same host.

- **What all information a JWT token has?**
    - Object used to create JWT toke.
    - Expries in time, Http flag, Secure flag.
    - No passwords should be store in it.

- **What is Profiling in Angular**
    - Technique/Process of measuring the performance of an Angular application to identify performance bottlenecks, optimize components, and improve the overall user experience.
    - how long certain operations take.
    - which areas of the app consume the most resources.
    - Angular DevTools extension.
    - Chrome DevTools Performance Tab.
    **Key Aspects of Profiling in Angular**
        - Change Detection Profiling.
        - Component Performance.
        - Memory Usage.
        - Event Handling and DOM Updates.
        - 

- **How to make routes/components protected in Angular?**
    - Using Accessbased check on routes using canActivate, canDeactivate etc.
    - This is just User guide and not actual resouce safety as actual security is supposed to be implemented at server end.
    - Each route that needs to be protected need to add canActivate in route in routes array.
    - Not all routes need to be protected.

- **Alternative methods to JWT.**
    - OAuth
    - Basic Auth.

- **Ways to pass data between unrelated components in Angular.**
    
- **Ways to pass data between related components.**
- **What is change detection in Angular and how it works?**
- **Change detection strategies**
- **What is Lazy loading?**
- **What is Content projection?**
- **List change detection strategies.**
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
- **What are types of lazy loading in angular**

---

# HTML

1. **Semantic elements** and features provided by semantics.
2. **How to make a password show and hide?**
3. **How to make my div resize and adjust to dynamic elements coming in?**
4. **How to create responsive web pages?**
5. **What does Less/Sass provide over CSS?**
6. **What is `em` and `rem`?**
7. **What are all relative units in CSS?**
8. **What is Mixins.**

---

# NodeJS

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
- **How to connect express app to MongoDB**

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
