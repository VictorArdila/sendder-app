# Clase Recipient
class Recipient:
    def __init__(self, fullName: str, company: str, street: str, neighborhood: str, city: str,state: str, country: str, postalCode: str, phones: list[str]):
        self.__fullName = fullName
        self.__company = company
        self.__street = street
        self.__neighborhood = neighborhood
        self.__city = city
        self.__state = state
        self.__country = country
        self.__postalCode = postalCode
        self.__phones = phones

    def getFullName(self) -> str:
        return self.__fullName

    def setFullName(self, fullName: str):
        self.__fullName = fullName

    def getCompany(self) -> str:
        return self.__company

    def setCompany(self, company: str):
        self.__company = company

    def getStreet(self) -> str:
        return self.__street

    def setStreet(self, street: str):
        self.__street = street

    def getNeighborhood(self) -> str:
        return self.__neighborhood

    def setNeighborhood(self, neighborhood: str):
        self.__neighborhood = neighborhood

    def getCity(self) -> str:
        return self.__city

    def setCity(self, city: str):
        self.__city = city

    def getState(self) -> str:
        return self.__state

    def setState(self, state: str):
        self.__state = state

    def getCountry(self) -> str:
        return self.__country

    def setCountry(self, country: str):
        self.__country = country

    def getPostalCode(self) -> str:
        return self.__postalCode

    def setPostalCode(self, postalCode: str):
        self.__postalCode = postalCode

    def getPhones(self) -> list[str]:
        return self.__phones

    def setPhones(self, phones: list[str]):
        self.__phones = phones

    def toJson(self):
            return {
                "full_name": self.__fullName,
                "company": self.__company,
                "street": self.__street,
                "neighborhood": self.__neighborhood,
                "city": self.__city,
                "state": self.__state,
                "country": self.__country,
                "postal_code": self.__postalCode,
                "phones": self.__phones
            }

    @staticmethod
    def fromJson(data):
        recipient = Recipient(
            data.get('full_name'),
            data.get('company'),
            data.get('street'),
            data.get('neighborhood'),
            data.get('city'),
            data.get('state'),
            data.get('country'),
            data.get('postal_code'),
            data.get('phones')
        )
        return recipient
    