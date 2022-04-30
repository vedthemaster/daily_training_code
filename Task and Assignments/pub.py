

import json

import numpy as np

import datetime

import time

import paho.mqtt.client as mqtt


client = mqtt.Client()


# Callback function-executed when the program successfully connects to the broker


def on_connect(client, userdata, flags, rc):


print("Connected with flag"+str(flags))

client.subscribe("test")


# Callback function-executed when the program gracefully disconnects from the broker


def on_disconnect(client, userdata, rc):


print("Disconnected with result code" + str(rc) + "userdata"+str(userdata))


# Callback function-executed whenever a message is published to the topics  tat


# this program is subscribed to


def on_message(client, userdata, msg):


print("msg.topic,str(msg.payload)", "retain",
      msg.retain, "qos", msg.qos, str(userdata))


# Setting callback functions for various client actions


client.on_connect = on_connect

client.on_message = on_message

client.on_disconnect = on_disconnect


# Reading the configuration file

f = open("config.json")

config = json.loads(f.read())

f.close()


# Initialising devices from the config.json file and assigning device_ids to each device

device_config = []

for devices in config['devices']:

for n in range(devices['device_count']):

dev = {}

dev['device_id'] = devices['type']+'_'+str(n)

dev['device_type'] = devices['type']

dev['publish_frequency'] = devices['publish_frequency']

dev['std_val'] = devices['std_val']

dev['publish_topic'] = devices['publish_topic']

device_config.append(dev)


# Connecting to broker

client.connect(host=config["broker_host"],
               port=config["broker_port"], keepalive=60)

client.username_pw_set(username="intern", password="ub6304")


''' 

Start the MQTT client non-blocking loop to listen the broker for messages 

in subscribed topics and other operations for which the callback functions 

are defined 

'''

client.loop_start()


clock = 0


while True:

try:

    # Iterating through the items in device configuration dictionary, every second

time.sleep(1)

clock = clock+1

for devices in device_config:

if clock % devices['publish_frequency'] == 0:

    print("Published to devices/" + devices["device_type"])

# Initialize a dictionary to be sent as publish message

message = {}


# Generate timestamp in YYYY-MM-DD HH:MM:SS format

prevday_timestamp = datetime.datetime.now() - datetime.timedelta(days=1)

#message["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

message["timestamp"] = prevday_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")

message["device_id"] = devices["device_id"]

message["device_type"] = devices["device_type"]

# Generate a random value using normal distribution function of the

# configured standard value for the given device type

message["value"] = round(np.random.normal(devices["std_val"], 2), 2)

# Publish the message


client.publish(devices["publish_topic"], json.dumps(message))


except KeyboardInterrupt:

client.disconnect()

client.loop_stop()

break
