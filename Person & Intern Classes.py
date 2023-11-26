class Personne:
    _count = 0

    def __init__(self, name="dev 102", age=21):
        self.name = name  
        self.age = age
        Personne._count += 1

    
    def get_count():
        return Personne._count
    
    def info(self):
        print(f"Personne Name: {self.name}, Age: {self.age}")



class Stagiaire(Personne):
    def __init__(self, name, age, note):
        super().__init__(name, age)
        self.note = note  

    def info(self):
        print(f"Stagiaire Name: {self.name}, Age: {self.age}, Note: {self.note}")

p1 = Personne()
s1 = Stagiaire("appah", 25, 20)

p1.info()
s1.info()


print("Total des instances  :", Personne.get_count())
