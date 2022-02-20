# #nestin dict in a dict
# capitals = {
#     "France": {
#         "cities_visited": ["Paris", "Lile", "Dijon"],
#         "total_vistis": 12
#         },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_vistis": 15
#         },
# }

# #nesting a list in a Dcitionary

# travel_log = {
#     "France": [
#         "Paris", "Lile", "Dijon"
#         ],
#     "Germany": [
#         "Berlin", "Hamburg", "Stuttgart"
#     ]
# }

# #nesting dicts in a list

# travel_log_list = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lile", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 2,
#     },
# ]

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]   
    
#🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
def add_new_country(country, visits, cities=[]):
    x = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(x)


# #🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
