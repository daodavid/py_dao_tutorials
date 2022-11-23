# setAttr.py
class StudentID:
    def __init__(self, id, name, age = "30"):
        self.id = id
        self.firstName = name
        self.age = age

    # all the init parameters need to be specified in 'setattr'
    def __setattr__(self, name, value):
        if(name == "id"): # setting id
            if isinstance(value, int) and value > 0 :
                self.__dict__["id"] = value
            else:
                # print("Id must be positive integer")
                raise TypeError("Id must be positive integer")
        elif (name == "firstName"): # setting firstName
            self.__dict__["firstName"] = value
        else: # setting age
            self.__dict__[name] = value

    # getattr is executed, when attribute is not found in dictionary
    def __getattr__(self, name):
        raise AttributeError("Attribute does not exist")

def main():
    s1 = StudentID(1, "Meher")
    print(s1.id, s1.firstName, s1.age) # 1 Meher 30

    ## uncomment below line to see the "TypeError" generated by 'setattr'
    # s2 = StudentID(-1, "Krishna", 28)
    """
    Traceback (most recent call last):
    [...]
    raise TypeError("Id must be positive integer")
    """

    s3 = StudentID(1, "Krishna", 28)
    print(s3.id, s3.firstName, s3.age) # 1 Krishna 28

    ## uncomment below line to see the "AttributeError" generated by 'getattr'
    # print(s3.lastName) # following message will be displayed
    """ Traceback (most recent call last):
        [...]
        AttributeError: Attribute does not exist
    """
# standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()