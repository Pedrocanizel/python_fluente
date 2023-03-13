from collections import namedtuple

city = namedtuple('City', 
                  'name country population coordinates')

tokyo = city('Tokyo', 'JP', 36.933, (35.6, 139.6))
brasil = city('brasil', 'BR', 36.933, (35.6, 139.6))

print(tokyo) # Todas as características de tokyo
print(brasil.name) # Campo nome apenas
print(tokyo.country)# Campo país apenas
print(tokyo.population)# Campo população apenas
print(tokyo.coordinates)# Campo coordenadas apenas
print(city._fields) # Quais campos city possui
print(city._asdict)
