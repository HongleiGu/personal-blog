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
# Device Types:
## 1.

**Which of the following are typically a character device?**

- DRAM ($\times$, DRAM is a memory)
- Serial Port ($\surd$, in a Serial Port, data is transmitted bit by bit, so character)
- Keyboard ($\surd$, this is of course, you type char by char)
- Hard Disk Drive ($\surd$, if character device, then likely bad file)
- SSD ($\surd$, same reason)
- Printer ($\surd$, before printing the printer does not know the size of the file to print)
- Mouse ($\surd$, you can only click once at a time)
- Network Interface Card ($\times$, NIC, transfer data in packets, packets has variable size, but they have to transfer packet in a whole)

## 2.

**Which of the following are typically a block device?**

- DRAM ($\times$, DRAM is a memory)
- Serial Port ($\times$, in a Serial Port, data is transmitted bit by bit, so character)
- Keyboard ($\times$, this is of course, you type char by char)
- Hard Disk Drive ($\surd$, the blocks are like pages, if it ened a large file then send multiple blocks)
- SSD ($\surd$, same reason)
- Printer ($\times$, before printing the printer does not know the size of the file to print)
- Mouse ($\times$, you can only click once at a time)
- Network Interface Card ($\times$, NIC, transfer data in packets, packets has variable size, but they have to transfer packet in a whole, it is neither a block device nor a character device)

## 3.
**Which of the following types of devices typically uses programmed I/O?**

Programmed I/O is a method of data transfer where the CPU actively controls the data transfer between the I/O device and memory. The CPU checks the status of the device and transfers data when it is ready.

The CPU will repeatly check(poll) the status of the I/O device

- DRAM ($\times$)
- Serial Port ($\surd$, in a Serial Port, data is transmitted bit by bit at a low data rate, so we need programmed I/O)
- Keyboard ($\times$)
- Hard Disk Drive ($\times$)
- SSD ($\times$)
- Printer ($\times$)
- Mouse ($\times$)
- Network Interface Card ($\times$)


## 4.

**Which of the following types of devices typically uses interrupt-driven I/O?**

Interruption-driven I/O is a method where the CPU is alerted (interrupted) by the I/O device when it is ready to send or receive data, rather than continuously polling the device.

It transfer data as a whole


- DRAM ($\times$)
- Serial Port ($\surd$, in a Serial Port, we interrupt wen the data rate is high)
- Keyboard ($\surd$, like the mouse, it interrupts the CPU, send the signal and then wait for the CPU to process)
- Hard Disk Drive ($\times$)
- SSD ($\times$)
- Printer ($\surd$, when the printer processed all the data, prints as a whole)
- Mouse ($\surd$, like the keyboard, interrupts the CPU, send the signal and then wait for the CPU to process)
- Network Interface Card ($\surd$, it sends in packets as a whole)

## 5.

**Which of the following types of devices typically uses DMA?**

DMA is a method where an external controller, the DMA controller, manages data transfers between the I/O device and memory without involving the CPU for each byte of data.

so all the memory-related device except DRAM

# Devices in Linux

This section covers device management in the context of the linux kernel 

You may find https://elixir.bootlin.com/linux/latest/source useful.

## 6.
**Which of the following callbacks in struct file_operations is used within the Linux kernel, when a user calls the function pipe()**

**Note: pipe() is not called over a VFS file.**

- open ($\surd$, pipe of course need to open a file)

- close ($\surd$, pipe of course need to close a file)

- read ($\surd$, pipe of course need to read a file)

- write ($\surd$, pipe of course need to write to a file)

- ioctl ($\surd$, this is io control, this is used when we want to access a device file)


## 7.
**A student would like to read from a file using asynchronous IO. Which C header must they include to use the aiocb struct?**

```C
#include <aio.h>
```

this is for async IOs

## 8.
**What is the file descriptor used by stdout (hint: a number)**

1, checkout the notes

we have three file descriptors by default

$\begin{array}
\text{file descriptor} & \text{input/output}\\
0 & \text{stdin}\\
1 & \text{stdout}\\
2 & \text{stderr}
\end{array}$

## 9.
**Where can files representing devices be found in the VFS?**

- /proc

- /dev ($\surd$, check the beginning, this is device)

- /sys


## 10.
**After typing 'ls -l /dev' in the terminal, a user spots a strange device with the following line**

``` 
crw-rw-rw-  1 root root   1,   3 Nov 21 22:08 ____ 
```

**When writing to this device, the data is discarded & the user cannot find it anywhere on the system, when attempting to read the user can only get 'EOF'**

**What is the name of this device?**

- tty

- null ($\surd$, cannot write to it, and not found, then the path is empty)

- stdout

- zero


## 11.
**Device drivers are modules that can be loaded and dynamically linked with the kernel as it runs (Loadable Kernel Modules).**

**What is the name of the kernel subsystem that loads and manages kernel loadable modules?**

- eBPF

- kmod ($\surd$, check out the LKM)

- kswapd

## 12.
**The kernel can cache data retrieved from a block device to improve performance of applications accessing the data.**

**For some applications, this reduces performance (e.g a database system managing its own in-memory cache does not need to added latency of checking kernel caches, and copying copies of data into this cache as well as its own).**

**When using open to access a device, which flag can be used to prevent the kernel from caching.**

O_DIRECT


# NAPI

This section covers the "New API" used by linux for improved high-speed networking. 

You may find https://wiki.linuxfoundation.org/networking/napi , https://en.wikipedia.org/wiki/New_API and https://elixir.bootlin.com/linux/latest/source/drivers/net/ethernet/intel/e1000 useful.

# 13.
**Which of the following method of IO are used by NAPI?**

- Programmed IO / Polling

- Interrupt Driven IO

- IO using Direct Memory Access (DMA)

all three are correct, see the document


## 14.
**Using interrupt driven IO for a driver allows for simple implementation & allows the handler to be immediately invoked upon the arrival of data, however when the rate of received data is high, the number of interrupts is high incurring considerable performance overhead.**

**Using programmed IO / polling to repeatedly check for data eliminates the overhead of interrupt processing, however the rate of polling is important (too high and time is wasted polling, too low and the latency between data being recieved and the driver handling it is too large).**

**How does the NAPI compromise to mitigate the disadvantages of both models.**

- NAPI uses an optimal polling rate to avoid the disadvantages of programmed IO, and hence does not use interrupt based IO or have it's disadvantages.

- NAPI significantly reduces the overhead of interrupts

- NAPI dynamically switches between interrupt driven and polling IO depending on the rate of packets recieved. ($\surd$)

## 15.
**Without NAPI, the kernel must handle every incoming packet. When the packets arrive at a higher rate than the kernel is able to handle them, what phenomenon occurs?**

- Reduced Latency

- Thrashing ($times$, $Here thrashing refers to constantly switching to interrupt handler, resulting in most of the system's time being spent handling interrupts. In memory management you will be familiar with thrashing being caused by a very high rate of page faults.)

- Squashing

- Packets are  $\surd$

## 16.
**The Intel e1000 ethernet driver can be found in drivers/ethernet/intel within the linux kernel repository. What does the e1000_probe function in e1000_main.c do?**

- Initialise the driver (hardware & software initialisation) $\surd$

- Checking the device is operational

- Checking if any packets are in the driver managed buffer

## 17.
**Which function in e1000_main.c is used for printing the device's registers, tx and rx rings?**

e1000_dump

# revision
## 18.
**A developer releases their own new operating system on github. They claim to use small pages (4KB pages) and support up to a terabyte of DRAM. Which of the following page table designs could they be using?**

- Hashed Page Table ($\surd$, If we assume that only pages in memory (not swapped out/paged-in) are stored, much like the inverted page table we can use the hashed page table. This is as the hashed page table will never be larger than the system's available memory (provided a page table entry is still smaller than 4KB). If all physical memory is being used, and more user-pages are added, the same number of pages will be paged-out and the number of entries in the page table will remain the same.)

- Single Level Page Table ($\times$, this cannot contain 1TB data)

- Inverted Page Table ($\surd$, An inverted page table only needs one entry per frame, hence as each frame requires an 8 byte entry in the page table and is 4KB large 8/(4KB) = 0.195% of system memory must be allocated to a single page table.)


## 19.
**During the synchronisation topic of this module, which memory model was assumed.**

- Release-Acquire Consistency

- Sequential Consistency $\surd$

- Coherence

## 20.
**A student is testing a FIFO page replacement simulator on a reference string of page accesses for a coursework. After increasing the number of available frames the number of page faults increases.**

**What is the name for this phenomena? (assume the student simulator is bug-free)**

- Belady's Anomaly ($\surd$, checkout notes9)

- Thrashing

- Working Set Transition