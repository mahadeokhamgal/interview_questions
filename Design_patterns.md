# Common Design Patterns in Java

1. Creational Patterns
Singleton
Factory Method
Abstract Factory
Builder
Prototype

2. Structural Patterns
Adapter
Decorator
Proxy
Facade
Composite
Flyweight

3. Behavioral Patterns
Observer
Strategy
Command
Template Method
Iterator
Chain of Responsibility
Mediator
Memento
State
Visitors

# Design Patterns Often Used in Spring Boot
1. Singleton
Spring Beans are Singleton by default.

2. Factory Method
Spring’s BeanFactory and ApplicationContext use this.

3. Dependency Injection (DI)
Core to Spring; it’s a pattern to inject dependencies rather than create them manually.

4. Proxy
Used heavily in Spring AOP (Aspect-Oriented Programming) for things like transaction management, security, etc.

5. Template Method
JdbcTemplate, RestTemplate and other template classes follow this pattern.

6. Observer
Application Events in Spring use this pattern.

7. Strategy
Used in Spring Security for authentication strategies or in other pluggable components.

8. Decorator
Common in Spring’s filter chains or wrappers around beans.