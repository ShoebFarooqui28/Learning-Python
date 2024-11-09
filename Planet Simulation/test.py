def Attraction(mass1, mass2, distance):
    G = 6.67430e-11
    force = (G * mass1 * mass2) / (distance ** 2)
    return force

m1 = float(input("Enter Mass 1 : "))
m2 = float(input("Enter Mass 2 : "))
d = float(input("Enter Distance : "))

G_force = Attraction(m1, m2, d)

print(G_force)