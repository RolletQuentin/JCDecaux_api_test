import matplotlib.pyplot as plt
import folium

from src.script import *

# get the number of bikes for the city of Bruxelles and show the proportion of them
def example1(contracts):
    
    mechanicalBikes, electricalBikes = numberOfBikesByContract(contracts, "bruxelles")

    # print a graph to show the proportions
    labels = ["Mechanical", "Electric"]
    plt.pie([mechanicalBikes, electricalBikes], labels=labels)
    plt.legend()
    plt.show()
    
# ranking about the number of bike available for each contract 
def example2(contracts):
    nuberOfBikesPerContract = {}
    for contract in contracts:
        res1, res2 = numberOfBikesByContract(contracts, contract["name"])
        numberOfBikes = res1 + res2
        nuberOfBikesPerContract[contract["name"]] = numberOfBikes
        
    sortedNumberOfBikesPerContract = dict(sorted(nuberOfBikesPerContract.items(), key=lambda item: item[1]))
    
    plt.bar(sortedNumberOfBikesPerContract.keys(), sortedNumberOfBikesPerContract.values())  
    plt.xticks(rotation=90)
    plt.xlabel('Contrats')
    plt.ylabel('Nombre de vélos disponibles')
    plt.title('Nombre de vélos disponibles par contrat')  
    plt.show()
    

# to genrate a map with all the stations with the number of bikes available
def example3(contracts):
    # create the map and centering on Toulouse
    maps = folium.Map(location=[43.6000, 1.4333])
    
    # get all stations
    stations = fetchStations()
    
    # for each stations, add a point of interests with some informations about the station
    for station in stations:
        folium.Marker([station["position"]["latitude"], station["position"]["longitude"]],
                      popup=(f"{station['name']}\n" + 
                        f"Nombre de vélos mécaniques : {station['totalStands']['availabilities']['mechanicalBikes']}\n" +
                        f"Nombre de vélos électriques : {station['totalStands']['availabilities']['electricalBikes']}")
                      ).add_to(maps)
    
    # save the maps in the root
    maps.save("maps.html")


if __name__ == "__main__":
    contracts = fetchContracts()
    
    example1(contracts)
    # example2(contracts)
    # example3(contracts)
