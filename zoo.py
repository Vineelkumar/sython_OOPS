class Animal:
    sound = "Buck Buck"
    food_increase = 12
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months = age_in_months
        
        self._breed = breed
        
        if required_food_in_kgs > 0:
            self._required_food_in_kgs = required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.food_increase
        
class LandAnimals:
    @classmethod
    def breathe(cls):
        print("Breathe in air")

class WaterAnimals:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")

class HuntingAnimals:
    animal_sound = "Buck Buck"
    jantu = "No deers to hunt" 
    @classmethod
    def hunt(cls,zoo_objects):
        c = 0
        for i in zoo_objects.lists:
            if i.sound == cls.animal_sound:
                c = 1
                zoo_objects.lists.remove(i)
                break
                
        if c == 0:
            print(cls.jantu)
    
class Deer(Animal,LandAnimals):
    food_increase = 2
    sound = "Buck Buck"

class Lion(Animal,LandAnimals,HuntingAnimals):
    food_increase = 4
    sound = "Roar Roar"
   
class Shark(Animal,WaterAnimals,HuntingAnimals):
    food_increase = 8
    sound = "Shark Sound"
    animal_sound = "Hum Hum"
    jantu = "No GoldFish to hunt"

class GoldFish(Animal,WaterAnimals):
    food_increase = 0.2
    sound = "Hum Hum"

class Snake(Animal,LandAnimals,HuntingAnimals):
    food_increase = 0.5
    sound = "Hiss Hiss"
  
class Zoo:
    animals_count = []
    def __init__(self,reserved_food_in_kgs = 0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self.lists = []
        
    @property    
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,reserved_food):
        self._reserved_food_in_kgs += reserved_food

    def add_animal(self,animal):
        self.lists.append(animal)
        self.animals_count.append(animal)
    
    def count_animals(self):
        return len(self.lists)
    
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
  
    @classmethod
    def count_animals_in_all_zoos(cls):
       return len(cls.animals_count)
    
    @staticmethod
    def count_animals_in_given_zoos(zoo_objects):
        count = 0
        for i in zoo_objects:
            count += len(i.lists)
        return count
