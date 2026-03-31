class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return 'Dog says Bark!'

class Cat(Animal):
    def speak(self):
        return 'Cat says Meow!'
    
def main():
    cat1 = Animal()
    dog1 = Dog()

    animals = [cat1, dog1]

    for animal in animals:
        print(animal.speak())

if __name__ == '__main__':
    main()