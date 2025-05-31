HLD
- Flow Diagrams
- Block Diagrams
- Tech Stack
- High-Level Security and Compliance Considerations
- Scalability and High Availability
- Deployment Architecture

LLD
Database - 
Tables - 
1. Users
 a. userId - ObjectId (PK)
 b. Name - varchar(50)
 c. email - varchar(50)
 d. passwordHash
 e. createdAt
 f. updatedAt

2. Transactions
 a. transactionId (PK)
 b. userId - ObjectId(FK)
 c. transactionDate - Date
 d. isDebt - boolean
 e. amount - decimal
 f. createdAt
 h. createdBy

3. Groups.
 a. groupId - ObjectId - (PK)
 b. groupName - NVARCHAR(50)
 c. userId - ObjectId - (FK)
 d. createdAt
 g. updatedAt

Service - 
Endponits - 
1. register user - POST - User object - return userId (No need in system design interview)
2. Add Transaction - POST - Transaction array - Data validation - return Transaction Id.
3. Settle up - POST - Validation - return success message.
4. Get latest report(All for user / by group / by expense ID) - GET - pagination support.
5. Create new group.
6. Exit group.
7. Remove user from group.

Events
1. Settle up.
2. Expense added.
3. Added to group.

UI - 
Screens - 
1. register user.(No need in system design interview)
    a. name
    b. email
    c. password
    
2. Add expense.
    a. payer.
    b. people who borrowed money.
    c. Split percentage per person.
    d. exclude me option.

3. Settle up.
    a. amount to settle.
    b. settle button.

4. Home screen (List of all groups/non group expenses)
    a. group Icon.
    b. Group name/non group name.
    c. amount owes/to receive.

5. Expenses grid for specific group / non group.
    a. expense name.
    b. how much you owe/to receive.

6. Expense details.
    a. Expense name.
    b. Payer.
    c. People who borrowed money and how much each.

7. Create new group.
    a. name of group.
    b. members list.