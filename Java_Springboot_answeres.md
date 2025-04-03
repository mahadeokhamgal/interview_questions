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
- **What are String, StringBuilder, and StringBuffer?**
- **Explain the difference between `final`, `finally`, and `finalize()`.**
- **How does the HashMap work internally in Java?**
- **What is the difference between ArrayList and LinkedList?**
- **Explain the concept of multithreading and the Thread lifecycle.**
- **What is a functional interface? Give an example.**
- **What is the significance of the `static` keyword?**
- **How are exceptions handled in Java?**
- **What is the purpose of the `super` keyword?**
- **How does `synchronized` work in Java?**
- **Explain `equals()` and `hashCode()` methods.**
- **What are wrapper classes in Java?**
- **How does Java ensure platform independence?**
- **What is the difference between `==` and `.equals()`?**
- **What is a volatile variable in Java?**
- **What is the use of the `transient` keyword?**
- **Explain the concept of the default method in interfaces (Java 8+).**
- **How does the Java memory model work?**
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

# Advanced Java (Java 8+) (25 Questions)

- **What are the new features introduced in Java 8?**
- **Explain the concept of lambda expressions.**
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
- **How is `@PathVariable` different from `@RequestParam`?**
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
