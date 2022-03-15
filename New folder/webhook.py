import requests
import json
import sys
import os 
import psutil
import subprocess
import time
import re
import collections
URL = 'https://discord.com/api/webhooks/916718551400861836/L4vw9dQkEelYi-7f7WDKckOI517lqFneLXMoBN8PeiHBR1T-q9id5Cw9luWWOnye6up5'
true = 'true'
false = 'false'


uptime = subprocess.getoutput("uptime -p")
cpuload=str(round(float(os.popen('''top -n 1 -b | awk '/^%Cpu/{print $2}' ''').readline())))
cpucores = psutil.cpu_count() 
ram = psutil.virtual_memory() 

# [Getting most frequesnt eye pee
count1 = 0;
word1 = "";
maxCount1 = 0;
words1 = [];


file1 =open("/root/TCPDUMP/extra/sortingip.txt", "r")

for line in file1:
    string=line.lower().replace(',','.').replace('.','.').split(" ");
    for s in string:
        words1.append(s);
for i in range(0, len(words1)):
    count1 = 1;
    for j in range(i+1, len(words1)):
        if(words1[i] == words1[j]):
            count1 = count1 + 1;
            
    if(count1 > maxCount1):
        maxCount1 = count1;
        eyepee = words1[i];
# ]


# El Porte part 2 [
count3 = 0;
word3 = "";
maxCount3 = 0;
words3 = [];


file =open("/root/TCPDUMP/extra/destport.txt", "r")

for line in file:
  # replacing shit bc kool
    string=line.lower().replace('80','80/HTTP').replace('443','443/HTTPS').replace('22','22/SSH').replace('1194','1194/OVPN').replace('53','53/DNS').split(" ");
    for s in string:
        words3.append(s);
for i in range(0, len(words3)):
    count3 = 1;
    for j in range(i+1, len(words3)):
        if(words3[i] == words3[j]):
            count3 = count3 + 1;
            
    if(count3 > maxCount3):
        maxCount3 = count3;
        word3 = words3[i];
# ]


# El Porte
count2 = 0;
word2 = "";
maxCount2 = 0;
words2 = [];


file1 =open("/root/TCPDUMP/extra/destport.txt", "r")

for line in file1:
    string=line.lower().replace(',','.').replace('.','.').split(" ");
    for s in string:
        words2.append(s);
for i in range(0, len(words2)):
    count2 = 1;
    for j in range(i+1, len(words2)):
        if(words2[i] == words2[j]):
            count2 = count2 + 1;
            
    if(count2 > maxCount2):
        maxCount2 = count2;
        destport = words2[i];
# ]


# El Porte2
count4 = 0;
word4 = "";
maxCount4 = 0;
words4 = [];


file1 =open("/root/TCPDUMP/extra/srcport.txt", "r")

for line in file1:
    string=line.lower().replace(',','.').replace('.','.').split(" ");
    for s in string:
        words4.append(s);
for i in range(0, len(words4)):
    count4 = 1;
    for j in range(i+1, len(words4)):
        if(words4[i] == words4[j]):
            count4 = count4 + 1;
            
    if(count4 > maxCount4):
        maxCount4 = count4;
        srcport = words4[i];
# ]

# My horrible attempt at ammount of attacking ips [
filename="/root/TCPDUMP/nigga/infoforfing.txt"
linescount=0
with open (filename,'r') as files:
  for i in files:
    linescount=linescount+1
# ]

file = open(sys.argv[1], "r")
capture_file = file.read()

definitionVer = "1.0.0"
attack_types = {
  "(UDP)": "17    ",
  "(ICMP)": "1    ",
  "(ICMP Destination Unreachable)": "1,17    ",
  "(IPv4/Fragmented)": "4   ",
  "(GRE)": "47    ",
  "(IPX)": "111   ",
  "(AH)": "51   ",
  "(ESP)": "50    ",
  "(OpenVPN Amp)": "17   1194",
  "(VSE)": "17    27015",
  "(ANY DNS Query Amp)": "00ff0001",
  "(NTP Amp)": "17   123",
  "(Chargen Amp)": "17   19",
  "(MDNS Amp)": "17    5353",
  "(BitTorrent Amp)": "17    6881",
  "(CLDAP Amp)": "17   389",
  "(STUN Amp)": "17    3478",
  "(MSSQL Amp)": "17   1434",
  "(SNMP Amp)": "17    161",
  "(WSD Amp)": "17   3702",
  "(ARD Amp)": "17   3283",
  "(SSDP Amp)": "17    1900",
  "(Plex Amp)": "17    32414",
  "(DVR Amp)": "17    37810",
  "(NETBIOS Amp)": "17   137",
  "(CoAP Amp)": "17    5683",
  "(Fivem Amp)": "17   30120",
  "(Halo Amp/1)": "17   2302",
  "(Halo Amp/2)": "17   2303",
  "(Tftp Amp)": "17   69",
  "(KillAll/1)": "6   443",
  "(SYN Flood To SSH)": "0x00000002   22",
  "(SYN,ACK Flood To SSH)": "0x00000012   22",
  "(KillAll/2)": "6   80",
  "(QOTD Amp)": "17    17",
  "(ISAKMP Amp)": "17    500",
  "(IPMI Amp)": "17    623",
  "(UdpHex)": "2f78",
  "(0x00)": "0000000000000000000",
  "(0xff)": "fffffffffff",
  "(TCP/SYN,ACK)": "0x00000012",
  "(TCP/PSH,ACK)": "0x00000018",
  "(TCP/RST,ACK)": "0x00000014",
  "(TCP/FIN)": "0x00000001",
  "(TCP/SYN)": "0x00000002",
  "(TCP/PSH)": "0x00000008",
  "(TCP/URG)": "0x00000020",
  "(TCP/RST)": "0x00000004",
  "(TCP/ACK)": "0x00000010",
  "(TCP/SYN,ECN,CWR)": "0x000000c2",
  "(TCP/SYN,ECN)": "0x00000042",
  "(TCP/SYN,CWR)": "0x00000082",
  "(TCP/SYN,PSH,ACK,URG)": "0x0000003a",
  "(TCP/SYN,ACK,ECN,CWR)": "0x000000d2",
  "(TCP/PSH,ACK,URG)": "0x00000038",
  "(TCP/FIN,SYN,RST,PSH,ACK,URG)": "0x0000003f",
  "(TCP/RST,ACK,URG,CWR,Reserved)": "0x000004b4",
  "(TCP/SYN,PSH,URG,ECN,CWR,Reserved)": "0x000004ea",
  "(TCP/FIN,RST,PSH,ECN,CWR,Reserved)": "0x00000ccd",
  "(TCP/FIN,RST,PSH,ACK,URG,ECN,CWR,Reserved)": "0x00000cfd"
}

attack_type = ''

for occurrences in attack_types:
  
  number = capture_file.count(attack_types[occurrences])
  if number > 2000:
    attack_type = attack_type + " " + occurrences

if attack_type == '':
  attack_type = "Could not define attack type"

# [Established connections counter
established = subprocess.getoutput("netstat -ant | grep ESTABLISHED | awk '{print $6}' | cut -d: -f1 | sort | uniq -c | sort -rn")
# ]

# [ PPS Counter
a = subprocess.getoutput("grep eth0: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'")
time.sleep(1)
b = subprocess.getoutput("grep eth0: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'")
pps = int(a) - int(b)
pps = str(pps)
pps = pps.replace("-", "")
# ]

# [ MBPS 
n = open("/sys/class/net/eth0/statistics/rx_bytes", "r")
n1 = n.read()
n.close()
n1 = int(n1)
time.sleep(1)
n2 = open("/sys/class/net/eth0/statistics/rx_bytes", "r")
n3 = n2.read()
n2.close()
n3 = int(n3)
byt2 = n1 - n3

mbps = byt2 / 125000
mbps = str(mbps)
mbps = mbps.replace("-", "")
# ]

# Discord Webhook [
payload = {
  "embeds": [
    {
      "title": "Attack detected",
      "description": "Details:",
      "color": 0000000,
      "fields": [
        {
          "name": ":computer: Server",
          "value": "CANADA-1",
          "inline": true
        },
        {
          "name": ":book: IP Address:",
          "value": "Hidden",
          "inline": true
        },
        {
          "name": "<a:load:906778673917620256> CPU Usage %:",
          "value": cpuload,
          "inline": true
        },
        {
          "name": "<a:load:906778673917620256> CPU Cores:",
          "value": cpucores
        },
        {
          "name": "<a:load:906778673917620256> Uptime:",
          "value": uptime,
          "inline": true
        },
        {
          "name": "<:port:916719924599214150> Attacked Port:",
          "value": destport,
          "inline": true
        },
        {
          "name": "<:port:916719924599214150> Source port:",
          "value": srcport,
          "inline": true
        },
        {
          "name": "<:attack:907786718701322270> Attack Type:",
          "value": attack_type
        },
        {
          "name": "<:server:907407963013148693> Established Connections:",
          "value": established
        },
        {
          "name": "<:server:907407963013148693> Most frequent Ip:",
          "value": eyepee
        },
        {
          "name": "<:server:907407963013148693> Estimated Attacking IpsCount:",
          "value": linescount
        },
        {
         "name": "<:fastdownload:907411168170229822> Mbit/s:",
         "value": mbps,
         "inline": true
        },
        {
         "name": "<:fastdownload:907411168170229822> Packet/s:",
         "value": pps,
         "inline": true
        }
      ],
      "author": {
        "name": "igamine trying to ddoz",
        "icon_url": "https://cdn.discordapp.com/attachments/890644370049626142/890904026139484170/icons8-error-cloud-96.png"
      },
      "footer": {
        "text": f"{sys.argv[2]}",
        "url": "https://cdn.discordapp.com/attachments/890644370049626142/890904247548383273/icons8-connected-no-data-96.png"
      },
      "thumbnail": {
        "url": "https://cdn.discordapp.com/attachments/890644370049626142/890894951523680256/icons8-bell-curve-96.png"
      }
    }
  ]
}
header_data = {'content-type': 'application/json'}
requests.post(URL, json.dumps(payload), headers=header_data)
# ]
print (f"[40;34m[[40;35m+[40;34m][40;37mAttack Details Sent To Webhook![40;34m[[40;35m+[40;34m][40;37m")
print ("Attack Stats:")
print (f"CPU Load: {cpuload} %")
print (f"Mbps: {mbps}")
print (f"Established Connections {established}")
print (f"Attack Type: {attack_type}")
print (f"Attacked Port: {destport}")
print (f"Source Port: {srcport}")