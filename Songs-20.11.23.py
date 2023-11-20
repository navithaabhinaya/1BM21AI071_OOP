'''3.Define a class called songs , it will show the lyrics of the song . its __init__() method should have two arguments : self and lyrics. lyrics is a list . insisde your class create a method called sing_me_a_song that prints each element of lyrics on his own line. DEfine a variable:
        happy_bday = Song (["May god bless you,",
                            "have a sunshine on you ,", "Happy Birthday to you !"])
Call the sing_me_song method on this variable.''' 
class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
happy_bday.sing_me_a_song()
         
    
        
        

