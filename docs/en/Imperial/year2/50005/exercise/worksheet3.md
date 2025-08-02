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

# Q01
**You type a website URL in your Web browser URL bar, you hit Enter and magic happen behind the scenes**

## i.

**Briefly describe how DNS facilitates the communication between a Web browser and a Web server**

DNSis a middleware that when the web brwoser tries to access the url, it will return the real IP address of the URL for ht web browser to access

## ii
**Briefly descirbe the role of CDNs in improving the performance of websites**

CDNs allow the website to include resource from another web server quickly, alllowing for more concise websites and the ease to load the website.

# Q02

**True or False?**

## i.
**HTTP is a stateless protocol used for transferring hypertext documents such as webpages**

True

## ii.
**SMTP is primarily used for retrieving email from a server to a client device**

True

<span style="color:red">No, SMTP sends and POP3, IMAP receive</span>

## iii.
**DNS operates at the Transport Layer of the OSI model**

False, should be the application layer

## iv.
**A CDN improves website perofrmance by caching content geographically distributed servers**

True

## v.
**HTTPS uses encryption to ensure secure communication between a Web brower and a Web server**

True

## vi.
**The role of DNS is to establish a direct physical connection between two devices on a network**

False, we need DNS to ensure safe routing

## vii.

**SMTP, DNS, HTTP are all protocols that function at the OSI Application layer**

False, Transport layer

<span style="color: red">correct</span>

# Q03:
**Tanenbaum, Ch7Q20: “You are building an instant messaging application for your computer networks lab assignment. The application must be able to transfer ASCII text and binary files. Unfortunately, another student on your team already handed in the server code without implementing a feature for transferring binary files. Can you still implement this feature by only changing the client code?”**

Yes, we can encrypt the files with base64

# Q04
**Exam 2017: “You log into your Linux system and use a terminal command to find the mail server of "diktion.net", and you learn that it is "smtp.diktion.net". You then use another terminal command and connect to that mail server in order to test – using plain text instructions – whether it allows unauthorised emailing. Write, in full, the commands and instructions.”**

```
HELLO diktion.net
DATA

```

## i.
One command for finding the mail server
```
nslookup -type=NS smtp.diktion.net
```

## ii.
Another command for connecting and communicating with it in plain text

```
telnet smtp.diktion.net 80
```
## iii.

And finally the SMPT instructions
```
HELO diktion,net
MAIL FROM <someone@example.com>
DATA
Subject: test
test
```
# Q05
**Exam 2019: “You execute your Web browser, type "AmazingMovies.org" in the address bar, hit the Enter key and, after a few seconds, the website loads. Briefly describe, step-by-step, what happened after you hit Enter. (Assume that you are not using a local proxy, and that the website is using a CDN. State any additional assumptions).”**

the web browser tries to find the IP address of the server in the DNS, then when loading the website, it attempts to load the file with CDN.


<span style="color:red">DNS Request => DNS Response with the IP of the nearest CDN => HTTP GET Request to the returned IP of the CDN => HTTP Response with the HTML/images/etc. from the CDN => Web browser shows the page </span>

<span style="color:red">Important Note: At this stage (Week 3), you are not required to mention anything TCP/UDP related, but, if this were a Coursework or Exam question after Week 4, you would indeed need to include those as well.</span>
