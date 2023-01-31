import nmap


nmScan = nmap.PortScanner()

output = nmScan.scan('127.0.0.1', '21-443')
print(output)
nmScan.command_line()

## https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap