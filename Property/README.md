# Property Method

Property methods in Python are a way to define methods in a class that act like attributes. They are used to manage the attributes of a class and control access to them, providing a way to get, set, and delete attributes with custom behavior while maintaining the syntax of regular attribute access.

## Basics of Property Methods

In Python, properties are defined using the property decorator or the property() function. They allow you to define methods that can be accessed like attributes. This helps encapsulate and control access to an object's data while preserving a clean and intuitive interface.

## Why Use Property Methods?

- Encapsulation: Allows you to control access to private data attributes.

- Validation: Enables validation of data before setting it.

- Computed Properties: Allows you to define properties that are computed dynamically rather than stored.

- Backward Compatibility: Allows you to change the internal representation of data without changing the public interface.

## Defining Property Methods

Using the property Decorator
You can define a property using the property decorator in conjunction with getter, setter, and deleter methods. Here’s a detailed breakdown:

1. Getter Method: Used to retrieve the value of a property.
2. Setter Method: Used to set the value of a property.
3. Deleter Method: Used to delete a property (optional).
