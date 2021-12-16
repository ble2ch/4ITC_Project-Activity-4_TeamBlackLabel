from ncclientnetconf import *
from sendMessage import *
import xml.dom.minidom

def edit(choice):
    if choice == "Yes":
        
        #Implement Changes
        # print("Input host name: ")
        hostname = input("Input host name: ")

        # print("Input host name: ")
        lbaddress = input("Input loopback address: ")

        # print("Input host name: ")
        lbmask = input("Input loopback mask name: ")

        changes = Modify_Configuration(hostname, lbaddress, lbmask)
        if(changes==True):
            print("------------------------------Changes Made!------------------------------")
            #Get new configuration
            getInterfaces()
            print("------------------------------Sending Updates to Teams!------------------------------")
            #Send message to teams
            sendUpdate("New Update!")
        
        print("------------------------------Modified Configuration------------------------------")
        InitialConfig()

#Print Current Configuration
print("------------------------------Current Configuration------------------------------")
InitialConfig()

print("------------------------------Modify Configuration ?------------------------------")
edit(input("Type 'Yes' to edit else type 'No': "))

updateNotif(2,1,"New Update")