from fractions import Fraction

def fraction_val(decimal, limit_denominator=False):
    return Fraction(decimal).limit_denominator()

def formatted_fraction_val(decimal, limit_denominator=False):
    return ("(" + str(fraction_val(decimal, limit_denominator)) + ")")