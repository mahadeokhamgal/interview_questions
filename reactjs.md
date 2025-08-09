# What is ReactJS and why is it used?
 - ReactJS is a JavaScript library developed by Facebook for building user interfaces, especially for single-page applications.
 - It is widely used because of its key features such as the virtual DOM, JSX syntax, and built-in state management using hooks.
 - React simplifies the development of fast, dynamic, and scalable client-side applications and addresses limitations of older approaches like plain JavaScript or jQuery.
 - Today, it is commonly used in enterprise-level frontend development due to its flexibility, performance, and large ecosystem.

# What are components in React? What is the difference between functional and class components?
 - In ReactJS, components are the fundamental building blocks used to build the user interface. They let you split the UI into reusable independent pieces that can manage their own state and logic.
 - There are two main types of components:
 - Class Components: Introduced in earlier versions of React, these are ES6 classes that extend `React.Component`. They use lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` to manage side effects and state.
 - Functional Components: These are simpler functions that return JSX. In modern React, they are preferred because of hooks such as `useState`, `useEffect`, and others, which allow functional components to manage state and side effects without needing classes.
 - Functional components are now the standard due to their concise syntax, easier testing, and better support for modern features like React Server Components and Concurrent Mode.

# What is JSX and how is it different from HTML?
 - JSX stands for JavaScript XML. It is a syntax extension for JavaScript used in React that allows developers to write HTML-like code directly within JavaScript.
 - JSX makes it easier to visualize the UI structure and improves readability by combining markup and logic in one place. For example, instead of using React.createElement(), you can simply write: <h1>Hello, world!</h1>
`Difference Between JSX and HTML:`
Syntax Differences:
 - In JSX, some attribute names are different. For example, class becomes className, and for becomes htmlFor.
 - Self-closing tags (like <img />, <input />) are mandatory.
 - Embedded JavaScript:
 - JSX allows you to embed JavaScript expressions using curly braces {}, which is not possible in plain HTML.
 - Example: <p>{user.name}</p>
 - Not a Browser Standard:
 - JSX is not understood by browsers directly—it needs to be transpiled (usually by Babel) into regular JavaScript before it can run.

# What are props in React? How are they different from state?
 - props are data being passed to child component as parameter.
 - whenever there is change in data in parent then the same will be reflected in child component.
 - Props are different than states in below sence.
   \| Feature     | Props                                | State                                  |
   \|-------------|---------------------------------------|-----------------------------------------|
   \| Ownership   | Passed from parent to child           | Local to the component                  |
   \| Mutability  | **Read-only**                         | **Mutable (using setState or useState)** |
   \| Purpose     | Used for configuration/input          | Used for internal data and UI control   |
   \| Controlled by | Parent component                   | Component itself                        |

# What is the virtual DOM and how does React use it?
 - Virtual DOM is a virtual copy of the real DOM.
 - React uses it to detect minimal changes via a diffing algorithm.
 - Only those minimal updates are applied to the actual DOM.
 - This results in better performance and smoother UI updates.

⚙️ Intermediate Questions
# What are hooks in React? Name a few commonly used hooks.
 - In ReactJS, hooks are special functions that allow functional components to use features like state, side effects, and more—without converting them into class components.
 - Hooks cannot be used in class components.
 - They let you "hook into" React features like state, lifecycle methods, context, etc.
 | Hook         | Purpose                                                          |

 |--------------|------------------------------------------------------------------|
 | `useState()` | Adds local state to a function component                         |
 | `useEffect()`| Performs side effects (e.g., data fetching, subscriptions, etc.) |
 | `useContext()` | Accesses context data                                          |
 | `useRef()`   | Accesses or stores a mutable reference to a DOM element or variable |
 | `useMemo()`  | Memoizes expensive calculations                                  |
 | `useCallback()` | Memoizes functions to prevent unnecessary re-renders          |

# What is the useEffect hook and how does it differ from useState?
 - useeffect hook is used to tap into the property and listen to whenever there is change in proprty.
 - useeffect can accept one or more properties to listen to changes to.
 - usestate is used to create local state for component which can be updated using the setstate function returned by usestate.

# how do functional component acheive componentDidMount, componentDidUpdate, componentWillUnmount ?
 | Class Lifecycle Method | Equivalent in Functional Component              |
 | ---------------------- | ----------------------------------------------- |
 | `componentDidMount`    | `useEffect(() => { ... }, [])`                  |
 | `componentDidUpdate`   | `useEffect(() => { ... }, [dependencies])`      |
 | `componentWillUnmount` | `useEffect(() => { return () => { ... } }, [])` |

# How do you handle forms and user input in React?
1. Using Controlled Components (Most Common Way)
- Use `useState` to create and manage input values.
- Bind input fields to state.
- Update state with `onChange` handlers.
 ```jsx
    const [name, setName] = useState('');
    <input value={name} onChange={(e) => setName(e.target.value)} />
 ```
2. Handling Form Submission
 - Wrap fields in a <form> tag.
 - Use onSubmit to capture form submit events.
 - Call e.preventDefault() to stop default browser behavior.
3. Using useEffect for Side Effects
 - Useful for:
 - Debounced input
 - Auto-saving
 - Fetching data based on input
4. Third-Party Libraries (Recommended for Complex Forms)
 - Formik
 - Declarative
 - Supports validation
 - Good for large forms

 - React Hook Form
 - Very lightweight and performant
 - Minimal re-renders
 - Built-in validation
 
 - react-jsonschema-form (RJSF)
 - Automatically renders forms from JSON Schema
 - Ideal for config-driven or dynamic forms

# What is React Context API and when would you use it?
 - The React Context API is a built-in feature in React that allows you to share data globally across the component tree without prop drilling (i.e., passing props manually at every level).
 - You create a context, provide a value at the top level (with a Provider), and consume that value in any nested component (with useContext or Context.Consumer).
 - You'd use the Context API when multiple components need access to the same data, such as:
 a. Theme toggling (dark/light mode)
 b. User authentication info

# What is the difference between controlled and uncontrolled components in React?
- Controlled Components
 - React controls the input through component state.
 - The form element’s value is set using useState, and updates happen via onChange.
 - Recommended approach in React because it keeps the UI and logic in sync.
| Feature            | Controlled Component      | Uncontrolled Component    |
| ------------------ | ------------------------- | ------------------------- |
| State Management   | React state (`useState`)  | DOM handles its own state |
| Access Input Value | `value` prop + `onChange` | `ref.current.value`       |
| Validation         | Easier and declarative    | Manual                    |
| Use Case           | Complex/interactive forms | Simple or legacy forms    |

# how to conditionally hide/show an element in react.
1. Using a Boolean condition
 - {isVisible && <p>This element is visible!</p>}
2. Using a ternary operator
 - {isLoggedIn ? <p>Welcome back!</p> : <p>Please log in.</p>}
3. Assign to a variable
```jsx
let content;
if (isLoading) {
  content = <p>Loading...</p>;
} else {
  content = <p>Data loaded!</p>;
}

return <div>{content}</div>;
```
# what is event delegation and event bubbling.
 - Event delegation
  - this is a technique by which we can listen to the event from child elements and do the work instead of attaching listener to child element.
  - this is beneficial to handle scenarios where child elements are dynamic in nature.
  - no overhead of attaching and removing listener to each child element.
 - Event bubbling.
  - This is way how events are propogated from any element where event is triggered to the top of dom tree.
  - cause of bubling we get same event access in any parent of the current element.
  - can stop propogation using event.stopPropagation();
  - can control order in which event should be captured as element.addEventListener(event, handler, useCapture);

# what is higher order component in reactjs ?
 - these are components that take another component as an argument and will return a component.
 - used to apply reusable logic accross components.
 - use cases like themes, global onclick handlers.
 - these are less common in modern javascript as hooks do the work.

# Hoew does JWT work in reactjs?
 - user logs in, backend sends JWT token, mostly http only cookie.
 - this cookie is then sent in every outgoing API.

# React authguard
 - can use Route to add protected routes in parent route, parent component is responsible to either render child or redirect it to login.
 - Outlet and Navigate are used to wither render the routed component or navigate to some path.

# React API interceptors.
 - Interceptors are functions/hooks that intercept HTTP requests or responses before they are handled by then or catch.
 - Commonly used in React apps when making API calls with libraries like `Axios`.
 - They allow you to modify requests or responses globally without changing individual calls.
  - api.interceptors.request.use(requestMethod, errorMethod);
  - api.interceptors.response.use(successResponseMethod, errorMethod);
  ```js
  const api = axios.create({
    baseURL: 'https://api.example.com',
  });
  ```

# What is the difference between React and ReactDOM?
| Aspect            | React                                                             | ReactDOM                |

| **What it is**    | Core React library for building UI components                     | Library for interacting with the DOM (web page)                                |
| **Purpose**       | Provides the **React API**: components, hooks, state, props, etc. | Handles rendering React components into the **actual browser DOM**             |
| **Functionality** | Defines how to create and manage components and their lifecycle   | Provides methods like `ReactDOM.render()` to mount React components to the DOM |
| **Where used**    | Used in both web and native (React Native) apps                   | Only used in **web applications** to manipulate the HTML DOM                   |
| **Example**       | `import React from 'react';` to create components                 | `import ReactDOM from 'react-dom';` to render components on the webpage        |

# What are keys in React and why are they important?
 - resemble trackby in angular.
 - instead of redrawing complete elements of list it checks for key order if key order is same then only changes in specific keys will be reflected.
 - this helps acheive performace.
 - `Uniqueness`  -> Helps React distinguish list items
 - `Performance` -> Enables efficient DOM updates
 - `Accuracy`    -> Preserves state and element identity
```jsx
{items.map(item => (
  <div key={item.id}>{item.name}</div>
))}
```

# What is reconciliation in React?
- Reconciliation is the process React uses to compare the current virtual DOM tree with the previous one and figure out what exactly changed.
- React then efficiently updates only the parts of the real DOM that need to change, rather than re-rendering everything.
 `Why ?`
 - Makes React apps fast and efficient.
 - Avoids full DOM re-renders.
 - Preserves component state where possible.
 - Enables smooth UI updates, even in large applications.

# Explain the concept of lifting state up in React.
Lifting state up means moving a piece of state from a child component to its closest common parent, so that:
-  The parent can manage the state, and
- Pass it down to the children via props.

# What are React Fragments and why would you use them?
- React Fragments let you group multiple JSX elements **without adding extra nodes** to the DOM.
- This helps keep your DOM clean and avoids unnecessary `<div>` wrappers.
- Fragments are useful in layouts (like table rows) or anywhere you need to return multiple elements from a component.
- You can use `<React.Fragment>` or the shorthand `<>...</>`.

# How does React’s rendering process work? When does a component re-render?
`How does React render?`
 - Triggering change: When a component’s state or props change, React starts the rendering process.
 - Re-rendering virtual DOM: React re-renders the component, producing a new virtual DOM tree.
 - Diffing (Reconciliation): React compares the new virtual DOM with the previous one using a diffing algorithm.
 - Minimal DOM updates: React then applies only the necessary changes to the real DOM — this is efficient and fast.
`When ?`
 - State changes - Using useState() or this.setState()
 - Props change	- If parent passes new props
 - Context value changes - If the component consumes a React Context
 - Force update - Manually triggered (rare) with forceUpdate()
 - Parent re-renders - Even if the component’s own props/state haven’t changed (unless optimized with React.memo, PureComponent, etc.)

# What is the difference between useEffect and useLayoutEffect hooks?
| Feature           | `useEffect`                                                    | `useLayoutEffect`                                   |
| ----------------- | -------------------------------------------------------------- | --------------------------------------------------- |
| **Timing**        | Runs **after** the browser paints the screen                   | Runs **before** the browser paints the screen       |
| **Use Case**      | Non-blocking side effects (e.g., data fetching, subscriptions) | DOM reads/writes that must happen before paint      |
| **Performance**   | Doesn't block rendering → more efficient                       | **Blocks paint** until it finishes (can cause jank) |
| **Runs after...** | The component is rendered and painted                          | The component is rendered but **before** painting   |
| **Risk**          | Safe for most UI updates                                       | Can cause **layout shift or flickering** if misused |
- `useEffect` is asynchronous with respect to painting — it's great for most side effects.
- `useLayoutEffect` runs synchronously before painting — use it when you need to measure or mutate the DOM before it’s shown to the user.
- Prefer `useEffect` unless you have a visual/layout reason to block paint.

# What are Pure Components and how do they differ from regular components?
- Pure Components prevent unnecessary re-renders by using shallow comparison of props and state.
- In class components, use `React.PureComponent`.
- In function components, use `React.memo`.
- They're useful for performance optimization, especially in large or frequently-updating UIs.

# How to acheive ngfor in react?
```jsx
<div>
  {products.map(product => (
    <Product key={product.id} name={product.name} />
  ))}
</div>
```

# How can you optimize performance in React applications?
 1. Use Keys for Lists
- Provide a unique `key` prop when rendering lists.
- Helps React identify items that have changed, added, or removed.
- Avoid using array indexes as keys if the list is dynamic.
 2. Memoization with `useMemo` and `useCallback`
- **`useMemo`**: Memoizes the result of expensive computations to avoid recalculations on every render.
- **`useCallback`**: Memoizes functions to prevent unnecessary re-creations and child re-renders.

 3. Use `React.memo` for Functional Components
- Wrap components in `React.memo` to avoid re-renders when props have not changed.

 4. Code Splitting and Lazy Loading
- Use `React.lazy` and `Suspense` to load components only when needed, reducing initial load time.

 5. Avoid Anonymous Functions and Inline Objects in JSX
- Inline functions and objects cause props to change on every render, triggering unnecessary updates.

 6. Optimize Context Usage
- Avoid passing frequently changing values in React Context to prevent excessive re-renders.

 7. Avoid Unnecessary State Updates
- Batch multiple state updates together.
- Avoid updating state with the same value repeatedly.
- Keep state minimal and focused.

 8. Use Production Build of React
- Production builds are optimized for smaller bundle size and better runtime performance.

# How do you handle error boundaries in React?
- Error boundaries are React components that catch errors in their children and display fallback UI.
- Implemented as class components using `getDerivedStateFromError` and `componentDidCatch`.
- Prevent the entire app from crashing by isolating UI errors.

# How does react application boot?
1. React starts from `index.js` (or `main.jsx`), rendering `<App />`.
2. It injects the React app into `<div id="root">` inside `index.html`.
3. The virtual DOM is built from `<App />` and compared to previous versions.
4. React efficiently updates the real DOM based on changes.
5. State, hooks, and effects initialize and react to updates.
```jsx
// index.js
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

# How to create build and deploy on server in react?
- Use `npm start` for local development with hot-reload.
- Use `npm run build` to generate a production-ready static build, `react-script build`.
- The `build/` folder contains all files needed for deployment.
- You can host this folder on any static server (e.g., Nginx, GitHub Pages, Netlify, Firebase).

# How to create custom elements in reactjs?
 - inside component file you will register component as native-web element.
 - customElements.define('my-react-element', MyReactElement);

# What is redux?
 `Why Use Redux?`
 - To share state across multiple components
 - To make state predictable and traceable
 - To have a single source of truth (the store)
 - To better debug and log state changes
 - To simplify data flow in large applications
| Concept      | Description                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| **Store**    | Central location that holds the app's entire state                          |
| **Action**   | Plain JS object that describes what happened (e.g., `{ type: 'ADD_TODO' }`) |
| **Reducer**  | Pure function that takes current state and action → returns new state       |
| **Dispatch** | Sends an action to the reducer                                              |
| **Selector** | Function to read values from the store                                      |

# implememtations.
# ReactJS Interview-style Problem Statements

1. Create a React app to render a random dog image and change on every click. While the image is being loaded, show a loading icon.

2. Create a React app for a counter. On click of a button, it should start a countdown from a user input number of seconds and on completion it should show "completed." If the user clicks reset in between, the timer will restart. The user should be able to see the timer clock on the UI.

3. Create a custom hook in ReactJS that calls the function passed to it as a parameter on the third render of the component.

4. Create a React app that fetches and displays a list of dog breeds from a public API. When a breed is clicked, show a random image of that breed below the list.

5. Build a stopwatch React app with Start, Stop, and Reset buttons. The timer should update every second and display minutes and seconds.

6. Create a React component with an input field that accepts only numbers. On typing, it should format the input as currency (e.g., 1000 → 1,000).

7. Build a custom hook `usePrevious` that stores and returns the previous value of a prop or state variable.

8. Implement a React app with a todo list where users can add, remove, and toggle completion status of tasks. Persist todos in `localStorage`.

9. Create a modal dialog component in React that traps focus within itself when open and returns focus to the trigger button on close.

10. Build a React component that renders a list of items. When an item is clicked, highlight it and display its details below the list.

11. Create a React app that implements infinite scrolling to load more items from an API as the user scrolls near the bottom of the page.

12. Develop a React app with a theme switcher (light/dark mode) using Context API, so the theme applies to all nested components.

13. Implement a React component with a search input that filters a list of users fetched from an API, updating results as the user types with debouncing.


# 20 ReactJS Problem Statements to Boost Your Skills

1. **Create a custom hook that calls a given function only once after the component mounts (like `componentDidMount`).**

2. **Build a controlled form component with validation that disables the submit button until all fields are valid.**

3. **Create a custom hook that calls a passed function on the 3rd render of the component.**

4. **Implement a reusable modal component that renders children content and can be opened/closed via props or context.**

5. **Create a component that fetches data from a public API and displays a loading indicator until data arrives.**

6. **Build a to-do list app where the tasks persist in `localStorage` and are loaded on component mount.**

7. **Make a custom hook that debounces an input value — updates only after the user stops typing for 500ms.**

8. **Design a higher-order component (HOC) that logs props changes every time the wrapped component re-renders.**

9. **Use React Context to implement a theme toggler (dark/light mode) affecting multiple nested components.**

10. **Create a paginated list component that fetches and displays data page by page on button click.**

11. **Build a form with dynamic input fields where users can add/remove inputs and submit all values.**

12. **Implement error boundaries to catch errors in child components and display a fallback UI.**

13. **Create a hook that tracks the window size and updates on resize events.**

14. **Build a multi-step form wizard that saves progress and allows moving between steps.**

15. **Implement a custom hook to detect clicks outside a given element (useful for dropdowns or modals).**

16. **Build a search component that filters a list in real-time as the user types.**

17. **Create a reusable accordion component where multiple items can expand/collapse independently.**

18. **Implement route-based code splitting with React.lazy and Suspense for a multi-route app.**

19. **Create a notification system where notifications appear for 5 seconds then disappear automatically.**

20. **Build a drag-and-drop list component allowing reordering of items using mouse events.**










------------------------------------------------------------------------------------------------------------------------------------
# React.js One-Liner Questions – Readiness Check
### 1. What is React?
→ A JavaScript library for building user interfaces using components.

### 2. What is JSX?
→ A syntax extension that lets you write HTML-like code inside JavaScript.

### 3. What is a component in React?
→ A reusable, independent piece of UI that can be a function or class.

### 4. What’s the difference between functional and class components?
→ Functional components are plain functions; class components use `class` and lifecycle methods.

### 5. What are props in React?
→ Props are inputs passed to components to make them dynamic.

### 6. What is state in React?
→ A built-in object used to store data that determines a component’s behavior and rendering.

### 7. What hook is used to manage state in a functional component?
→ `useState`.

### 8. What hook is used for side effects in React?
→ `useEffect`.

### 9. What is the virtual DOM?
→ A lightweight in-memory representation of the real DOM used for efficient updates.

### 10. What is the key prop in React lists used for?
→ To uniquely identify elements and help React optimize rendering.

### 11. How do you conditionally render JSX in React?
→ Using ternary operators, logical `&&`, or `if` statements inside the component.

### 12. Can you update props inside a component?
→ No, props are read-only.

### 13. How to lift state up in React?
→ Move state to the nearest common parent and pass it down via props.

### 14. What is a controlled component in React?
→ An input element whose value is controlled by React state.

### 15. What is an uncontrolled component?
→ An input element that manages its own state internally via the DOM.

### 16. What does `useEffect(() => {}, [])` mean?
→ It runs once after the component mounts (like `componentDidMount`).

### 17. What is the purpose of React Router?
→ To enable client-side routing in a React app.

### 18. How to pass data from child to parent in React?
→ By calling a function passed from parent as a prop.

### 19. What is context in React used for?
→ To share data globally without passing props through every level.

### 20. What does lifting state up mean?
→ Sharing state between sibling components by moving it to their common ancestor.

### 21. What does `React.memo` do?
→ Prevents re-rendering of a component if its props haven’t changed.

### 22. What is the purpose of `useRef` hook?
→ To persist values across renders or access DOM elements directly.

### 23. What is a higher-order component (HOC)?
→ A function that takes a component and returns a new enhanced component.

### 24. What’s the difference between `useEffect` and `useLayoutEffect`?
→ `useLayoutEffect` runs synchronously after DOM changes, `useEffect` runs after paint.

### 25. What are fragments in React used for?
→ To group multiple elements without adding extra nodes to the DOM.

# More React.js One-Liner Questions (Advanced)

### 26. What is reconciliation in React?
→ The process by which React updates the DOM by comparing the new virtual DOM with the previous one.

### 27. What is a pure component in React?
→ A component that renders the same output for the same props and state, with shallow comparison.

### 28. How does `React.StrictMode` help in development?
→ It highlights potential issues like unsafe lifecycle methods and deprecated APIs in development mode.

### 29. What is prop drilling in React?
→ Passing data through many nested components that don’t need it, just to reach a deeply nested one.

### 30. How can you avoid prop drilling?
→ By using React Context or state management libraries like Redux or Zustand.

### 31. What is lazy loading in React?
→ A technique to load components only when needed, improving initial load time.

### 32. How do you implement code splitting in React?
→ Using `React.lazy()` and `Suspense` to load components on demand.

### 33. What is a custom hook in React?
→ A reusable function that uses built-in hooks to encapsulate logic shared across components.

### 34. How do you handle errors in React components?
→ Using Error Boundaries — components that catch JavaScript errors in their child components.

### 35. What’s the role of keys in React lists?
→ Keys help React identify which items changed, are added, or removed for efficient re-rendering.


---

# Java One-Liner Questions – Readiness Check
### 1. What is Java?
→ A high-level, platform-independent, object-oriented programming language.

### 2. What is the JVM?
→ Java Virtual Machine, which runs Java bytecode on any platform.

### 3. What is the JDK?
→ Java Development Kit, which includes tools to develop and run Java programs.

### 4. What is the difference between JDK and JRE?
→ JDK includes development tools; JRE provides runtime environment only.

### 5. What are the main features of Java?
→ Platform independence, OOP, automatic memory management, multithreading.

### 6. What is bytecode in Java?
→ Intermediate, platform-independent code generated by the Java compiler.

### 7. What is inheritance?
→ A mechanism where a new class acquires properties and behaviors of an existing class.

### 8. What is polymorphism?
→ The ability of an object to take many forms, especially method overriding.

### 9. What is encapsulation?
→ Wrapping data (variables) and code (methods) together and restricting access.

### 10. What is abstraction?
→ Hiding complex implementation details and showing only necessary features.

### 11. What are constructors in Java?
→ Special methods used to initialize new objects.

### 12. What is method overloading?
→ Defining multiple methods with the same name but different parameters.

### 13. What is method overriding?
→ Redefining a superclass method in a subclass with the same signature.

### 14. What is the difference between `==` and `.equals()`?
→ `==` compares references; `.equals()` compares object content.

### 15. What is an interface?
→ A contract that defines abstract methods a class must implement.

### 16. Can Java support multiple inheritance with classes?
→ No, Java supports multiple inheritance through interfaces.

### 17. What is a package in Java?
→ A namespace that organizes classes and interfaces.

### 18. What is the difference between `ArrayList` and `LinkedList`?
→ `ArrayList` uses dynamic arrays; `LinkedList` uses doubly linked lists.

### 19. What is the purpose of the `final` keyword?
→ To make variables constant, prevent method overriding, or inheritance.

### 20. What are checked and unchecked exceptions?
→ Checked exceptions must be handled or declared; unchecked are runtime exceptions.

### 21. What is garbage collection?
→ Automatic memory management that deletes unused objects.

### 22. What is the difference between `abstract class` and `interface`?
→ Abstract classes can have implementations and state; interfaces are pure contracts (before Java 8).

### 23. What is the `static` keyword used for?
→ To define class-level variables or methods shared across all instances.

### 24. How does the `synchronized` keyword work?
→ It prevents multiple threads from accessing a block or method simultaneously.

### 25. What is the difference between `HashMap` and `Hashtable`?
→ `HashMap` is unsynchronized and allows null keys/values; `Hashtable` is synchronized and does not allow nulls.

### 26. What is factory design pattern in java?
→ In the Factory Pattern, you define an interface or abstract class for creating an object, but let subclasses or methods decide which class to instantiate. It promotes loose coupling between client code and the classes it uses.


⚛️ React Mock Interview Questions
1. What is the difference between props and state in React?
 - Props are readonly.
 - states are mutable.
 - states are local to the component.
 - props are passed from component to childs.
 - props are created just by passing parameter to child component.
 - states are created using usestate, which returns state and setState.

2. What will be the output of the following code?
```jsx
function Counter() {
  const [count, setCount] = React.useState(0);

  const handleClick = () => {
    setCount(count + 1);
    setCount(count + 1);
  };

  return (
    <button onClick={handleClick}>
      Count: {count}
    </button>
  );
}
```
➡️ What will happen when the button is clicked once?
 - output will be 1.

3. What is the purpose of the useEffect hook, and when does it run?
 - this is multipurpose hook in functional components.
 - this runs based on use case as below.
 - if paramater2 is [], meaning only on mounting the callback will execute.
 - if parameter2 has [key], then the callback will be called on first render and everytime the state of key changes.
 - if returned any function from the arg1 callback in useeffect when arg2 is [] then it will get called when component is getting unmounted i.e. cleanup stage.
 - if returned fn from arg1 callback in useeffect when arg2 is [key1] then it'll get called when key1 changes then will get called with new val and on final cleanup it'll get called.

4. Explain the virtual DOM and how React uses it.
 - Virtual DOM is a virtual copy of the actual DOM, that react hold.
 - it is used to optimize performance using mechanism called reconsilliation.
 - whenever there is state change, prop change, etc, react creates new copy of the virtual DOM, then applies the updated state of component to it and then compares the copies to get the changes only.
 - then it applies those changes to the actual DOM, this in turn optimises app performance.

5. How do you conditionally apply a CSS class in React?
 - className is the attribute that can accept the conditional statement.
 - based on condition it'll interpret the classname and at runtime will use that call.
 - can use style attribute for conditional styling as well.

6. What is the difference between controlled and uncontrolled components in React?
 - Controlled components are input fields which are handled by react states via stet variable and setState.
 - uncontrolled components are input fields which are handler by DOM itself.
 - react component can access the uncontrolled components using useRef to access them.
 - react component can directly change the controlled components by changing the state that is bound to the input.

7. How does React handle events? Explain event delegation in React.
 - React uses synthetic events, which are its cross-browser wrapper around native browser events. These events behave consistently across different browsers.
 - React handles event using attributes like onClick, onChange.
 - handlers are attched to the elements and the handler functions get called whenever there is action.
 - In react event delegation is a technique by which the event handler is attached to the root element rather than all the childs, 
 - this way it doesn't cause overhead of attaching and detaching event handler everytime element is born/dies.

8. What are React hooks? Name a few common hooks other than useState and useEffect.
 - react hooks are way to intercept any change/lifecycle happening in component.
 - you get to to side actions or update state using hooks.
 - e.g. useRef, ueContext, useLayoutEffect, useMemo, useCallback.

9. Explain React’s Context API and when to use it.
 - context api is one of the way in react to resolve the prop drillig issue.
 - using context API you get to create a global state and react will make it accessible accross components.
 - although contextAPI has few performance issues when it comes to complex state updates.
 - it is recommended to use redux like solution when handling complex states.

10. What is React.memo and when should you use it?
 - it is a HOC that memoises the component.
 - It prevents unnecessary re-renders by reusing the last rendered output if the component’s props haven’t changed.
 - so to avoid re calculculating the component again, memo helps use the cached version.
```jsx
const MyComponent = React.memo(function MyComponent({ value }) {
  console.log('Rendering:', value);
  return <div>{value}</div>;
});
```
11. What is the difference between useMemo and useCallback hooks?
| Hook            | Purpose                               | What it memoizes                                           | When to use                                                                              |
| --------------- | ------------------------------------- | ---------------------------------------------------------- | 
| **useMemo**     | Memoizes the **result of a function** | Returns **a memoized value** (e.g., expensive calculation) | Use when you want to avoid recalculating a **value** unless dependencies change          |
| **useCallback** | Memoizes the **function itself**      | Returns a **memoized function**                            | Use when you want to avoid recreating a **callback function** unless dependencies change |


12. How does React handle reconciliation? What is the key role of the key prop in lists?
 - reconsilliation is way how react handles DOM updates.
 - react keeps copy of the DOM, called virtual DOM, etc. this is many time repeated so i'm skiping.
 - the key prop in lists is an optimisation technique in react that helps to know the relative position of elements in list has changed or not and it avoids recalculating the position od element in DOm, and just content if order is same.
 - this resembles trackby from angular.

13. Explain the concept of higher-order components (HOC) in React.
 - Higher order components in react are components that take a component as an argument and return updated/processed component.
 - this is used to implement some common resuble functionality, like applying theme to components, etc.

14. What is the difference between useRef and createRef?
 - useRef is used to wither create a ref that doesnot reinitialise on every rerender, and remains intact and can be used as persistent store.
 - using useRef we can access elements from DOM using ref property.
 - createRef I haven't used.

15. How would you optimize performance in a large React application?
 - use keys on list.
 - use useMemo and useCallback hooks.
 - use redux like state management to aviod pitfalls of context api of frequent state changes.
 - use React.lazy to reduce intial load time.
 - use pagination when dealing with large grids.

26. What is the difference between useLayoutEffect and useEffect in React?
 - useLayoutEffect runs before paint.
 - useeffect runs after paint is completed.
 - uselayoutEffect blocks the paint till its callback completed.
 - useeffect is asynchronous and doesn't block render.
 - useefect is preffered unless there's need of uselayouteffect.

27. How does useReducer differ from useState in React? When should you use it?
- useState
  - Used to manage simple state or few state variables.
  - Provides a setter function to update state directly.
  - Updates are independent and often straightforward.
- useReducer.
  - Used to manage complex state logic or when state depends on previous state.
  - Inspired by Redux-like reducer pattern.
  - Uses a reducer function (state, action) => newState to update state based on actions.
  - Useful when multiple related state variables must update together.
```jsx
const initialState = { count: 0 };
function reducer(state, action) {
  switch(action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      return state;
  }
}
const [state, dispatch] = useReducer(reducer, initialState);
dispatch({ type: 'increment' });
```

28. What are controlled vs uncontrolled forms in React?
 - controlled components are where fields are controlled by react itself, using states and setState, useState, etc.
 - uncontrolled components are the ones which are handled by DOM and can be later access by component, accessed by useRef.
 - controlled components are useful when working with immediate sideeffects.
 - uncontrolled components are good when no need to handle immediate sideeffects.
 - Examples.
 - controlled - typeahead, calculating user input and show on ui like calculator.
 - uncontrolled - just need to do some action on form submit.

29. What is React Portals and when would you use them?
 - React Portals provide a way to render a component’s subtree into a DOM node that exists outside the parent component’s DOM hierarchy.
 - Normally, React components render inside their parent DOM node, but portals let you render children somewhere else in the DOM.
 - Created using ReactDOM.createPortal(child, container).
 - Useful for UI elements that need to visually "escape" their container without losing React context.

30. How do you test a React component? What tools do you use?
 - Use Jest as the test runner
 - Use React Testing Library(`@testing-library/react`) to test component rendering and simulate user behavior.
 - Write tests that focus on what the user sees and does, not implementation details.
 - Run tests regularly and include them in CI/CD pipelines for reliability.

☕ Java Mock Interview Questions
6. What is the difference between ArrayList and LinkedList in Java?
 - Arraylist is variable size array, - constant time fetch like array, when deleting element takes linear time.
 - Linked list is data structure when it's about working with ends of array. it's efficient accessing front and rear end of list in constant time.
 - removing elemtn from ends also is constant time.

7. What are functional interfaces? Give an example.
 - funtional interfaces are interfaces that are designed for single task, they have single method signature, used in fucntional programming to instanciate using lambda expressions.
 - E.g. Runnable, Predicate.
 
8. Explain how the Java Stream API works and give an example use case.
 - java stream api is introduced in java8.
 - this introduced fucntional programming style in java.
 - this helps using labda expressions to process data in steps like, filter then map then print in single statement.
 - they have operators either ones which doen't return stream(`Terminal operations`) and few who return stream(`Intermediate operations`), the returned strem can be piped to next operator to process further. if used the non returning operator in end then strem ends.

9. What is the difference between == and .equals() in Java?
 - == compares the referance.
 - .equals compares content of the object.
 - it's good idea to override .equals when having your own object and going to compare.

10. Explain the Factory Design Pattern with a simple example.
 - Factory method centralizes object creation.
 - Client code is independent of the concrete classes.
 - Easy to add new products without changing client code.

11. What is the difference between abstract class and interface in Java?
 - abtract class can have abstract and concrete methods, variables and can have constructor.
 - interface can have abstract, default and static methods and static final variables.
 - interfaces need to be implemented.

12. Explain the concept of Exception Handling in Java and the difference between checked and unchecked exceptions.
 - Exption handling is way to handle the exception either at compile time or run-time to avoid unexpected failure in code.
 - Checked exceptions are those that come at compile time, you can either handle them using try catch or use trows keyword to pass that error to next handler.
 - Unchecked exceptions are the ones that show up at runtime.

13. What is the purpose of the final keyword in Java?
 - final keyword is used to note that the entity is not modifiable and should be treated as constant.
 - interfaces can have constants as static final.
 - if declared as final in class then that variable is constant there.
 - also finals cannot be overriden in child classes.

14. What is multithreading in Java? How do you create a thread?
 - multithreading is a way to achive performance in java where you can create threads which will run in parallel to complete tasks.
 - threads can be started calling start(in turn calls run) method.
 - can create thread using.
 ```java
 //1.  can extend Thread class.
 //2. can implement Runnable interface.
 //3. can use lambda expressions. 
 Thread t = new Thread((data: str) -> System.out.println(str));
 ```
15. Explain the difference between HashMap and Hashtable in Java.
 - Hashmaps are key value pair data structure.
 - Hashmap is not syncronised and allows null key values.
 - Hashtables are synchronised and don't allow null key values.
 - When working with Multithreading, then Hashtables are must.

16. What is the difference between synchronized method and synchronized block?
| Feature              | `synchronized` Method                                | `synchronized` Block                                        |
| -------------------- | ---------------------------------------------------- | ----------------------------------------------------------- |
| **Scope**            | Locks the **entire method**                          | Locks **only a specific section/block** of code             |
| **Flexibility**      | Less flexible — locks on the current object (`this`) | More flexible — can lock on any object or class             |
| **Performance**      | Can be less efficient (locks more code than needed)  | More efficient — allows fine-grained synchronization        |
| **Lock granularity** | Coarse-grained lock                                  | Fine-grained lock                                           |
| **Usage**            | Use when whole method must be thread-safe            | Use when only a part of the method needs to be synchronized |

17. Explain the Java Memory Model (JMM) and how it relates to multithreading.
 - uses heaps and stack.
 - has garbage collectors.
 - when dealing with common variables/resource in threads, better to syncronise them.
 - not much detail i know.

18. What are Java annotations? How and why are they used?
 - annotations are keywords.
 - when used on attributes they mark those attribute with some metadata, i.e. to have some specific behavior.
 - annotations are used to mark the enitity for some specific purpose.
 - you use @annotationName on top of the entity to use.

19. Explain the difference between ArrayList and Vector in Java.
| Feature                | `ArrayList`                             | `Vector`                                  |
| ---------------------- | --------------------------------------- | ----------------------------------------- |
| **Thread Safety**      | ❌ Not synchronized (not thread-safe)    | ✅ Synchronized (thread-safe)              |
| **Performance**        | Faster (no overhead of synchronization) | Slower due to synchronization             |
| **Synchronization**    | Must manually synchronize for threads   | Built-in synchronization                  |
| **Growth Policy**      | Grows by **50%** of current size        | Grows by **100%** (doubles in size)       |
| **Legacy**             | Part of **Java Collections Framework**  | Older (introduced in Java 1.0)            |
| **Use in modern code** | Preferred for **single-threaded use**   | Rarely used now; replaced by alternatives |

20. What is the difference between throw and throws in Java exception handling?
 - throw → Used to actually throw an exception (with new Exception).
 - throws → Used to declare that a method might throw one or more exceptions.
 - If you're writing a method that might fail, use throws to pass the responsibility to the caller.
 - If you're intentionally stopping execution with an error, use throw.

21. What is the difference between Comparable and Comparator in Java?
 - Use Comparable to define one natural ordering inside the class.
 - Use Comparator to define multiple/custom orderings outside the class.

22. What is dependency injection? How is it used in Spring Framework?
➡️ Covers concepts of loose coupling, and usage of annotations like @Autowired.

23. What are wrapper classes in Java, and why are they used?
➡️ Covers conversion between primitives and objects (int → Integer, etc.)

24. Explain the concept of garbage collection in Java. How does it work?
➡️ Talk about memory management, GC roots, and automatic cleanup.

25. What is the difference between == and .equals() in Java for strings?
➡️ They might test this again — useful to explain interning and heap vs pool

### Harsh
----------------
Q1.
Promise.resolve().then(()=>console.log('Promise 1'));

setTimeout(()=>console.log('Timeout 1'),0);

Promise.resolve().then(()=>console.log('Promise 2'));

setTimeout(()=>console.log('Timeout 2'),0);

console.log('End')
-----------------------------------------
Q2.
- destructuring

const person = {
  name: "Alice",
  age: 25,
  address: {
    city: "New York",
    state: "NY",
  },
};
const [address] = person;
const [city] = address;


-----------------------
Q3.
var a = 10
const b = 10
let c = 10
var a = 5 

console.log(window.a) // 5
console.log(window.b) // 10
console.log(window.c) // 10
-------------------------
abort controller
-------------------------
intersection observer
-------------------------
forwarRef
-----------------------
does use effect propogate from parent to child or child to parent (lifecycle hooks)
--------------------
what is Next js used for
------------------