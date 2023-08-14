class ParentClass:
    def __init__(self, value):
        self.value = value


class Subclass(ParentClass):
    pass


# Creating instances of the subclasses
instance = Subclass("Hello")

print(instance.value)  # Outputs: Hello
