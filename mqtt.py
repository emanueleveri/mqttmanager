import paho.mqtt.client as mqtt
client = mqtt.Client(client_id="myTime")

client.connect("broker.hivemq.com", 1883, 60)
def read(topic):
    client.on_message = on_message
    client.subscribe(str(topic))
    client.loop_forever()

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    
def publish(topic,message):
    res = client.publish(str(topic),str(message))


print("MQTT Manager ")
i=0
funzioni=["iscriversi","Pubblicare"];
error = True
for i in range (0,2):
    print(i+1,"\t"+funzioni[i])
    i+=1
    
while error==True:
    continua='s'
    choose=int(input("Scegli >> " ))
    if choose==1:
        topic=input("Inserire il topic ")
        read(topic)

    elif choose==2:
        topic = input("Inserire il nome del topic a cui iscriversi ")
        while continua=='s' or continua=='S':
            message =input("Inserire il messaggio da inviare ")
            publish(topic,message)
            continua=input("continuare ? s/n >> ")
    else:
        print (" Numero non corrispondente ")
        
