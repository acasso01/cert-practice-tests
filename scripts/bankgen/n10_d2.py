from common import item

P = "n10"
Q = []

Q.append(item(P, 39, "2.1", "hard",
    "A router has these routes for destinations that include 10.1.5.10: a static default route 0.0.0.0/0, an OSPF route to 10.1.0.0/16, and a RIP route to 10.1.5.0/24. Which route does the router use for 10.1.5.10, and why?",
    ["The static default, because static routes always beat dynamic routes", "The OSPF route, because OSPF has a better administrative distance than RIP", "The RIP route, because 10.1.5.0/24 is the longest matching prefix", "None of them, because the three protocols cannot be in one table"],
    2,
    "The first comparison is the longest prefix, not the administrative distance. 10.1.5.10 matches the /24, the /16, and the default. The /24 is the most specific, so the RIP route wins even though RIP's administrative distance is worse than OSPF and worse than a normal static route. Administrative distance matters when two routes have the same prefix length.",
    ["The default is the least specific match. A static route does not beat a longer prefix just because it is static.",
     "OSPF would win against RIP if both offered the same prefix. Here OSPF's prefix is shorter, so it is not the best match.",
     "The /24 includes the host and is more specific than the /16 and the default. Longest match is decided before administrative distance.",
     "A routing table can hold routes from many sources at once. The router still picks one best route per destination."]))

Q.append(item(P, 40, "2.1", "medium",
    "The same prefix, 192.168.50.0/24, is learned from OSPF and is also configured as a static route with the default administrative distance. Which route is installed?",
    ["The OSPF route, because OSPF is link state", "The static route, because its administrative distance is lower", "Both, and the router load-balances across them", "Neither, until RIP is also enabled"],
    1,
    "When the prefix lengths are equal, the source with the lower administrative distance wins. A connected route is 0 and a normal static route is 1. OSPF is 110. The static route is more trusted, so it goes into the table and the OSPF route is a candidate only if the static route is removed. Equal-cost load balancing happens inside one protocol, not between a static route and OSPF of different distances.",
    ["Link state describes how OSPF learns the topology. It does not override a lower administrative distance.",
     "Static routes have administrative distance 1 by default, which is preferred to OSPF's 110 for the same prefix.",
     "The router does not split traffic across routes with different administrative distances. It installs the better one.",
     "RIP is not required for a static route or for OSPF to be considered."]))

Q.append(item(P, 41, "2.1", "medium",
    "A company router must exchange routes with its internet provider and with other companies across the public internet. Which routing protocol is used for that exterior job?",
    ["OSPF", "EIGRP", "BGP", "A host ARP cache"],
    2,
    "BGP is the path-vector protocol that carries routes between autonomous systems, including the internet. OSPF is an interior link-state protocol used inside an organization. EIGRP is a Cisco interior protocol. ARP resolves an IP address to a MAC address on a LAN and is not a routing protocol.",
    ["OSPF is an interior gateway protocol. You do not peer with the global internet using OSPF.",
     "EIGRP is an interior protocol and is Cisco-specific. Providers do not use it as the internet's routing protocol.",
     "BGP is the exterior protocol. Provider edge routers speak BGP with their customers and with other providers.",
     "ARP maps addresses on a local link. It does not advertise prefixes between companies."]))

Q.append(item(P, 42, "2.1", "easy",
    "Dozens of workstations use private addresses and share one public IPv4 address when they browse the web. The firewall rewrites both the address and the source port. What is that translation called?",
    ["Port address translation, also called NAT overload", "A static one-to-one NAT entry for every workstation", "Dynamic ARP inspection", "A VLAN trunk"],
    0,
    "PAT, or NAT overload, lets many private hosts share one public address by giving each session a different source port. A static NAT entry maps one private address to one public address and would not scale to dozens of workstations on a single public address. ARP inspection and trunking are unrelated to address translation.",
    ["PAT keeps a table of inside addresses and ports and presents one public address to the internet. That is the behavior described.",
     "Static NAT is one private address to one public address. It would require a public address per workstation.",
     "Dynamic ARP inspection checks ARP replies. It does not rewrite IP addresses for outbound web traffic.",
     "A trunk carries multiple VLANs on one link. It is not an address-translation feature."]))

Q.append(item(P, 43, "2.1", "medium",
    "A mail server on a private address must be reachable from the internet at a fixed public address, on the same ports, all the time. Which translation fits?",
    ["PAT only, with no inbound mapping", "Static NAT", "APIPA", "Disabling the default route"],
    1,
    "Static NAT publishes one inside address as one outside address, so inbound connections have a stable target. PAT is built for outbound sessions that start on the inside. It does not, by itself, give the internet a fixed address for a new inbound connection to a chosen server. APIPA is a failed DHCP address. Removing the default route would break the path.",
    ["PAT is many-to-one and is driven by outbound sessions. It is not the fixed public identity this server needs.",
     "Static NAT is the one-to-one mapping. The public address always belongs to that mail server.",
     "APIPA is 169.254 addressing when DHCP fails. It is not reachable from the internet.",
     "Without a default route, replies and other unknown destinations fail. That does not publish the server."]))

Q.append(item(P, 44, "2.1", "medium",
    "Two routers can each be the default gateway for a subnet. Hosts are configured with one gateway address that stays the same when the active router fails and the standby takes over. What did the designer give the hosts?",
    ["The physical address of router A only", "A virtual IP provided by a first-hop redundancy protocol", "A different gateway on every host, chosen at random", "The broadcast address as the gateway"],
    1,
    "FHRP protocols such as HSRP and VRRP share a virtual IP and a virtual MAC. Hosts use the virtual IP as their gateway. If the active router dies, the standby answers for the same address and the hosts do not have to be reconfigured. Pointing hosts at one router's real address defeats the failover. The broadcast address is not a gateway.",
    ["If the hosts use router A's real address, they lose the gateway when A fails, even if B is healthy.",
     "The virtual IP is the address FHRP moves between the routers. Hosts keep one gateway setting.",
     "Random gateways are not a protocol, and half of the hosts would still be aimed at a dead router.",
     "The broadcast address is the subnet's all-hosts address. Packets sent there are not routed as a default gateway."]))

Q.append(item(P, 45, "2.1", "hard",
    "A branch has one router from vendor A and another from vendor B. Both must share a default-gateway address for the LAN. The team wants a standards-based protocol rather than a Cisco-only one. Which protocol should they run?",
    ["HSRP", "VRRP", "GLBP only, because it is vendor neutral", "STP"],
    1,
    "VRRP is the standards-based first-hop redundancy protocol and is the one mixed-vendor routers can share. HSRP and GLBP are Cisco protocols. STP prevents Layer 2 loops. It does not create a virtual default gateway.",
    ["HSRP works well on Cisco gear, but it is not the open standard you choose for two different vendors.",
     "VRRP is defined so routers from different vendors can share one virtual gateway address.",
     "GLBP is also Cisco. It adds load sharing, but it is not the vendor-neutral choice.",
     "Spanning Tree picks root and blocking ports. It does not hand hosts a virtual IP."]))

Q.append(item(P, 46, "2.1", "medium",
    "One router interface connects to a switch trunk that carries three user VLANs. The router must be the default gateway for each VLAN, and there is no Layer 3 switch. How should the router be built?",
    ["One physical interface with a subinterface and an 802.1Q tag for each VLAN", "Three hubs and no IP addresses", "A single untagged IP and a hope that all VLANs share it", "NAT overload instead of gateway addresses"],
    0,
    "Router-on-a-stick uses subinterfaces. Each subinterface has the gateway address for one VLAN and an 802.1Q tag that matches the trunk. The switch port is a trunk. One untagged address can serve only the native VLAN. NAT does not create gateways. Hubs do not route.",
    ["Subinterfaces plus 802.1Q give each VLAN its own gateway on the one physical link. That is the standard design.",
     "Hubs repeat signals. They cannot be a per-VLAN default gateway.",
     "An untagged address is one subnet. The other two VLANs would have no gateway on this router.",
     "NAT translates addresses. It is not a substitute for a gateway interface in each VLAN."]))

Q.append(item(P, 47, "2.1", "easy",
    "Users on connected LANs can reach local servers, but nobody can reach the internet, and the router's table has no route to unknown destinations. What is missing?",
    ["A default route", "A second copy of every connected route", "An APIPA address on the WAN", "A hub on the LAN"],
    0,
    "Connected routes cover the networks that are configured on the router's own interfaces. Everything else, including the internet, needs a route. A default route, 0.0.0.0/0, sends unknown destinations to the provider. APIPA does not belong on a WAN. A hub would not add a route.",
    ["A default route is how a router forwards packets that do not match a more specific network, which is the internet case.",
     "Connected routes are already in the table. Duplicating them does not create a path to other networks.",
     "169.254 addressing means DHCP failed. It is not a provider route and it is not routed.",
     "A hub does not create routing entries and would not restore internet access."]))

Q.append(item(P, 48, "2.2", "medium",
    "A user was moved to a new jack. The PC gets an address in the facilities VLAN and cannot see the file server that lives in the staff VLAN. The DHCP server for staff is healthy, and other staff jacks work. What should be checked on this switch port first?",
    ["Whether the access VLAN on the port is the staff VLAN", "Whether the PC's MAC address is a multicast address", "Whether the building needs a new IP protocol", "Whether the fiber between cities is single-mode"],
    0,
    "An access port puts the attached device in one VLAN, untagged. If that VLAN is wrong, the PC hears the wrong DHCP scope and never reaches the staff servers. The rest of the staff VLAN working means the server and the router are fine. Start with the port's VLAN assignment before you redesign the WAN.",
    ["The access VLAN decides which broadcast domain and which DHCP scope this jack is in. A wrong VLAN matches the symptom exactly.",
     "A normal PC uses a unicast MAC. A multicast MAC is not why a jack landed in the facilities scope.",
     "The network is already IP. A new protocol is not the first check for one jack in the wrong VLAN.",
     "A city-to-city fiber issue would affect more than one newly patched user."]))

Q.append(item(P, 49, "2.2", "hard",
    "Two switches trunk several VLANs. Users in VLAN 20 on one switch cannot pass traffic to VLAN 20 on the other, and the switches log a native VLAN mismatch. VLAN 20 is tagged. What is the most likely configuration error?",
    ["The native VLAN is not the same on both ends of the trunk", "VLAN 20 must be the native VLAN or it cannot be tagged", "Native VLAN mismatch only affects untagged traffic, so it cannot be logged", "The switches need hubs between them"],
    0,
    "The native VLAN is the VLAN sent untagged on an 802.1Q trunk. Both ends must agree. When they do not, untagged frames are accepted into the wrong VLAN and the switches warn about the mismatch. Tagged VLAN 20 can also suffer if the trunk is unhappy, but the log line points at the native VLAN, not at a rule that VLAN 20 has to be native. A hub between switches would create a loop risk and is not the fix.",
    ["The native VLAN has to match on both ends. A mismatch is exactly what the log is reporting and it can black-hole or misdeliver untagged frames.",
     "Tagged VLANs are the normal way user VLANs cross a trunk. VLAN 20 does not need to be native.",
     "The switches are logging the mismatch, so it is visible. Untagged traffic is what the native VLAN carries, and the mismatch still matters.",
     "Adding hubs does not repair a trunk configuration and can introduce loops."]))

Q.append(item(P, 50, "2.2", "medium",
    "IP phones and PCs share a jack. The phone should tag its voice traffic, and the PC plugged into the phone should stay on the data VLAN untagged. Which switchport feature does that?",
    ["A voice VLAN, with the data VLAN as the access VLAN", "Making the user port a trunk that allows every VLAN and no access VLAN", "Disabling 802.1Q on the phone", "Putting the phone and the PC in the native VLAN of every trunk in the building"],
    0,
    "A voice VLAN tells the switch that tagged frames from the phone belong to the voice VLAN, while untagged frames from the PC stay in the access VLAN. That is the usual one-cable design. Opening the port as a trunk of every VLAN would let a PC hop into other VLANs. The phone has to tag, so 802.1Q stays on for the voice frames.",
    ["The voice VLAN plus an access VLAN is the feature built for a phone with a PC behind it.",
     "A wide-open trunk on a desk port is a security problem and is more access than the phone needs.",
     "If the phone does not tag, its traffic mixes with the data VLAN and voice QoS and DHCP options are lost.",
     "The native VLAN should be consistent and usually unused by users. It is not a dump for every phone in the building."]))

Q.append(item(P, 51, "2.2", "medium",
    "Two switches are bundled with LACP. A single large file copy between two servers does not exceed the speed of one physical link, even though four links are up. Users expected four times the throughput on that one copy. What is the realistic explanation?",
    ["Link aggregation spreads flows across members, and one flow usually stays on one link", "LACP cannot pass any traffic until a fifth link is added", "Aggregation turns the links into a hub", "LACP encrypts the file and the encryption cuts the speed by 75 percent"],
    0,
    "A port channel adds capacity and can survive a member failing, but the hash that picks a member is based on fields such as addresses and ports. Packets in one conversation are kept on one link so they stay in order. A single file copy is one flow, so it tops out near one member's speed. Other flows can use the other links at the same time.",
    ["The bundle has more capacity for many flows. One flow is pinned to one member, so it does not run at four times the link speed.",
     "LACP works with two or more matching links. A fifth link is not a requirement.",
     "A port channel is still switched. It does not become a hub.",
     "LACP does not encrypt. Any speed limit here is the hash, not a cipher."]))

Q.append(item(P, 52, "2.2", "hard",
    "One side of an Ethernet link is hard-set to 100 Mbps full duplex. The other side is set to auto. Users complain of terrible performance, and the auto side shows late collisions. What is happening?",
    ["The auto side fell back to half duplex, so the two ends no longer match", "Both sides negotiated 10 Gbps and the cable is Category 3", "Late collisions mean the default route is missing", "The link is down, so collisions cannot be counted"],
    0,
    "When one side is forced to full duplex and the other is automatic, autonegotiation does not complete a duplex agreement. The automatic side commonly lands on half duplex at the forced speed. One end transmits whenever it wants and the other waits for silence, so you get late collisions, CRC errors, and a link that is up but slow. Set both ends the same way, preferably both to auto.",
    ["A duplex mismatch is the classic result of hard-setting only one side. Half against full produces late collisions.",
     "The forced speed is 100 Mbps, not 10 Gbps, and Category 3 is not what created the collision counter.",
     "A missing default route drops off-network traffic. It does not increment late-collision counters.",
     "The link is up enough to pass some frames. The counters are evidence of a bad operating mode, not of a dark port."]))

Q.append(item(P, 53, "2.2", "medium",
    "After someone patches both jacks at a desk into the same switch, that switch's CPU spikes and MAC addresses flap between ports. Spanning Tree was turned off last year to 'make everything forward.' What is the right correction?",
    ["Leave Spanning Tree off and add a third cable for more bandwidth", "Remove the extra loop and turn Spanning Tree back on", "Replace the switch with a hub", "Increase every interface MTU to 9000"],
    1,
    "Two paths between the same devices, with nothing blocking, are a Layer 2 loop. Broadcasts multiply, and the MAC table thrashes because the same address arrives on more than one port. Spanning Tree exists to block the extra path. Turning it off made the loop fatal. Pull the extra cable and enable Spanning Tree again. A hub or jumbo frames do not stop a loop.",
    ["Another cable adds another loop. More bandwidth is not available while the switch is drowning in its own flooded frames.",
     "Break the loop and let Spanning Tree block any future extra path. That is the actual fix.",
     "A hub floods even more and has no loop control. It is a step backward.",
     "Jumbo frames change payload size. They do not stop a broadcast storm."]))

Q.append(item(P, 54, "2.2", "hard",
    "Traffic between two access switches takes a long path through a closet switch that should have been blocking. All switches still have the default Spanning Tree priority, and the closet switch has the lowest MAC address. What should be changed so the core becomes the root bridge?",
    ["Set the core bridge priority lower than the others", "Disable Spanning Tree on the core only", "Set the closet switch priority to 0 so it remains root", "Turn the core into a hub"],
    0,
    "The root bridge is the switch with the lowest bridge ID, which is the priority plus the MAC address. With every priority left at the default, the lowest MAC wins, and a closet switch can become root by accident. Set the core's priority to a lower number so it wins even if its MAC is higher. Priority 0 on the closet would make the accident permanent. Disabling Spanning Tree removes the protection.",
    ["A lower priority value on the core makes its bridge ID win, so the tree is rooted where the design says it should be.",
     "Disabling Spanning Tree on the core removes loop protection at the most important switch.",
     "Priority 0 is the strongest claim. Putting it on the closet switch keeps the bad root in place.",
     "A hub cannot be a root bridge and cannot forward the campus properly."]))

Q.append(item(P, 55, "2.2", "medium",
    "A storage network was built with a 9000-byte MTU. The new switch in the path was left at the default of 1500. Large copies fail or crawl, while small pings work. What is the mismatch?",
    ["Jumbo frames are being dropped or fragmented by a device that is still at 1500", "The storage servers are using /31 masks", "Spanning Tree is blocking pings", "The native VLAN must be 9000"],
    0,
    "Jumbo frames only work when every device on the path accepts the larger MTU. A 1500-byte switch drops an oversized frame or forces fragmentation behavior that the storage stack may not survive. Small pings fit in 1500 bytes, so they hide the problem. The MTU has to match end to end. VLAN IDs and /31 masks are a different subject.",
    ["The path MTU has to be the same. One 1500-byte hop breaks a 9000-byte storage design.",
     "A /31 is a point-to-point address mask. It does not explain why only large frames fail.",
     "If Spanning Tree were blocking the path, small pings would fail too.",
     "The native VLAN is a VLAN number, not a frame size. 9000 is an MTU."]))

Q.append(item(P, 56, "2.2", "easy",
    "Users in VLAN 30 say their gateway, which is the switch virtual interface, stopped answering after a change window. The VLAN still exists, and access ports are in VLAN 30. The interface VLAN 30 is administratively down. What does that mean?",
    ["Someone shut the SVI, so the switch is not routing for that VLAN", "The VLAN was deleted, even though the ports still show it", "Administrative down means the cable is unplugged", "The SVI is forwarding and the users are wrong"],
    0,
    "An SVI is the Layer 3 interface for a VLAN. If it is shut, the gateway address does not answer, even though the Layer 2 VLAN is still passing frames between local hosts. Administratively down means a configuration shutdown, not a missing cable. Bring the SVI back up after you know why it was shut.",
    ["A shutdown SVI removes the gateway. Hosts in the VLAN can still talk locally, but they cannot leave it through this switch.",
     "The question says the VLAN exists and the ports are in it. The SVI is a separate interface and it is the one that is down.",
     "Administratively down is a configured shutdown. An unplugged cable looks like a line-down or notconnect state on a physical port.",
     "An interface that is shut does not forward. The users are describing a real outage."]))

Q.append(item(P, 57, "2.3", "easy",
    "Three access points cover one floor on 2.4 GHz. A survey shows them on channels 1, 2, and 3. Clients near the middle are slow even when the signal is strong. What is the channel plan that avoids overlap in the 2.4 GHz band?",
    ["Channels 1, 6, and 11", "Channels 1, 2, and 3, because adjacent numbers are farthest apart", "Channel 6 on all three access points", "Channel 14, because it never overlaps anything in this band"],
    0,
    "In the 2.4 GHz band the only non-overlapping set used in most regions is 1, 6, and 11. Channels 1, 2, and 3 sit on top of each other and the access points spend their time waiting on each other's energy. Putting everyone on channel 6 is also overlap. Channel 14 is not a general-purpose plan and is not available in many countries.",
    ["1, 6, and 11 are separated enough that their main signals do not overlap. That is the usual 2.4 GHz plan.",
     "Adjacent channel numbers overlap heavily. 1, 2, and 3 are almost the same slice of spectrum.",
     "Three access points on channel 6 contend with each other everywhere their cells meet.",
     "Channel 14 is not the standard non-overlapping choice and is restricted or unavailable in many regulatory domains."]))

Q.append(item(P, 58, "2.3", "medium",
    "A warehouse has thick walls and a few old scanners that only speak 2.4 GHz. Newer laptops support both bands. The 2.4 GHz cells are crowded and the 5 GHz cells are almost empty. Which feature pushes capable clients to 5 GHz while leaving the scanners on 2.4 GHz?",
    ["Band steering", "Disabling 5 GHz", "Setting every AP to channel 1", "Replacing 5 GHz with a hub"],
    0,
    "Band steering encourages dual-band clients onto the 5 GHz radio, where there are more channels and usually less interference. Devices that only know 2.4 GHz stay there. Turning off 5 GHz would dump everyone onto the crowded band. One shared channel makes the crowding worse.",
    ["Band steering is the control that prefers 5 GHz for clients that can use it, which is what this floor needs.",
     "Disabling 5 GHz removes the empty capacity and forces laptops onto the crowded 2.4 GHz radios.",
     "Channel 1 on every AP guarantees overlap. It does not move laptops to 5 GHz.",
     "A hub is not a wireless band and cannot steer clients."]))

Q.append(item(P, 59, "2.3", "medium",
    "An employee who used the shared Wi-Fi password left the company this morning. The password is also saved on fifty phones and a conference-room display. Changing it will be a long day. Which design avoids this the next time someone leaves?",
    ["WPA2-Personal with the password printed on the wall", "WPA2-Enterprise or WPA3-Enterprise with individual accounts", "Open authentication with a hidden SSID", "WEP, because the key is shorter and easier to rotate"],
    1,
    "Enterprise Wi-Fi uses 802.1X and a RADIUS account per person. Disabling the account removes that person without touching anyone else's login. A shared key has to change everywhere the moment anyone who knows it leaves. Hiding the SSID does not keep out someone who already has the key, and WEP is obsolete and unsafe.",
    ["A shared password, posted or not, is the operational problem. Everyone must be updated when one person leaves.",
     "Enterprise authentication gives each user credentials. You disable one account and the rest of the phones keep working.",
     "An open network does not authenticate anyone. Hiding the name is not access control.",
     "WEP is broken and should not be deployed. A shorter key is not a rotation strategy."]))

Q.append(item(P, 60, "2.3", "hard",
    "A security review says the current WPA2-Personal deployment lets an attacker who captures the handshake guess the shared key offline. The company is not ready to deploy RADIUS, but it can replace the access points and the clients. Which protection is designed to close that offline-guessing hole?",
    ["WPA3-Personal with SAE", "WEP with a longer key", "Disabling the SSID broadcast and keeping WPA2-Personal", "Switching the passphrase to Telnet"],
    0,
    "WPA3-Personal uses SAE, Simultaneous Authentication of Equals, so the handshake is resistant to the offline dictionary attack that hurts a captured WPA2-Personal handshake. Hiding the SSID does not change the handshake. WEP is weaker, not stronger. Telnet is an unencrypted management protocol and has no place in a Wi-Fi passphrase.",
    ["SAE is the WPA3-Personal handshake. It was built so a captured exchange is not a free offline guess against the passphrase.",
     "WEP is retired because it can be broken quickly. A longer WEP key does not make it a modern choice.",
     "A hidden SSID is still advertised in frames the clients send, and it does not fix the WPA2 handshake.",
     "Telnet is clear-text remote login. It is not a Wi-Fi authentication method."]))

Q.append(item(P, 61, "2.3", "medium",
    "Guests join an open SSID, a web page asks them to accept a policy, and then they reach the internet. A manager calls that page 'the encryption.' What is the accurate description?",
    ["The page is a captive portal, and it does not encrypt the Wi-Fi", "The page is WPA3-SAE", "The page is MACsec on the access switch", "The page is a VPN that encrypts all radio frames"],
    0,
    "A captive portal intercepts the first web request and forces a login or an acceptance page. It is an access gate, not a cipher. An open SSID still sends radio frames without WPA encryption. If guests need privacy on the air, the SSID should use WPA2 or WPA3 as well, often with the portal in front of an isolated VLAN.",
    ["A captive portal is exactly that web gate. It does not encrypt the wireless frames.",
     "SAE is a WPA3 key exchange. A browser policy page is not SAE.",
     "MACsec encrypts Ethernet on a wired port. It is not a guest web page.",
     "A VPN can encrypt a user's traffic after they connect, but the portal page itself is not a VPN and it does not encrypt the radio."]))

Q.append(item(P, 62, "2.3", "easy",
    "A technician looking at a wireless controller sees the same SSID on twelve access points. Each radio has its own MAC address listed next to that SSID. What is that per-radio identifier called?",
    ["The BSSID", "The default gateway", "The native VLAN", "The OSPF area"],
    0,
    "The SSID is the network name people see. The BSSID is the identifier of one access point's radio for that SSID, and it is normally that radio's MAC address. The ESS is the set of access points sharing the SSID so clients can roam. A gateway, a native VLAN, and an OSPF area are not wireless identifiers.",
    ["The BSSID identifies one AP radio. Twelve radios advertising one SSID have twelve BSSIDs.",
     "The default gateway is an IP address used to leave the subnet. It is not the radio's identifier.",
     "The native VLAN is the untagged VLAN on a trunk. It is not a wireless MAC.",
     "An OSPF area is a routing-process boundary. It has nothing to do with the radio list."]))

Q.append(item(P, 63, "2.3", "medium",
    "Two buildings are 200 meters apart and need a wireless bridge. An omnidirectional antenna on the roof covers the parking lot and wastes most of its energy away from the other building. Which antenna fits the link?",
    ["A directional antenna aimed at the far building", "A second omnidirectional antenna pointed at the sky", "No antenna, because bridges use TFTP", "A Bluetooth adapter"],
    0,
    "A directional antenna concentrates energy in one direction, which is what a point-to-point bridge wants. An omnidirectional antenna covers a broad area around itself and is the right shape for clients on a floor, not for a shot down a 200 meter path. Bluetooth is short-range personal area gear. TFTP is a file transfer.",
    ["Aim a directional antenna at the other building so the signal goes where the bridge needs it.",
     "An omnidirectional antenna already radiates around the mast. Pointing one at the sky does not make a focused link.",
     "TFTP does not carry a wireless bridge. The link still needs the right antenna.",
     "Bluetooth is a short personal-area radio. It will not bridge two buildings."]))

Q.append(item(P, 64, "2.3", "hard",
    "All of the lightweight access points reboot after a power event and never start forwarding. The controller that manages them is powered off for maintenance. Autonomous access points in a lab closet are fine. Why are the lightweight access points down?",
    ["Lightweight access points depend on the wireless controller", "Lightweight access points only work on channel 14", "A controller is optional eye candy and cannot affect forwarding", "Autonomous access points require the same controller, so the lab result is impossible"],
    0,
    "A lightweight access point downloads its configuration and often its forwarding policy from a wireless LAN controller. If the controller is down, those access points do not come back as a normal service. An autonomous access point stores its own configuration and keeps working alone. The lab result fits that difference. The controller is not optional for this design.",
    ["Lightweight APs are managed by the controller. With the controller off, they do not resume normal service after the reboot.",
     "Channel 14 is not a dependency for lightweight APs, and it is not a general-purpose channel.",
     "In a controller-based design the controller is required. It is not a decorative dashboard.",
     "Autonomous APs are standalone by definition. They do not need the controller, which is why the lab closet stayed up."]))

Q.append(item(P, 65, "2.4", "medium",
    "A new desk is 140 meters of copper away from the nearest closet, and the link will not train reliably. The permanent link was pulled as one Category 6a run with no intermediate gear. What is the constraint?",
    ["Twisted-pair Ethernet channels are limited to about 100 meters", "Category 6a cannot exceed 20 meters", "Copper has no distance limit if the VLAN is correct", "The run is fine and the failure must be BGP"],
    0,
    "The Ethernet channel over twisted pair, including the permanent link and the patch cords, is specified at up to 100 meters. A 140 meter pull is past that, so attenuation wins no matter how good the category is. Category 6a is the long 10 Gbps copper rating, but it is still a 100 meter channel. The fix is a closer closet or a fiber run, not a routing-protocol change.",
    ["One hundred meters is the channel limit. One hundred forty meters of copper is outside the standard, so the link is unreliable.",
     "Category 6a is allowed to 100 meters for 10 Gbps. Twenty meters is far too short a description of its limit.",
     "VLANs do not extend the physics of copper. A correct VLAN on an over-long cable still fails.",
     "BGP is an exterior routing protocol. It does not bring up a switch port at the end of a too-long cable."]))

Q.append(item(P, 66, "2.4", "easy",
    "A closet has a metered power strip that feeds the switches, and a separate battery-backed unit that keeps those switches up during a one-minute utility blink so they can be shut down cleanly if the blink becomes an outage. Which device is the battery-backed unit?",
    ["The UPS", "The PDU, because a PDU includes the batteries by definition", "The patch panel", "The cable tester"],
    0,
    "A UPS is the uninterruptible power supply. It bridges short outages and gives you time to shut down. A PDU distributes power in the rack. It may be metered or switched, but metering is not the same thing as a battery. Patch panels and cable testers have nothing to do with ride-through power.",
    ["The UPS is the battery-backed device. A one-minute blink is the event it is there to cover.",
     "A PDU distributes power. Some are fancy, but a meter does not make it a battery.",
     "A patch panel terminates cables. It does not store energy.",
     "A cable tester checks wire maps. It is not part of the power path."]))

Q.append(item(P, 67, "2.4", "medium",
    "Cold air is supplied in the aisle in front of a row of racks. A new switch was installed backward, and its fans blow hot air into that cold aisle. What is wrong with the installation?",
    ["The airflow fights the hot-aisle and cold-aisle plan", "Switches must exhaust into the cold aisle so the cold aisle gets warmer", "Fan direction does not matter if the VLAN is correct", "The switch should sit on the floor outside the rack"],
    0,
    "Hot-aisle and cold-aisle designs only work if the equipment pulls cold air from the cold aisle and exhausts into the hot aisle. A reversed switch dumps heat into the cold air that the other gear needs. Check the intake and exhaust arrows before the switch is screwed in. VLANs do not move heat, and a switch on the floor is a worse installation, not a cooling plan.",
    ["Port-side intake or exhaust has to match the aisle. Exhaust into the cold aisle recirculates heat and starves the row.",
     "The cold aisle should stay cold. Exhaust belongs in the hot aisle, which is where the return air is expected.",
     "VLANs are a traffic design. They do not fix a reversed chassis.",
     "Leaving the switch on the floor blocks airflow further and is not an acceptable rack installation."]))

Q.append(item(P, 68, "2.4", "easy",
    "The intermediate distribution frame on each floor is a closet with open doors. Visitors walk through it to reach a conference room, and the patch panels and switches are unlabeled and within reach. What is the first physical correction?",
    ["Lock the closet and stop using it as a hallway", "Publish the switch passwords on the door so visitors can help", "Remove the patch panels so there is nothing to touch", "Turn off Spanning Tree"],
    0,
    "An IDF is a distribution space, not a corridor. It should be locked, and only people who work on the network should get in. Labeling comes with that, but an open door is the immediate exposure. Posting passwords makes the problem worse. Removing patch panels destroys the cabling plant. Spanning Tree is unrelated.",
    ["A lockable IDF, with the through-traffic routed another way, is the basic physical control for the floor closet.",
     "Passwords on the door give every visitor administrative access. That is the opposite of a correction.",
     "The patch panels are how the floor is cabled. Removing them is an outage, not a security control.",
     "Spanning Tree does not lock a door and should not be turned off as a physical fix."]))

Q.append(item(P, 69, "2.4", "medium",
    "In winter the equipment rooms measure very low humidity. Technicians get a shock when they touch racks, and switch ports show occasional unexplained errors that disappear in the summer. What environmental change should they make?",
    ["Raise the humidity into the range recommended for the room so static drops", "Lower the humidity further so the air is completely dry", "Spray water directly into the switch intakes", "Disable grounding so shocks cannot occur"],
    0,
    "Very dry air raises the chance of electrostatic discharge, which people feel as a shock and which can disturb electronics. The room needs humidity brought back up into the recommended band, not driven lower. Soaking the intakes causes corrosion and shorts. Grounding is part of how you want the room built, not something you remove.",
    ["Low humidity encourages static. Bringing the room back into the recommended humidity range addresses the seasonal errors and the shocks.",
     "Drier air makes electrostatic problems worse. The winter symptom is already the dry case.",
     "Liquid water in the intakes will damage the equipment. Humidifying the room is not the same as spraying the gear.",
     "Removing grounds makes electrical faults more dangerous. It does not cure static."]))

if __name__ == "__main__":
    from common import dump
    dump("n10-009", {"q-d2.json": Q})
