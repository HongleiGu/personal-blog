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
# Basic Concepts

**Circuit switched network** need to establish a connection, reserve all the necessary resources and transfer through the dedicated link throughout their conversation, the connection is destroyed upon completion(little processing needed after connection, inefficient since the resources are blocked after connection); **packet switched network** packs all data in packets, use switch/router to operate on individual packets(no setup cost, better utilisation);

**Protocols** are set of rules that prescribe the layout and the meaning of packets, and the order in which packets should be send;**Services**: set of primitives that a layer provides to the layer above it.

**Layer model**: **Application Layer**: defines applications functionality and message formats (CNS, SMTP, FTP,HTTP/HTTPS...)**Transport Layer**:offers services connection-oriented/connectionless, provides the actual networks interface to applications**Network layer(layer3)**: describes how routing (and congestion) is to be done;**Data Link layer(layer2)**: use **CRC checksum** and to detect transmission errors and use **MAC** to specify how computers can share a common channel, **Physical Layer**: how data is transferred in phsyical manner

**Connection-oriented**: the telephone model, establish a connection then exchange data and then release the connection, circuit switch is a form of connection-oriented protocol;**Connection less**: The postal model: data packed in "envelopes", the destination has been written and the content is send to the dest, packet switch is a form of connectionless protocol

**Units**:$1GB = 10^3MB = 10^6KB = 10^9B = 8*10^9b$, $1TB = 10^{12}B$, $1GiB = 2^{10}MiB = 2^{20}KiB = 2^{30}B = 2^{33}b$

