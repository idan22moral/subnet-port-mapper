import re
import subprocess as sp
import pprint

IP = 0
MAC = 1


def get_ports_by_ip(ip: str):
    ports = {}
    nmap_output = sp.getoutput(f'nmap --top-ports 100 {ip}')
    ports_data = list(filter(lambda line: " open " in line,
                             nmap_output.split('\n')[5:-3]))

    if len(ports_data) > 0:
        for line in ports_data:
            port, rest = line.split('/')[:2]
            rest = rest.split(' ')
            over = rest[0]
            protocol = rest[-1]
            ports[port] = {'type': over, 'protocol': protocol}
        return ports
    return None


def get_open_ports_in_subnet():
    hosts = {}
    # get information about the addresses in the subnet using the ARP tool
    raw_arp_data = re.split(
        r'\s+\n?', sp.getoutput('arp -a').split('Type')[1])[1:-1]
    zipped_arp_data = list(
        zip(raw_arp_data[::3], raw_arp_data[1::3], raw_arp_data[2::3]))
    # remove all the static IPs in the subnet
    filtered_arp_data = filter(
        lambda x: x if x[2] == 'dynamic' else None, zipped_arp_data)

    for endpoint in filtered_arp_data:
        ports = get_ports_by_ip(endpoint[IP])

        if ports:
            hosts[endpoint[IP]] = {
                'MAC': endpoint[MAC],
                'ports': ports
            }
    return hosts


if __name__ == "__main__":
    pprint.pprint(get_open_ports_in_subnet())
