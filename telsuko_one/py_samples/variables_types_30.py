class Car:
    weels = 4

    def __init__(self):
        self.color = "Red"
        self.brand = "BMW"
        self.mil = 10
        # Car.weels =6

def main():
    c1 = Car()
    c2 = Car()

    Car.weels = 6 # Update class variables
    c1.weels = 8  # Update instance variable

    print(c1.brand, c1.weels, c1.mil, c1.color)
    print(c2.brand, c2.weels, c2.mil, c2.color)

if __name__ =='__main__':
    main()