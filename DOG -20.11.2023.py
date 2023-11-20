'''4.Class dog
Attributes :
     name, size, breed Default :Unknown , DAte of birth in DD/MM/YYYY format Default: 'unknown'
     -bark --this should get the dog bark (print out the word "woof')
     -get_name --this should return the dogs name
     -set_name --this should allow the user to set an alphabetical name between  2 and 30 characters.
                -- convert the name to title case before setting
     -dog_years --this should calculate a dog's age in dog years (use 1 year = 7 dog years).''' 
class Dog:
    def __init__(self, name, size, breed='Unknown', dob='Unknown'):
        self.name = name
        self.size = size
        self.breed = breed
        self.dob = dob

    def bark(self):
        print("woof!")

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if 2 <= len(new_name) <= 30 and new_name.isalpha():
            self.name = new_name.title()
        else:
            print("Invalid name.")

    def dog_years(self):
        if self.dob == 'Unknown':
            print("Enter the Dog's dob in dd/mm/yyyy.")
            return
        else:
                birth_year = int(self.dob[-4:])
                current_year = 2023 
                age_in_years = current_year - birth_year
                age_in_dog_years = age_in_years * 7
                return age_in_dog_years
          


my_dog = Dog(name='Jimmy', size='large', breed='Labrador', dob='12/07/2019')

print("Dog's name:", my_dog.get_name())
my_dog.bark()

my_dog.set_name('Max')
print("Updated dog's name:", my_dog.get_name())

print("Dog's age in dog years:", my_dog.dog_years())

         
    
        
        

