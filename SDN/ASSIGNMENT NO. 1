## Software Defined Networks (SDN)

### 1. Prepare setup for Mininet network emulation environment with the help of Virtual box and Mininet. Demonstrate the basic commands in Mininet and emulate different custom network topology(Simple, Linear, and Tree).View flow tables.

# Mininet Network Emulation Environment Setup

## Overview
This guide provides step-by-step instructions to set up a **Mininet** network emulation environment using **VirtualBox** and Ubuntu. It includes basic Mininet commands, network topology emulation, and viewing OpenFlow flow tables.

## Prerequisites
- **VirtualBox**: Download from [VirtualBox](https://www.virtualbox.org/)
- **Ubuntu (Server/Desktop)**: Download from [Ubuntu](https://ubuntu.com/download)
- **Minimum System Requirements**:
  - RAM: **2GB or more**
  - Disk Space: **20GB or more**

---

## Step 1: Install VirtualBox and Ubuntu
1. Install VirtualBox on your system.
2. Download the **Ubuntu ISO**.
3. Create a new Virtual Machine in VirtualBox:
   - Name: `Mininet-VM`
   - Type: `Linux`
   - Version: `Ubuntu (64-bit)`
   - Allocate **at least 2GB RAM** and **20GB storage**.
   - Attach the Ubuntu ISO and complete the installation.

---

## Step 2: Install Mininet
Once Ubuntu is installed, open the terminal and run:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install mininet openvswitch-switch -y
```

Verify the installation:
```bash
sudo mn --test pingall
```

---

## Step 3: Basic Mininet Commands
### Start Mininet with the default topology:
```bash
sudo mn
```
### List available commands:
```bash
help
```
### Show nodes (hosts, switches, and controllers):
```bash
nodes
```
### Display network links:
```bash
net
```
### Test connectivity between hosts:
```bash
pingall
```
### Run a command on a specific host:
```bash
h1 ifconfig
h2 ping -c 3 h3
```
### Exit Mininet:
```bash
exit
```

---

## Step 4: Emulate Custom Network Topologies

### **1. Simple Topology (1 Switch, 2 Hosts)**
```bash
sudo mn --topo single,2 --mac --switch ovsk --controller remote
```

### **2. Linear Topology (3 Switches, 3 Hosts)**
```bash
sudo mn --topo linear,3 --mac --switch ovsk --controller remote
```

### **3. Tree Topology (Depth = 2, Fanout = 2)**
```bash
sudo mn --topo tree,depth=2,fanout=2 --mac --switch ovsk --controller remote
```

---

## Step 5: View OpenFlow Flow Tables
To inspect the OpenFlow flow table of switch `s1`:
```bash
sudo ovs-ofctl dump-flows s1
```

---

## Conclusion
You have successfully set up **Mininet** on a **VirtualBox VM**, executed basic commands, and emulated different network topologies. This setup is useful for **SDN (Software-Defined Networking) experiments** and **network simulations**.
