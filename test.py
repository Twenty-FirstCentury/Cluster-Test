
#2022
#STEM@GTRI
#ELSYS

from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import docker
from docker import client
import json
import sys
import textwrap


client = docker.from_env()


network_list={}
for net in client.networks():
    network_list[net['Name']]=1


jsondump = json.dumps(client.containers())
loadedjson = json.loads(jsondump)


graph_attr = {

    "shape": "ellipse",

    "fontsize": "150",

    "splines": "spline",

    "nodesep": "5",
    "ranksep": "10",

    "dpi": "250",

}


with Diagram("\n \n \n \n \n \n" "Docker Container Diagram", show=False, direction="TB", graph_attr=graph_attr, outformat="jpg"):\

    for net in network_list.keys():
        #print("NetworkName " + net) Debug


        bridge = Custom(net, "./Images/bridge.png")


        for i in loadedjson: 
           # print(i)  Debug    

            # if i["Image"]:
            #     print ("ImageName " + i["Image"])

            if i["Mounts"] and 'Name' in (i["Mounts"][0]):                          
                # print("Name: Exists") Debug
                namevar = str(i["Mounts"][0]["Name"])
                namevar2 = (namevar[0:40] + "...")
            else:
                # print("Name: doesn't exist") Debug
                namevar2 = "                              N/A                              "

            if i["Ports"] and 'IP' in i["Ports"][0]:                                    
                # print("IP: Exists") Debug
                ipvar = str(i["Ports"][0]["IP"])
            else:
                # print("IP: doesn't exist") Debug
                ipvar = "N/A"

            if i['NetworkSettings']['Networks']:
                networkName = list(i['NetworkSettings']['Networks'].keys())[0]
                # print("Network is :" + str(networkName)) Debug
                netvar = str(networkName)
            else:
                # print("Network: doesn't exist") Debug
                netvar = "N/A"
                
            if i["Ports"] and 'PublicPort' in i["Ports"][0]:                             
                # print("PublicPort: Exists") Debug
                publicportvar = str(i["Ports"][0]["PublicPort"])
            else:
                # print("PublicPort: doesn't exist") Debug
                publicportvar = "N/A"
            
            if i["Ports"] and 'PrivatePort' in i["Ports"][0]:                        
                # print("PrivatePort: Exists") Debug
                privateportvar = str(i["Ports"][0]["PrivatePort"])
            else:
                # print("PublicPort: doesn't exist") Debug
                privateportvar = "N/A"

                
            with Cluster("Name: " + i["Image"]):
                
                with Cluster("Command: \n" + str(i["Command"]) + "\n" + "\n" + "Volume Name: " + "\n" + namevar2):

                    # print("Check for Network :" + netvar) Debug

                    if netvar == net:
                        Subcontainer0 = [Custom("IP: " + ipvar + "\n" + "Network: " + netvar +  "\n" + "Public Port: " + publicportvar + "\n" + "Private Port: " + privateportvar, "./Images/docker.png")] 

                        # print("Check for len") Debug
                        # print(len(Subcontainer0)) Debug

                        if len(Subcontainer0) != 0:
                            Subcontainer0 - bridge 
                        
    

                
            
