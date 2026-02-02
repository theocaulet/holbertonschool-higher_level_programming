0. Abstract Animal Class and its Subclasses
Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.
1. Shapes, Interfaces, and Duck Typing
Create an abstract class named Shape with two abstract methods: area and perimeter.
Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class should provide implementations for the area and perimeter methods.
Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
Test the shape_info function with instances of both Circle and Rectangle.
2. Extending the Python List with Notifications
Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).
3. CountedIterator - Keeping Track of Iteration
Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.
4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Construct a FlyingFish class that inherits from both a Fish class and a Bird class. Within FlyingFish, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.
5. The Mystical Dragon - Mastering Mixins
Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively. Next, construct a class Dragon that inherits from both these mixins. Your aim is to show that a Dragon instance can both swim and fly.