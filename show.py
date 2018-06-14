from colors import color
from decimal import Decimal, ROUND_HALF_UP

def aggregate(p, c, a, m, e):
    # Can change the weight of each factor here
    # Currently the highest possible is 10.5 with enjoyment factored in
    # & 10 without it if all input is <= 10
    if p > 5:
        plot_agg = p * 0.49
        char_agg = c * 0.17
        art_agg = a * 0.17
        vis_agg = m * 0.17
    else:
        plot_agg = p * 0.7
        char_agg = c * 0.1
        art_agg = a * 0.1
        vis_agg = m * 0.1
    # If enjoyment < 5 it will negatively affect the score
    enjoy_agg = (e - 5) * 0.1
    agg = plot_agg + char_agg + art_agg + vis_agg + enjoy_agg
    return agg

def header():
    return color.BOLD + '{:30}'.format('NAME') \
        + '{:12}'.format('PLOT') \
        + '{:12}'.format('CHARACTERS') \
        + '{:12}'.format('VISUALS') \
        + '{:12}'.format('SOUND') \
        + '{:12}'.format('ENJOYMENT') \
        + color.RED \
        + '{:12}'.format('RAW') \
        + color.BLUE \
        + '{:12}'.format('OVERALL') \
        + color.END

class Show:
    """A class to resemble a show listing on MAL"""

    def __init__(self, name="Default Name", p=0, c=0, a=0, m=0, e=0):
        self.name = name
        self.plot = p
        self.characters = c
        self.visuals = a
        self.sound = m
        self.enjoyment = e
        self.overall = round(aggregate(p,c,a,m,e),2)
        self.score = Decimal(self.overall).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        # If you want the raw total/10 (takes out enjoyment factor)
        self.raw = round(self.overall - ((self.enjoyment - 5) * 0.1),2)

    def __str__(self):
        return '{:30}'.format(self.truncate(25)) \
        + '{:<12g}'.format(self.plot) \
        + '{:<12g}'.format(self.characters) \
        + '{:<12g}'.format(self.visuals) \
        + '{:<12g}'.format(self.sound) \
        + '{:<12g}'.format(self.enjoyment) \
        + color.RED \
        + '{:<12}'.format(self.raw) \
        + color.BLUE \
        + '{:<12}'.format(self.score) \
        + color.END

    def __repr__(self):
        return "Show<" + self.name + ">"

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def refactor(self):
        self.overall = round(aggregate(self.plot, self.characters, \
        self.visuals, self.sound, self.enjoyment), 2)
        self.raw = round(self.overall - ((self.enjoyment - 5) * 0.1),2)
        self.score = Decimal(round(self.overall)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    def set_plot(self, value):
        self.plot = value
        self.refactor()

    def set_chars(self, value):
        self.characters = value
        self.refactor()

    def set_art(self, value):
        self.visuals = value
        self.refactor()

    def set_music(self, value):
        self.sound = value
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
