    """
    Refer: https://javapapers.com/design-patterns/flyweight-design-pattern/

    Flyweight is used when there is a need to create high number of objects of almost similar nature. 
    High number of objects consumes high memory and flyweight design pattern gives a solution to reduce the load on memory by sharing objects.
     It is achieved by segregating object properties into two types intrinsic and extrinsic.

     Example:
     ---------
     example of text editors in their book. 
     If we create an object for every character in a file, think of it how many objects we will create for a long document. What will be the application performance
    """