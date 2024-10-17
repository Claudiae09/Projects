"""
The SimUDuck App - Strategy Design Pattern
Joe works for a company that makes a highly successful duck
pond simulation game, SimUDuck. The game can show a large
variety of duck species swimming and making quacking sounds.
"""
###############################################################################
# Ducks
###############################################################################
# Abstract class Duck
class Duck:
    fly_behavior = None
    quack_behavior = None

    def display(self):
        pass

    def fly(self):
    #TODO: implement this method

    def quack(self):
    # TODO: implement this method
    # TODO: write the set_quack_behavior method
    # TODO: write the set_fly_behavior method

    def swim(self):
    print("All ducks float, even decoys!!")

class MallardDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")

class DecoyDuck(Duck):
    # TODO: write the init method
    # TODO: write the display method

class RubberDuck(Duck):
    # TODO: write the init method
    # TODO: write the display method

class RedHeadDuck(Duck):
    # TODO: write the init method
    # TODO: write the display method
    # TODO: write the ModelDuck class

###############################################################################
# Quack behaviors

###############################################################################

class QuackBehavior:
    def quack(self):

        pass


class Quack(QuackBehavior):
    def quack(self):

        print("Quack")


# TODO: write the MuteQuack class
# TODO: write the Squeak class
# TODO: write the FakeQuack class
###############################################################################
# Fly behaviors
###############################################################################
class FlyBehavior():
    def fly(self):

        pass


class FlyWithWings(FlyBehavior):
    def fly(self):

        print("I'm flying!!")


# TODO: write the FlyNoWay class
# TODO: write the FlyRocketPowered class
if __name__ == '__main__':
    # TODO: instantiate an object of MallardDuck
    mallard = MallardDuck()
    mallard.fly()
# TODO: instantiate an object of RedHeadDuck
    redduck = RedHeadDuck()
    redduck.fly()
# TODO: instantiate an object of ModelDuck
    model = ModelDuck()
    model.fly()
    model.set_fly_behavior(FlyBehavior())
    model.fly()
    model.swim()
    model.display()
"""
References:
This lecture was designed by Dr Gregory Reis based on the book
Elisabeth Freeman, Eric Freeman, Bert Bates, and Kathy Sierra. 2004
Head First Design Patterns. O' Reilly & Associates, Inc.,
Dr Kip Irvine's class notes, and using the simuduck.py written
by Miguel Alba and modified by Dr Gregory Reis
"""
