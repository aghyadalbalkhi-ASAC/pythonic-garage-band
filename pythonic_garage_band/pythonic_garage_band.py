from abc import abstractmethod, ABC

class Band(ABC):

    all_bands=[]

    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.all_bands.append(self)

    def play_solos(self):
        solos=[]
        if len(self.members) != 0:
            for i in self.members:
                # access each member and run  the play solo function
                solos.append(i.play_solo())
            return solos
        else:
            return 'There is No Members in This Band'
        
    def __str__(self):
        return f'The Band Name {self.name}  Members are : {self.members}'.strip()

    def __repr__(self):
        return  f'The Band Name {self.name}  Members are : {self.members}'.strip()

    @classmethod
    def to_list(cls):
        return cls.all_bands


class Musician(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo (self):
        pass

    def __str__(self):
        
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__(self):
        
        return f'{self.__class__.__name__} instance. Name = {self.name}'       

    
class Guitarist(Musician):

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

    # def __repr__(self):
    #     return f' Guitarist instance. Name = {self.name}.'
class Bassist(Musician):

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


if __name__ == "__main__":
    x = Guitarist("aghayad")
    b = Bassist("hadeel")
    c = Drummer("joudi")

    ASAC_Band = Band('ASAC',[])
    print(ASAC_Band.to_list())