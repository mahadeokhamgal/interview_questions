1) rest vs spread operator.
    *REST* -
    `Rest operator introduced in ES6 is used to collect remaining entries(arguments in case of function) in single variable. It's commonly used in function arguments and destructuring assignmentss`
    *Syntax* - 
    `Function` - function fun(a, ...b) {}; //b contains all arguments from 2 and next.
    `Assignment` - const [a, ...b] = c; //c is array.

    *Spread* -
    `Spread operator introduced in ES6, uses tripple dot syntax. used to spread/unpack array/object into elements/entries. It is essentially the opposite of the rest operator`
    *Syntax* -
    ```js
    let a = [...b, ...c]; //b and c are arrays.
    ```

2) find vs find one in mongo db.
    `find and findOne are methods provided by mongoose, that are called on mongoose model and have purpose of finding matching document/documents from collection.`
    *findOne* -
    `findOne is method used to fetch first matching document from mongo collection. the return type is document(or a promise, in Mongoose). If no document matches the query, it returns null`
    e.g.
    ```js
    User.findOne({ username: 'john_doe' })//User is mongoose model.
        .then(user => {
            console.log(user);  // Output: Single document or null if not found
        })
    ```
    *find* -
    `find method is used to fetch all matching documents from mongo collection. this returns cursor(or a promise, in Mongoose) which is an iterable object that can be used to loop through the results.`
    e.g.
    ```js
    User.find({ age: { $gte: 18 } })
    .then(users => {
        console.log(users);  // Output: Array of matching documents
    })
    .catch(err => console.error(err));
    ```

3) how to create express server in express.
```js
// npm init -y
// npm i express cors

//app.js
const express = require('express');
const app = express();

app.use(cors());

app.get('', (req, res) => {
    res.status(200).send('Hello');
})

app.listen(3000, () => {
    console.log("Server strted on 3000");
})
```
4) what module in angular is used to perform REST apis.
    - HttpClientModule
    - Can use Axios.
    - Can use fetch.

5) how to connect node to mongo.
```js
//npm i mongoose
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/dbname', {})
    .then(() => {
        console.log("mongodb connected");
    })

//additionally can create schema and model.
const userSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,   // Ensures email is unique
    },
    createdAt: {
        type: Date,
        default: Date.now, // Default value is the current date and time
    }
});

const User = mongoose.model('User', userSchema);
```

6) how variables are declared in JavaScript.
- let, const, var.

7) what is difference between let, const, var

8) what is difference between map()and filter() 
9) what is life cycle hooks in angular explain.
    `Lifecycle hooks in angular are methods which gets invoked on components/directives lifecycle, which can be used to execute some task on specific component state/change.`

    1. ngOnChanges - `called when databound input property to component changes. has object type as SimpleChanges(prev, new)`
    2. ngOnInit - `called once after ngOnChanges during component initialisation.`
    3. ngDoCheck - `called on every change detection cycle unless onPush is enabled in that case will get called only if dataBound property is changed.`
    4. ngAfterContentInit - `called once projected content is initialised.`
    5. ngAfterContentChecked - `called when projected content is checked.`
    6. ngAfterViewInit - `called once when component view and child component view is initialised.`
    7. ngAfterViewChecked - `called when view component and child is checked.`
    8. ngOnDestroy - `called just before the component dies.`
    **Additionals.**
    *Change Detection*: Angular uses change detection to keep the view in sync with the data model. The lifecycle hooks like ngOnChanges, ngDoCheck,  ngAfterContentChecked, and ngAfterViewChecked are related to this process. These hooks allow you to monitor and react to changes in the  component or view.

    *Change Detection Strategies*:
    `Default Strategy`: Angular checks all components for changes during every change detection cycle.
    `OnPush Strategy`: Angular checks components only when an input property changes or when an event originates inside the component. This can   significantly improve performance by reducing the number of checks Angular performs.

10) what is component directive in angular.

11) what is service in angular
12) what is middleware in node. Js
13) what is promise in JavaScript with method names
14) what is call back and why it is use in JavaScript
15) router handling in node. Js
16) what is template in angular
17) es6 feature
18) what is lazy loading and it's types
    - route based lazy loading.
    - 
19) local storage scenario question
20) what is feature of angular 16
21) what is standalone components
22) life cycle hooks of angular