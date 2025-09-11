1. Angular Fundamentals & Basics
# What is Angular, and how does it differ from React or Vue?
# Difference between AngularJS and Angular.
# Angular 16 Features (Standalone, Signals).
# What are components in Angular?
# What are directives in Angular, and how are they different from components?
# What is a template in Angular? How is it different from a view?
# What is a module in Angular? Why is it important?
# Explain the purpose of NgModule.
# What is Angular CLI, and how do you use it?
# What are Angular lifecycle hooks? Name some commonly used hooks.
# What is the purpose of the ngOnInit lifecycle hook?
# What is bootstrapping in Angular?
# Why is Angular an SPA?
# How Angular application starts?
# How is Angular better than other frameworks?
# Challenges migrating AngularJS to Angular.
# What is a standalone component?
`TypeScript`
# Advantages over JavaScript
# Interface vs type
# Generics
# Enums
# Type checking and inference
# Tuples
# Optional parameters
# any, unknown, never types
# readonly keyword
# Type assertion
# Classes and decorators
# as keyword
# Modules

2. Component Communication & View Handling
# Ways to pass data between related components.
# Ways to pass data between unrelated components.
# What is the difference between @ViewChild and @ContentChild?
# What is purpose of @ViewChild?
# What is purpose of ngOnChanges?
# What is EventEmitter in Angular, and how is it used?
# What is content projection in Angular?
# What is difference between ng-content vs ng-container?
# How does two-way data binding work in Angular?
# What is the role of ngModel in Angular?
# What is view encapsulation in Angular?
# What is ::ng-deep in Angular?
# How styles react if components have different encapsulation (Emulated, ShadowDom, None)?

3. Routing & Navigation
# Routing in Angular?
# How does Angular routing work?
# What is RouterModule? How do you configure it?
# When to use forChild in Angular?
# What are Angular guards, and how are they used in routing?
# What is an auth guard?
# What is the purpose of canActivate and canDeactivate guards?
# What is Lazy loading in Angular?
# What are types of lazy loading in Angular?
# How does lazy loading work in Angular?
# How is Lazy loading better? When will you recommend it?
# What are micro-frontends in Angular?
# What is SSR (Server-Side Rendering) in Angular?
# What is Angular Universal?

4. Services & Dependency Injection
# What are Angular services, and how do you create one?
# What is Dependency Injection in Angular?
# Explain the difference between providedIn: 'root' and registering a service in a specific module.
# How do you create and use a singleton service in Angular?
# inject vs @Inject vs TestBed.inject vs constructor injection.
# What is the Inject keyword?
# When should one use MockServices and when to use Actual services?
# async/await in Angular services/components

5. Change Detection & Zone.js
# What is change detection in Angular and how it works?
# What is change detection in Angular?
# Change detection strategies.
# List change detection strategies.
# What is OnPush change detection strategy? When would you use it?
# What is role of Zone.js in Angular?
# What is Profiling in Angular?
# Angular change detection and async operations
# Event loop impact on Angular execution
# Zone.js and NgZone usage

6. Forms
# How do you handle forms in Angular?
# What is the difference between template-driven and reactive forms in Angular?
# How do you validate a form in Angular?
# How can you create a custom validator in Angular?
# How do you use the FormBuilder class?
# What is ngModel, and how does it work in Angular forms?
# How to implement multi-step Angular form?
# Coding Challenge → Write a reactive form with 3 input fields (name, dob, phone).

7. Pipes
# What are Angular pipes, and how do you create one?
# Name some commonly used Angular pipes and their purpose.
# What is the difference between pure and impure pipe?
# What is keyvalue pipe and its optional arguments?
# Can you use multiple pipes in the same expression? Provide an example.
# Coding Challenge → Create a custom pipe.
# async pipe in templates

8. RxJS & Observables
# What is RxJS, and how is it used in Angular?
# What is an observable, and how do you subscribe to it in Angular?
# Difference between Promise and Observable.
# What is the difference between Observable and Subject?
# What are the different types of Subjects in RxJS?
# What is the difference between BehaviorSubject and ReplaySubject?
# What is the difference between cold and hot Observables?
# What is MergeMap vs ForkJoin?
# Difference between MergeMap and SwitchMap.
# Difference between concatMap, switchMap, and exhaustMap.
# What is Debouncing and Throttling?
# How does the debounceTime operator work? When is it useful?
# How does the takeUntil operator work? Provide an example.
# How do you cancel an Observable subscription in Angular?
# How can you combine multiple Observables (combineLatest, forkJoin)?
# What are multicasting operators in RxJS? How do you use share or multicast?\
# Explain the purpose of map, tap, shareReplay.
# How to create simultaneous/parallel API calls?
# Explain how to handle multiple HTTP requests using concat, merge, or zip.
# Debouncing user input (Observables vs Promises)
# Combining asynchronous data with real-time updates
# rxjs/ajax usage
# Key differences: JS Promises vs RxJS Observables
# then()/catch() vs subscribe() in Observables

9. HTTP & Interceptors
# How do you make HTTP calls in Angular?
# Handling race conditions in HTTP calls
# What is the role of the HttpClientModule in Angular?
# How can you handle errors in HTTP calls in Angular?
# What are the benefits of using interceptors in Angular?
# What is the return type of interceptor in Angular?
# What is JWT?
# Where should client store JWT?
# What all information does a JWT token have?
# Alternative methods to JWT?
# Is it needed to use JWT on socket?
# What is SSO (Single Sign-On)?

10. Performance Optimization
# How to reduce Angular Build Size?
# How to optimise grid-like data in Angular?
# How do you handle large datasets in Angular efficiently?
# How can you optimize the performance of an Angular application?
# How is Lazy loading better for performance?
# Explain the purpose and usage of the Angular CLI.

11. Testing
# How to perform integration testing in Angular?
# beforeEach vs beforeAll in Angular.
# What is tick in Angular?
# What is fakeAsync in Angular?
# Unit testing vs Integration testing.

12. Advanced Angular Topics
# Microtasks vs macrotasks in Angular
# What are custom elements in Angular?
# How are custom elements different in standalone and non-standalone components?
# Are JS components possible in Angular?
# What is a decorator?
# What is Renderer2 in Angular?
# What is a Service Worker in Angular?
# What is a singleton component?
# What is PWA (Progressive Web App)?
# Is multithreading possible in Angular?
# When to use UpgradeModule and DowngradeModule in Angular?
# Bootstrap vs Angular Material.
# What is compodoc in angular?
# How do you manage store/access sensitive data like database password etc in angular.

13. Coding Challenges
# Create Angular component with progress bar.
# Create Angular app with an Image and Reset button (on reset fetch from https://dog.ceo/api/breeds/image/random).
# Reactive form with 3 inputs (name, dob, phone).
# Custom pipe creation.
# Create Angular  component which will have a progress bar.`
  1. It will initiate from 0% on page load. 
  2. It will increment after 1 secs by 10%.
  3. The progress bar will keep on incrementing till the width of the page is met.
  4. Create reset button which will start the progress bar from 0 again.