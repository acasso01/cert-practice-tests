from common import item

P = "n10"
Q = []

Q.append(item(P, 100, "4.1", "medium",
    "A user signs in to the VPN with a password and then approves a prompt in an authenticator app on a phone. A coworker says a password plus a PIN typed on the same page would have been the same thing. Which statement is right?",
    ["The password and the app are two different factor types. A password and a PIN are both something you know", "A PIN is something you are, so password plus PIN is biometric MFA", "An authenticator app is not a factor because it is software", "MFA means two passwords stored in the same field"],
    0,
    "Factors are something you know, something you have, and something you are. A password is something you know. An authenticator app is something you have, because the phone holds the secret. A PIN typed next to a password is a second thing you know, so it is not a second factor. The app is still a factor even though it is software.",
    ["Different factor types are what make the VPN login MFA. Two secrets the user remembers are still one type.",
     "A PIN is knowledge, not a biometric. Fingerprints and face scans are the 'something you are' factor.",
     "A soft token in an authenticator app is a possession factor. The fact that it is an app does not disqualify it.",
     "Two passwords are still one factor type. MFA is not a longer password."]))

Q.append(item(P, 101, "4.1", "hard",
    "Network devices must send administrator logins to a central server. The security team wants the entire authentication payload encrypted, and they want authorization separated from authentication so command rights can be decided separately. Which protocol fits better?",
    ["TACACS+", "RADIUS, because it encrypts the whole payload and uses TCP 49", "Telnet", "TFTP"],
    0,
    "TACACS+ uses TCP 49, encrypts the body of the packet, and separates authentication, authorization, and accounting. That matches device administration. RADIUS is commonly used for network access such as Wi-Fi and VPN. It traditionally encrypts the password field rather than the whole packet and combines authentication and authorization. Telnet and TFTP are not AAA protocols.",
    ["TACACS+ is the better fit for device administration when you want full-packet encryption and separated authorization.",
     "RADIUS is strong for network access, but the description of full-body encryption and separated AAA is TACACS+. RADIUS does not use TCP 49.",
     "Telnet is clear-text remote access. It does not centralize AAA.",
     "TFTP transfers files with no authentication worth using for administrators."]))

Q.append(item(P, 102, "4.1", "medium",
    "Users sign in once to a company portal and then reach several web applications without typing the password again. The applications trust an assertion from an identity provider. Which technology is that web sign-on?",
    ["SAML", "A DHCP lease", "STP", "A cable certifier"],
    0,
    "SAML is a common way for an identity provider to hand a web application a signed assertion that the user already authenticated. That is single sign-on for the browser. DHCP only provides addressing. Spanning Tree blocks loops. A certifier tests cable. None of those create a web login assertion.",
    ["SAML carries the web single sign-on assertion between the identity provider and the application.",
     "A DHCP lease is an IP address assignment. It does not log a user into applications.",
     "Spanning Tree is a Layer 2 loop protocol. It is not an identity protocol.",
     "A cable certifier measures wiring. It does not issue authentication assertions."]))

Q.append(item(P, 103, "4.1", "easy",
    "A file server is encrypted by malware and users cannot open their documents until the data is restored. Confidentiality of the old backups is intact, and the backups have not been altered. Which part of the CIA triad did this outage hit hardest?",
    ["Availability", "Confidentiality, because the users can no longer read the files", "Integrity of the backups, which the scenario says are unchanged", "The OSI physical layer as a substitute for CIA"],
    0,
    "Availability means the information is there when people need it. Encrypted production data that nobody can use is an availability failure first. Confidentiality would be the failure if the data had been disclosed. Integrity would be the failure if the contents had been quietly changed. The scenario says the backups are intact and unchanged, so the immediate pain is that production is unusable.",
    ["The documents are unavailable. That is the availability leg of the triad, whatever else the malware also did.",
     "Confidentiality fails when someone who should not see the data sees it. Users being locked out of their own files is not a disclosure.",
     "The scenario says the backups were not altered. Integrity of those copies is not the thing that failed.",
     "The OSI model describes network layers. It is not a replacement name for the CIA triad."]))

Q.append(item(P, 104, "4.1", "medium",
    "An unpatched VPN appliance is reachable from the internet. No one has used the hole yet, as far as the logs show. In risk language, what is the unpatched hole itself?",
    ["A vulnerability", "An exploit that has already succeeded", "A risk score with no weakness underneath it", "A physical lock"],
    0,
    "A vulnerability is a weakness, such as a missing patch. A threat is something that could take advantage of it, such as an attacker scanning the internet. An exploit is the method that uses the weakness. Risk is the exposure you have when a threat can use a vulnerability and cause harm. The hole, by itself, is the vulnerability. It is not yet an incident.",
    ["The missing patch is the weakness. That is the vulnerability, whether or not someone has used it today.",
     "An exploit is the technique that uses a weakness. The logs do not show that this has happened.",
     "Risk is what you get when a threat meets a vulnerability. The unpatched hole is the vulnerability, not the whole calculation.",
     "A lock is a physical control. A missing software patch is not a lock."]))

Q.append(item(P, 105, "4.1", "medium",
    "A laptop disk is encrypted with a full-disk product. The VPN encrypts traffic while the user is traveling. Which statement pairs the controls correctly?",
    ["Disk encryption protects data at rest. The VPN protects data in transit", "The VPN protects the files while the laptop is powered off in a hotel safe", "Disk encryption protects packets on the hotel Wi-Fi", "Neither control matters if the user has a password"],
    0,
    "Data at rest is stored data. Full-disk encryption protects the drive if the laptop is stolen and powered off. Data in transit is data crossing a network. The VPN encrypts that path. Each control does the job the other one does not. A password on the login screen does not replace either one if the disk is unencrypted or the cafe Wi-Fi is open.",
    ["At rest is the disk. In transit is the VPN. That is the correct pairing.",
     "A powered-off laptop is not sending VPN traffic. The VPN does not protect a disk sitting in a safe.",
     "Disk encryption does not wrap the packets leaving the Wi-Fi radio. Those packets need a VPN or another transit control.",
     "A password helps at login. It does not encrypt a stolen disk that was never encrypted, and it does not encrypt the hotel Wi-Fi."]))

Q.append(item(P, 106, "4.1", "easy",
    "A retailer stores cardholder data, and a separate product stores personal data of people in the European Union. Which pairing of obligations is accurate?",
    ["PCI DSS applies to the cardholder data. GDPR applies to the EU personal data", "PCI DSS applies only to EU personal data and says nothing about cards", "GDPR is the wireless encryption standard", "Neither framework can apply if the servers are in a cloud region"],
    0,
    "PCI DSS is the card-brand standard for handling payment cards. GDPR is the EU privacy law, and it can apply based on whose data you hold, not only on which country the office is in. Cloud does not erase either duty. You also have to care about data locality if a contract or a law says the data must stay in a region. GDPR is not a Wi-Fi cipher.",
    ["Cards point to PCI DSS. EU personal data points to GDPR. A company can owe both at once for different data.",
     "PCI DSS is about payment cards. It is not the EU privacy regulation.",
     "GDPR is a privacy law. WPA2 and WPA3 are wireless protections.",
     "Putting a server in a cloud region does not cancel PCI or GDPR. The region may itself be a compliance choice."]))

Q.append(item(P, 107, "4.1", "medium",
    "A decoy server sits on a network with no production data. Any login to it is, by definition, unwelcome, and the security team gets an alert. What is that decoy?",
    ["A honeypot", "A hot site", "A golden configuration", "A load balancer"],
    0,
    "A honeypot is a system meant to be touched by attackers so you can see them. It should not hold real customer data. A network of them is a honeynet. A hot site is a real recovery site. A golden configuration is a known-good backup of a device. A load balancer serves production users. None of those should page you merely because someone logged in.",
    ["A honeypot is the decoy. An alert on any access is the point, and production data does not belong on it.",
     "A hot site is a staffed, current disaster-recovery site. People are supposed to fail over to it.",
     "A golden configuration is a baseline you restore. It is not a trap.",
     "A load balancer distributes real traffic. A login to it is not automatically an attack."]))

Q.append(item(P, 108, "4.2", "medium",
    "Several PCs suddenly think the default gateway's IP address belongs to a MAC address that is actually a desktop in the accounting VLAN. Traffic toward the internet is intermittent, and that desktop is sending unsolicited ARP replies. Which attack is this?",
    ["ARP poisoning", "A fiber cut", "A DNS AAAA record", "A Spanning Tree root election"],
    0,
    "ARP poisoning, or ARP spoofing, is a host answering ARP requests with the wrong MAC so that other hosts send traffic to the attacker. The gateway IP moving to a desktop's MAC is the textbook symptom. A fiber cut would drop the path rather than rewrite ARP. An AAAA record is IPv6 DNS. A root election changes the Layer 2 tree, not the gateway's MAC in the ARP cache.",
    ["Unsolicited false ARP replies that steal the gateway's address are ARP poisoning. Find that desktop and stop it from answering for addresses it does not own.",
     "A fiber cut is a loss of light. It does not rewrite anyone's ARP cache.",
     "An AAAA record maps a name to IPv6. It does not change a LAN gateway's MAC address.",
     "A root-bridge change alters forwarding ports. It does not make a desktop claim the router's IP."]))

Q.append(item(P, 109, "4.2", "easy",
    "In a coffee shop, a laptop sees two networks named the same as the company's guest SSID. One is much stronger and is being advertised by a small device on a nearby table. Users who join it are prompted for their company password. What is the stronger network?",
    ["An evil twin", "The company's legitimate access point, because stronger always means legitimate", "A DHCP reservation", "A plenum cable"],
    0,
    "An evil twin is a rogue access point using a trusted name so people join the attacker's radio. Signal strength is not identity. The company password should not be typed into a network that has not been authenticated. The right user action is to disconnect and report it. Staff wireless should use Enterprise authentication so a lookalike SSID is not enough.",
    ["An evil twin copies a known SSID. A stronger signal from a device on a table is a reason to distrust it, not a reason to trust it.",
     "Strength only means the radio is close. It does not prove who operates it.",
     "A DHCP reservation binds a MAC to an IP. It is not a second wireless network.",
     "Plenum is a cable rating. It does not advertise an SSID."]))

Q.append(item(P, 110, "4.2", "medium",
    "New laptops on one floor receive a default gateway and DNS server that point at a workstation, not at the company router. The company DHCP server never sees their requests. A second device on the floor is offering leases. What is on that floor?",
    ["A rogue DHCP server", "A healthy DHCP relay", "An authoritative DNS secondary", "A cable certifier"],
    0,
    "Whoever answers the DHCP discover first can hand out a gateway and DNS server of their choosing and send the client's traffic through themselves. A server no one installed is a rogue DHCP server. The fix is to remove it and to restrict which ports are allowed to offer DHCP. A relay forwards requests to the real server. It does not invent a workstation as the gateway. A certifier tests cable.",
    ["A rogue DHCP server is an unauthorized device answering lease requests. The bad gateway and DNS give it away.",
     "A relay sends the client's broadcast to the authorized server. It would not hide the request from that server and invent a new gateway.",
     "A DNS secondary answers name lookups for a zone. It does not hand out leases and gateways.",
     "A certifier measures cable. It does not offer IP addresses."]))

Q.append(item(P, 111, "4.2", "hard",
    "A user port was left as a negotiable trunk, and the native VLAN is VLAN 1, which is also a user VLAN. A security review calls this a VLAN-hopping exposure. Which change matches the defensive guidance, without any attack steps?",
    ["Make user ports access ports, tag the native VLAN or move it to an unused ID, and do not use VLAN 1 for users", "Disable Spanning Tree so trunks form faster", "Set every user port to trunk all VLANs", "Put all users in the native VLAN and disable tagging"],
    0,
    "VLAN hopping abuses a port that will become a trunk, or abuses the untagged native VLAN, to reach a VLAN the user should not reach. The defensive configuration is boring on purpose: access mode on user ports, an unused native VLAN that is not a user VLAN, and explicit trunks only where a trunk belongs. Opening every port as a trunk, or putting users in the native VLAN, widens the exposure. Spanning Tree is unrelated and should stay on.",
    ["Access ports, an unused native VLAN, and no automatic trunking are the controls that close the hopping exposure.",
     "Disabling Spanning Tree creates loop risk and does nothing for VLAN boundaries.",
     "Trunk-all on a user port is the configuration the review is complaining about, not the fix.",
     "Users in the native VLAN are in the untagged VLAN an attacker would abuse. That is the wrong direction."]))

Q.append(item(P, 112, "4.2", "easy",
    "A caller pretends to be the help desk and asks a payroll clerk to read a VPN password over the phone. A different incident last week was an email that asked the same clerk to click a link. What are the two techniques? (Choose two.)",
    ["Vishing", "Phishing", "A fiber attenuation budget", "A Spanning Tree election"],
    [0, 1],
    "Vishing is voice phishing, the phone call that asks for a secret. Phishing is the same trick in email or a similar message. They are both social engineering. Fiber budgets and Spanning Tree are network mechanics and do not describe a person being talked out of a password.",
    ["Vishing is the phone version. The caller pretending to be the help desk is vishing.",
     "Phishing is the email that baits a click or a password. The link incident is phishing.",
     "Attenuation is signal loss on a cable. It is not a conversation.",
     "A root-bridge election is a switching event. It does not ask anyone for a password."]))

Q.append(item(P, 113, "4.2", "medium",
    "A public website is unreachable because thousands of compromised home devices are sending it traffic at the same time. A single lab PC sending the same kind of traffic yesterday was a smaller event. Which labels fit yesterday and today?",
    ["Yesterday was a denial of service. Today is a distributed denial of service", "Both are ARP poisoning", "Today is a VLAN hop. Yesterday was DNSSEC", "Both are captive portals"],
    0,
    "A denial of service overwhelms a target so legitimate users cannot use it. When the traffic comes from many sources, it is distributed. One lab PC is a DoS. Thousands of devices are a DDoS. The victim's useful response is upstream filtering and the provider, not a new access VLAN. ARP poisoning, VLAN hopping, and captive portals are different problems.",
    ["One source is DoS. Many coordinated sources are DDoS. The scale and the number of sources are the difference.",
     "ARP poisoning rewrites LAN address mappings. It is not a flood from home devices against a public site.",
     "A VLAN hop crosses a Layer 2 boundary. DNSSEC signs DNS data. Neither one is this flood.",
     "A captive portal is a login page on a guest network. It does not describe a traffic flood."]))

Q.append(item(P, 114, "4.2", "medium",
    "Only users of the branch resolver are sent to a fake banking site. Users of a resolver in another city get the real address. The fake answer appeared in the branch cache after a suspicious response. Which attack fits?",
    ["DNS poisoning", "A bad crimp on one user's patch cord", "STP blocking one access port", "A full disk on a laptop"],
    0,
    "DNS poisoning puts a false record in a resolver's cache so later clients are sent to the wrong address. The clue is that everyone who uses that resolver is affected and everyone who uses a different resolver is not. A bad patch cord, a blocked port, or a full disk would be one computer, and they would not rewrite a name for the whole branch.",
    ["A poisoned resolver hands out the attacker's address until the bad cache entry expires or is flushed. That matches a one-site, one-resolver failure.",
     "A bad patch cord affects the person using that cord. It does not change the answer for every user of a resolver.",
     "Spanning Tree blocking a port would drop that port's traffic entirely, not rewrite one website.",
     "A full disk is a local storage problem. It does not change DNS for a branch."]))

Q.append(item(P, 115, "4.2", "hard",
    "On an untrusted wireless network, a device sits in the path of a user's sessions and relays them, reading anything that is not protected end to end. Which term describes that position?",
    ["An on-path attack", "A cable certifier", "A golden configuration", "A cold site"],
    0,
    "An on-path attack, the current name for what older material called a man-in-the-middle attack, is an attacker who relays traffic between two parties. Encryption that ends at the real server, plus a VPN that does not trust the local network, is what keeps the relay from reading the payload. A certifier, a baseline config, and a cold site are not attackers.",
    ["On-path is the position between the user and the destination, relaying the session. Untrusted Wi-Fi is a common place it shows up.",
     "A certifier tests cable quality. It does not relay sessions.",
     "A golden configuration is a known-good backup of a device.",
     "A cold site is an empty recovery location. It is not an attacker on a wireless network."]))

Q.append(item(P, 116, "4.3", "easy",
    "A new switch still has the vendor's admin password, and twenty unused access ports are enabled. A hardening checklist is open. Which two changes belong on the first pass? (Choose two.)",
    ["Change the default password", "Disable the unused ports", "Turn off Spanning Tree", "Set the SNMP community to public"],
    [0, 1],
    "Hardening starts with the defaults an attacker already knows and with the ports nobody is watching. Change the password and shut the unused ports. Spanning Tree should stay on so a loop still gets blocked. The community string 'public' is the famous insecure SNMP default and should not be introduced.",
    ["The vendor password is published in manuals. Leaving it is an open door, so changing it is a first-day item.",
     "An open port is a place to plug in. Disabling unused ports removes that opportunity until someone needs the jack.",
     "Spanning Tree is a safety feature. Turning it off is not hardening.",
     "The community 'public' is a well-known read string. Setting it is the opposite of hardening SNMP."]))

Q.append(item(P, 117, "4.3", "hard",
    "Users authenticate before a switch port forwards general traffic. The PC runs a supplicant, the switch is the authenticator, and a RADIUS server decides. Which framework is this?",
    ["802.1X", "STP root guard only", "A captive portal on an open SSID with no port authentication", "TFTP"],
    0,
    "802.1X is port-based network access control. The supplicant is the client, the authenticator is the switch or access point, and the authentication server is usually RADIUS. Until the user or the device succeeds, the port does not carry ordinary traffic. Root guard is a Spanning Tree feature. A captive portal is a web gate. TFTP is file transfer.",
    ["802.1X is the standard that uses those three roles. The switch enforces, and RADIUS decides.",
     "Root guard protects which switch can be root. It does not authenticate a user on a port.",
     "A captive portal can gate a browser session. It is not the supplicant-authenticator-RADIUS port control described here.",
     "TFTP copies files and does not decide whether a switch port should forward."]))

Q.append(item(P, 118, "4.3", "medium",
    "A switch port is limited to one learned MAC address. When a small unmanaged switch is plugged in and a second MAC appears, the port goes error-disabled. Which feature did that, and what should the technician do?",
    ["Port security did that. Find out what was plugged in, and do not just disable the feature", "DNSSEC did that", "The port shut down because the native VLAN matched", "A heat map disabled the port"],
    0,
    "Port security caps how many MAC addresses a port may learn. A violation can shut the port, which is the error-disabled state. That is the feature working, not a mystery failure. The technician should see what was added, remove it if it is not allowed, and only then restore the port. Turning the feature off would hide the next unauthorized switch. DNSSEC, the native VLAN, and a heat map do not error-disable a port for a second MAC.",
    ["Port security is the MAC limit. The right follow-up is to identify the extra device, not to remove the control.",
     "DNSSEC validates DNS data. It does not count MAC addresses on a switch port.",
     "A matching native VLAN is what you want on a trunk. It does not shut a port because two MACs appeared.",
     "A heat map is a picture of wireless signal. It does not error-disable switch ports."]))

Q.append(item(P, 119, "4.3", "hard",
    "A router ACL is processed top down and stops at the first match. The current list permits 10.0.0.0/8 and, farther down, denies 10.1.1.50. Users at 10.1.1.50 are still getting through. Why?",
    ["The broader permit matches first, so the later deny never runs", "ACLs process the last line first", "An implicit permit at the top allows everything before the list is read", "Denies only work on UDP"],
    0,
    "First match wins. 10.1.1.50 is inside 10.0.0.0/8, so the permit catches it and the more specific deny below is dead. Put the specific deny above the broad permit, or narrow the permit. There is an implicit deny at the end of an ACL, not an implicit permit at the top. ACLs are not limited to UDP.",
    ["The /8 permit matches the host, and processing stops. The deny has to be placed before that permit if it is going to matter.",
     "ACLs are first match, from the top. The last line is not the one that wins.",
     "The implicit rule at the end is a deny, not a permit at the top. Traffic is not allowed before the list is read.",
     "ACLs can match TCP, UDP, and other traffic. The miss here is the order, not the protocol."]))

Q.append(item(P, 120, "4.3", "medium",
    "A public web server must be reachable from the internet and must not sit on the same subnet as payroll. The design puts it on a network between the outside firewall and the inside firewall. What is that network called?",
    ["A screened subnet", "The native VLAN of the user access layer", "An anycast group", "A cold site"],
    0,
    "A screened subnet, often still called a DMZ in older speech, is a zone for systems the internet must reach. If that web server is compromised, the inside firewall is still between the attacker and payroll. Putting the server on the user VLAN removes that wall. Anycast is an addressing method. A cold site is a recovery location.",
    ["A screened subnet is the in-between zone for public services. It is the right place for this web server.",
     "The user native VLAN is an internal network. A public web server does not belong there with payroll.",
     "Anycast shares an address among servers for routing. It is not the name of the security zone.",
     "A cold site is an empty recovery site. It is not the live zone in front of the inside firewall."]))

Q.append(item(P, 121, "4.3", "medium",
    "The company wants to block a list of known malicious websites by address, and separately wants to stop a file upload that contains a restricted customer-account number even if the site itself is allowed. Which two controls match those two jobs? (Choose two.)",
    ["URL filtering for the known-bad sites", "Content filtering for the restricted number inside the upload", "A larger MTU", "Disabling ARP"],
    [0, 1],
    "URL filtering decides based on the address or category of the site. Content filtering looks at what is inside the traffic, such as a sensitive number in an upload. You need both because an allowed site can still carry a forbidden payload, and a forbidden site should be blocked even when the payload looks boring. MTU and ARP do not implement either policy.",
    ["URL filtering is the control that blocks destinations by site or category. That is the known-bad list.",
     "Content filtering inspects the material being transferred. A customer-account number inside an otherwise allowed upload is a content decision.",
     "MTU is a frame-size setting. It does not classify websites or files.",
     "Disabling ARP would break LAN addressing. It is not a web-control feature."]))

if __name__ == "__main__":
    from common import dump
    dump("n10-009", {"q-d4.json": Q})
