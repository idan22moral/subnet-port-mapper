# subnet-port-mapper
Super simple tool that uses ARP and NMAP to map ports in your subnet.  
Prints the subnet port map in JSON format.  
It should work cross-platform as long as you have the prerequisites.

## Usage
Simply run this file with python:
```sh
$ python3 subnet_port_mapper.py
```

## Prerequisites
Make sure you have the following programs installed:
* Python 
* Nmap
* `arp`

## Notes
If you're using WSL 1 - modify the code to use `arp.exe` instead of `arp`.
