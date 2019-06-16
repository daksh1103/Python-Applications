import psutil
import logging
import owncloud
import sys
import json
import os
import paho.mqtt.client as paho
from threading import Thread


def on_publish(client, userdata,mid):
    print ("Message published with mid value as ...."+str(mid))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
def on_connect1(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("AI/TEST/RESTART")
def on_message(client, userdata, msg):
    a=str(msg.payload.decode("utf-8"))
    restart(a)
    

def restart(a1):
    oc = owncloud.Client('https://files.aparinnosys.com')
    oc.login('test.python','@parinnosys')
    oc.get_file('/IEC/'+a1, str(sys.argv[0]))
    os.execv(sys.executable, ['python3'] + sys.argv)
def func1():
    while(True):
        a=input()
        if a.upper()=='YES':
            file1=input('Enter the updated file with correct version number ')
            client1.publish("AI/TEST/RESTART",file1,qos=1)

        
if __name__ == '__main__':
    client1= paho.Client() #create client object
    client1.on_connect = on_connect
    client1.on_publish =on_publish #assign function to callback
    client1.username_pw_set("mqtt_innformer",password="7WDk9Xi7ICbVzDIAo71F")
    client1.connect("kvbmqtt.innoculate.in",port=1883)
    client1.loop_start()
    client = paho.Client()
    client.on_connect = on_connect1
    client.on_message = on_message
    client.username_pw_set("mqtt_innformer",password="7WDk9Xi7ICbVzDIAo71F")
    client.connect("kvbmqtt.innoculate.in", 1883, 60) #subscriber and Mosquitto sit in same server
    Thread(target = func1).start()
    client.loop_forever()