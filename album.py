from show import *

class Album:
    """A class to resemble an album"""
    def calculateAverages(self):
        self.overall = 0
        self.raw = 0
        self.score = 0
        self.meaning = 0
        self.production = 0
        self.enjoyment = 0
        
        for show in self.songs:
            self.overall += show.overall / len(self.shows)
            self.raw += show.raw / len(self.shows)
            self.meaning += show.meaning / len(self.shows)
            self.production += show.production / len(self.shows)
            self.enjoyment += show.enjoyment / len(self.shows)
        
        self.score = Decimal(round(self.overall)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        
    def __init__(self, name="Default Name", songs=set()):
        self.name = name.strip()
        self.songs = songs
        self.calculateAverages()
        
    def __repr__(self):
        return "Album<" + self.name + ">"

    def __str__(self):
        return f'({str(len(self.shows))}) ' \
        + '{:36}'.format(Show.truncate(self, 35)) \
        + '{:<12g}'.format(round(self.meaning,2)) \
        + '{:<12g}'.format(round(self.production, 2)) \
        + '{:<12g}'.format(round(self.enjoyment, 2)) \
        + color.RED \
        + '{:<12g}'.format(round(self.raw, 2)) \
        + Show.get_overall_color(self) \
        + '{:<12g}'.format(self.score) \
        + color.END
    
    def str_no_color(self, value=25):
        return f'({str(len(self.shows))}) ' \
        + '{:45}'.format(Show.truncate(self, value)) \
        + '{:<12g}'.format(round(self.meaning,2)) \
        + '{:<12g}'.format(round(self.production, 2)) \
        + '{:<12g}'.format(round(self.enjoyment, 2)) \
        + '{:<12g}'.format(round(self.raw, 2)) \
        + '{:<12g}'.format(self.score) \
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, Series):
            return False
        
        return self.name == other.name
    
    def __ne__(self, other):
        return self.name != other.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def addSong(self, song):
        self.songs.discard(song)
        self.songs.add(song)
        self.calculateAverages()
    
    def getSongs(self):
        return [song.name for song in sorted(self.songs)]
    
    def truncate(self, value):
        if len(self.name) < value:
            return self.name
        printname = self.name[:(value - 3)]
        printname += '...'
        return printname
    