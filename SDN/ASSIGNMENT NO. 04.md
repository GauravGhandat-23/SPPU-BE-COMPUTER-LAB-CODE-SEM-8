## 4 Using Mininet as an Emulator and POX controller, build your own internet router. Write simple outer with a static routing table. The router will receive raw Ethernet frames and process the packet forwarding them to correct outgoing interface. You must check the Ethernet frames are received and the forwarding logic is created so packets go to the correct interface. Ref: https://github.com/mininet/mininet/wiki/SimpleRouter

# Mininet POX Router

This project sets up a simple internet router using Mininet as an emulator and POX as the controller. The router processes raw Ethernet frames and forwards packets based on a static routing table.

## Prerequisites
Ensure you have the following installed:
- Ubuntu/Linux environment
- Python 3
- Mininet
- POX Controller

## Installation & Setup

### 1. Install Mininet
```bash
sudo apt-get update
sudo apt-get install mininet
```

### 2. Clone the POX Controller Repository
```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

### 3. Create Mininet Topology
Create a new file `router_topo.py` and add the following:

```python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_topology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    r1 = net.addSwitch('s1')

    h1 = net.addHost('h1', ip='192.168.1.1/24', mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', ip='192.168.2.1/24', mac='00:00:00:00:00:02')

    net.addLink(h1, r1)
    net.addLink(h2, r1)

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
```

### 4. Implement the POX Controller
Create a new file `simple_router.py` inside the `pox/ext/` directory:

```python
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

ROUTING_TABLE = {
    "192.168.1.0/24": 1,
    "192.168.2.0/24": 2
}

class SimpleRouter(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if not packet.parsed:
            return

        src_ip = packet.next.srcip
        dst_ip = packet.next.dstip

        out_port = None
        for subnet, port in ROUTING_TABLE.items():
            if str(dst_ip).startswith(subnet.split('/')[0]):
                out_port = port
                break

        if out_port:
            msg = of.ofp_flow_mod()
            msg.match.dl_dst = packet.dst
            msg.actions.append(of.ofp_action_output(port=out_port))
            self.connection.send(msg)


def launch():
    def start_switch(event):
        SimpleRouter(event.connection)
    core.openflow.addListenerByName("ConnectionUp", start_switch)
```

## Running the Router

### 1. Start Mininet
```bash
sudo python3 router_topo.py
```

### 2. Start the POX Controller
```bash
cd pox
./pox.py log.level --DEBUG forwarding.l2_learning ext.simple_router
```

### 3. Test Packet Forwarding
In the Mininet CLI, test connectivity:
```bash
h1 ping h2
```

If everything is set up correctly, `h1` should be able to ping `h2` successfully.

## Features
- Static routing
- Packet forwarding based on a simple routing table
- Logs packet flow in POX controller
