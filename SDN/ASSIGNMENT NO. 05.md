## Software Defined Networks (SDN)

### 5 Emulate and manage a Data Center via a Cloud Network Controller: create a multi-rooted tree-like (Clos) topology in Mininet to emulate a data center. Implement specific SDN applications on top of the network controller in order to orchestrate multiple network tenants within a data center environment, in the context of network virtualization and management. Ref:https://opencourses.uoc.gr/courses/pluginfile.php/13576/mod_resource/content/2/exercise 5.pdf

**# Stepwise Guide: Emulating and Managing a Data Center via a Cloud Network Controller**

## **Step 1: Install Required Software**
Ensure you have the necessary dependencies installed:
- **Mininet** (for network emulation)
- **Open vSwitch (OVS)** (for SDN-enabled switches)
- **POX or Ryu** (for SDN controller implementation)
- **Python 3**
- **Ubuntu 20.04+ (recommended)**

Commands to install:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y mininet openvswitch-switch
sudo pip3 install ryu
```

## **Step 2: Create a Multi-Rooted Clos Topology in Mininet**
Write a Python script to generate a Clos topology.
Example (`clos_topo.py`):
```python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

class ClosTopo(Topo):
    def build(self, spine=2, leaf=2, hosts_per_leaf=2):
        spine_switches = [self.addSwitch(f's{i}') for i in range(1, spine+1)]
        leaf_switches = [self.addSwitch(f'l{i}') for i in range(1, leaf+1)]

        for i, leaf in enumerate(leaf_switches):
            for spine in spine_switches:
                self.addLink(leaf, spine)
            for h in range(1, hosts_per_leaf+1):
                host = self.addHost(f'h{i+1}{h}')
                self.addLink(leaf, host)

if __name__ == '__main__':
    setLogLevel('info')
    topo = ClosTopo()
    net = Mininet(topo=topo, controller=RemoteController)
    net.start()
    CLI(net)
    net.stop()
```
Run the script:
```bash
sudo python3 clos_topo.py
```

## **Step 3: Configure an SDN Controller**
Use **Ryu** or **POX** to implement SDN-based network orchestration.

### Example: Launching Ryu Controller
```bash
ryu-manager ryu.app.simple_switch_13
```

Alternatively, for POX:
```bash
cd pox
./pox.py forwarding.l2_learning
```

## **Step 4: Implement Network Virtualization**
Use **VXLAN** or **OpenFlow rules** for tenant isolation. Example of adding VXLAN:
```bash
ovs-vsctl add-br br0
ovs-vsctl add-port br0 vxlan0 -- set interface vxlan0 type=vxlan options:remote_ip=192.168.1.2
```

## **Step 5: Test Network Connectivity**
Run `pingall` from the Mininet CLI:
```bash
mininet> pingall
```
Run `iperf` for performance testing:
```bash
mininet> iperf h1 h2
```

---

# README.md (Markdown Format)

## **Data Center Emulation with Mininet & SDN**

### **Project Description**
This project emulates a data center network using Mininet and an SDN Controller. It implements a Clos topology to support multiple network tenants, utilizing OpenFlow-based network management for virtualization.

### **Installation & Setup**
#### **Prerequisites**
- Ubuntu 20.04+
- Mininet
- Open vSwitch (OVS)
- SDN Controllers: Ryu or POX

#### **Installation Steps**
```bash
sudo apt update && sudo apt install -y mininet openvswitch-switch python3-pip
sudo pip3 install ryu
```

### **Running the Topology**
```bash
sudo python3 clos_topo.py
```

### **Starting the SDN Controller**
For Ryu:
```bash
ryu-manager ryu.app.simple_switch_13
```
For POX:
```bash
cd pox
./pox.py forwarding.l2_learning
```

### **Testing**
From the Mininet CLI:
```bash
mininet> pingall
mininet> iperf h1 h2
```

### **License**
MIT License

