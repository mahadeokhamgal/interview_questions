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

10. Java GTO.
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