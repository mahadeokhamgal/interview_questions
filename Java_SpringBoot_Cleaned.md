1. Spring Boot Basics & Core Concepts
# What is Spring Boot, and why is it used?
# Why would you choose Spring Boot over the traditional Spring Framework?
# What are Spring Boot starters?
# Which Spring Boot starters or modules have you worked with in your projects?
# What is Spring Boot dependency management?
# What is the starter dependency of the Spring Boot module?
# How do you launch a Spring Boot application?
# What happens behind the scenes when the run() method is invoked in Spring Boot?
# What is the purpose of a CommandLineRunner in Spring Boot?

2. Annotations & Bean Management
# What is the role of the @SpringBootApplication annotation in a Spring Boot project?
# Can you replace the @SpringBootApplication annotation with @EnableAutoConfiguration, @ComponentScan, and @Configuration? If so, would the application behave the same way?
# What is the purpose of the @RestController annotation?
# Explain the difference between @Component, @Service, @Repository, and @Controller.
# What is the purpose of the @RequestMapping annotation?
# How does the @RequestBody annotation work?
# How is @PathVariable different from @RequestParam?
# What is the purpose of the @Autowired annotation?
# What is the purpose of the @Bean annotation?
# What is the purpose of the @Transactional annotation?
# What is the purpose of the @Entity annotation in JPA?
# Can you describe the purpose of stereotype annotations in Spring?
# How do you declare a bean in the Spring Framework?

3. Dependency Injection & IoC
# Explain the concept of dependency injection in Spring.
# What is dependency injection, and why is it important?
# What are the different ways to implement dependency injection in Spring and Spring Boot?
# How does the Spring IoC container work?
# Constructor Injection vs Field Injection vs Setter Injection.

4. Configuration & Profiles
# How does Spring Boot handle configuration?
# How does Spring Boot manage application properties?
# What is the role of application.properties and application.yml files?
# What are Spring profiles, and how are they used?
# How do you override the default configurations in Spring Boot?

5. Auto-Configuration & Embedded Server
# What is auto-configuration in Spring Boot, and how does it work?
# How can you disable a specific auto-configuration in Spring Boot?
# How do you disable a specific auto-configuration class?
# Is it possible to change the port of the embedded Tomcat server in Spring Boot?
# What is the default port of Tomcat in Spring Boot?
# Can we disable the default web server in a Spring Boot application?
# Can we create a non-web application in Spring Boot?

6. REST APIs & Web Layer
# Write a Controller in Java that’ll get API from URL in format /\<id>?name=\<name> and return dynamic object as response → {id: <id>, name: <name>}
# How does Spring Boot handle REST APIs?
# Explain the difference between GET, POST, PUT, and DELETE in REST APIs.
# Describe the flow of HTTPS requests through the Spring Boot application.
# How do you handle file uploads in Spring Boot?
# How do you implement pagination in Spring Boot?
# How do you implement exception handling in Spring Boot?
# What is the ModelAndView object used for?

7. Data Layer & JPA
# How do you configure a data source in Spring Boot?
# What are Hibernate and JPA? How are they related?

8. Security
# How to use JWT in Spring Boot?
# How do you secure a Spring Boot application?

9. Advanced Features & Tools
# Explain the concept of Actuators in Spring Boot.
# How does caching work in Spring Boot?
# How does Spring Boot handle asynchronous tasks?
# Explain the use of DevTools in Spring Boot.

10. JUnit & Testing
# What is JUnit, and why is it used?
# Explain the difference between unit testing and integration testing.
# How do you write a simple JUnit test case?
# What is the purpose of the @Test annotation?
# How do you handle exceptions in JUnit tests?
# What is the role of the assert methods in JUnit?
# Explain the difference between @BeforeEach and @BeforeAll.
# What is the difference between @AfterEach and @AfterAll?
# How do you test a method that returns void?
# What is parameterized testing in JUnit?
# How do you create a custom test suite in JUnit?
# How does JUnit handle assertions for collections?
# What is the purpose of @Mock and @InjectMocks in JUnit?
# How do you use Mockito in JUnit?
# How do you test private methods in JUnit?