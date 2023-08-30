def call_internal(func):
    def wrapper(self, *args, **kwargs):
        # call the original method and store its result
        result = func(self, *args, **kwargs)
        # call the internal method after the original method
        self._internal_method()
        # return the result of the original method
        return result
    return wrapper


class MyClass:
    def __init__(self):
        self._value = 0

    def _internal_method(self):
        # do something internal
        print("Internal method called")

    @call_internal
    def increment(self):
        # increment the value by 1
        self._value += 1
        print(f"Value is now {self._value}")

    @call_internal
    def decrement(self):
        # decrement the value by 1
        self._value -= 1
        print(f"Value is now {self._value}")


# Create an instance of MyClass
obj = MyClass()

# Call methods and see the after-method behavior
obj.increment()
obj.decrement()
