### 2 After studying open source POX and Floodlight controller, Install controller and run custom topology using remote controller like POX and floodlight controller. Recognize inserted flows by controllers.

# OpenFlow Controllers: POX and Floodlight

This guide provides step-by-step instructions on installing POX and Floodlight controllers, running a custom topology using Mininet, and recognizing inserted flows by controllers.

## Prerequisites
- Ubuntu or any Linux-based system
- Python (for POX)
- Java and Ant (for Floodlight)
- Mininet installed

## Step 1: Install POX Controller
1. Clone the POX repository:
   ```sh
   git clone https://github.com/noxrepo/pox.git
   cd pox
   ```
2. Run POX with Layer-2 learning switch:
   ```sh
   ./pox.py forwarding.l2_learning
   ```

## Step 2: Install Floodlight Controller
1. Install Java:
   ```sh
   sudo apt update
   sudo apt install default-jdk
   ```
2. Clone the Floodlight repository:
   ```sh
   git clone https://github.com/floodlight/floodlight.git
   cd floodlight
   ```
3. Build Floodlight:
   ```sh
   sudo apt install ant
   ant
   ```
4. Run Floodlight:
   ```sh
   java -jar target/floodlight.jar
   ```

## Step 3: Run a Custom Topology in Mininet
1. Install Mininet (if not already installed):
   ```sh
   sudo apt-get install mininet
   ```
2. Run a custom topology with a remote controller:
   ```sh
   sudo mn --topo=tree,depth=2 --controller=remote,ip=<controller_ip>,port=6633
   ```
   Replace `<controller_ip>` with the IP of the machine running POX or Floodlight.

## Step 4: Recognize Inserted Flows
### For POX:
- View logs:
  ```sh
  tail -f pox.out
  ```
### For Floodlight:
- Check installed flows using REST API:
  ```sh
  curl http://localhost:8080/wm/core/switch/all/flow/json | jq .
  ```

## Step 5: Insert Custom Flow Entries
### For Floodlight:
1. Create a JSON file (`flow.json`):
   ```json
   {
     "switch": "00:00:00:00:00:01",
     "name": "myflow",
     "cookie": "0",
     "priority": "32768",
     "active": "true",
     "actions": "output=2"
   }
   ```
2. Push flow entry:
   ```sh
   curl -X POST -d @flow.json http://localhost:8080/wm/staticflowpusher/json
   ```

### For POX:
1. Modify `pox/ext/mycontroller.py`:
   ```python
   from pox.core import core
   import pox.openflow.libopenflow_01 as of

   def _handle_ConnectionUp(event):
       flow_mod = of.ofp_flow_mod()
       flow_mod.match.in_port = 1
       flow_mod.actions.append(of.ofp_action_output(port=2))
       event.connection.send(flow_mod)

   core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
   ```
2. Run POX with the custom controller:
   ```sh
   ./pox.py mycontroller
   ```

## Step 6: Verify Flow Rules
- In Mininet:
  ```sh
  sudo ovs-ofctl dump-flows s1
  ```
- In Floodlight:
  ```sh
  curl http://localhost:8080/wm/core/switch/all/flow/json | jq .
  ```

## Conclusion
You have successfully:
1. Installed POX and Floodlight controllers.
2. Created a custom topology in Mininet.
3. Configured a remote controller.
4. Inserted custom flows.
5. Verified the inserted flow rules.
