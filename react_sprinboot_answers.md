37. What is the `@Configuration` annotation in Spring?
38. What is Spring Boot’s auto-configuration?
39. What are Spring Boot’s application properties?
40. How do you handle file uploads in Spring Boot?
41. How to enable and allow cors on spring boot application.
    @CrossOrigin(origins ='/')

## Full-Stack Development Topics:

### API Development and Integration:
1. What is RESTful API, and how is it used in full-stack applications?
2. What is the difference between REST and SOAP APIs?
3. How do you secure REST APIs using OAuth2?
4. How do you handle cross-origin resource sharing (CORS)?
5. What is JWT (JSON Web Token) and how is it used for authentication?
6. How do you integrate third-party APIs in a full-stack application?
7. How do you manage API versioning?

### Database and ORM:
1. What is the difference between SQL and NoSQL databases?
    1. SQL are relational(Foereign keys), and NoSQL are non relational.
    2. SQL supports JOINS/Cross table queries, NoSQL's are Hard to query such.
    3. Data mdoel - SQL are table rows and No relations are Mongo is Document and collection.
    4. Schema - SQL is fixed, No SQL is dynamic.

2. How does Hibernate ORM work in a Spring Boot application?
    1. Spring Boot automatically configures Hibernate as the JPA provider(comes from `spring-boot-starter-data-jpa`)
    2. Building Database Queries.
    3. Entity Mapping to map Java objects to db tables.
    4. Caching - Hibernate supports both `first-level` and `second-level` caching.

3. How do you handle database migrations in a Spring Boot application?
    1. Flyway - Create migration scripts and run spring boot app.
    2. LiquiBase - Create liquibase changelog.
    3. Use versioning(`v1.0, etc`) and rollbacks options on.

4. What are the advantages of using a relational database (e.g., MySQL) with Spring Boot?
    1. Natively supportd by JPA - `JpaRepository`.
    2. Structured Data Model.
        1. Schema-based design.
        2. Data Integrity.
    3. ACID Transactions.
    4. Strong Querying Capabilities with SQL(`SQLs` and `Joins`).
    5. Data Relationships and Foreign Key Constraints
    6. Scalability and Performance. (Horizontal scaling, Indexes).


5. What is JPA (Java Persistence API), and how does it relate to Hibernate?
    1. An Interface that provides inbuilt layer to connect to Databases with minimal configurations.
    2. Supports All crud operations and many more.
    3. Supported both on mongoDB `MongoRepository`, PostgreSQL `JpaRepository`.
    - For mongo/posgreSQL.
        1. Add mongodb/postgreSQL dependancy in pom.xml
        1. Add apllication properties.
        2. create Entity class `@Document(collection = "users")` / `@Entity` for Postgresql.

### Frontend Integration:
1. How do you integrate ReactJS with a Spring Boot backend?
    1. Use Axios or Fetch to make an API from react.
    1. Allow cors from react host to allow API's. `@RestController \n @CrossOrigin(origins = "http://localhost:3000")`
    2. Use JWT's for authentication and authorization.
    3. Try using same host for more security. `Nginx or Apache`
    4. Use websockets for realtime updates between client server.


2. What is the role of AJAX(`Asynchronous JavaScript and XML`) in full-stack development?
    **AJAX refers to any client-server communication that happens asynchronously and allows for partial page updates**
    1. Asynchronous Communication with the Server
    2. Fetching Data for Dynamic Rendering
    3. Form Submissions and Dynamic Interactions
    4. Real-Time Updates Using WebSockets (AJAX-like behavior)
    5. Handling Errors and Responses from the Server
    6. Security Considerations.

3. How do you secure your frontend (React) application?
    1. Use JWT's to make sure each API call is authenticated.
    2. Use Token refreshing to avoid token forgery.
    3. Store tokens in Cookies with `HttpOnly`, `Secure`, `sameSite` and `maxAge` flags.
    4. Secure routes.
    5. Validate each API for JWT on Server side.

4. What are the best practices for state management in React for full-stack applications?
    1. **useState** for simple local state - Local states only.
    2. **useReducer** - for complex state logic - nested objects. Local states only.
    3. **useContext** - provides global state - not much frequent change in state is needed.
    4. **Redux** - External library, good with complex states - middleware support for API calls and caching - ideal for large scale application.
    5. `React.memo`(for functional components), `useMemo` and `useCallback` for memoizing.

5. How do you optimize the performance of full-stack web applications?
    # How to find out what's causing performance issue.
    1. Use profiling tools on client, server, db side.
    2. Check for network tab for API's taking longer times.
    3. Check for non-closed Socket connections.
    
    # Remedies
    1. Use Parallel Asynchronous Programming(multithreading in Java) wherever possible.
    2. Use Client Side and Server side caching, use meoisation techniques and hooks provided by reactjs.
    3. Use DSA Techniques to optimise runtime of heavy logics and optimal space.
    4. Use Pagination API's for pages having lot's of data to load.(React and Spring boot supports pagination API's)
    5. Make sure all connections are closed on component death to avoid memory leackage.
    6. Add indexes on SQL tables.
    7. Use Leader/(Master)-Follower architecture archetecture for separate read write servers.
    8. Use sharding and Partitioning.


