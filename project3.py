import urllib.parse
import requests
from tabulate import tabulate
 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "lM0Ws0jAdViYuHweNA4rsOfIWwMaLkA7" 
print("Type 1 for Miles and 2 for Metric System")
distanceType = input("Miles or Metric System: ")
inputStart = []
inputDestination = []
startCount = 0
destCount = 0
headers = ["Narration","Distance"]
headers2 = ["Start","Destination"]
if distanceType == '1':
    while True:
        narrate = []
        distance = []
        tablePlace = 0
        orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            break
        if orig == "history" or orig == "h":
            table = zip(inputStart, inputDestination)
            print(tabulate(table, headers=headers2, tablefmt="fancy_grid"))
        startCount += 1
        inputStart.insert(startCount,orig)
        dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            break
        if dest == "history" or dest == "h":
            table = zip(inputStart, inputDestination)
            print(tabulate(table, headers=headers2, tablefmt="fancy_grid"))
            break
        destCount += 1
        inputDestination.insert(destCount,dest)
        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration: " + (json_data["route"]["formattedTime"]))
            print("Miles: " + str(json_data["route"]["distance"]))
            print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
            print("=============================================")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                narrate.insert(tablePlace,(each["narrative"]))
                distance.insert(tablePlace,((str("{:.2f}".format((each["distance"])))) + "Miles"))
                tablePlace += 1

            table = zip(narrate, distance)
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
            
        elif json_status == 402:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("For Staus Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")
elif distanceType == '2':
    while True:
        narrate = []
        distance = []
        tablePlace = 0
        headers = ["Narration","Distance"]
        orig = input("Starting Location: ")
        if orig == "quit" or orig == "q":
            break
        if orig == "history" or orig == "h":
            table = zip(inputStart, inputDestination)
            print(tabulate(table, headers=headers2, tablefmt="fancy_grid"))
            break
        startCount += 1
        inputStart.insert(startCount,orig)
        dest = input("Destination: ")
        if dest == "quit" or dest == "q":
            break
        if dest == "history" or dest == "h":
            table = zip(inputStart, inputDestination)
            print(tabulate(table, headers=headers2, tablefmt="fancy_grid"))
            break
        destCount += 1
        inputDestination.insert(destCount,dest)
        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
        print("URL: " + (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration: " + (json_data["route"]["formattedTime"]))
            print("Kilometer: " + str((json_data["route"]["distance"]) * 1.61))
            print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
            print("=============================================")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                narrate.insert(tablePlace,(each["narrative"]))
                distance.insert(tablePlace,((str("{:.2f}".format(((each["distance"]) * 1.61)))) + " km"))
                tablePlace += 1

            table = zip(narrate, distance)
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        elif json_status == 402:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("For Staus Code: " + str(json_status) + "; Refer to:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")
else:
    print("Please input 1 or 2")