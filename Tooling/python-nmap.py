import nmap


nmScan = nmap.PortScanner()

output = nmScan.scan('127.0.0.1', '21-443')
print(output)
nmScan.command_line()

# run a loop to print all the found result about the ports
for host in nmScan.all_hosts():
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())
    for proto in nmScan[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nmScan[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
## https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap