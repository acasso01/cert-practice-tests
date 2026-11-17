from common import item

P = "c1"
Q1, Q2 = [], []

Q1.append(item(P, 1, "1.1", "easy",
    "A laptop needs more memory. The technician has a desktop DDR4 DIMM from a donor PC and a SODIMM of the same generation. Which module belongs in the laptop?",
    ["The SODIMM", "The desktop DIMM, because the pins are the same", "Either one, because laptops accept both sockets", "A DIMM with the heat spreader removed so it fits"],
    0,
    "Laptops use SODIMMs, the short modules. A desktop DIMM is longer, has a different pin count, and will not seat in a laptop slot. Forcing it, or cutting a heat spreader to make it fit, damages the machine. Match the generation too: a DDR4 SODIMM is not a DDR5 SODIMM.",
    ["SODIMM is the laptop form factor. That is the module that fits the slot.",
     "Desktop DIMMs and SODIMMs are not the same length or pinout, even in the same DDR generation.",
     "A laptop does not have a desktop DIMM socket. There is no either-or.",
     "Removing a heat spreader does not change the connector. The DIMM still will not fit, and you can damage it."]))

Q1.append(item(P, 2, "1.1", "medium",
    "After a laptop screen is replaced, Wi-Fi signal is terrible. The new panel displays a normal image, and the wireless card was not removed. What should be checked in the hinge and bezel area?",
    ["The wireless antenna leads that route through the hinge into the lid", "The SODIMM, because the screen uses system memory as an antenna", "The PSU voltage switch", "The desktop PCIe slot"],
    0,
    "Laptop Wi-Fi antennas are commonly in the display lid, with thin leads that run through the hinges to the wireless card. A screen replacement that forgets to reconnect those leads leaves the radio transmitting into the chassis. The image working means the panel is fine. There is no desktop power switch or PCIe slot involved.",
    ["The antenna leads are the usual casualty of a lid repair. Re-seat them on the wireless card before you replace the card.",
     "System memory is not the Wi-Fi antenna. A bad SODIMM would show memory errors, not a weak radio after a screen swap.",
     "A laptop does not have the red 115/230 switch of an old desktop power supply.",
     "There is no desktop PCIe slot in this repair. The radio is an internal laptop card."]))

Q1.append(item(P, 3, "1.1", "medium",
    "A user wants the old spinning laptop drive replaced with an SSD and wants the laptop to boot the existing Windows installation. Copying the Documents folder to the new drive did not make it boot. What was missing?",
    ["A disk clone or image that includes the boot and system partitions, not just the user files", "Formatting the SSD as FAT16", "Deleting the recovery partition and nothing else", "Enabling Bluetooth during the copy"],
    0,
    "A bootable migration has to bring the boot records and the Windows partitions, not only the user's documents. Cloning or imaging the disk does that. A file copy of Documents leaves a blank drive with no bootloader. FAT16 is obsolete and too small. Bluetooth is unrelated. After the clone, do not leave both drives connected in a way that confuses which disk is first in the boot order.",
    ["The boot environment lives outside the Documents folder. Clone or image the whole disk, then confirm the boot order.",
     "FAT16 is not a Windows system file system for a modern laptop and cannot hold the installation.",
     "Deleting recovery does not create a bootable copy of Windows on the new drive.",
     "Bluetooth does not copy boot sectors and does not make a drive bootable."]))

Q1.append(item(P, 4, "1.1", "easy",
    "A laptop fingerprint reader fails, and the user cannot sign in even though they know the PIN. The reader is the only method configured. What is the practical expectation for a biometric sign-in?",
    ["Biometrics should fall back to a PIN or password, and that fallback has to be enrolled", "A failed fingerprint must lock the drive permanently", "Biometrics replace the need for any other factor and have no fallback", "The fingerprint reader stores the Windows installation"],
    0,
    "A fingerprint or a face scan is a convenience factor and a second check. It fails closed to something the user knows, usually a PIN or a password. If that fallback was never set, or the user has forgotten it, the reader failing locks them out until the account is recovered. The reader does not contain the operating system, and a failed scan should not destroy the drive.",
    ["Enroll a PIN or password alongside the fingerprint. When the reader fails, that knowledge factor is how the user gets in.",
     "A failed reader is a hardware problem, not a command to wipe the disk.",
     "Vendors design biometrics with a fallback because readers get dirty, wet, or damaged.",
     "The reader stores a template, not the Windows installation. Replacing the reader does not reinstall Windows."]))

Q1.append(item(P, 5, "1.1", "medium",
    "A technician is about to replace a laptop keyboard. The battery is internal but is reachable, and the AC adapter is still plugged in. What should happen before a screwdriver touches the keyboard screws?",
    ["Power the laptop off, unplug the adapter, and disconnect the battery if the service manual allows it", "Leave it running so the keyboard lights show which screws are live", "Only remove the AC adapter and keep the battery connected while prying", "Heat the keyboard with a heat gun before disconnecting power"],
    0,
    "Internal work starts with the machine off and the power sources removed. Unplug the adapter and, when the manual shows a connector, disconnect the battery so a slip does not short a live rail. Leaving it running is how a screwdriver becomes a short. Heat is for some glued screens, not a reason to skip power removal on a keyboard.",
    ["Off, unplugged, and battery disconnected when the design allows it. That is the safe start for a keyboard replacement.",
     "A running laptop plus metal tools is a short waiting to happen. The lights are not worth it.",
     "The battery can still feed the board after the adapter is out. Disconnect it if the manual gives you that connector.",
     "A heat gun is the wrong first tool for a screwed-in keyboard and does not replace isolating power."]))

Q1.append(item(P, 6, "1.2", "medium",
    "An older laptop uses a fluorescent backlight. The screen is very dim, and a flashlight shone on it reveals a faint image. A newer LED-backlit laptop with the same faint-image symptom does not have the part this older unit uses. What is that older part?",
    ["The inverter", "The SODIMM", "The Ethernet magnetics", "The CMOS battery"],
    0,
    "CCFL backlights need an inverter to produce the high voltage that lights the lamp. A failed inverter gives you a faint panel and no backlight. LED backlights do not use that inverter, so the same faint image on an LED machine points at the LED circuit or the panel instead. Memory, Ethernet, and the CMOS battery do not light the panel.",
    ["The inverter drives a CCFL backlight. Dim image, visible with a flashlight, on a fluorescent-era laptop is the inverter or the lamp.",
     "SODIMM is memory. A bad module does not selectively turn the backlight off while leaving a faint image.",
     "Ethernet magnetics are in the network jack. They do not backlight a panel.",
     "The CMOS battery keeps firmware settings. It does not power a backlight."]))

Q1.append(item(P, 7, "1.2", "easy",
    "A designer complains that a laptop screen washes out when several people view it from the sides. A different laptop stays readable from those angles and has better color, at a higher price. Which panel type is the better wide-angle choice?",
    ["IPS", "TN", "A CRT salvaged from a desktop", "A panel with the inverter removed"],
    0,
    "IPS panels are the ones with wide viewing angles and stronger color. TN panels are cheaper and often faster, and they shift and darken when you leave the center. A CRT is not a laptop panel. Removing an inverter does not improve angles. If the job is color and a shared view, IPS is the specification to ask for.",
    ["IPS holds color and contrast as you move off center. That is the panel the designer is asking for.",
     "TN is the panel that looks wrong from the side. It is the symptom, not the upgrade.",
     "A CRT is a tube display. It does not fit a laptop lid and is not a current option.",
     "An inverter lights an old backlight. Removing it makes the screen dark. It does not change the viewing angle of the liquid crystal."]))

Q1.append(item(P, 8, "1.2", "medium",
    "A tablet shows a perfect image, but touches land an inch away from the finger and sometimes not at all. The glass is intact. Which component is failing?",
    ["The digitizer", "The backlight inverter on a device that has no CCFL", "The CMOS battery", "The SATA cable"],
    0,
    "The digitizer is the touch layer. A good image with bad or offset touch is the digitizer or its calibration, not the display panel. There is no fluorescent inverter on a typical tablet, no CMOS battery in the laptop sense doing this job, and no SATA cable driving the touch layer. Recalibrate if the OS offers it, and replace the digitizer if calibration does not hold.",
    ["The digitizer turns touch into coordinates. Offset or dead touch with a healthy picture is that layer.",
     "A tablet backlight is not a CCFL inverter problem, and the image is already visible, so the light is working.",
     "A CMOS battery holds firmware time and settings on a PC. It does not map touch coordinates.",
     "SATA connects storage. It is not the touch sensor."]))

Q1.append(item(P, 9, "1.2", "medium",
    "A laptop with an OLED panel has a ghost of a toolbar that stayed on screen for months. The ghost is visible on every wallpaper. What is that called, and is it a dead pixel?",
    ["Burn-in. It is not the same thing as a single dead pixel", "A dead pixel, because OLED cannot burn in", "Backlight bleed, because OLED uses a CCFL", "A stuck inverter"],
    0,
    "OLED pixels emit their own light and can age unevenly. A static toolbar that remains as a shadow is burn-in. A dead pixel is one dot that stays dark or one color. OLED does not use a CCFL backlight, so there is no inverter and no backlight bleed in the LCD sense. Reduce static content and brightness to slow further burn-in. The existing ghost may not fully disappear.",
    ["Burn-in is the permanent shadow of a static image. That is the toolbar ghost, and it is a known OLED risk.",
     "A dead pixel is a single element. A toolbar-shaped ghost across the panel is burn-in, and OLED can suffer it.",
     "OLED has no CCFL backlight. Bleed is an LCD backlight symptom, not this shadow.",
     "There is no inverter on an OLED panel. The symptom is worn pixels, not a missing high-voltage board."]))

Q1.append(item(P, 10, "1.2", "easy",
    "A laptop lid is cracked and the image is a black smear, but an external monitor works. The GPU is therefore probably fine. Which statement is the right next conclusion?",
    ["The internal panel or its cable is the failed part", "The motherboard video circuit is dead because the lid is cracked", "Replace the power supply before the panel", "The SODIMM is the display"],
    0,
    "An external monitor that looks normal means the graphics output is producing a picture. The failure is between that output and the internal panel: the panel itself or the cable that runs through the hinge. A cracked lid makes those two parts the likely ones. Replacing the board or the power supply ignores the test you already ran.",
    ["The external display isolates the fault to the internal panel or its cable. Start there.",
     "A working external monitor is evidence the graphics circuit is alive. The cracked lid points at the panel path, not at a dead GPU.",
     "The power supply is not indicated. The laptop is up and driving an external screen.",
     "Memory is not the display panel. A bad SODIMM would not be proven by a cracked lid and a good external picture."]))

Q1.append(item(P, 11, "1.3", "easy",
    "A phone must connect to a modern Windows laptop to charge and to transfer photos, and the phone's only port is USB-C. The laptop has USB-C and USB-A. Which cable is the direct fit?",
    ["USB-C to USB-C", "Lightning to VGA", "A serial DB9 cable", "RG-6 coax"],
    0,
    "USB-C on both ends is the direct cable. USB-C to USB-A also works if you use the laptop's USB-A port, but the direct match for the ports named as preferred is C to C. Lightning is an Apple connector. DB9 is legacy serial. RG-6 is cable-TV coax. None of those carry this phone's photos.",
    ["USB-C to USB-C connects the two USB-C ports for charge and data, assuming the laptop port supports that role.",
     "Lightning is not the phone's port, and VGA is a video connector. That cable does not fit either device.",
     "DB9 serial is an old PC port. It is not how a USB-C phone transfers photos.",
     "RG-6 carries RF cable signals. It is not a phone cable."]))

Q1.append(item(P, 12, "1.3", "medium",
    "A user wants to move a 2 GB video from a phone to a laptop and suggests NFC because the devices can already tap to pair. What is the right guidance?",
    ["NFC is for very short range and tiny exchanges. Use USB or Wi-Fi for a 2 GB file", "NFC is faster than USB 3 for multi-gigabyte video", "NFC requires a 100 meter cable", "NFC is the same thing as a docking station"],
    0,
    "NFC works across a few centimeters and is used for pairing, badges, and payments, not for moving gigabytes. A 2 GB video wants a USB cable or a Wi-Fi transfer. NFC is not faster than USB 3, it does not use a long cable, and it is not a dock.",
    ["NFC is the tap. It is the wrong transport for a large video. Plug in USB or use a wireless file transfer.",
     "USB 3 moves large files far faster than NFC. NFC was never the bulk-transfer bus.",
     "NFC is wireless and extremely short. A 100 meter cable is the opposite description.",
     "A dock is a physical accessory that adds ports and often power. NFC is a radio."]))

Q1.append(item(P, 13, "1.3", "medium",
    "A laptop on a desk must gain two monitors, Ethernet, and power through one connection to a device that also charges it. A cheaper accessory only breaks out extra USB ports and does not charge the laptop. Which is the fuller device?",
    ["A docking station", "A port replicator that the question says does not charge or add video", "A Bluetooth headset", "A microSD card"],
    0,
    "A docking station is the fuller accessory: power, video, and network, often through one connector. A port replicator is the simpler breakout of ports and, in this question, does not charge or drive the monitors. A headset and a memory card do not add desktop ports.",
    ["The dock is the device that supplies power, displays, and Ethernet together. That matches what the desk needs.",
     "The question's simpler accessory is the port replicator. It is not the one that charges and drives two monitors.",
     "A headset is audio. It does not add monitors or Ethernet.",
     "A microSD card is storage. It is not a port expander."]))

Q1.append(item(P, 14, "1.3", "easy",
    "A Bluetooth headset is not discovered by a phone. The headset is charged and the phone's Bluetooth radio is on. Which sequence should the user follow?",
    ["Put the headset in pairing mode, select it on the phone, enter the PIN if asked, and test audio", "Enable NFC on a monitor and expect the headset to appear", "Install a desktop DIMM in the phone", "Disable the phone radio before pairing"],
    0,
    "Bluetooth pairing is: make the accessory discoverable, find it on the phone, confirm the PIN or the prompt, and then play audio to prove the link. Turning the phone radio off makes discovery impossible. NFC is a different radio. A DIMM does not fit a phone and does not pair a headset.",
    ["Pairing mode, selection, PIN, and a real audio test is the complete Bluetooth setup.",
     "NFC will not discover a Bluetooth headset. The headset has to be in Bluetooth pairing mode.",
     "A desktop memory module is not a phone part and has nothing to do with a headset.",
     "The radio has to be on for the phone to see the headset. Turning it off is the opposite of the fix."]))

Q1.append(item(P, 15, "1.4", "medium",
    "A legacy CDMA phone cannot roam in a city where it used to work. The carrier says the roaming list on the phone is stale. What kind of update is that?",
    ["A PRL update", "A BIOS update on a desktop motherboard", "A SATA firmware update", "An inverter replacement"],
    0,
    "CDMA phones used a Preferred Roaming List to decide which towers they may use. When that list is old, roaming fails even though the radio is fine. GSM phones use a SIM and do not depend on a PRL the same way. A desktop BIOS, a disk firmware, and a display inverter are unrelated repairs.",
    ["PRL is the CDMA roaming list. Updating it is the carrier's fix for this legacy phone.",
     "A desktop BIOS does not store a phone's tower list.",
     "SATA firmware is for a storage device. It does not update cellular roaming.",
     "An inverter lights an old laptop backlight. It is not a phone firmware object."]))

Q1.append(item(P, 16, "1.4", "easy",
    "A company phone must receive corporate email, and the company must be able to require a PIN and remove company data if the phone is lost. Which control plane does that?",
    ["Mobile device management", "A local hosts file", "A desktop port replicator", "The laptop inverter"],
    0,
    "MDM enrolls the phone, pushes mail and corporate apps, enforces a PIN, and can remote-wipe company data. That is the tool for a lost phone. A hosts file, a port replicator, and an inverter do not manage mobile policy.",
    ["MDM is how the company configures mail, requires the PIN, and wipes the device if it goes missing.",
     "A hosts file overrides name resolution on a computer. It does not enroll a phone.",
     "A port replicator adds laptop ports. It does not manage a handset.",
     "An inverter is a backlight part. It has no remote-wipe function."]))

Q1.append(item(P, 17, "1.4", "medium",
    "A user tethers a laptop to a phone all day and then is surprised by a huge cellular bill and a hot, empty phone. The laptop was downloading cloud photos. What should change?",
    ["Stop bulk sync while on the hotspot, and prefer Wi-Fi for large transfers", "Leave the hotspot on and raise the screen brightness to save power", "Replace the phone's digitizer", "Convert the laptop to a CDMA PRL-only device"],
    0,
    "A hotspot shares the cellular plan and the battery. Photo libraries are the classic way to burn both. Restrict background sync to Wi-Fi and turn the hotspot off when it is not needed. Brightness does not save cellular data. The digitizer and a PRL update do not move the traffic onto Wi-Fi.",
    ["Large syncs belong on Wi-Fi. The hotspot metered the photos and drained the phone. Limit what is allowed to run over cellular.",
     "More brightness spends more battery. It does not reduce the cellular download.",
     "The touch layer is not why the bill is large. The radio was busy.",
     "A PRL is a legacy roaming list. It does not stop a cloud client from downloading photos."]))

Q1.append(item(P, 18, "1.4", "medium",
    "A phone shows full cellular bars indoors and still places the user on the wrong street in a map app. GPS is enabled, and the user is between tall buildings. What is the likely limitation?",
    ["GPS needs a sky view, so indoors the phone is falling back to a coarser location", "The map requires a desktop DIMM", "Bars of cellular signal are the same measurement as a GPS fix", "The digitizer is the GPS antenna"],
    0,
    "GPS listens to satellites. Indoors, and in urban canyons, that signal is weak, so the phone leans on cellular and Wi-Fi location, which can be a building or two off. Cellular bars mean the tower is strong. They are not a count of GPS satellites. Memory modules and the touch layer are not the GPS receiver.",
    ["Weak satellite visibility explains a wrong indoor position even when cellular looks perfect. Move near a window to test the GPS fix.",
     "A DIMM is desktop or laptop memory. It is not part of phone location.",
     "Cellular signal and a GPS fix are different radios. Full bars do not mean several satellites are locked.",
     "The digitizer senses touch. It is not the satellite antenna."]))

Q1.append(item(P, 19, "1.4", "easy",
    "A user wants contacts, calendar, and mail from a company Microsoft 365 account on a new phone, and does not want personal photos uploading on the cellular plan. What should be configured?",
    ["The Microsoft 365 account, syncing mail, contacts, and calendar, with photo sync limited to Wi-Fi or turned off", "Only a Bluetooth pairing to a headset", "A PRL update and nothing else", "An inverter calibration"],
    0,
    "Microsoft 365, Google Workspace, and iCloud are the account types the exam expects you to add, and mail, contacts, calendar, and photos are the data types. You can choose which of those sync, and you should keep large photo uploads off the cellular radio. A headset pairing, a PRL, and an inverter do not create the mailbox.",
    ["Add the work account and sync the three data types they asked for. Leave photos off the metered connection.",
     "Bluetooth audio does not download a mailbox or a calendar.",
     "A PRL update is a legacy roaming-list refresh. It does not configure Microsoft 365.",
     "An inverter is a laptop backlight part. It does not sync mail."]))

# Domain 2 starts at 20
Q2.append(item(P, 20, "2.1", "easy",
    "A technician must allow encrypted web traffic and block the unencrypted web port. Which ports are those?",
    ["Allow 443 and block 80", "Allow 80 and block 443", "Allow 25 and block 110", "Allow 3389 and block 53"],
    0,
    "HTTPS is TCP 443 and HTTP is TCP 80. Encrypted web traffic is 443. Port 25 is SMTP and 110 is POP3, which are mail. Port 3389 is Remote Desktop and 53 is DNS. None of those pairs is the web pair.",
    ["443 is HTTPS and 80 is HTTP. Allowing 443 and blocking 80 matches the request.",
     "That is the reverse. Port 80 is the clear-text web port.",
     "25 and 110 are mail ports, SMTP and POP3. They are not web.",
     "3389 is RDP and 53 is DNS. Blocking DNS would break name resolution rather than clear-text web."]))

Q2.append(item(P, 21, "2.1", "easy",
    "Users need Remote Desktop to a Windows PC. The firewall is wide open except for the RDP port, which is still closed. Which port should be opened?",
    ["3389", "53", "25", "143"],
    0,
    "RDP listens on TCP 3389. DNS is 53, SMTP is 25, and IMAP is 143. Opening the mail or name ports will not let Remote Desktop complete. Also remember that Windows Home cannot host an incoming RDP session even if the port is open. That edition limit is a Core 2 topic, but the port itself is 3389.",
    ["TCP 3389 is Remote Desktop. That is the port the firewall still has closed.",
     "Port 53 is DNS. Opening it does not start an RDP session.",
     "Port 25 is SMTP mail transfer. It is not a desktop session.",
     "Port 143 is IMAP mail retrieval. It is not RDP."]))

Q2.append(item(P, 22, "2.1", "medium",
    "A mail client must send mail to a server and download mail with IMAP. Which ports are the send port and the IMAP port on the A+ list?",
    ["SMTP 25 to send, IMAP 143 to retrieve", "POP3 110 to send, DNS 53 to retrieve", "RDP 3389 to send, HTTP 80 to retrieve", "DHCP 67 to send, DHCP 68 to retrieve"],
    0,
    "SMTP on port 25 is the transfer protocol clients and servers use to send mail in the A+ objective list. IMAP on 143 retrieves and leaves mail on the server. POP3 on 110 also retrieves, but it is not IMAP. DNS, RDP, HTTP, and DHCP are not mail retrieval.",
    ["25 is SMTP and 143 is IMAP. That is the send-and-retrieve pair the question asked for.",
     "POP3 retrieves mail. It does not send it. DNS resolves names and does not download a mailbox.",
     "RDP is a remote desktop and HTTP is the web. Neither one is the mail protocol in the question.",
     "DHCP assigns addresses on 67 and 68. It does not carry email."]))

Q2.append(item(P, 23, "2.1", "medium",
    "Which two protocols are connection-oriented on the A+ objective list? (Choose two.)",
    ["HTTPS", "SSH", "DHCP", "TFTP"],
    [0, 1],
    "HTTPS and SSH use TCP, which sets up a connection and recovers lost data. DHCP and TFTP use UDP. They are connectionless, which is why a device can use them before it has a full session. The question is about the transport, not about which service is more important.",
    ["HTTPS is TCP 443. It is connection-oriented.",
     "SSH is TCP 22. It is connection-oriented.",
     "DHCP uses UDP. It does not build a TCP session before offering an address.",
     "TFTP uses UDP 69. It is connectionless file transfer."]))

Q2.append(item(P, 24, "2.1", "easy",
    "A PC cannot resolve names. Other traffic to numeric addresses works. Which port and protocol are the first suspect?",
    ["DNS on port 53", "RDP on port 3389", "IMAP on port 143", "SMTP on port 25"],
    0,
    "DNS is the name service, and it uses port 53. If numbers work and names do not, DNS is the service to test. RDP is remote desktop, IMAP and SMTP are mail. None of those translate a name into an address.",
    ["Port 53 is DNS. That is the lookup that turns a name into an address.",
     "Port 3389 is Remote Desktop. It assumes you already know where the host is.",
     "IMAP downloads mail. It is not the general name service.",
     "SMTP sends mail. A failure there would not, by itself, explain every name failing while IP addresses work."]))

Q2.append(item(P, 25, "2.2", "easy",
    "A small office still has a hub between the modem and four PCs. Every PC sees every frame, and collisions are common. Which replacement separates those collision domains?",
    ["A switch", "Another hub", "A longer coax run", "A Bluetooth adapter on one PC"],
    0,
    "A hub is one collision domain. Every port hears every frame. A switch learns MAC addresses and gives each port its own collision domain, so the four PCs no longer collide with each other. Another hub repeats the problem. Coax and Bluetooth are not the wired fix.",
    ["A switch forwards by MAC address and breaks the hub's single collision domain into one per port.",
     "Another hub is the same device class that is causing the collisions.",
     "A longer coax run does not learn MAC addresses and does not replace the hub's behavior.",
     "One Bluetooth adapter does not re-architect the wired segment."]))

Q2.append(item(P, 26, "2.2", "medium",
    "An IP phone is silent and unpowered. The access switch has no PoE, and a midspan injector is available. Where does the injector go?",
    ["Between the switch and the phone, adding power onto the Ethernet run", "Between the monitor and the HDMI port", "Inside the phone's SIM slot", "On the fiber uplink, because PoE is optical"],
    0,
    "A PoE injector sits in the copper Ethernet path and adds power so a phone or an access point can run from the cable when the switch cannot supply it. It does not go on HDMI, in a SIM slot, or on fiber. Fiber does not carry 802.3af power to a phone.",
    ["The injector is an in-line power source on the copper drop. That is how you feed a phone from a non-PoE switch.",
     "HDMI carries video and audio. It is not the phone's Ethernet power path.",
     "A SIM slot is a cellular identity. It does not accept a PoE injector.",
     "Standard PoE is an electrical signal on twisted pair, not light on fiber."]))

Q2.append(item(P, 27, "2.2", "medium",
    "Horizontal cables from the wall jacks are punched onto the back of a passive device in the closet. Short patch cords then run from the front of that device to the switch. What is the passive device?",
    ["A patch panel", "A router", "A firewall", "An active DHCP server"],
    0,
    "A patch panel is the passive termination for the permanent runs. You punch the horizontal cable on the back and use short, replaceable patch cords on the front. The router, the firewall, and the DHCP server are active devices. They are not the punch-down field.",
    ["The patch panel is the passive connector field between the in-wall cable and the switch.",
     "A router forwards between networks. It is not where you punch horizontal cabling.",
     "A firewall filters traffic. It is not a passive termination block.",
     "A DHCP server hands out addresses. It does not terminate the building cabling."]))

Q2.append(item(P, 28, "2.2", "easy",
    "A fiber handoff from the provider lands on a small box that presents Ethernet to the customer's router. The Wi-Fi is down, and the box's optical light is dark. What is that box, and why does it matter?",
    ["It is the ONT. A dark optical light means the fault may be the provider fiber, not the Wi-Fi router", "It is a hub, so a dark light means the Wi-Fi password is wrong", "It is a SODIMM", "It is a print spooler"],
    0,
    "An optical network terminal converts the provider's fiber to Ethernet. If its optical light is out, the router has no internet feed, and replacing the Wi-Fi router will not restore the fiber. Check the ONT and the provider before you reconfigure wireless. A hub, a memory module, and a print spooler do not terminate a fiber handoff.",
    ["The ONT is the fiber handoff. No light means you escalate the circuit, rather than blaming the SSID.",
     "A hub does not terminate optical service, and a dark optical light is not a password error.",
     "SODIMM is laptop memory. It is not a provider demarcation.",
     "The print spooler queues print jobs. It does not convert fiber to Ethernet."]))

Q2.append(item(P, 29, "2.3", "easy",
    "A buyer asks for a Wi-Fi 5 laptop radio and the spec sheet uses the 802.11 letters instead of the marketing name. Which 802.11 description matches Wi-Fi 5?",
    ["802.11ac, primarily 5 GHz", "802.11b, 2.4 GHz at 11 Mbps", "802.11a described as 2.4 GHz", "802.11g described as a 6 GHz-only standard"],
    0,
    "802.11ac is Wi-Fi 5 and operates in the 5 GHz band. 802.11b is the old 2.4 GHz standard at 11 Mbps. 802.11a is 5 GHz, not 2.4. 802.11g is 2.4 GHz at 54 Mbps, not a 6 GHz standard. Wi-Fi 6 is 802.11ax.",
    ["802.11ac is Wi-Fi 5. If a question says Wi-Fi 5, it means ac, and the band is 5 GHz.",
     "802.11b is an early 2.4 GHz standard. It is not Wi-Fi 5.",
     "802.11a uses 5 GHz. Calling it 2.4 GHz swaps it with b and g.",
     "802.11g is 2.4 GHz. It is not a 6 GHz-only standard."]))

Q2.append(item(P, 30, "2.3", "medium",
    "Two neighboring access points on 2.4 GHz are set to channels 6 and 7. Users between them are slow. Which change follows the non-overlapping channel plan?",
    ["Use channels 1, 6, and 11, and do not place adjacent numbers next to each other", "Set both radios to channel 6 so they cooperate", "Move both to channel 2", "Disable 5 GHz so everything shares 2.4"],
    0,
    "Channels 1, 6, and 11 are the non-overlapping set in the 2.4 GHz band. Channels 6 and 7 overlap almost completely, so the two access points fight. Putting both on the same channel also makes them share airtime. Turning off 5 GHz removes the cleaner band. Separate them onto non-overlapping channels.",
    ["1, 6, and 11 are spaced so their main lobes do not sit on top of each other. That is the plan to use.",
     "One shared channel means both cells contend for the same air. It is not cooperation.",
     "Channel 2 overlaps channel 1 and is not part of the non-overlapping set.",
     "Disabling 5 GHz crowds more clients onto the band that is already overlapping."]))

Q2.append(item(P, 31, "2.3", "easy",
    "A badge reader uses a short-range radio at the door, and a headset uses a different radio that works across the room. Which pairing is right?",
    ["The badge is NFC or RFID. The headset is Bluetooth", "Both are NFC, and Bluetooth cannot leave the door", "The headset is a fiber optic", "The badge is a DHCP relay"],
    0,
    "NFC and RFID are the close-range technologies used for badges and taps. Bluetooth is the personal-area radio used for headsets, and it works across a room, not just a touch. Fiber is a cable. A DHCP relay forwards address requests. Neither one is a headset.",
    ["Badges tap because NFC or RFID is very short range. A headset that works across the room is Bluetooth.",
     "Bluetooth is built for room-scale accessories. Calling both NFC ignores the range in the question.",
     "A headset is not a strand of fiber. Fiber does not speak audio to a laptop by radio.",
     "A DHCP relay is a router feature. It does not read badges or play audio."]))

Q2.append(item(P, 32, "2.4", "easy",
    "A branch office has no server of its own and gets addresses from a device at headquarters. Clients arrive with 169.254 addresses when the WAN is down. Which server role is missing when that happens?",
    ["DHCP", "A print server that is only used for drivers", "A syslog server", "A web server"],
    0,
    "169.254 means the client asked for DHCP and nobody answered, so it made up a link-local address. The role that failed to answer is DHCP. Print, syslog, and web services do not hand out the client's own IP configuration. When the WAN is down, a local DHCP server or a relay that can still reach one is what those clients lack.",
    ["DHCP is the role that leases addresses. No answer, then APIPA. That is the role to restore or relay.",
     "A print server shares printers. It does not assign IP addresses.",
     "Syslog receives logs. It does not lease addresses to clients.",
     "A web server hosts pages. It is not the addressing service."]))

Q2.append(item(P, 33, "2.4", "medium",
    "A firewall, an intrusion-prevention feature, and a content filter are sold as one appliance at the edge of a small office. Which exam name fits that combined device?",
    ["Unified threat management", "A patch panel", "A hub", "A SODIMM"],
    0,
    "UTM is the all-in-one security appliance: firewall, IPS, filtering, and often VPN, in one box. Small offices buy them so they do not run five separate products. A patch panel terminates cable, a hub repeats frames, and a SODIMM is memory. None of those inspect threats.",
    ["UTM is the combined edge appliance. One box, several security jobs, is the definition.",
     "A patch panel is passive copper termination. It does not filter content.",
     "A hub repeats electrical signals. It is not a security product.",
     "SODIMM is laptop RAM. It does not sit at the network edge."]))

Q2.append(item(P, 34, "2.4", "medium",
    "Users authenticate to the wireless network, and a server records who logged in, what they were allowed to do, and the session accounting. Which service is that trio?",
    ["AAA", "SMTP", "A cable tester", "APIPA"],
    0,
    "AAA is authentication, authorization, and accounting. Authentication asks who you are, authorization asks what you may do, and accounting records the session. RADIUS is a common way to deliver it. SMTP is mail. A cable tester and APIPA are not identity services.",
    ["AAA is the three-part access service. The wireless login that also logs the session is this role.",
     "SMTP transfers mail. It does not authorize a wireless session.",
     "A cable tester checks wiring. It does not keep an account of who connected.",
     "APIPA is a self-assigned address after DHCP fails. It is not an account database."]))

Q2.append(item(P, 35, "2.5", "medium",
    "A new SOHO PC is set to DHCP and shows 169.254.12.8. The rest of the office is fine, and this PC's cable tests good. What does the address prove?",
    ["This PC did not get a DHCP lease", "The PC has a working public address", "The address is inside 192.168.0.0/16", "The PC is the DHCP server"],
    0,
    "169.254.0.0/16 is APIPA, the address a Windows PC assigns itself when DHCP does not answer. It is not a public address and it is not RFC 1918. The next checks are the port's VLAN, the DHCP scope, and whether this PC is isolated from the server that everyone else can hear. The PC is a client, not the server.",
    ["APIPA means the lease never arrived. Find out why this one PC cannot hear DHCP.",
     "169.254 is not routable on the internet and was not assigned by a provider.",
     "192.168.0.0/16 is a different private range. 169.254 is link-local.",
     "The PC invented the address because it could not find a server. It is not serving leases."]))

Q2.append(item(P, 36, "2.5", "hard",
    "A printer is statically set to 192.168.1.50. The router's DHCP pool is 192.168.1.10 through 192.168.1.200. Some mornings a laptop cannot browse, and the printer drops off. What is the addressing mistake?",
    ["The static address sits inside the DHCP pool, so a laptop can be leased the same address", "Static addresses must always be .1", "The pool is illegal because it includes more than ten addresses", "The printer should use 169.254.1.50 so it never conflicts"],
    0,
    "A static address inside the dynamic pool will eventually be handed to someone else. Put the printer outside the pool or create a reservation and an exclusion. There is nothing magic about .1 except that people often use it for the router. A pool of more than ten addresses is normal. 169.254 is what you get when DHCP fails, and it is a bad plan for a printer.",
    ["The overlap is the bug. Exclude .50 or move the printer outside the pool so the server never offers it.",
     "The router is often .1, but a printer may be any free address outside the dynamic range.",
     "DHCP pools are supposed to be large enough for the clients. Ten is not a maximum.",
     "169.254 is an automatic failure address, not a stable printer design, and other devices will not route to it."]))

Q2.append(item(P, 37, "2.5", "medium",
    "A SOHO router is 192.168.0.1/24. A PC is 192.168.0.40/24 with a blank gateway. Local file shares work, and the internet does not. What value belongs in the gateway field?",
    ["192.168.0.1", "192.168.0.40", "127.0.0.1", "10.0.0.1"],
    0,
    "The default gateway is the router on the PC's own subnet, which is 192.168.0.1. Leaving it blank means the PC has no next hop for anything off the LAN, so local shares still work. The PC's own address is not a gateway. Loopback sends traffic to itself. 10.0.0.1 is a different network and is not on this subnet.",
    ["192.168.0.1 is the router. That is the gateway this PC is missing.",
     "192.168.0.40 is the PC. Using it as the gateway sends off-net traffic nowhere useful.",
     "127.0.0.1 is loopback. Internet traffic would never leave the PC.",
     "10.0.0.1 is not in 192.168.0.0/24, so the PC could not ARP for it even if a router lived there."]))

Q2.append(item(P, 38, "2.6", "medium",
    "Company mail started landing in spam after a new cloud mail host was added. Web browsing to the company site still works. The DNS change that was forgotten is the one that lists who may send mail. Which record is that?",
    ["An SPF record in TXT", "An A record for the website only", "A DHCP reservation", "A VLAN ID"],
    0,
    "SPF is a TXT record that names the servers allowed to send mail for the domain. A new mail host that is not in the SPF record looks like a forgery to receivers. The website's A record can be perfect and mail will still fail. DKIM signs messages, and DMARC sets the policy, but the stem describes the list of allowed senders, which is SPF. DHCP and VLANs are not that list.",
    ["SPF is the sender list. Add the new mail host there so receivers accept its mail.",
     "The A record is why the website still loads. It does not authorize outbound mail.",
     "A DHCP reservation binds a MAC to an IP. It is not a public mail policy.",
     "A VLAN ID is a Layer 2 tag. Receivers on the internet do not check it to score spam."]))

Q2.append(item(P, 39, "2.6", "easy",
    "A printer keeps getting a new address, and the scanning software breaks until someone updates the address. The printer should keep one address without being typed by hand on the printer. What should be created on the DHCP server?",
    ["A reservation bound to the printer's MAC address", "A shorter lease and no reservation", "An MX record", "A second identical scope on a rogue server"],
    0,
    "A reservation ties the printer's MAC to a chosen IP, and the printer can stay on DHCP. A shorter lease makes the address change more often, which is worse. An MX record is for mail. A second DHCP server handing out the same range creates duplicates.",
    ["The reservation is the stable DHCP assignment. The scanner can keep using one address.",
     "Shorter leases increase churn. They do not pin the printer.",
     "MX records direct email. They do not reserve a printer address.",
     "A rogue or overlapping scope is a source of conflicts, not a fix."]))

Q2.append(item(P, 40, "2.6", "medium",
    "Guests and staff currently share one switch with no segmentation, and guest laptops can see staff discovery traffic. The switch can place ports into separate broadcast domains. What should the technician create?",
    ["A VLAN for guests, separate from the staff VLAN", "A single VLAN that includes every port, which they already have", "A DNS MX record for the guest laptops", "A larger hub"],
    0,
    "A VLAN is a separate broadcast domain on a switch. Put guests in one VLAN and staff in another, and route between them only if you mean to, with a filter. One VLAN for everyone is the current problem. MX records and a hub do not split broadcast domains.",
    ["A guest VLAN keeps guest broadcasts off the staff ports. That is the segmentation the switch can provide.",
     "One VLAN for every port is the flat network that is already failing the requirement.",
     "An MX record routes mail between servers. It does not separate laptop broadcasts.",
     "A hub is one collision domain and one broadcast domain. It removes segmentation."]))

Q2.append(item(P, 41, "2.7", "medium",
    "A remote worker's video calls are usable, but every action in a remote desktop feels delayed by a large fraction of a second. The connection is satellite. Which limitation of satellite explains the delay?",
    ["High latency because of the distance the signal travels", "Satellite has no upload path at all", "Satellite is a form of Ethernet over coax inside the house", "Latency means the SSID is hidden"],
    0,
    "Satellite has to go up to orbit and back, so the round trip is long even when the speed test shows plenty of megabits. Remote desktops and games feel that latency. Video calls can tolerate it better than a click that needs a response. Satellite does have an upload path. It is not in-house coax, and a hidden SSID is a wireless setting, not orbital delay.",
    ["The distance is the latency. More bandwidth will not make the orbit closer. This link is a poor fit for snappy remote desktops.",
     "Satellite internet is bidirectional. A missing upload is not the definition of the technology.",
     "In-house coax is a cable-modem or MoCA problem. Orbital satellite is a different access type.",
     "Hiding an SSID does not add a quarter second of propagation delay."]))

Q2.append(item(P, 42, "2.7", "easy",
    "A study guide asks for one example of a PAN, one of a LAN, and one of a WAN, in that order. Which description matches a PAN, a LAN, and a WAN in that order?",
    ["A phone and a headset, an office floor, and circuits between cities", "Circuits between cities, a headset, and one office floor", "A headset, circuits between cities, and a SAN", "One switch port, a headset, and a badge tap"],
    0,
    "A PAN is the personal bubble: a phone and a headset. A LAN is the office or the home. A WAN connects sites across a city or farther. Reversing them is the usual trap. A SAN is storage, not the wide-area network, even though the letters look related.",
    ["Personal, local, then wide. The headset, the office, and the inter-city circuits are in the right order.",
     "That list is WAN, PAN, LAN. It is the right technologies in the wrong order.",
     "A SAN is a storage network. It does not replace the WAN in this trio.",
     "A badge tap is NFC, which can be part of a personal area, but the order and the middle item do not match the question."]))

Q2.append(item(P, 43, "2.8", "easy",
    "A technician is terminating RJ45 plugs on patch cords. Which tool crimps the plug onto the pairs?",
    ["A crimper", "A punchdown tool", "A toner probe with no crimper", "A loopback plug"],
    0,
    "The crimper seats the contacts of an RJ45 or RJ11 plug into the conductors. A punchdown tool seats cable into a jack or a panel, which is the other end of the skill. A toner traces a cable. A loopback plug tests a port. You do not punch a modular plug.",
    ["The crimper is the plug tool. That is what finishes a patch cord.",
     "A punchdown tool is for keystones and panels, not for the plug on a patch cord.",
     "A toner finds the other end of a cable. It does not attach a connector.",
     "A loopback plug is a test adapter. It does not terminate cable."]))

Q2.append(item(P, 44, "2.8", "medium",
    "A NIC is suspected bad. The technician unplugs the switch and puts a device in the NIC that connects transmit back to receive. The link comes up and a test passes. What did the loopback result show?",
    ["The NIC can send and receive, so the fault is likely the cable or the switch port", "The NIC is dead, because a loopback always fails on a good card", "The DNS server is down", "The loopback proves the WAN provider is up"],
    0,
    "A loopback plug folds the NIC's transmit into its receive. If that test passes, the card can frame and see its own signal, so you move on to the cable and the far-end port. A failure would implicate the NIC. The test never left the computer, so it says nothing about DNS or the WAN.",
    ["A passed loopback clears the NIC. Look at the cable, the patch panel, and the switch port next.",
     "A good card passes a loopback. Failure, not success, would condemn the NIC.",
     "DNS was not on the path. The plug is local to the NIC.",
     "The WAN was not involved. Loopback never reached the provider."]))

if __name__ == "__main__":
    from common import dump
    dump("220-1101", {"q-d1.json": Q1, "q-d2.json": Q2})
