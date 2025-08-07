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
# What is reconciliation in React?
# Explain the concept of lifting state up in React.
# What are React Fragments and why would you use them?
# How does React’s rendering process work? When does a component re-render?
# What is the difference between useEffect and useLayoutEffect hooks?
# What are Pure Components and how do they differ from regular components?
# How can you optimize performance in React applications?
# How do you handle error boundaries in React?
# How does react application boot?
# How to create build and deploy on server in react?
