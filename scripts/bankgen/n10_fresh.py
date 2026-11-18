"""Original N10-009 questions that do not restate the existing bank."""

from common import PROBLEMS, dump, item
from gate import collisions

P = "n10"
Q = []


def add(*args):
    Q.append(item(P, *args))


add(185, "1.1", "medium",
    "A client opens a dialog, keeps it alive while several requests ride it, and then tears the dialog down. Routing and frames are someone else's job. Which OSI layer owns that dialog?",
    ["Session", "Network", "Physical", "Data link"],
    0,
    "The session layer sets up, maintains, and ends a dialogue between applications. The network layer forwards packets. The physical layer is bits on the medium. The data link layer delivers frames on one hop. None of those three manage the dialog itself.",
    ["Setup, keep-alive, and teardown of the dialog are the session layer.",
     "The network layer chooses a next hop. It does not open or close the application dialog.",
     "The physical layer moves bits. It does not track a conversation.",
     "The data link layer stops at the local link. It does not tear down an application dialog."])

add(186, "1.2", "medium",
    "Three web servers sit behind one address. When one server stops answering checks, new sessions go only to the other two. Which device made that decision?",
    ["A load balancer using a health check", "A passive hub", "A cable certifier", "A visual fault locator"],
    0,
    "A load balancer distributes sessions and withdraws a server that fails its health check. A hub repeats every signal. A certifier and a visual fault locator test cable. They do not choose a healthy web server.",
    ["The health check is why the dead server stopped receiving new sessions.",
     "A hub has no idea whether a server is answering.",
     "A certifier measures a cable. It does not steer web sessions.",
     "A visual fault locator shines light into fiber. It does not run a server pool."])

add(187, "1.4", "easy",
    "Two routers must exchange routing updates with BGP. The firewall between them allows established TCP and is blocking the BGP port. Which port should be permitted?",
    ["TCP 179", "TCP 389", "UDP 123", "TCP 110"],
    0,
    "BGP uses TCP 179. TCP 389 is LDAP. UDP 123 is NTP. TCP 110 is POP3. Opening the wrong one leaves the BGP session closed.",
    ["TCP 179 is the BGP session. Permit that port between the peers.",
     "TCP 389 is LDAP. These routers are not doing a directory lookup.",
     "UDP 123 synchronizes clocks. It is not the BGP update session.",
     "TCP 110 is POP3 mail retrieval, not a routing protocol."])

add(188, "1.5", "medium",
    "A router has no address yet. The technician must reach its command line from a laptop on the console port. Which cable belongs in that port?",
    ["A rollover console cable", "A plenum-rated cable into a LAN jack as the only first-time method", "Twinax into the console jack", "RG-6 with an F connector"],
    0,
    "Router consoles expect a rollover cable into the console port, which needs no IP address. A LAN jack is not the console. Twinax is a high-speed data cable. RG-6 is RF coax. Neither speaks the console pinout.",
    ["The console port plus a rollover cable is the no-address way in.",
     "A LAN jack needs an address and a straight-through or auto-MDIX link. It is not the console.",
     "Twinax does not terminate on a router console port.",
     "An F connector is for coax video or DOCSIS, not a serial console."])

add(189, "1.7", "hard",
    "A planner is using 10.4.4.0/28 for a small link. Which address is the broadcast of that subnet?",
    ["10.4.4.15", "10.4.4.16", "10.4.4.255", "10.4.5.0"],
    0,
    "A /28 has 16 addresses. The block that starts at 10.4.4.0 runs through 10.4.4.15, and .15 is the broadcast. .16 is the next subnet. .255 would be the broadcast of a /24. 10.4.5.0 is a different third octet.",
    ["Sixteen addresses from .0 ends at .15. That is the broadcast.",
     ".16 is the first address of the next /28, not the broadcast of this one.",
     ".255 is the broadcast only when the mask reaches the whole last octet.",
     "10.4.5.0 is a different third octet. It is not inside the 10.4.4.0/28 block."])

add(190, "1.8", "medium",
    "A server is given a global IPv6 address and keeps its private IPv4 address. Clients that only speak IPv4 still reach it through the IPv4 address, and IPv6 clients use the IPv6 address directly. Which transition approach is that?",
    ["Dual stack", "Throwing IPv4 away before any IPv6 route exists", "Replacing the server NIC with a hub", "An F-type coax segment"],
    0,
    "Dual stack runs IPv4 and IPv6 on the same node so each client uses the family it has. Removing IPv4 first would strand the IPv4-only clients. A hub and a coax drop do not add an address family.",
    ["Both families on one server is dual stack. Each client uses the address it can reach.",
     "Removing IPv4 before those clients can speak IPv6 takes the service away from them.",
     "A hub does not give a server an IPv6 address.",
     "Coax with an F connector is not an address-family transition."])

add(191, "2.1", "hard",
    "Two OSPF routers sit only in area 3. They never learn routes from the rest of the company. There is no link from area 3 into area 0 and no virtual link. What is missing?",
    ["A path into the backbone area", "A public web certificate on every PC", "A longer HDMI run", "An F-type splitter"],
    0,
    "Every OSPF area must connect to area 0, the backbone, unless a virtual link is built on purpose. Area 3 alone cannot exchange routes with the other areas. Certificates, video cables, and coax splitters are not OSPF adjacencies.",
    ["Area 0 is the backbone. Area 3 needs a connection to it.",
     "A web certificate does not create an OSPF area border.",
     "HDMI does not carry routing adjacencies.",
     "An F connector is coax. It is not an OSPF area design."])

add(192, "2.2", "medium",
    "Someone plugs a switch with a very low bridge priority into a conference-room jack, and it must not become the spanning-tree root. Which feature on that downlink enforces the rule?",
    ["Root guard", "A longer DHCP lease", "An MX record", "A plenum rating"],
    0,
    "Root guard blocks a port from becoming the root port toward a switch that advertises a better priority. A DHCP lease, a mail record, and a cable jacket do not protect the root bridge.",
    ["Root guard is the feature that refuses a better BPDU on that port.",
     "A DHCP lease times addresses. It does not elect a root bridge.",
     "An MX record directs mail. It is not spanning tree.",
     "Plenum cable is about the jacket in an air space, not the root."])

add(193, "2.3", "medium",
    "A Wi-Fi 6E laptop sees a corporate SSID on 6 GHz. An older Wi-Fi 5 laptop in the same chair cannot see that SSID at all, while a 5 GHz SSID from the same AP is visible to both. Why is the 6 GHz name missing on the older laptop?",
    ["Wi-Fi 5 radios do not operate on 6 GHz", "The SSID is hidden, which removes it from every radio including Wi-Fi 6E", "Channel 14 is mandatory for every client", "WPA3 changes the frequency by itself"],
    0,
    "6 GHz is the Wi-Fi 6E band. A Wi-Fi 5 radio has 2.4 and 5 GHz only, so it cannot hear a 6 GHz BSS. Hiding a name would also hide it from the 6E laptop, which can see it. Channel 14 and WPA3 are not why the band is missing.",
    ["No 6 GHz radio means no 6 GHz SSID. The older laptop needs a 6E adapter or a 5 GHz name.",
     "The 6E laptop can see the name, so it is not hidden.",
     "Channel 14 is a rarely used 2.4 GHz channel, not a 6 GHz requirement.",
     "WPA3 is an authentication choice. It does not move an SSID onto a band the radio lacks."])

add(194, "2.4", "medium",
    "A cable passes through a fire-rated wall and the hole was left open around the jacket. The inspector rejects the install even though the link passes traffic. What is missing?",
    ["A firestop that restores the wall rating", "A second DHCP scope", "A faster NTP server", "An extra SSID"],
    0,
    "A penetration in a rated wall has to be sealed with an approved firestop so the wall still holds fire. Traffic passing does not restore the rating. DHCP, NTP, and an SSID do not seal a hole.",
    ["Seal the opening with the listed firestop. The link light is not the inspection.",
     "Another DHCP scope does not close a hole in a rated wall.",
     "NTP synchronizes clocks. It does not restore a fire rating.",
     "An SSID is a wireless name. It does not seal a wall."])

add(195, "2.1", "medium",
    "A static route for 10.8.0.0/16 is entered with administrative distance 200. OSPF is already advertising that same prefix and the adjacency is up. Which route is used?",
    ["The OSPF route, until OSPF withdraws it", "The static route, because every static route has distance 0", "Neither, because a /16 cannot be static", "The static route only for IPv6"],
    0,
    "Lower administrative distance wins. OSPF is 110 and this static route was set to 200, so OSPF stays installed while it exists. The static route is the backup. Static routes do not all have distance 0, a /16 can be static, and the prefix in the stem is IPv4.",
    ["110 beats 200. The floating static route waits for OSPF to disappear.",
     "A static route can be given a worse distance on purpose. It is not always 0.",
     "A /16 is a normal prefix. The mask is not why the route is rejected.",
     "10.8.0.0/16 is IPv4. The distance comparison is not an IPv6 rule."])

add(196, "2.3", "easy",
    "A site survey finds almost no signal in a stairwell and a strong signal in the hallway beside it. What should the installer do?",
    ["Cover the stairwell with an access point placed for that spot", "Raise hallway power until the stairwell is saturated and ignore the neighbors", "Replace the DHCP database", "Change the company's SMTP banner"],
    0,
    "A dead spot is a coverage problem. Put radio where the people are, then check the neighbors. Cranking one hallway AP often spills into other floors and still may not bend through the stairwell. DHCP and SMTP are not the survey result.",
    ["Place or aim an access point for the stairwell. That is what the survey measured.",
     "More power in the hallway is a blunt tool and can make the roaming problem worse.",
     "The DHCP database did not create a stairwell dead spot.",
     "The mail banner is unrelated to signal in a stair."])

add(197, "3.1", "medium",
    "A contractor needs the network diagram, and the company wants the drawing kept private. Which agreement belongs in place before the file is sent?",
    ["A non-disclosure agreement", "A DHCP lease", "A cable test report", "A warranty card for a patch cord"],
    0,
    "A non-disclosure agreement is how you bind someone to keep a diagram private. A lease, a test report, and a warranty do not create that duty.",
    ["Get the non-disclosure agreement signed, then send the diagram.",
     "A DHCP lease hands out an address. It does not protect a drawing.",
     "A test report describes a cable. It is not a promise of secrecy.",
     "A warranty covers a product defect, not a confidential diagram."])

add(198, "3.2", "medium",
    "A router reboots and its on-box log buffer starts empty, so last night's messages are gone. Which design would still have those lines?",
    ["A remote syslog server that received them as they were generated", "A longer console cable stored in a drawer", "A darker rack bezel", "An extra access VLAN with no collector"],
    0,
    "Local buffers die with a reboot or when they wrap. A syslog server keeps the copy that was sent at the time of the event. Cables, bezels, and an empty VLAN do not store logs.",
    ["Ship the logs as they happen. The collector still has them after the reboot.",
     "A console cable does not archive last night.",
     "The bezel color does not retain messages.",
     "A VLAN without a collector is not a log archive."])

add(199, "3.3", "hard",
    "Payroll may be unavailable for at most two hours. The last restore drill took five hours before users could work. Which target did the drill miss?",
    ["The recovery time objective", "The wireless channel plan", "The native VLAN ID", "The SMTP greeting"],
    0,
    "The recovery time objective is how long the business can stand to be down. Two hours was the limit and the drill took five, so the time target failed. Channels, a VLAN number, and a mail banner are not that clock.",
    ["Five hours is longer than the two-hour recovery time. That is the miss.",
     "The channel plan does not say how fast payroll must return.",
     "The native VLAN is a trunk setting, not a downtime budget.",
     "The SMTP greeting is a mail banner, not a restore target."])

add(200, "3.4", "medium",
    "A server's name already has an A record so IPv4 clients can find it. IPv6 clients need the same name to resolve. Which record do you add?",
    ["AAAA", "An MX record with a 128-bit priority", "A TXT record that replaces the need for any address", "A PTR that stores the IPv6 address as a name lookup"],
    0,
    "AAAA maps a name to an IPv6 address. The existing A record stays for IPv4. MX directs mail. TXT holds text. A PTR is the reverse lookup, from the address back to the name, and it is not how clients resolve the name.",
    ["Add the AAAA record beside the A record.",
     "MX priority is a mail preference, not an IPv6 address.",
     "TXT does not answer an address query for this host.",
     "PTR is reverse DNS. Clients looking up the name need AAAA."])

add(201, "3.5", "medium",
    "The WAN is down and nobody is on site. A cellular modem on the console server in the other city's rack still accepts a call. Which path is that modem?",
    ["Out-of-band management", "The same failed WAN circuit", "A guest SSID that has no backhaul", "A loopback route that is only advertised across the failed WAN"],
    0,
    "Out-of-band management does not depend on the production WAN. A cellular console path is the classic example. The failed circuit, a guest network with no path, and a loopback that is only reachable through the WAN are all still down.",
    ["The cellular modem is a separate path. That is out of band.",
     "The WAN is the path that failed. It cannot be the working path.",
     "A guest SSID with no backhaul does not reach the other city.",
     "A route that exists only on the failed WAN is unreachable too."])

add(202, "4.1", "medium",
    "The person who requests a firewall change is not allowed to be the only person who approves it. Which principle is that?",
    ["Separation of duties", "One shared administrator password", "Security through an unpublished SSID", "An open mail relay"],
    0,
    "Separation of duties splits a sensitive action so one person cannot both request and approve it. A shared password, a hidden name, and an open relay do the opposite of that control.",
    ["Two people, two roles. That is separation of duties.",
     "A shared password collapses accountability. It is not the principle.",
     "Hiding an SSID is obscurity, not a second approver.",
     "An open relay accepts mail from anyone. It is not an approval rule."])

add(203, "4.2", "medium",
    "A small access point is found plugged into a conference-room jack, advertising the company name. The switch learned a new MAC on that jack. Wireless tools did not see a second over-the-air twin of an existing AP. What was added?",
    ["A rogue access point on the wired network", "A BGP hijack of the company prefix", "A cut fiber in the parking lot", "A failed UPS battery"],
    0,
    "A rogue access point is unauthorized wireless hardware, here bridged onto the LAN through a jack. A BGP hijack is a routing announcement on the internet. A fiber cut and a dead UPS would remove connectivity, not add an SSID.",
    ["The jack and the new MAC are the rogue AP. Unplug it and shut unused ports.",
     "BGP hijacking is a prefix announced by someone else. It does not sit on a conference-room jack.",
     "A cut fiber drops links. It does not advertise an SSID.",
     "A UPS battery does not broadcast a wireless name."])

add(204, "4.3", "hard",
    "Users who plug into one closet get addresses from a small DHCP box someone hid there. Legitimate servers are on trusted ports. Which switch feature drops the unauthorized offers?",
    ["DHCP snooping", "A faster NTP poll", "Jumbo frames on every port", "LACP between two servers that are not involved"],
    0,
    "DHCP snooping treats access ports as untrusted and drops server messages that do not arrive from a trusted port. NTP, jumbo frames, and an unrelated aggregation do not filter DHCP offers.",
    ["Trust the real server's port and drop offers everywhere else. That is snooping.",
     "NTP does not decide which DHCP offer a client may accept.",
     "A larger MTU does not stop a rogue DHCP server.",
     "LACP bundles links. It does not filter DHCP."])

add(205, "4.3", "medium",
    "One access port starts forwarding a broadcast storm and the switch rate-limits that port. Which feature is doing the limiting?",
    ["Storm control", "A longer IP TTL", "An extra A record", "A clean full-duplex fiber link with no errors"],
    0,
    "Storm control caps broadcast, multicast, or unknown unicast so one port cannot consume the LAN. TTL, a DNS record, and a healthy fiber link do not rate-limit a broadcast flood.",
    ["The rate limit on the flooding port is storm control.",
     "TTL limits hops for a packet. It does not police a switch port.",
     "An A record publishes an address. It does not stop a storm.",
     "A clean fiber link is not the port that is flooding."])

add(206, "5.1", "easy",
    "The user confirms the share works again. The technician has not recorded the cause or the change that fixed it. Which step is still open?",
    ["Document the findings, the actions, and the outcome", "Replace the core switch before writing anything", "Format the file server", "Skip the note because the user is already working"],
    0,
    "The Network+ method ends by documenting what you found, what you changed, and the result. Replacing a working core, formatting the server, or skipping the note throws away the next person's map.",
    ["Write it down. The user confirming the fix is the moment to document, not a reason to skip it.",
     "The core is not the failed part in this story. Replacing it is not the remaining step.",
     "Formatting destroys the data the share just started serving.",
     "A working user is why you can close the ticket, after the note exists."])

add(207, "5.2", "medium",
    "A certifier's wiremap on a new run shows pin 6 open. The jack was punched in a hurry and the link will not pass traffic. What is the fault?",
    ["An open conductor on that pin", "A DNS name that expired", "A spanning-tree block on a fiber that is not this run", "An expired web certificate"],
    0,
    "A wiremap open means that conductor does not connect end to end. Repunch pin 6. DNS, spanning tree, and a web certificate do not show up as an open pin on a certifier.",
    ["Pin 6 never lands. Punch it again and retest.",
     "A DNS failure would show up in name lookups, not as an open pin on a wiremap.",
     "Spanning tree acts on a link that is already up. This run is open.",
     "A web certificate can expire without lifting a conductor off a punch-down."])

add(208, "5.3", "medium",
    "Office PCs can ping each other. Some of them cannot open new internet sessions, and the firewall log says the translation table has no free entries. What is exhausted?",
    ["The NAT address pool", "The stairwell's wireless channel", "The number of fiber strands inside one desk cord", "A DHCP scope that still has free addresses"],
    0,
    "If internal pings work and new outbound translations fail because the pool is empty, the NAT pool is the bottleneck. Add addresses or shorten idle translations. A channel, a fiber count in a patch cord, and a healthy DHCP scope do not fill a NAT table.",
    ["No free translations means the pool is exhausted. That matches the log.",
     "A wireless channel does not store NAT entries.",
     "A desk cord's strand count is not the firewall table.",
     "The stem says local addressing still works. The full table is NAT, not DHCP."])

add(209, "5.4", "medium",
    "A speed test shows the full rate of the circuit, but calls lag whenever a large download runs. The edge router holds a queue for several seconds. What is the performance problem?",
    ["Bufferbloat, a queue that stores too much traffic", "A dark fiber with no light", "An unplugged console cable in a drawer", "A host that cannot ping its own gateway because the mask is wrong"],
    0,
    "A deep queue keeps the speed test high and makes interactive traffic wait. That is bufferbloat. It is fixed with a smaller queue or smarter scheduling, not with a new fiber, a console cable, or a mask change on a host that is not the symptom.",
    ["The full-rate test plus a multi-second queue is bufferbloat.",
     "Dark fiber would fail the speed test. This circuit is full, not dark.",
     "A console cable in a drawer is not in the forwarding path.",
     "A bad mask would break local reachability. The stem is about delay under load."])

add(210, "5.5", "medium",
    "A PC sends DHCP Discover messages and never gets an address. The technician wants to see whether an Offer comes back. Which tool shows those packets?",
    ["A packet capture on the PC or a mirrored port", "A punch-down tool", "A crimper", "A continuity tester with no view of frames"],
    0,
    "Discover and Offer are packets. A capture shows whether they are sent and answered. A punch-down tool, a crimper, and a continuity tester build or check copper. They do not decode DHCP.",
    ["Capture the exchange. You need to see Discover and Offer, not just the link light.",
     "A punch-down tool seats wires. It does not display DHCP.",
     "A crimper ends a plug. It does not show an Offer.",
     "Continuity says a wire conducts. It does not decode a UDP exchange."])

add(211, "5.5", "easy",
    "A wireless survey shows a high noise floor on channel 6 and a quiet channel 11. Clients on the noisy channel are slow, and the AP can be moved. What should change?",
    ["Move the AP to the quieter channel", "Empty the DHCP scope on purpose", "Put the default gateway outside the subnet", "Replace the single-mode fiber in a different building"],
    0,
    "A high noise floor means the channel is a poor place to send. A quieter channel is the direct fix when the AP can change. DHCP, a wrong gateway, and unrelated fiber do not lower that noise.",
    ["Use the quiet channel. The survey already compared them.",
     "Emptying the scope takes addresses away. It does not quiet a channel.",
     "A gateway outside the subnet breaks routing. It is not a channel plan.",
     "Fiber in another building is not the 2.4 GHz noise the survey measured."])

add(212, "5.2", "hard",
    "A fiber jumper was pulled tight around a zip tie. Received optical power is far below the optic's minimum, and a scope shows the glass cracked at the kink. What failed?",
    ["The bend radius was exceeded", "An SSID was hidden", "NTP fell back a stratum", "The mail banner was rewritten"],
    0,
    "Fiber has a minimum bend radius. A tight kink cracks the glass and the light never arrives. An SSID, NTP, and a mail banner do not crack a strand or drop optical power.",
    ["Replace the jumper and respect the bend radius. The kink is the fault.",
     "Hiding a wireless name does not reduce optical power.",
     "NTP stratum is a clock-quality number, not a light level.",
     "A mail banner is text. It does not crack fiber."])

add(213, "5.4", "easy",
    "The WAN graph sits near 100 percent all afternoon and the output-drop counter climbs. File transfers are slow and there are no CRC errors. What do the drops support?",
    ["The queue is full and the interface is discarding packets", "The link is idle", "DNSSEC is the counter being graphed", "A rollover cable in a desk drawer is the forwarding path"],
    0,
    "Output drops with a full utilization graph and no CRCs are congestion: the queue overflowed. An idle link would not be at 100 percent. DNSSEC and a spare console cable do not increment output drops.",
    ["The interface cannot send as fast as the LAN is handing it traffic. That is the drop counter.",
     "An idle link does not sit at 100 percent or increment drops.",
     "DNSSEC validates names. It is not this counter.",
     "A cable in a drawer is not the WAN interface."])

add(214, "5.1", "medium",
    "A technician's theory is that a new ACL is dropping the payroll port. The ACL has not been checked, and no counter has been read. What is the next method step?",
    ["Test the theory against the ACL counters or a temporary permit", "Implement a core replacement before the test", "Document a cause that is not confirmed", "Ask the user to stop reporting it"],
    0,
    "After a theory, you test it. Reading the ACL counters or trying a controlled permit confirms or kills the idea. Replacing the core, writing a guess as fact, or silencing the user skips the test.",
    ["Check the counters. A theory is not a fix until it is tested.",
     "A core swap is an implementation, and this theory is about an ACL.",
     "Documentation comes after you know the cause.",
     "The report is the symptom. Stopping it does not test the ACL."])

if __name__ == "__main__":
    found = collisions("n10-009", Q)
    if PROBLEMS or found:
        raise SystemExit("\n".join(PROBLEMS + found))
    dump("n10-009", {"q-fresh.json": Q})
