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
11. Stringbuilder vs StringBuffer.
12. Explain system.out.println().
13. Types of inheritance.
14. How multiple inheritance achieved in java.
15. Why Java is platform independent.
16. 