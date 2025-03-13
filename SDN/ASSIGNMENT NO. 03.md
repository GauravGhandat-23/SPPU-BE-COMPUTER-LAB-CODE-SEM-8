## Software Defined Networks (SDN)

## 3 Create a SDN environment on Mininet and configure a switch to provide a firewall functionality using POX controller.
Ref: https://github.com/mininet/openflow-tutorial/wiki/Create- Firewall

# SDN Firewall Using Mininet and POX

This project demonstrates how to create a Software-Defined Networking (SDN) environment using Mininet and configure a switch to act as a firewall using the POX controller.

---

## **Prerequisites**
Ensure you have the following installed:
- Ubuntu (or a Linux-based OS)
- Mininet
- Python3
- POX controller

---

## **1. Install Mininet and POX**
### **Install Mininet**
```sh
sudo apt update
sudo apt install mininet -y
```
Verify the installation:
```sh
sudo mn --test pingall
```

### **Clone POX Controller**
```sh
git clone https://github.com/noxrepo/pox.git
cd pox
```

---

## **2. Create a Mininet Topology**
Run the following command to start Mininet with a simple topology:
```sh
sudo mn --topo single,3 --mac --controller=remote
```
This creates a topology with 1 switch and 3 hosts.

---

## **3. Configure POX Controller as a Firewall**
Navigate to the POX directory:
```sh
cd ~/pox
```
Create a new Python script for the firewall:
```sh
nano ext/firewall.py
```

Paste the following code:
```python
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class SimpleFirewall (object):
    def __init__ (self):
        core.openflow.addListeners(self)

    def _handle_ConnectionUp (self, event):
        log.info("Firewall is enabled on %s", event.connection)

        # Block all traffic from h1 (10.0.0.1) to h2 (10.0.0.2)
        block_rule = of.ofp_match()
        block_rule.dl_type = 0x0800  # IP traffic
        block_rule.nw_src = "10.0.0.1"
        block_rule.nw_dst = "10.0.0.2"

        msg = of.ofp_flow_mod()
        msg.match = block_rule
        event.connection.send(msg)

        log.info("Blocking traffic from 10.0.0.1 to 10.0.0.2")

def launch ():
    core.registerNew(SimpleFirewall)
```
Save and exit (`Ctrl + X`, then `Y` and `Enter`).

---

## **4. Start the POX Controller**
Run the POX controller with the firewall module:
```sh
cd ~/pox
sudo python3 pox.py log.level --DEBUG forwarding.l2_learning firewall
```

---

## **5. Test the Firewall in Mininet**
Open another terminal and start Mininet:
```sh
sudo mn --topo single,3 --mac --controller=remote
```

Test connectivity between hosts:
```sh
h1 ping h2
```
Traffic from `h1` to `h2` should be blocked.

---

## **6. Verify Logs**
Check the POX terminal logs to confirm firewall rules are applied:
```sh
INFO:Firewall is enabled on <switch>
INFO:Blocking traffic from 10.0.0.1 to 10.0.0.2
```

---

## **Customization**
- Modify `nw_src` and `nw_dst` in the `firewall.py` script to block/allow different hosts.
- Extend the script to allow specific traffic types or implement a dynamic firewall.

---

## **Conclusion**
This setup successfully creates an SDN environment with a POX-based firewall that blocks specific traffic. You can modify the script to allow or block additional traffic based on your requirements.
