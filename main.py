class Patient:
    def __init__(self, ssn, dob, hin, first_name, last_name, address):
        self.__dob = dob
        self.__ssn = ssn
        self.__hin = hin
        self.__first_name= first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def ssn(self):
        return self.__ssn

    @property
    def dob(self):
        return self.__dob
    
    @property
    def hin(self):
        return self.__hin
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string value for the address')
    



bubba = Patient(400440404, "09/22/1967", 1234567, "Bubba", "Gump", "11 1st street")

print(bubba.full_name)

