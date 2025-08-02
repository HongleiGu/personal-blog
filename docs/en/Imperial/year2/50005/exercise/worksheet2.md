---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# Q02:
**True or False**

## i.
**A computer network lets device share data with each other**

True

## ii.
**You need an Internet connection to have a network**

False, no LAN does not require Internet access

## iii.
**Networks are only used for business, not for homes**

False

## iv.
**Wi-Fi is the only way to connect devices to a network.**

False, no, you can use a cable
## v.
**A network can include devices like printers and smartphones**

True

## vi
**The Internet is an exmaple of a very large network**

True

## vii.
**All networks require wires to work**

False, no Wifi are wireless

## viii.
**A single computer connected to nothing else is part of network**

False

<span style="color:red">Yes and No: it is False if you just answer at face value, but True if you consider a virtual/local network</span>

# Q03 
Exam 2024: **“You find a large room containing four identical VR headsets, sharing the same network connection that ends up in a Fibre-To-The-Premises 2-Gbps router. Each headset is linked to a miniPC, using its integrated wireless 802.11ac 1,300-Mbps-only NIC card to gain Internet access via the Wireless Access Point of the fibre router. The headset-to-miniPC link is achieved via a USB3.1 port at 5-Gbps where the headset USB dongle connects to, exchanging data with the wireless headset via 5G, at a theoretical maximum speed of 20Gbps. Each headset allows you to set its 5G connection speed to one of the following four values: 125-Mbps, 500-Mbps, 1-Gbps, 2-Gbps. What is the ideal speed for parallel use of all four headsets and why? Justify your answer, and state any reasonable assumptions.”**

The maximum speed is bottlenecked by the lowest speed

The transfer speed of the headset to miniPC is 5Gbps

and the total transfer speed of the 4 headset is 2-Gbps

so the ideal speed is 2-Gbps /4 = 500Mbps

assuming nothing else is using the same network

# Q04

**"You find yourself in the digital twin of a sushi restaurant. You can see that there is a conveyor belt where four sushi chefs place dishes on, for diners to choose what they like. You are able to measure that the belt can support a constant transmission rate of 0.0336Mbps, while each dish has a constant packet length of 2981B, with the four chefs combined averaging about 12 dishes (i.e., packets) per minute.**

## i.
**Calculate the traffic intensity. **

in one minute, the four chefs can make 12 sushi, and each sushi has 2981B in size

so the intensity is $\frac{12 * 2981B}{60s} = 596.2B/s = 596.2Bps$



## ii. 
**What is the highest possible number of dishes per minute that this conveyor belt can support before queuing delay becomes a real problem? Type out all your calculations in full, and state any reasonable assumptions.”**


assume the maximum number of dish per min to be x

then $\frac{x * 2981B}{60s} = 0.0336Mbps = 33.6KBps = 33600Bps$

so $x = \frac{33600 * 5}{2981} = 56.36$


