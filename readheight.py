class convert:
    def __init__(self,cm):
        self.cm=cm
    def toInch(self):
        self.inches=0.394*self.cm
        print("The length in inches:",round(self.inches,2))
    def toFeet (self):
        self.feet=0.0328*self.cm
        print("The length in feet:",round(self.feet,2))  

def main():
    cm=int(input("Enter the height in centimeters:"))
    convert1=convert(cm)
    convert1.toInch()
    convert1.toFeet()

if __name__ == "__main__":
    main()
