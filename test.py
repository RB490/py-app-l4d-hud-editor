class HudDescriptions:
    def read_from_disk(self):
        print("Reading descriptions from disk...")


class Hud:
    def __init__(self):
        self.hud = {}
        self.desc = HudDescriptions()

    def some_method(self):
        # Note that we're trying to call read_from_disk() here
        self.desc.read_from_disk2()


# Scenario 1: Everything works fine since HudDescriptions has a read_from_disk() method
my_hud = Hud()
my_hud.some_method()  # "Reading descriptions from disk..." gets printed


class AnotherClass:
    pass


# Scenario 2: AttributeError is raised since AnotherClass doesn't have a read_from_disk() method
my_hud.hud["desc"] = AnotherClass()
my_hud.some_method()  # AttributeError: 'AnotherClass' object has no attribute 'read_from_disk'
