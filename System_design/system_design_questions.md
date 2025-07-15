## System Design Questions
1. [How would you design a system to handle **10M reads/sec** with low latency?](#q1)
2. [How do you ensure **data consistency** across distributed databases?](#q2)
3. How would you design a system to store and retrieve user sessions efficiently?
4. How do you handle cache invalidation in a large-scale caching system?
5. How would you design an API rate limiter for thousands of users?
6. How can you design a fault-tolerant message queue?
7. How would you design a system to upload and process large files asynchronously?
8. How do you approach scaling a relational database when writes increase dramatically?
9. How would you design a recommendation engine that updates in real-time?
10. How do you ensure secure and scalable authentication in a microservices architecture?

# Answers
1. How would you design a system to handle **10M reads/sec** with low latency?{#q1}
 - Create `read replicas` (Estimate number needed to support 10M reads/sec).
   - Assuming 50,000 (reads/sec)/replica ->  ~260 read replicas (including buffer and failover margin).
 - Use `regional` or `language-based shards` to reduce latency via geographic proximity.
 - Implement `internal and external caching` (e.g., Redis, CDN) for frequently accessed queries.
 - Use appropriate `indexes` to reduce DB query time.
 - Use `load balancers` to evenly distribute traffic across replicas and nodes.
 - Choose high-read-throughput DBs like `Cassandra` for massive scale.
 - Consider `CDNs` to serve static or precomputed content closer to users.
 - Use `pre-computed views` or `denormalized data` for heavy, repeated queries.
 - Enable `auto-scaling` for read replicas or stateless services to handle traffic spikes efficiently.

2. How do you ensure **data consistency** across distributed databases?{#q2}
 - `Data Uniqueness`: Ensuring that each record exists only in one shard or partition to avoid duplication and conflicts.
 - `Consistent Hashing`: Using a consistent and uniform hashing algorithm to distribute data evenly and ensure predictable placement across shards.
 - `Replication and Synchronization`: Data is replicated across nodes, and synchronization protocols like two-phase commit or consensus algorithms (Paxos, Raft) are used to ensure all replicas agree on the data state.
 - `Consistency Models`: Depending on system requirements, databases may implement strong consistency (all nodes see the same data immediately) or eventual consistency (nodes converge over time).
 - `Conflict Resolution`: Mechanisms like vector clocks or timestamps help detect conflicts, which are resolved through predefined rules or reconciliation processes.
 - `Consensus Algorithms`: Protocols such as Paxos or Raft are used to achieve agreement among distributed nodes.
 - `Versioning`: Tracking data changes with timestamps or version numbers to maintain order and resolve conflicts.
 - `Practical examples`: Distributed databases like Google Spanner use global timestamps to maintain strong consistency, while Cassandra uses eventual consistency with tunable consistency levels.