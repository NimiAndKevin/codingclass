class Llama():
    def __init__(self,name,colour,personality,gender,hobby,country):
        self.name=name
        self.colour=colour
        self.personality=personality
        self.gender=gender
        self.hobby=hobby
        self.country=country

    def roll(self):
        print(f"{self.name} is rolling")
    def walk(self):
        print(f"{self.name} is a {self.gender}, walking on the desert")
    def sing(self):
        print(f"{self.name} is singing")
    def introduce():
        print(f"Hi i'm {self.name}, My gender is a {self.gender}, My colour is {self.colour}, I live in {self.country},my personality is {self.personality}, I have a hobby and its called {self.hobby}")
    def shout(self):
        print(f"{self.name} is shouting")
    def body_weight(self):
        print(f"{self.name} body weigth is 25-30%")
    def clap(self):
        print(f"{self.name} is clapping with his paws")
    def introduce_skin(self):
        print(f"{self.name} skin is made of wool")
    def dance(self):
        print(f"{self.name} is dancing")
    def transport(self):
        print(f"{self.name} transports people from distances")

nimi_llama=Llama("max", "white", "stuborn", "male", "drinks water", "Nigeria")
nimi_llama.roll()
nimi_llama.walk()
nimi_llama.sing()
nimi_llama.introduce()
nimi_llama.shout()
nimi_llama.body_weight()
nimi_llama.clap()
nimi_llama.introduce_skin()
nimi_llama.dance()
nimi_llama.transport()