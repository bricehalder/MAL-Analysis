from colors import color
from decimal import Decimal, ROUND_HALF_UP

ENJOY_THRESH = 7

def aggregate(m, p, e):
    # Can change the weight of each factor here
    # Currently the highest possible is 10.5 with enjoyment factored in
    # & 10 without it if all input is <= 10
    meaning_agg = m * 0.2
    production_agg = p * 0.8
    
    # If enjoyment < THRESH it will negatively affect the score
    enjoy_agg = (e - ENJOY_THRESH) * 0.1
    agg = meaning_agg + production_agg + enjoy_agg
    return agg

def header():
        return color.BOLD + '{:40}'.format('NAME') \
            + '{:12}'.format('MEANING') \
            + '{:12}'.format('PRODUCTION') \
            + '{:12}'.format('ENJOYMENT') \
            + color.RED \
            + '{:10}'.format('RAW') \
            + color.BLUE \
            + '{:12}'.format('OVERALL') \
            + color.END
    
def header_file():
        return '{:45}'.format('NAME') \
        + '{:12}'.format('MEANING') \
        + '{:12}'.format('PRODUCTION') \
        + '{:12}'.format('ENJOYMENT') \
        + '{:12}'.format('RAW') \
        + '{:12}'.format('OVERALL') \

class Song:
    """A class to resemble a song"""

    def __init__(self, name="Default Name", m=0, p=0, e=0):
        self.name = name.strip()
        self.meaning = m
        self.production = p
        self.enjoyment = e
        self.overall = round(aggregate(m, p, e),2)
        self.score = Decimal(self.overall).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        # If you want the raw total/10 (takes out enjoyment factor)
        self.raw = round(self.overall - ((self.enjoyment - ENJOY_THRESH) * 0.1),2)
        
    def refactor(self):
        self.overall = round(aggregate(self.name, self.meaning, \
        self.production, self.enjoyment), 2)
        self.raw = round(self.overall - ((self.enjoyment - ENJOY_THRESH) * 0.1),2)
        self.score = Decimal(round(self.overall)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    
    def __str__(self):
        return '{:40}'.format(self.truncate(35)) \
        + '{:<12g}'.format(self.meaning) \
        + '{:<12g}'.format(self.production) \
        + '{:<12g}'.format(self.enjoyment) \
        + color.RED \
        + '{:<12g}'.format(self.raw) \
        + self.get_overall_color() \
        + '{:<12g}'.format(self.score) \
        + color.END
    
    def str_no_color(self, value=25):
        return '{:45}'.format(self.truncate(value)) \
        + '{:<12g}'.format(self.meaning) \
        + '{:<12g}'.format(self.production) \
        + '{:<12g}'.format(self.enjoyment) \
        + '{:<12g}'.format(self.raw) \
        + '{:<12g}'.format(self.score) \

    def __repr__(self):
        return "Song<" + self.name + ">"
    
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Show):
            return False
        
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name
    
    def __lt__(self, other):
        return self.name < other.name

    def set_meaning(self, value):
        self.meaning = value
        self.refactor()

    def set_production(self, value):
        self.production = value
        self.refactor()

    def set_enjoy(self, value):
        self.enjoyment = value
        self.refactor()


    def truncate(self, value):
        if len(self.name) < value:
            return self.name
        printname = self.name[:(value - 3)]
        printname += '...'
        return printname
    
    def get_overall_color(self):
        ret = ''
        if self.overall > 10 or self.raw > 9.5:
            ret = color.BOLD
        if self.score == 10:
            ret += color.BLUE
        elif self.score == 9:
            ret += color.GREEN
        elif self.score == 8:
            ret += color.DARKCYAN
        elif self.score == 7:
            ret += color.YELLOW
        elif self.score == 6:
            ret += color.PURPLE
        elif self.score <= 5:
            ret += color.RED
        return ret
   
        
