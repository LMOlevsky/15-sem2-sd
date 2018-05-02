def passMinSafe(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    digit = [x for x in password if x.isdigit()]
    return len(lower) != 0 and len(upper) !=0 and len(digit) != 0

print passMinSafe("i2D>>")


def passStrength(password):
    nonAlphaChars = ",?!&#,;:-_*"
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    digit = [x for x in password if x.isdigit()]
    nonalpha = [x for x in password if x in nonAlphaChars]

    strength = 0
    if len(lower) == 1:
        strength += 1
    elif len(lower) > 1:
        strength += 2
    if len(upper) == 1:
        strength += 1
    elif len(upper) > 1:
        strength += 2
    if len(digit) == 1:
        strength += 1
    elif len(digit) > 1:
        strength += 2
    if len(nonalpha) == 1:
        strength += 1
    elif len(nonalpha) > 1:
        strength += 2
    if len(password) > 7 and len(password) <= 14:
        strength += 1
    elif len(password) > 14:
        strength += 2

    return strength

print passStrength("")
print passStrength("l")
print passStrength("le")
print passStrength("leV")
print passStrength("leVI")
print passStrength("leVI1")
print passStrength("leVI12")
print passStrength("leVI12#")
print passStrength("leeI12#!")
print passStrength("leVI12#!a")
print passStrength("leVI12#!sdfsdfvfdvdgsrgf")
