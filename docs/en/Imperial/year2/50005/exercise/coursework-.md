---
level: Imperial
---
---
level: Imperial
---
---
level: Imperial
---
---
level: Imperial
---
---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# Q10

**Finally, you have been asked to design the LAN setup of an IoT R&D Institute. Their organisation has the following departments: HR (10 hosts), Sales (50 hosts), Research (10,000 hosts), Design (60,000 hosts). For each subnet write: i) its usable size, ii) its IP address (as a whole), iii) the IP of its gateway, iv) its broadcast address, and v) its subnet mask in decimal and CIDR. Use contiguous IPv4 address blocks for all subnets. (State any reasonable assumptions).**

Assumptions:

- we use 10.0.0.0/8 as private address space
- each subnet may be design to accommodate the number of host needed plus some additional addresses
- the gateway IP is the first usable IP address
- the broadcast IP is the last usable IP address (with every remaining bit to be 1)
- we exclude the gateway IP and the broadcast IP to avoid conflicts


design:

| Department | Usable size | IP address   | Gateway IP | Broadcast address | subnet mask     | CIDR |
| ---------- | ----------- | ------------ | ---------- | ----------------- | --------------- | ---- |
| HR         | 14          | 10.0.0.0/28  | 10.0.0.1   | 10.0.0.15         | 255.255.255.240 | /28  |
| Sales      | 62          | 10.0.0.16/26 | 10.0.0.17  | 10.0.0.79         | 255.255.255.192 | /26  |
| Research   | 16382       | 10.0.0.80/18 | 10.0.0.81  | 10.0.63.255       | 255.255.192.0   | /18  |
| Design     | 65536       | 10.1.0.0/16  | 10.1.0.1   | 10.1.255.255      | 255.255.0.0     | /16  |
