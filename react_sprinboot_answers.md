### Frontend Integration:
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
