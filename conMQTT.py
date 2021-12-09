import machine
import time
import ubinascii
import webrepl
from umqtt.simple import MQTTClient


#mqtt_server ='192.168.1.5'
mqtt_server ='10.6.0.26'
#mqtt_server ='172.16.200.88'

topic_sub ='TEST2'

#port      =10890
#port      =10884
port      =1883

#topic_pub ='TEST1'
topic_pub ='iot_team1'

client_id ="team_1"

counter =0
last_message=0

client = None

def connect():
    import network
 
 #   ssid = "mokkula_925936"
 #   password =  "12345678"
    ssid = 'SOURCE'
    password =  'Pelle!23'

    print("Start connecting")
       
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        print(station.ifconfig())
        return 1
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    tp=(station.ifconfig())
    print("My IP is ="+tp[0])
 

def mqtt_connect():
  global client_id, mqtt_server, topic_sub
  global client
  client = MQTTClient(client_id, mqtt_server,port)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to: %s MQTT broker, Port: %s' % (mqtt_server,  port))
  print('subscribed to Topic :%s ' % (topic_sub))


def sub_cb():
    print("call back")

def reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()


def send():

    global client

#    msg = 'IOTJS={\"S_name\":\"Team1_temp\",\"S_value\": %d }' % value
    msg = ' This is my team 1 message'
   
    client.publish(topic_pub, msg)
    print(msg)
             

print(" WLAN start connecting ")
connect()
print(" MQTT start connecting ")
mqtt_connect()
print(" MQTT start sending message")
while True:
    send()
    print(" MQTT message send") 
