1. Abstract class vs interface difference.
| Feature                      | **Abstract Class**                                            | **Interface**                                                                         |
| ---------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Purpose**                  | Used when classes share a common base with default behavior   | Used to define a contract (what a class must do, not how)                             |
| **Methods**                  | Can have both abstract and **concrete (implemented)** methods | All methods are **abstract by default** (until Java 8+ allows default/static methods) |
| **Fields (Variables)**       | Can have instance variables with any access modifier          | Only constants (public static final) in most languages                                |
| **Constructors**             | Can have constructors                                         | Cannot have constructors                                                              |
| **Access Modifiers**         | Can use public, protected, private                            | All methods are public by default                                                     |
| **Multiple Inheritance**     | **Cannot** extend multiple abstract classes                   | **Can** implement multiple interfaces                                                 |
| **Use case**                 | When related classes share base functionality                 | When unrelated classes need to share common behavior                                  |
| **Extending / Implementing** | Use `extends` keyword                                         | Use `implements` keyword                                                              |

2. Compile time vs runtime polymorphism.
- Compile-time polymorphism (Static polymorphism):
 - Achieved through method overloading, where multiple methods share the same name but differ in parameters. The compiler decides which method to call based on the method signature during compile time.
- Runtime polymorphism (Dynamic polymorphism):
 - Achieved through method overriding, where a child class provides a specific implementation of a method declared in the parent class. At runtime, the method of the actual object type (child or parent) is called based on the reference, enabling `dynamic method dispatch.`

3. Oop pillars in java.
 - Abstraction.
  - Hiding internal implementation details and showing only the essential features to the user. Achieved using `abstract classes` and `interfaces`.
 - Encapsulation.
  - Wrapping data (variables) and code (methods) together and restricting direct access to some of an object’s components. Implemented using access modifiers (`private`, `protected`, `public`).
 - Inheritance.
  - Mechanism where one class acquires the properties and behaviors (methods) of another. Achieved using the `extends` keyword for classes and `implements` for interfaces.
 - Polymorphism.
  - Ability of an object to take many forms. Implemented via:
   - `Method overloading `(compile-time polymorphism)
   - Method overriding (runtime polymorphism)

4. Class vs interface diff.
| Feature             | **Class**                                                  | **Interface**                                                       |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| **Purpose**         | Used to define the **structure and behavior** of objects   | Used to define a **contract** that implementing classes must follow |
| **Inheritance**     | Supports **single inheritance** (`extends`)                | Supports **multiple inheritance** via `implements`                  |
| **Coupling**        | More **tightly coupled** (shares implementation)           | More **loosely coupled** (shares behavior only)                     |
| **Methods**         | Can have fully implemented methods (concrete), overridable | Can have **abstract**, **default**, and **static** methods          |
| **Variables**       | Can have instance variables                                | Only `public static final` constants allowed                        |
| **Usage Keywords**  | `extends`                                                  | `implements`                                                        |
| **Object creation** | Can create objects from concrete classes                   | Cannot create objects directly from interfaces                      |

5. Oop pillars with example.
6. Mysql connection step with java.
 - import.
 ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   Connection connection = DriverManager.getConnection(url, username, password);
   Statement stmt = connection.createStatement();
   ResultSet rs = stmt.executeQuery("SELECT * FROM users");
   
   while (rs.next()) {
        System.out.println("User: " + rs.getString("username"));
   }
```

7. Jdk, jre, JVM, bytecode.
 - JDK
  - stands for Java developement kit.
  - holds JRE, javac, and utilities.
 - JRE.
  - Java Runtime Environment.
  - Java byte code is executed on this env.
  - contains JVM, core libraries.
 - JVM.
  - Java virtual machine.
  - converts bycode to machine executable code.
 - Bytecode.
  - created by compiler.
  - this is platform independant code that can be executed on JRE of that OS.
`JDK is the full kit for developing Java apps, including the compiler. JRE is the environment to run Java apps, which includes the JVM. JVM runs the bytecode — a platform-independent intermediate code generated by the compiler.`

8. Lambda expression Java 11.
 - functional way of writing code.
 - are must when working with java stream apis.
 `Lambda expressions allow writing concise, functional-style code in Java. They are especially useful with functional interfaces and are widely used in Streams API for processing collections. Java 11 supports var in lambda parameters for more readable code.`
 ```java
 Runnable r2 = () -> System.out.println("Running");
 ```

9. Java 8 vs Java 11 features.
 - Java8.
  - lambda expressions.
  - stream API.
  - Functional interfaces.
  - default and static methods in interfaces.
 - Java11.
  - var in labda expressions.
  - New String Methods – isBlank(), lines(), repeat(), strip(), stripLeading(), stripTrailing()
  
10. String pool in java.
 - The String pool is a special memory area within the Java heap that stores interned String literals.
 - When a String literal is created, Java checks the pool. If an identical string already exists, the new reference points to the existing object instead of creating a new one.
 - This sharing is possible because String objects are immutable, meaning their values cannot be changed once created. This ensures the integrity of shared references.
 - If a String is modified (e.g., via concatenation), a new String object is created in memory, not in the pool unless explicitly interned using intern().

11. Stringbuilder vs StringBuffer.
 - Both StringBuilder and StringBuffer are mutable classes used to perform operations on strings without creating new objects, unlike String, which is immutable.
 - StringBuffer was introduced first (in Java 1.0) and is t hread-safe because its methods are synchronized.
 - StringBuilder was introduced later (in Java 1.5) as a faster alternative for use in single-threaded environments, as it is not thread-safe.
 - In general, use StringBuilder when thread safety is not required, and StringBuffer when multiple threads might access the same instance concurrently.

12. Explain system.out.println().
 - System is a final class in the java.lang package.
 - out is a static final field in the System class, and it refers to a PrintStream object.
 - println() is a method of the PrintStream class, used to print output to the console, followed by a new line.
 - So, System.out.println() calls the println() method on the PrintStream object referred to by System.out.

13. Types of inheritance.
 - Single Inheritance:
  - A class inherits from only one superclass.
 - Multilevel Inheritance:
  - A class inherits from a class, which itself inherits from another class.
 - Hierarchical Inheritance:
  - Multiple classes inherit from a single superclass
 - Multiple Inheritance:
  - A class implements multiple interfaces.

14. How multiple inheritance achieved in java.
 - this is acheived via intefaces, where one class can implement multiple interfaces.

15. Diamond Problem in Interfaces.
 - If a class implements two interfaces that both have the same default method, Java needs to resolve the conflict — this is similar to the Diamond Problem in C++ (which Java avoids with classes).

15. Why Java is platform independent.
 - Java is platform independent because of its bytecode and Java Virtual Machine (JVM).
 - When a Java program is compiled, it is converted into bytecode, which is a platform-independent intermediate code.
 - This bytecode can be executed on any platform that has a compatible JVM.
 - The JVM is platform-specific, but it knows how to run the same bytecode on its own platform.
 - This "write once, run anywhere" behavior is what makes Java platform independent.

16. How to achieve multi threading in Java?