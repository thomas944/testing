import requests
import json

#this creates link 
def requestSummonerData(region, summonerName):
    URL = "https://" + region + ".whatismymmr.com/api/v1/summoner?name=" + summonerName
    #goes to url and returns back json
    req = requests.get(URL)
    response = req.json()
    return response

def average():
    i =1
    total = 0
    names = []
    region = input("Enter Region:")
    while i<6:
        name = input("Enter Summoner " + str(i) + ": ")
        names.append(name)
        responseJSON = requestSummonerData(region,name)
        total = total + responseJSON['ranked']['avg']
        i = i + 1

    print("Avg MMR of ", end=" ") 
    for x in names:
        print(str(x) + ",", end = " ")
    print(str(total/5))
    return 

def single():
    name = input("Enter Summoner Name: ")
    region = input("Enter Summoner Region: ")
    responseJSON = requestSummonerData(region,name)
    print(name+"'s MMR is " + str(responseJSON['ranked']['avg']))
    return 

def main():
    option = input("Single Search or Multi-Search? ")
    if option == "Single Search":
        single()
    else:
        average() 
    return       

if __name__ == '__main__':
    main()



        