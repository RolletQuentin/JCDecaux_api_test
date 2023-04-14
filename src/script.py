import requests
import json


# to not share the private data on github, we use config file with private data
with open('src/config.json') as config_file:
    config = json.load(config_file)


api_key = config["api_key"]
id_map = "jcdecaux_899547"


def fetchContracts():
    """To get all the contracts of jcdecaux

    Returns:
        JSON: the response to a api call with all the contacts
    """
    contracts = requests.get(f"http://api.jcdecaux.com/vls/v3/contracts?apiKey={api_key}")
    
    if contracts.status_code != 200:
        print("Le call api n'a pas fonctionné. Error : " + str(contracts.status_code))
        exit()
        
    return contracts.json()


def fetchStations():
    """To get all the stations

    Returns:
        JSON: the response to a api call with all the stations
    """
    stations = requests.get(f"https://api.jcdecaux.com/vls/v3/stations?apiKey={api_key}")
    
    if stations.status_code != 200:
        print("Le call api n'a pas fonctionné. Error : " + str(stations.status_code))
        exit()
        
    return stations.json()


def fetchStationsFromContract(contract_name):
    """To get all the stations from a contract

    Returns:
        JSON: the response to a api call with all the stations of the contract
    """
    stations = requests.get(f"https://api.jcdecaux.com/vls/v3/stations?contract={contract_name}&apiKey={api_key}")
    
    if stations.status_code != 200:
        print("Le call api n'a pas fonctionné. Error : " + str(stations.status_code))
        exit()
        
    return stations.json()


def numberOfBikes(contracts):
    """Return the number of bikes available

    Args:
        contracts (JSON): all the contracts
        
    Returns:
        (int, int) : (mechanicalBikes, electricalBikes) -> the total number of bikes
    """
    numberOfMechanicalBikes = 0
    numberOfElectricalBikes = 0
    
    for contract in contracts:
        contract_name = contract["name"]
        stations = fetchStationsFromContract(contract_name)
        
        for station in stations:
            numberOfMechanicalBikes += station["totalStands"]["availabilities"]["mechanicalBikes"]
            numberOfElectricalBikes += station["totalStands"]["availabilities"]["electricalBikes"]
    
    return (numberOfMechanicalBikes, numberOfElectricalBikes)


def numberOfBikesByContract(contracts, contract_name):
    """Return the number of bikes available for a contract

    Args:
        contracts (Response): all the contracts
        contract_name (str, optional): You have to know the contract name. Defaults to "".

    Returns:
        (int, int) : (mechanicalBikes, electricalBikes) -> the number of bikes for a contract
    """
    numberOfMechanicalBikes = 0
    numberOfElectricalBikes = 0
    
    
    stations = fetchStationsFromContract(contract_name)
    
    for station in stations:
        numberOfMechanicalBikes += station["totalStands"]["availabilities"]["mechanicalBikes"]
        numberOfElectricalBikes += station["totalStands"]["availabilities"]["electricalBikes"]
    
    return (numberOfMechanicalBikes, numberOfElectricalBikes)

if __name__ == "__main__":
    contracts = fetchContracts()
    print(contracts)
    # print(numberOfBikes(contracts))
    
    pass