1. Java Basics & Fundamentals
# What is the difference between JDK, JRE, JVM, and bytecode?
# Why is Java platform independent?
# Explain System.out.println().
# What is the String pool in Java?
# What is the difference between String, StringBuilder, and StringBuffer?
# What is the difference between a class and an interface?
# What is the difference between an abstract class and an interface?

2. OOP Concepts
# What are the OOP pillars in Java?
# Explain OOP pillars with examples.
# What are the types of inheritance in Java?
# How is multiple inheritance achieved in Java?
# What is the Diamond Problem in interfaces?
# What is the difference between compile-time and runtime polymorphism?

3. Memory Management & Keywords
# How does garbage collection work in Java?
# What is the difference between final, finally, and finalize()?
# What is the significance of the static keyword?
# What is a volatile variable in Java?
# What is the use of the transient keyword?
# How does the Java memory model work?

4. Collections & Data Structures
# How does HashMap work internally in Java?
# What is the difference between ArrayList and LinkedList?
# What is the Collections framework in Java?
# How does the Comparator interface work?
# How are generics used in Java?

5. Exception Handling & Annotations
# What is the difference between checked and unchecked exceptions?
# How are exceptions handled in Java?
# Explain how try-with-resources works in Java.
# Explain equals() and hashCode() methods.
# What is the difference between == and .equals()?
# How does reflection work in Java?
# What are annotations, and how are they used in Java?

6. Multithreading & Concurrency
# Explain the concept of multithreading and the Thread lifecycle.
# How to achieve multithreading in Java?
# How does synchronized work in Java?
# What is the purpose of the super keyword?
# How does CompletableFuture work in Java?
# How do you implement parallel streams?

7. Java 8 & Beyond
# What are the new features introduced in Java 8?
# What are the differences between Java 8 and Java 11 features?
# Explain the concept of lambda expressions in Java 11.
# What is a functional interface? Give an example.
# Explain the concept of the @FunctionalInterface annotation.
# What is the purpose of the Optional class?
# Explain the concept of default and static methods in interfaces.
# How do streams work in Java?
# What is the difference between intermediate and terminal stream operations?
# Explain the use of the map and flatMap methods in streams.
# How is method reference used in Java?
# Explain the purpose of the Collectors utility class.
# What is the difference between forEach() and map() in streams?
# How do you sort a list using streams?
# What is the Predicate functional interface?
# What is the BiConsumer functional interface?
# How does the Collectors.toMap() method work?
# What is a Spliterator?
# What is the difference between reduce() and collect() in streams?
# What is the purpose of the LocalDate and LocalTime classes in Java 8?
# How does the Instant class differ from Date?
# What is the difference between Stream.findAny() and Stream.findFirst()?

8. Database Connectivity
# What are the steps for MySQL connection with Java?

9. Coding Challenges
# Write Java code to find elements that occur only once in an array.

10. `Logical questions.`

# Given a string, return the first character that does not repeat. Use Java Streams in your solution.
Input: "swiss"
Output: "w"
```java
IP.chars()
.mapToObj(c -> (char) c)
.filter(c -> IP.indexOf(c) == IP.lastIndexOf(c))
.findFirst()
.orElse('\0');
```

# Group Words by Their Length. Use Java Streams in your solution.
Input: ["apple", "bat", "cat", "banana", "dog"]
Output: {3=[bat, cat, dog], 5=[apple], 6=[banana]}
```java
public static Map<Integer, List<String>> groupByLength(String[] IP) {
  return 
    Arrays.stream(IP)
    .collect(Collectors.groupingBy(String::length));
}
```

# Find Duplicate Elements in an Array. Use Java Streams in your solution.
Input: [1,2,3,2,4,5,1,6]
Output: [1, 2]
```java
public static List<Integer> getDuplicates(int[] IP) {
    return
        Arrays.stream(IP)
        .boxed()
        .collect(Collectors.groupingBy(e -> e, Collectors.counting()))
        .entrySet()
        .stream()
        .filter(e -> e.getValue() > 1)
        .map(Map.Entry::getKey)
        .collect(Collectors.toList());
}
```

# Find the Kth Largest Element in an Array. Use Java Streams in your solution.
Input: [3,2,1,5,6,4], k=2
Output: 5

# Employee Salary Problem. Use Java Streams in your solution.
You have a list of employees (id, name, department, salary). Using Streams:
 - Find the highest-paid employee in each department.
 - Sort employees by salary in descending order.
 - Find the average salary of the company.

# Given a list of integers, how would you use streams to count how many numbers are even and greater than 10?
IP = [5, 12, 18, 7, 20, 3, 10];
OP = 3;  //[12, 18, 20]
```java
public static int getCountEvenAndGT10(int[] IP) {
  return (int) Arrays
  .stream(IP)
  .boxed()
  .filter(e -> e%2 == 0 && e > 10)
  .count();
}
```

# Given a list of strings, convert all strings to uppercase and collect only those that start with the letter 'A'.
IP = ["apple", "banana", "avocado", "berry", "apricot"]
OP = ["APPLE", "AVOCADO", "APRICOT"]
```java
public static List<String> getAllACaps(String[] IP) {
  return
  Arrays.stream(IP)
  .filter(w -> w.startsWith("A") || w.startsWith("a"))
  .map(String::toUpperCase)
  .collect(Collectors.toCollection(ArrayList::new));
}
```

# Given a list of strings, group them by their first character using streams.
IP = ["Alice", "Arnold", "Bob", "Brian", "Charlie"];
OP = {
  A=[Alice, Arnold],
  B=[Bob, Brian],
  C=[Charlie]
}
```java
public static Map<Character, List<String>> groupByFirstChar(String[] IP) {
  return
  Arrays.stream(IP)
  .collect(Collectors.groupingBy(s -> s.charAt(0)));
}
```

# Given a list of strings, find the first element that is longer than 5 characters and contains the letter 'e'.
IP = "pen", "notebook", "eraser", "book", "pencil"
OP = notebook
```java
public static String firstLongerThan5nWithE(String[] IP) {
  return
    Arrays.stream(IP)
    .filter(e -> e.length() > 5 && e.toLowerCase().indexOf('e') > -1)
    .findFirst()
    .orElse(null);
}
```
# Given a list of names and a corresponding list of ages, use streams to map them into a list of Person objects.
IP = class Person {
    String name;
    int age;
    // Constructor, getters, setters
}
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
List<Integer> ages = Arrays.asList(25, 30, 35);

OP = A list of Person objects:
Alice (25)
Bob (30)
Charlie (35)
```java
List<Person> personObjList = 
    IntStream.range(0, Math.min(names.size(), ages.size()))
      .mapToObj(i -> new Main().new Person(names.get(i), ages.get(i)))
      .collect(Collectors.toList());
```

11. Java GTO.
```java
//1
public class Test1 {
    public static void main(String[] args) {
        String s1 = "hello";
        String s2 = new String("hello");
        System.out.println(s1 == s2);
        System.out.println(s1.equals(s2));
    }
}

//2
public class Test2 {
    public static void main(String[] args) {
        Integer a = 100;
        Integer b = 100;
        Integer c = 200;
        Integer d = 200;
        System.out.println(a == b);
        System.out.println(c == d);
    }
}

//3
public class Test3 {
    public static void main(String[] args) {
        double d1 = 0.1 + 0.2;
        System.out.println(d1 == 0.3);
    }
}

//4
public class Test4 {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.print(i);
            i++;
        }
    }
}

//5
public class Test5 {
    public static void main(String[] args) {
        int x = 5;
        System.out.println(x++ + ++x);
    }
}

//6
public class Test6 {
    public static void main(String[] args) {
        print(null);
    }
    static void print(Object o) { System.out.println("Object"); }
    static void print(String s) { System.out.println("String"); }
}

//7
public class Test7 {
    public static void main(String[] args) {
        try {
            throw new RuntimeException("try");
        } finally {
            throw new RuntimeException("finally");
        }
    }
}


//8
public class Test8 {
    public static void main(String[] args) {
        int[] arr = new int[5];
        System.out.println(arr[0]);
        System.out.println(arr[5]);
    }
}

//9
public class Test9 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("abc");
        System.out.println(sb.reverse().reverse());
    }
}


//10
public class Test10 {
    static { System.out.println("static block"); }
    public static void main(String[] args) {
        System.out.println("main");
    }
}


//11
class A {
    static void show() { System.out.println("A"); }
}
class B extends A {
    static void show() { System.out.println("B"); }
}
public class Test11 {
    public static void main(String[] args) {
        A obj = new B();
        obj.show();
    }
}


//12
public class Test12 {
    public static void main(String[] args) {
        Integer x = null;
        int y = x;
        System.out.println(y);
    }
}


//13
public class Test13 {
    public static void main(String[] args) {
        System.out.println("Result: " + 1 + 2);
        System.out.println(1 + 2 + "Result");
    }
}

//14
public class Test14 {
    public static void main(String[] args) {
        String s = "ONE";
        switch (s.toLowerCase()) {
            case "one": System.out.println("one"); break;
            case "two": System.out.println("two"); break;
            default: System.out.println("default");
        }
    }
}

//15
interface I {
    static void hello() { System.out.println("Hello from I"); }
}
public class Test15 {
    public static void main(String[] args) {
        I.hello();
    }
}

//16
public class Test16 {
    public static void main(String[] args) {
        String s = null;
        System.out.println(s + "test");
        System.out.println(s.concat("test"));
    }
}

//17
public class Test17 {
    public static void main(String[] args) {
        print(10);
    }
    static void print(int i) { System.out.println("int"); }
    static void print(Integer i) { System.out.println("Integer"); }
    static void print(Object o) { System.out.println("Object"); }
}

//18
public class Test18 {
    public static void main(String[] args) {
        print(null);
    }
    static void print(String... s) { System.out.println("varargs"); }
    static void print(String[] s) { System.out.println("array"); }
}

//19
import java.util.*;
public class Test19 {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put(null, "first");
        map.put(null, "second");
        System.out.println(map.size());
        System.out.println(map.get(null));
    }
}

//20
public class Test20 {
    public static void main(String[] args) {
        Thread t = new Thread(() -> System.out.println("running"));
        t.start();
        t.start();
    }
}

```