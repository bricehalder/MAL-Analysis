from show import *

class Series:
    """A class to resemble a series"""
    def calculateAverages(self):
        self.overall = 0
        self.raw = 0
        self.score = 0
        self.plot = 0
        self.characters = 0
        self.visuals = 0
        self.sound = 0
        self.enjoyment = 0
        
        for show in self.shows:
            self.overall += show.overall / len(self.shows)
            self.raw += show.raw / len(self.shows)
            self.plot += show.plot / len(self.shows)
            self.characters += show.characters / len(self.shows)
            self.visuals += show.visuals / len(self.shows)
            self.sound += show.sound / len(self.shows)
            self.enjoyment += show.enjoyment / len(self.shows)
        
        self.score = Decimal(round(self.overall)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        
    def __init__(self, name="Default Name", shows=set()):
        self.name = name.strip()
        self.shows = shows
        self.calculateAverages()
        
    def __repr__(self):
        return "Series<" + self.name + ">"

    def __str__(self):
        return f'({str(len(self.shows))}) ' \
        + '{:36}'.format(Show.truncate(self, 35)) \
        + '{:<12g}'.format(round(self.plot,2)) \
        + '{:<12g}'.format(round(self.characters, 2)) \
        + '{:<12g}'.format(round(self.visuals, 2)) \
        + '{:<12g}'.format(round(self.sound, 2)) \
        + '{:<12g}'.format(round(self.enjoyment, 2)) \
        + color.RED \
        + '{:<12g}'.format(round(self.raw, 2)) \
        + Show.get_overall_color(self) \
        + '{:<12g}'.format(self.score) \
        + color.END
    
    def str_no_color(self, value=25):
        return f'({str(len(self.shows))}) ' \
        + '{:45}'.format(Show.truncate(self, value)) \
        + '{:<12g}'.format(round(self.plot,2)) \
        + '{:<12g}'.format(round(self.characters, 2)) \
        + '{:<12g}'.format(round(self.visuals, 2)) \
        + '{:<12g}'.format(round(self.sound, 2)) \
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
    
    def addShow(self, show):
        self.shows.discard(show)
        self.shows.add(show)
        self.calculateAverages()
    
    def getShows(self):
        return [show.name for show in sorted(self.shows)]
    
    def truncate(self, value):
        if len(self.name) < value:
            return self.name
        printname = self.name[:(value - 3)]
        printname += '...'
        return printname
    