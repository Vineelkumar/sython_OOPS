class Pokemon:
    sounds = ""
    runs = ""
    swims = ""
    flies = ""
    def __init__(self,name,level = 1):
        self._master = ''
        if name == "":
            raise ValueError("name cannot be empty")
        else:    
            self._name = name
        if level <= 0:
            raise ValueError("level should be > 0")
        else:
            self._level = level
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @classmethod
    def make_sound(cls):
        print(cls.sounds)

    @classmethod    
    def run(cls):
        print(cls.runs)
    
    @classmethod    
    def swim(cls):
        print(cls.swims)
        
    @classmethod        
    def fly(cls):
        print(cls.flies)
    
    @property    
    def master(self):
        if self._master == '':
            print("No Master")
        else:
            return self._master
        
    
    def __str__(self):
        return "{} - Level {}".format(self._name,self._level)
    
        

# class ElectricAttack:
    
#     attacks = ""
#     @classmethod
#     def attack(cls):
#         print(cls.attacks)

# class WaterAttack:
    
    
#     @classmethod
#     def attack(cls):
#         return 'l'

# class AirAttack:
    
    
#     @classmethod
#     def attack(cls):
#         return 'l'

    
class Pikachu(Pokemon):
    
    sounds = "Pika Pika"
    runs = "Pikachu running..."
    #pikachu_attack = 67
    def attack(self):
        pikachu_attack = 10
        pikachu_attack *= self._level
        print("Electric attack with {} damage".format(pikachu_attack))
    

class Squirtle(Pokemon):
    
    sounds = "Squirtle...Squirtle"
    runs = "Squirtle running..."
    swims = "Squirtle swimming..."
    def attack(self):
        Squirtle_attack = 9
        Squirtle_attack *= self._level
        print("Water attack with {} damage".format(Squirtle_attack))

class Swanna(Pokemon):
    
    sounds = "Swanna...Swanna"
    runs = "Swanna running..."
    flies = "Swanna flying..."
    swims = "Swanna swimming..."
    def attack(self):
        Swanna_water_attack = 9
        Swanna_water_attack *= self._level
        Swanna_air_attack = 5
        Swanna_air_attack *= self._level
        print("Water attack with {} damage".format(Swanna_water_attack))
        print("Air attack with {} damage".format(Swanna_air_attack))
    
class Pidgey(Pokemon):
    sounds = "Pidgey...Pidgey"
    flies = "Pidgey flying..."
    def attack(self):
        Pidgey_air_attack = 5
        Pidgey_air_attack *= self._level
        print("Air attack with {} damage".format(Pidgey_air_attack))
    
class Zapdos(Pokemon):
    
    sounds = "Zap...Zap"
    flies = "Zapdos flying..."
    def attack(self):
        Zapdos_electric_attack = 10
        Zapdos_electric_attack *= self._level
        Zapdos_air_attack = 5
        Zapdos_air_attack *= self._level
        print("Electric attack with {} damage".format(Zapdos_electric_attack))
        print("Air attack with {} damage".format(Zapdos_air_attack))
    

class Island:
    pokemon_list = []
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_list.append(self)
        
        
        
    @property
    def name(self):
        return self._name
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    @property    
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs

    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self._pokemon_left_to_catch += 1 
        
        else:
            print("Island at its max pokemon capacity")
        
    @classmethod    
    def get_all_islands(cls):
        return cls.pokemon_list
    
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self.pokemon_left_to_catch,self._total_food_available_in_kgs)

class Trainer:
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = self._experience * 10
        self._food_in_bag = 0
        self._current_island = ''
        self.list_of_catched = []
        
    @property
    def experience(self):
        return self._experience
    
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    @property    
    def name(self):
        return self._name
    
    @property    
    def current_island(self):
        if self._current_island == '':
            print('You are not on any island')
        else:
            return self._current_island
    
    def __str__(self):
        return '{}'.format(self._name)

    def collect_food(self):
        if self._current_island == '' or self._current_island._total_food_available_in_kgs == 0:
            print("Move to an island to collect food")
            
        
        elif self._max_food_in_bag > self._current_island._total_food_available_in_kgs:
            self._food_in_bag = self._current_island._total_food_available_in_kgs
            self._current_island._total_food_available_in_kgs = 0
        
        
        elif self._food_in_bag != self._max_food_in_bag:
            self._food_in_bag = 1000
            self._current_island._total_food_available_in_kgs -= 1000
    
    def move_to_island(self,island):
        self._current_island = island
        

    def catch(self,pokemon):
        if (pokemon._level * 100) > self._experience:
            print("You need more experience to catch {}".format(pokemon.name))
        
        else:
            print("You caught {}".format(pokemon.name))
            self._experience += pokemon.level * 20
            self.list_of_catched.append(pokemon)
            pokemon._master = self
 
    def get_my_pokemon(self):
        return self.list_of_catched
