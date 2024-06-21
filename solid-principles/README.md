### Single Responsibility Principle (SRP)

A single class should always have one reason to change and should only serve one purpose. It encourages a class to be cohesive and only do one thing.

### Open Closed Principle (OCP)

Objects or entities should be open for extension but closed for modification, which means that you should be able to extend the behavior of a class without modifying its code.

### Liskov Substitution Principle (LSP)

Derived types must be completely substitutable for their base types, meaning replacing objects of a superclass with objects of its subclass should not break the application.

### Interface Segregation Principle (ISP)

Clients must not be forced to depend upon interfaces or methods they don't use. It suggests that large interfaces should be segregated into more specific ones so that clients only need to know about the methods that are of interest to them.

### Dependency Inversion Principle (DIP)

High-level modules/classes should not depend on low-level modules/classes. Both should rather depend on abstractions, and abstractions should not depend on details; rather, the details should depend on abstractions.

### Limitations/ Challenges:

    Increased Initial Complexity:
        Implementing SOLID principles can lead to a more complex initial design. This might involve creating additional classes and interfaces, which can make the codebase harder to understand for newcomers.

    Over-Engineering:
        There's a risk of over-engineering, especially for smaller projects where the overhead of applying these principles may not be justified. This can lead to unnecessary abstraction and complexity.

    More Code:
        Adhering to these principles often results in more code. More classes, more interfaces, and more boilerplate can increase the maintenance burden.

    Refactoring Effort:
        Applying SOLID principles to an existing codebase may require significant refactoring. This can be time-consuming and may introduce bugs if not done carefully.

    Performance Overhead:
        The additional layers of abstraction can introduce a performance overhead. While this is often negligible, it can be significant in performance-critical applications.

    Steep Learning Curve:
        Understanding and correctly applying SOLID principles requires a deep understanding of object-oriented design. This can be a steep learning curve for junior developers.
