# sandwich = [["rye", "sourdough", "baguette"],
#             [["ham", "salami", "turkey"],
#              ["swiss", "munster", "cheddar"]],
#             ["mayo", "mustard", "tabasco"]]
# print sandwich[1][1][2]

class City:
    def __init__(self, mayor, pop, website):
        self.mayor = mayor
        self.pop = pop
        self.website = website

city_info = {'newyork' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8406000,
                            'website' : "http://www.nyc.gov"
                            },
             'losangeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomas Regalado",
                            'population' : 417650,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2719000,
                            'website' : "http://www.cityofchicago.org/"
                            }
        }
# print city_info["los_angeles"]
# print city_info["chicago"]["mayor"]

# print city_info["new_york"][population]
# print city_info["miami"]['website']
# print city_info["los_angeles"]['mayor']
# print city_info["chicago"]

# def citydictionary (c):
#     for i in city_info[c]:
#         print "the " + i + " of " + c + " is " + str(city_info[c][i])
# citydictionary('newyork')

print city_info['newyork'].keys()
COI = raw_input("I'm a dictionary, I know about New York, Los Angeles, Miami, and Chicago. What city would you like to know about?")
COI = COI.lower().replace(" ", "")
print COI
print city_info[COI][0]
# fact = raw_input('Would you like to know about ' + city_info[COI][0] + "," + city_info[COI][1] + "or" + city_info[COI][2] + "?")
fact = raw_input('Would you like to know about the mayor, population or website "?")
print "the " + fact + " of " + COI + " is " + str(city_info[COI][fact])
