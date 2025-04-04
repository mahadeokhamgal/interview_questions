# Core Java (30 Questions)

- **What is the difference between JDK, JRE, and JVM?**
    **JDK**
    `This is complete java developement kit which encomposes, JRE, JVM and a set of development tools such as compilers, debuggers, and other utilities that are necessary for developing Java applications.`

    **JRE**
    `This is Java Runtime, on which Java code gets executed. and core libraries but does not contain developement tools like compilers, debuggers, Essensially JRE allows you to execute Java programms.`
    **JVM**
    `This is Java virstual machine which executes compiled java bytecode. The JVM enables Java's platform independence by abstracting the underlying operating system and hardware.`

- **Explain OOP principles with examples.**
    1. Abstraction.
        `Achieved by:`
        1. Abstract classes and methods.
        2. Interfaces.

        `Example:`
        An abstract class Vehicle might have an abstract method move(). Different vehicle subclasses (like Car and Bike) implement  the  move() method with specific behavior.

    2. Encapsulation.
    `Encapsulation is the concept of bundling data (variables) and methods that operate on the data into a single unit (class). It also involves restricting access to some of the object's components using access modifiers to protect the object's state.`
        `Achieved by`
        1. Using access modifiers (private, public, protected).
        2. Getters and setters to control access to private fields.

        `Example`
        1. A class Person encapsulates personal information (like name and age) and provides controlled access via getters and setters.

    3. Inheritance.
    `Inheritance is a mechanism where one class acquires the properties and behaviors (methods) of another class. It allows for the creation of a new class based on an existing class, promoting code reusability.`
        `Achieved by:`
        1. The extends keyword for class inheritance.
        2. The implements keyword for implementing interfaces.

        `Example:`
        A Dog class can inherit from a Animal class, gaining its properties and methods.
    
    4. Polymorphism.
    `Polymorphism allows objects of different classes to be treated as objects of a common superclass. It supports method overriding (runtime polymorphism) and method overloading (compile-time polymorphism)`
        `Achieved by:`
        1. Method Overloading: Same method name, but different parameters.
        2. Method Overriding: Same method signature in the subclass as in the parent class, but with a different implementation.

        `Example:`
        - Method Overloading: Multiple constructors in a Rectangle class with different parameters.

- **What is Method overloading and Method Overriding?**
    *Method overloading*
    `Method overloading occurs when multiple methods have the same name but differ in the number, type, or order of their parameters. It is a compile-time polymorphism feature in Java, meaning the method to be invoked is determined at compile time based on the method signature.`
    Key fetures-
    - Methods with the same name.
    - Differing parameters (number, type, or both).
    - Compile-time polymorphism.

    *Method overriding*
    `Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its parent class. It is a runtime polymorphism mechanism because the method to be called is determined at runtime, depending on the object being referenced.`
    Key points:
    - The method signature in the subclass must match that of the parent class.
    - It allows the subclass to change or extend the behavior of the parent class method.
    - Runtime polymorphism.

- **How does garbage collection work in Java?**
    `Garbage collection in Java is an automatic memory management mechanism that removes objects that are no longer in use or referenced by the program. This helps to ensure efficient memory usage by reclaiming unused memory, preventing memory leaks.`

- **What are String, StringBuilder, and StringBuffer?**
    *String*
    - `String is one of the primitive data types in Java, that represents series of characters.`
    - String is immutable, meaning everytime you want to update something in string, a new memory will be created.

    *StringBuilder*
    - `StringBuilders are good way to manipulate strings as it is mutable in nature, provides lot of methods to process string. Stringbuilders are not thread safe in case of multithreading.`

    *StringBuffer*
    - `StringBuffer are an similar to stringbuiler and are thread safe as compared to stringbuilder. These are good to use in case multithreading is needed to be used.`

- **Explain the difference between `final`, `finally`, and `finalize()`.**
    *final*
        - Variables: When a variable is declared final, it can be assigned a value only once. After that, its value cannot be changed (i.e., it's immutable).
        - Methods: When a method is declared final, it cannot be overridden by any subclass.
        - Classes: When a class is declared final, it cannot be subclassed.
    
    *finally*
    `Used in exception handling to define a block of code that will always execute after the try and catch blocks, even if an exception occurs. It's commonly used for cleanup, such as closing files or releasing resources.`
    
    *finalize()*
    `A method in the Object class that is called by the garbage collector before an object is garbage collected. It was intended for resource cleanup, but it's deprecated and should not be used in modern Java. It is not thread-safe.`

- **How does the HashMap work internally in Java?**
    `A HashMap in Java is a key-value data structure that uses a hashing mechanism to store and retrieve data efficiently. When you add an entry (key-value pair), the key is hashed to generate a hash code, which determines the index in an internal array (called the bucket array).`
    **Hashing**: The hashCode() method of the key is called to generate a hash code. The hash code is then used to compute an index in the array where the entry should be placed.
    **Handling Collisions**: If two keys generate the same hash code (a collision), the HashMap handles it using a technique called separate chaining. In this case, a linked list or a balanced tree (starting from Java 8) is used to store multiple key-value pairs at the same index in the array.
        *From Java 8 onwards*: If the number of elements in a bucket (due to collisions) exceeds a certain threshold (typically 8), the HashMap switches from a linked list to a balanced tree (Red-Black Tree) to ensure that the lookup time remains O(log n) instead of O(n) in the worst case.
    **Load Factor & Resizing**: 0.75
    **Null Keys/Values**: A HashMap allows one null key and any number of null values, which is important for certain use cases.

- **What is the difference between ArrayList and LinkedList?**
    *ArrayList*
    1. Arraylist is resizable array like data structure.
    2. Contegious memory locations.
    3. Element access is constant time.
    4. Element update constant time.
    5. deleting fist element is linear time.
    6. ideal when frequent element update is needed.

    *LinkedList*
    1. Linkedlist is data structure where nodes are connected by pointers.
    2. Non contagios memory location.
    3. Element access is linear time.
    4. Element update is linear time.
    5. deleting first element is constant time.
    6. Ideal when parse/spread around memory allocation is required.

- **Explain the concept of multithreading and the Thread lifecycle.**
    - How to create threads.
    *Extend thread way.*
    1. create class B that represents a thread.
    2. extend Thread class on it as `B extends Thread`.
    3. override run method in it, add what to execute in parallel thread in run method.
    4. create instance of B in main thread can be main method, and call start method of B's instance to start the parallel thread.
    
    *implements Runnable way.*
    1. create class B that represents a thread.
    2. extend Thread class on it as `B implements Runnable`.
    3. override run method in it, add what to execute in parallel thread in run method.
    4. create instance of B in main thread can be main method.
    5. create new thread using Thread t1 = new Thread(b's instance);
    6. call t1.start(); to start the alternative thread.

    *Using labda expression*
        Runnable task = () -> System.out.println("Lambda thread is running");
        Thread thread = new Thread(task);
        thread.start(); // starts the thread
        `Pros`: Very concise and clean. `Cons`: Only works for Runnable tasks (not Thread directly).
    *Using the ExecutorService (Thread Pool)*
    *Using ForkJoinPool*

    Lifecycle - 
    1. New.
    2. Runnable.
    3. Running.
    4. Blocked/Waiting.
    5. Terminated.

- **What is a functional interface? Give an example.**
    `Functional interface a special type of interface in java, that has exactly one abstract method, These interfaces are primarily intended to be used with lambda expressions`.
    - In Java, a functional interface can be created using the @FunctionalInterface annotation.
    Example - Runnable, Comparator.

- **What is the significance of the `static` keyword?**
    1. Static Variables (Class-level Variables)
    - static variables are bound to class itself rather than it's instances, these have only one instance, these are accessed by classname.<variablename>.
    2. Static Methods (Class-level methods)
    - Static methods are called by Classname than instance name, generally used for utility methods which don't need to rely on instance.
    3. Static Blocks (Initialization block) -
    `used to initialise static variables or any class level setup when class is loaded.`
    4. Static Classes (Static Nested Classes)
    `A static nested class is a class defined within another class, but it does not require an instance of the enclosing class to be instantiated.`
    5. Static Imports.
    `Allows to call static members(methods /variables) from class directly using method() or variable syntax.`
    6. Global Constants.

- **How are exceptions handled in Java?**
- **What are unhandled exceptions in java and how to handle them?**
    Handled (Checked) Exceptions:
    - Checked exceptions are exceptions that the compiler forces you to handle. If these exceptions are not handled, a    compilation error occurs.
    - These exceptions are typically related to issues that are outside the control of the programmer (e.g., I/O errors,  database issues).
    - They can be handled using try-catch-finally blocks.
    - Example: IOException, SQLException
    - It is recommended to handle specific exceptions instead of catching a generic Exception, as it provides more meaningful     error handling and debugging information.
    - You can also propagate them to the caller using the throws keyword if you choose not to handle them within the method itself.

    *Unhandled(Unchecked) exceptions*
    - Unchecked exceptions (also known as runtime exceptions) are not checked by the compiler at compile-time. These exceptions   can occur during the program’s execution, but you are not forced to handle them.
    - These exceptions often represent programming errors, such as null pointer access, array index out of bounds, or     arithmetic errors (e.g., division by zero).
    - Example: NullPointerException, ArithmeticException, ArrayIndexOutOfBoundsException
    - Since unchecked exceptions are not subject to the throws clause requirement, they don’t need to be explicitly handled using try-catch blocks. However, they can still be caught in the same way as checked exceptions.
    - Best Practice: Handle unchecked exceptions only when there is a real need to recover from them or log them meaningfully, but avoid catching them blindly unless necessary.

    `try`: Code that may throw an exception is placed inside the try block.
    `catch`: This block catches and handles specific exceptions thrown in the try block.
    `finally`: This block is executed whether or not an exception occurs, useful for cleanup code like closing files or       releasing resources.

- **Why strings are immutale in java ?**
    1. Security.
    2. Efficiency in String Pooling.
    3. Thread Safety.
    4. Hashcode Caching.

- **How to overcome/alternative for strings immutable behavior**
    - StringBuilder.
    - StrinBuffer.(Thread safe)

- **What is the purpose of the `super` keyword?**
    `Super is keyword, similar to this, whereas this refers to current object/class, whereas super refers to super class`
    - keyword used to refer to immediate parent context.
    - can call parent class contructor using super()
    - can user super.<fieldName> to access super class properties.
    - can call parent/supe class methods using super.methodName(), especially if the child class has overridden that method.

- **How does `synchronized` work in Java?**
    `synchronized keyword is used to make blocks/functions/properties thread safe`
    - Synchronized Methods: When a method is marked as synchronized, it locks the object (for instance methods) or the class (for static methods) before executing the code inside it. Only one thread can hold the lock at any given time, and other threads will have to wait until the lock is released.
    - Synchronized Blocks: If you don't want to synchronize an entire method, you can use synchronized blocks inside methods to lock only a portion of the code, which can improve performance.
    - **DeadLock**: situation when two or more threads are waiting for each other to release, leading to standstill.

- **Explain `equals()` and `hashCode()` methods.**
    equals() -
    - used to compare two objects for equality.
    Purpose: To determine if two objects are logically equivalent.
    Contract:
    `Reflexive`: An object must be equal to itself.
    `Symmetric`: If a.equals(b) is true, then b.equals(a) should also be true.
    `Transitive`: If a.equals(b) and b.equals(c) are true, then a.equals(c) must be true.
    `Consistent`: If a.equals(b) is true, then it should remain true as long as the objects are not modified.
    `Null comparison`: Any object should not be equal to null (a.equals(null) should return false).
    
    hashCode() -
    The hashCode() method returns an integer that is used by hash-based collections (like HashMap, HashSet, and Hashtable) to determine the bucket where an object should be stored.
    Purpose: To return a hash code that represents the "identity" of an object for use in hash-based collections.
    Contract:
    `Consistent`: If the object is not modified, multiple invocations of hashCode() should return the same result.
    `Equality`: If two objects are equal according to equals(), they must return the same hash code.
    `Non-equality`: If two objects are not equal according to equals(), they do not have to return different hash codes, but  it's generally good practice to minimize hash collisions.
    
    `Override both equals() and hashCode() together when you need logical equality based on object data.`

- **What are wrapper classes in Java?**
    `Object Representation of Primitives`: A wrapper class wraps a primitive value into an object. For example, int is wrapped into an Integer object.
   ` Autoboxing and Unboxing`:
    Autoboxing: Java automatically converts primitive types to their corresponding wrapper class when needed.
    Unboxing: Java automatically converts wrapper objects back to their corresponding primitive type when needed.

    Use Cases for Wrapper Classes:
    `Collections`: Java collections (like ArrayList, HashMap, etc.) can only store objects. If you need to store primitive data types in these collections, you must use the corresponding wrapper classes.
    `Methods that require objects`: Some methods, especially in APIs or libraries, may require objects instead of primitives. Wrapper classes provide the object representation of primitive types in such cases.
    `Null Representation`: Wrapper classes can be assigned null, which allows you to represent the absence of a value. For example, Integer can be null, while int cannot.

- **How does Java ensure platform independence?**
    - Java bytecode(.class) is platform independant, i.e. can be executed on any system.
    - Java JVM's are used to execute the bytecode on where the JVM is installed and it uses JIT to compile code to machine specific code.

- **What is the difference between `==` and `.equals()`?**
    ==
    - Used on objects to compare for referance.
    - Cannot alter behavior of == operator.
    `For Primitives`: When used with primitive types (e.g., int, char, boolean), == compares their values directly.
    `For Objects`: When used with objects, == compares whether the two references point to the same memory location. In other words, it checks if both references point to the same object in memory.

    .equals()
    - Used on objects to compare for equality.
    - Can override .equals method.

- **What is a volatile variable in Java?**
    - In Java, the volatile keyword is used to indicate that a variable's value may be modified by multiple threads. When a variable is declared as volatile, it ensures that.
    1. Visibility of changes.
    2. No Caching.
    3. Atomicity.

- **What is the use of the `transient` keyword?**
    - The transient keyword is used in Java to prevent serialization of specific fields in an object. When a field is marked as transient, it will not be serialized when the object is serialized. Serialization is the process of converting an object into a byte stream so it can be saved to a file, sent over a network, or stored in a database. The transient keyword is particularly useful when you want to exclude sensitive or unnecessary data from the serialization process.

- **Explain the concept of the default method in interfaces (Java 8+).**
    - default methods in interfaces introduced in java8.
    - default methods provide default implementations to methods allowing interfaces to have non abstract methods.
    - the default methods can be overriden in child class or can directly inherit them using implements.
    Benefits of Default Methods:
    1. Backward Compatibility: adding new default method doesn't need to add implementation for it like abstract methods.
    2. Multiple Inheritance of Behavior.


- **How does the Java memory model work?**
    `The Java Memory Model (JMM) is an essential part of Java's concurrency model that defines how threads interact through memory and what behaviors are allowed in a multithreaded environment. The primary goal of the JMM is to ensure that Java programs behave correctly when running on multiple threads, especially regarding shared variables and their visibility.`
    1. Shared Memory and Threads.

- **What are design patterns in Java? Name a few common ones.**
- **What is the difference between checked and unchecked exceptions?**
- **Explain how `try-with-resources` works in Java.**
- **How are generics used in Java?**
- **What is the Collections framework?**
- **How does the `Comparator` interface work?**
- **Explain the purpose of `enum` in Java.**
- **How does reflection work in Java?**
- **What are annotations, and how are they used in Java?**

---
# 12 Multithreading Interview Questions in Java

1. **What is multithreading in Java?**
2. **What is the difference between a process and a thread?**
3. **What is the life cycle of a thread in Java?**
- How to pause current thread for specific amount of time ?
- How to make my main thread wait for thread p1 to get completed ?
- When does thread instance/object get eligible for garbage collection ?
- When will you suggest Thread class and when will you suggest to use Runnable Interface?.

4. **How can you create a thread in Java?**
5. **What is the purpose of the `join()` method in Java?**
6. **What is thread synchronization in Java? Why is it important?**
7. **What are the different types of thread synchronization in Java?**
8. **What is the `volatile` keyword in Java? How does it relate to multithreading?**
9. **What is the difference between `wait()` and `sleep()` methods in Java?**
10. **What are thread pools, and why should you use them?**
11. **Explain the concept of deadlock in Java. How can you avoid it?**
12. **What are the differences between `CountDownLatch` and `CyclicBarrier` in Java?**


# Advanced Java (Java 8+) (25 Questions)

- **What are the new features introduced in Java 8?**
- **Explain the concept of lambda expressions.**
- What are ways to handle unhandled exceptions.
- **What is the purpose of the `Optional` class?**
- **How do streams work in Java?**
- **What is the difference between intermediate and terminal stream operations?**
- **Explain the use of the `map` and `flatMap` methods in streams.**
- **How is method reference used in Java?**
- **What is a functional interface?**
- **How do you implement parallel streams?**
- **Explain the purpose of the `Collectors` utility class.**
- **What is the difference between `forEach()` and `map()` in streams?**
- **How do you sort a list using streams?**
- **Explain the concept of default and static methods in interfaces.**
- **What is the `Predicate` functional interface?**
- **How does the `CompletableFuture` work?**
- **What is the purpose of the `LocalDate` and `LocalTime` classes in Java 8?**
- **What is the difference between `reduce()` and `collect()` in streams?**
- **Explain the concept of the `@FunctionalInterface` annotation.**
- **What are parallel streams?**
- **How does the `Stream.filter()` method work?**
- **What is the `BiConsumer` functional interface?**
- **How does the `Instant` class differ from `Date`?**
- **What is the difference between `Stream.findAny()` and `Stream.findFirst()`?**
- **How does the `Collectors.toMap()` method work?**
- **Explain the concept of a `Spliterator`.**

---

# Spring Boot (30 Questions)

- **What is Spring Boot, and why is it used?**
- **Explain the concept of dependency injection in Spring.**
- **What is the purpose of the `@SpringBootApplication` annotation?**
- **How does the Spring IoC container work?**
- **What are Spring Boot starters?**
- **Explain the difference between `@Component`, `@Service`, `@Repository`, and `@Controller`.**
- **What is the purpose of the `@RestController` annotation?**
- **How does Spring Boot handle configuration?**
- **What are Spring profiles, and how are they used?**
- **How do you implement exception handling in Spring Boot?**
- **What is the purpose of the `@RequestMapping` annotation?**
- **Explain how Spring Boot manages application properties.**
- **What is the `@Autowired` annotation used for?**
- **How do you configure a data source in Spring Boot?**
- **What is the purpose of the `@Entity` annotation in JPA?**
- **How does Spring Boot handle REST APIs?**
- **Explain the difference between GET, POST, PUT, and DELETE in REST APIs.**
- **How is `@` different from `@RequestParam`?**
- **What is the purpose of the `@Transactional` annotation?**
- **How do you implement pagination in Spring Boot?**
- **What are Hibernate and JPA? How are they related?**
- **How does caching work in Spring Boot?**
- **Explain the concept of Actuators in Spring Boot.**
- **What is the purpose of the `@Bean` annotation?**
- **How do you secure a Spring Boot application?**
- **What is the role of `application.properties` and `application.yml` files?**
- **How does Spring Boot handle asynchronous tasks?**
- **What is the `ModelAndView` object used for?**
- **How does the `@RequestBody` annotation work?**
- **Explain the use of DevTools in Spring Boot.**
- **Constructor Injection vs Field Injection (Not recommended) vs Setter Injection (Optional).**

---

# JUnit (15 Questions)

- **What is JUnit, and why is it used?**
- **Explain the difference between unit testing and integration testing.**
- **How do you write a simple JUnit test case?**
- **What is the purpose of the `@Test` annotation?**
- **How do you handle exceptions in JUnit tests?**
- **What is the role of the assert methods in JUnit?**
- **Explain the difference between `@BeforeEach` and `@BeforeAll`.**
- **How do you test a method that returns void?**
- **What is the purpose of `@Mock` and `@InjectMocks` in JUnit?**
- **How do you use Mockito in JUnit?**
- **What is the difference between `@AfterEach` and `@AfterAll`?**
- **How do you test private methods in JUnit?**
- **What is parameterized testing in JUnit?**
- **How do you create a custom test suite in JUnit?**
- **How does JUnit handle assertions for collections?**
