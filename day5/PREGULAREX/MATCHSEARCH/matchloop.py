import re



# Sample strings.
list = ["dog dot", "do don't", "dumb-dumb", "no match"]

# Loop.
for element in list:
    # Match if two words starting with letter d.
    m = re.match(r"(d\w+)\W(d\w+)", element)

    # See if success.
    if m:
        print(m.groups())






##Pattern: (d\w+)\W(d\w+)
##
##d        Lowercase letter d.
##\w+      One or more word characters.
##\W       A non-word character.
