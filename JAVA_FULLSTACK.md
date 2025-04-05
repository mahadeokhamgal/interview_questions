- How do you handle file uploads in spring boot.
    ``
    ```java
    //using post API, 
    @PostMapping(value = "/upload", consumes = "multipart/form-data")
    public ResponseEntity<String> uploadFile(@RequsetParam("file") MultiPartFile file) {
        try {
            String fileName = file.getOriginalFilename();

            file.transferTo(new File("C:\\uploads\\" + fileName));

            return ResponseEntity.ok("File uploaded successFully");
        } catch(IOException e) {
            return ResponseEntity.status(500).body("File upload failed: " + e.getMessage());
        }
    }
    ```
- Why would you choose Spring Boot over the traditional Spring Framework?
    - Has inbuilt production grade features. (`health checks, metrics, application monitoring`)
    - Has embedded server Tomcat which makes app ready deploy in no time.
    - Uses spring initialisers to speed up developement.
    - Minimal configuration to create Endpoints.
    - autoconfigurations.
    - Microservices Support.
    - Profiles for Environment Management.
    - Testing Support.
    - Spring security.

- Which Spring Boot starters or modules have you worked with in your projects?
    1. spring-boot-starter-web
    2. spring-boot-starter-security
    3. spring-boot-starter-jpa
    4. spring-boot-starter-data-mongodb
    5. spring-boot-starter-actuator
    6. spring-boot-starter-validation
    7. spring-boot-starter-test

- How do you launch a Spring Boot application?
    1. manually - `mvn spring-boot:run`
    2. in intellij/vs code, in @SpringBootApplication class click on run.
    3. can do using manually creating build jar and then executing(e.g. for prod).
        1. mvn clean package -DskipTests
        2. then copy jar to your destination
        3. java -jar your-application-name.jar
-How to use jwt in Spring boot
    1. add dependacies in pom.
    - jjwt-api
    - jjwt-impl <scope>runtime</scope>
    - jjwt-jackson
    2. on login route create jwt token using, headers, object and secrete key, and send this jwt in response.

- What is the role of the `@SpringBootApplication` annotation in a Spring Boot project?
    1. @EnableAutoConfiguration
    2. @ComponentScan
    3. @Configuration - Marks class as configuration class that can contain spring beans.

- Can you replace the `@SpringBootApplication` annotation with `@EnableAutoConfiguration`, `@ComponentScan`, and `@Configuration`? If so, would the application behave the same way?
    - `Yes we can replace it. However, the behavior may not be exactly the same unless you make sure to explicitly define the scanning path in @ComponentScan and configure the auto-configuration properly. In general, @SpringBootApplication simplifies this setup by combining these annotations and providing sensible defaults.`
    - @ComponentScan(basePackages = "com.example")
    - @Configuration
    - @EnableAutoConfiguration

- What is auto-configuration in Spring Boot, and how does it work?
    - auto-configuration is a mechanism that Spring Boot uses to automatically configure beans and application settings based on the project's classpath and dependencies. `@EnableAutoConfiguration`
    - Auto-configuration automatically configures Spring beans based on the libraries and properties available in the application, helping developers avoid explicit configuration and making the setup process easier and faster.

    - e.g. if you used `spring-boot-starter-web` as dependancy then project use `tomcat` as default server unless configured something else manually.

- How can you disable a specific auto-configuration in Spring Boot?
    1. Using @EnableAutoConfiguration with exclude Attribute.
    - @EnableAutoConfiguration(exclude = {TomcatAutoConfiguration.class}).
    2. Using application.properties or application.yml to Disable Specific Auto-Configurations.
    - spring.main.web-application-type=none.
    3. Using @SpringBootApplication with exclude Attribute.
    - @SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
    4. Disabling Auto-Configuration via Command-Line Arguments.

- How do you override the default configurations in Spring Boot?
    1. Override Default Properties in application.properties or application.yml.
    - server.port=9090
    - spring.datasource.url=jdbc:mysql://localhost:3306/mydb
    - spring.datasource.username=myuser
    - spring.datasource.password=mypassword

- What happens behind the scenes when the `run()` method is invoked in Spring Boot?
    1. SpringApplication Initialization.
    2. Creating the ApplicationContext (IOC)
    3. Setting up the Environment.
    4. Starting the Spring Context (Context Initialization).
        - Scans the classpath for components, services, controllers, repositories, etc., defined by annotations like @Component, @Service, @Repository, @Controller, and so on.
        - Automatically wires these beans by resolving their dependencies using dependency injection
    5. Handling Auto-Configuration.
    6. ApplicationListeners and ApplicationEventPublisher.
    7. Running the Embedded Web Server (For Web Applications).

- What is the purpose of a command-line runner in Spring Boot?
    `In Spring Boot, a CommandLineRunner is a functional interface that can be used to execute code at startup, immediately after the Spring application context has been initialized and the application has been fully configured. The primary purpose of a CommandLineRunner is to provide a way to execute tasks or logic when the application starts, such as loading initial data, performing initialization tasks, or running background jobs.`

- Can you describe the purpose of Stereotype annotations in Spring?
    `In Spring Framework, stereotype annotations are special types of annotations that are used to define Spring-managed beans and mark a class as a specific type of Spring component. These annotations are essentially shorthand for defining beans and help Spring to automatically detect and register beans in the Spring ApplicationContext through component scanning.`
    - @Component: A generic annotation for any Spring-managed bean.
    - @Service: Specialization of @Component for service layer beans.
    - @Repository: Specialization of @Component for DAO classes with additional persistence-related behavior.
    - @Controller: Specialization of @Component for Spring MVC controllers in web applications.
    - @RestController: Specialization of @Controller for REST API controllers that automatically handle responses as JSON or XML.

- How do you declare a bean in the Spring Framework?
    1. Using Annotations (@Component, @Service, @Repository, @Controller).
    2. Using Java Config (@Configuration and @Bean).
    3. Using XML Configuration (Traditional Spring)
    4. Using @Import to Import Configuration Classes

- What is dependency injection, and why is it important?
    - dependancy injection is centreal part of spring boot which is used to manage beans and their instances and make those accessible anywhere in application.
    - it uses IOC to manage dependancies.
    *Why important* -
    `this is important to not needing to manage objects manually and creating object in every class, rather DI enables classes to access beans from ioc directly.` 
    - Decoupling of Components
    - Simplifies Unit Testing
    - Improved Maintainability
    - Centralized Object Creation
    - Easier Configuration and Setup
    - Improves Flexibility and Extensibility

- What are the different ways to implement dependency injection in Spring and Spring Boot?
    - can inject dependancy using.
        1. @Autowired.
        2. Contructor injection.
        3. Setter Injection.

- What is Spring Boot dependency management?
    `Spring Boot Dependency Management is a feature in Spring Boot that simplifies the process of managing dependencies (external libraries or modules) in your application. It automatically handles the configuration of dependencies and their versions, ensuring that your project remains consistent, up-to-date, and conflict-free.`
    1. Dependency Management with Spring Boot Starter POMs:
    2. Spring Boot Dependency Version Management:
    3. Transitive Dependencies:
    4. Excluding Transitive Dependencies:
    5. Spring Boot BOM (Bill of Materials):
    6. Customizing Dependency Versions:

- Is it possible to change the port of the embedded Tomcat server in Spring Boot?
    - Yes it is possible to change the default port.
    - can change in application.properties, `application.port: 9002` or Command-Line Arguments `java -jar myapplication.jar --server.port=9002`

- What is the starter dependency of the Spring Boot module?
    `In Spring Boot, starter dependencies are a set of pre-configured, commonly used dependencies grouped together to help you quickly get started with different functionalities or modules without needing to manually configure each individual dependency. These starters simplify adding functionality to your application by grouping related dependencies into a single artifact.`

- What is the default port of Tomcat in Spring Boot?
    - 8080

- Can we disable the default web server in the Spring Boot application?
    
- How do you disable a specific auto-configuration class?
- Can we create a non-web application in Spring Boot?
- Describe the flow of HTTPS requests through the Spring Boot application.

Practical.

1. Write java code to find elements that occur only once in array.
2. Create Angular app that'll have Image and reset button, on click of reset button the image should be updated.(use "https://dog.ceo/api/breeds/image/random")
3. Write a Controller in Java that'll get API from URl in format, /<id>?name=<name> and return dynamic object as  resonse -> {id: <id>, name: <name>}