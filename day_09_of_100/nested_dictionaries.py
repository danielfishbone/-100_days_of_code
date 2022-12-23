#
travel_log = {
    "France" :{"cities_visited":["Paris","Lille","Dijon"]},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"]},
}

#Nesting dictionary in a list 
travel_log2 = [
        {
            "Country":"France" ,
            "cities_visited":["Paris","Lille","Dijon"],
            "total_visits":2
        },
        
        {
            "Country":"Germany",
            "cities_visited":["Berlin","Hamburg","Stuttgart"],
            "total_visits":3

        },
]

def add_new_country(_country,_visits,_cities):
    new_log ={}
    new_log["Country"] = _country
    new_log["cities_visited"]  = _visits
    new_log["total_visits"]  = _cities
    travel_log2.append(new_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)    
print(travel_log2[0]["Country"])