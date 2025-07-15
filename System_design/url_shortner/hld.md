# URL Shortner system.
# HLD
1. Tech stack
- Angular, Springboot, mongoDB.
2. API layer.
 - POST /shorten
 - GET /:shortCode

3. Short code generator.
 - Base62 Enconding
 - Hashing
 - Autoincreament ID + Base62 for predictability

4. Database design.
 - table - urls

5. Load balancer.
 - active mq.
 
# LLD