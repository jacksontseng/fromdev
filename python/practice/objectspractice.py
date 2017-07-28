class Musician:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre

    def description(self):
        print "Hi i am %s and I make %s music." %(self.name, self.genre)


Tame_Impala = Musician("Tame Impala", "Rock")
Eminem = Musician("m&m", "rap")


print Tame_Impala.name + ":" + Tame_Impala.genre
print Tame_Impala.name + ":" + Eminem.genre
Tame_Impala.description
