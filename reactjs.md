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
1. Create a react app to render a random dog image and change on every click. while image is beling loaded show loading icon.
2. Create react app for counter. On click of button it should start countdown of user input s and on complete it should show completed. if user clicks reset in between then timer will restart. usetr should be able to see timer clock on UI.
3. 











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