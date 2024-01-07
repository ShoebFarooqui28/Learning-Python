computer = {"processor", "RAM", "graphiccard", "PSU", "Assembly"}
software = {"Windows", "Linux", "MacOS", "Ubuntu", "Assembly"}

computer.remove("PSU")
computer.add("motherboard")
# computer.update(software)

# myPc = computer.union(software)
# for x in computer:
#    print(x)

print(software.difference(computer))
print(computer.difference(software))
print(computer.intersection(software))

