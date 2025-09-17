def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    description = "Making a"
    
    if toasted:
        description += " toasted"
    
    description += f" {bread_type} sandwich with {filling}"
    
    if cheese:
        description += f" and {cheese} cheese"
    
    description += "."
    return description