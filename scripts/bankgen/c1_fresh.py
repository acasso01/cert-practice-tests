"""Original 220-1101 questions that do not restate the existing bank."""

from common import PROBLEMS, dump, item
from gate import collisions

P = "c1"
Q = []


def add(*args):
    Q.append(item(P, *args))


add(172, "1.1", "medium",
    "A laptop on a dock drives the monitors and the USB devices, but the battery percentage falls all afternoon. The dock's own power brick is unplugged. What restores charging?",
    ["Plug the dock's power brick back in", "Replace the keyboard", "Turn off the touchpad in software", "Set the panel to 60 Hz"],
    0,
    "Many docks only pass power when their own brick is attached. Video and USB can still work from the laptop's battery, which is why the percentage falls. The keyboard, touchpad, and refresh rate are not the missing power source.",
    ["The dock cannot charge the laptop without its brick. Plug that in.",
     "The keyboard is typing and is not why the battery is falling.",
     "The touchpad setting does not feed the battery.",
     "Refresh rate changes the panel timing. It does not replace a power brick."])

add(173, "1.2", "medium",
    "A convertible laptop shows a sharp image, and the image turns the wrong way when the user folds it into a tablet. The panel test pattern is fine. Which sensor is the first suspect?",
    ["The accelerometer or gyroscope", "A dead pixel in the corner", "The Ethernet magnetics", "The CMOS battery"],
    0,
    "Rotation in a convertible depends on the motion sensor. A sharp test pattern means the panel is drawing. Dead pixels, Ethernet magnetics, and the CMOS battery do not decide which way a tablet image points.",
    ["The motion sensor is what tells the OS the fold orientation.",
     "A dead pixel is a dot, not a rotation of the whole image.",
     "Ethernet magnetics sit on the network jack. They do not rotate the panel.",
     "The CMOS battery keeps firmware settings. It does not sense the hinge."])

add(174, "1.4", "easy",
    "A phone is paired to a Bluetooth speaker. Music still comes out of the phone's earpiece. The speaker shows as connected. What should the user change?",
    ["Select the speaker as the media output", "Replace the phone's display", "Turn on airplane mode and leave it on", "Delete the carrier's SIM"],
    0,
    "A paired device is not always the selected output. Point media audio at the speaker. The display is showing the controls. Airplane mode would drop the radio the speaker may need, and the SIM is not the audio path.",
    ["Choose the speaker in the output list. Pairing alone left the earpiece selected.",
     "The display is not the playback device in this report.",
     "Airplane mode turns radios off. It does not move audio to the speaker.",
     "The SIM identifies the cellular line. It does not pick a Bluetooth output."])

add(175, "1.3", "medium",
    "A USB-C cable charges a laptop and never shows a picture on a USB-C monitor. The laptop manual says that port is charge-only and does not support DisplayPort alt mode. What is required?",
    ["A port or adapter that actually carries video", "A longer charge-only cable of the same type", "A SIM card in the laptop", "A 3.5 mm microphone"],
    0,
    "Charge-only USB-C does not include the display alt mode, so a longer version of that cable still will not light the monitor. Use a port or a dock that carries video. A SIM and a microphone are not video paths.",
    ["Video has to be in the port's feature list. Charging is not enough.",
     "Length does not add alt mode to a charge-only port.",
     "A SIM is a cellular identity. It does not drive a monitor.",
     "A microphone jack does not carry the display signal."])

add(176, "2.5", "medium",
    "A small-office router still accepts administration from its WAN address with the vendor password. What should change before it stays on the modem?",
    ["Turn off administration from the WAN and set a unique password", "Publish the admin password on the guest SSID's splash page", "Forward every port to one PC", "Leave the vendor password so the next owner is comfortable"],
    0,
    "WAN-side admin plus a published password is how the router gets taken over. Disable remote admin and set a unique password. A splash page, a wide port forward, and keeping the vendor password all increase the exposure.",
    ["Close WAN administration and replace the vendor password.",
     "Putting the password on a splash page hands it to every guest.",
     "Forwarding every port exposes the PC. It does not harden the router.",
     "The vendor password is already public. Comfort is not a control."])

add(177, "2.6", "medium",
    "A PC pings its default gateway and cannot open any name, including a public one. Another PC on the same switch resolves names. This PC's DNS field is 1.2.3.4, which is not a resolver. What is wrong on this PC?",
    ["The configured DNS server is not a resolver", "The gateway is missing, because pings to it fail", "The monitor cable", "The printer's fuser"],
    0,
    "Ping reaching the gateway means the address, mask, and gateway work. Names fail only on this PC and the DNS field is a nonsense address, so fix DNS. The monitor and the fuser do not resolve names.",
    ["Point DNS at a real resolver. 1.2.3.4 is not doing that job.",
     "The gateway answered the ping. It is not missing.",
     "A monitor cable carries a picture. It does not resolve DNS names.",
     "The fuser melts toner. It is not a DNS server."])

add(178, "2.7", "easy",
    "A rural site gets its internet from a radio on the roof aimed at a tower, with low latency compared with satellite and no fiber in the ground. Which connection type is that?",
    ["A fixed wireless internet service", "Satellite, which this latency does not match", "A dial-up modem on a phone pair", "A Bluetooth PAN between two phones"],
    0,
    "Fixed wireless, often called a wireless ISP, uses a directed radio to a provider tower. Satellite latency is much higher. Dial-up is a phone pair. Bluetooth is a personal area network, not a building's internet handoff.",
    ["The roof radio to a tower is fixed wireless.",
     "Satellite would show the long delay this site does not have.",
     "Dial-up uses a modem and a phone line, not a tower radio.",
     "Bluetooth does not backhaul a building to an ISP tower."])

add(179, "2.8", "medium",
    "A switch port is suspected of failing. The technician has no second device and wants the port to hear its own signal. Which tool does that?",
    ["A loopback plug", "A flashlight", "A plastic spudger", "A thermal camera"],
    0,
    "A loopback plug returns the port's transmit to its receive so the port can be tested alone. A flashlight, a spudger, and a thermal camera do not close that electrical loop.",
    ["Install the loopback plug on the suspected port so the port hears its own signal.",
     "A flashlight does not return a signal into the port.",
     "A spudger pries cases. It is not a port tester.",
     "A thermal camera looks for heat. It does not loop a port."])

add(180, "3.1", "easy",
    "A fiber NIC and the patch panel both use small square duplex connectors that click in. Which connector family is that?",
    ["LC", "RJ11", "F-type", "DB9"],
    0,
    "LC is the small latching duplex connector common on fiber NICs and modern panels. RJ11 is a phone plug. F-type is coax. DB9 is a serial shell. None of those click into an LC transceiver.",
    ["LC is the small fiber connector in the description.",
     "RJ11 terminates a phone pair, not a fiber NIC.",
     "An F-type connector screws onto coax. It does not click into a fiber NIC.",
     "DB9 is a serial connector, not an optical duplex."])

add(181, "3.2", "medium",
    "A database server must correct single-bit memory errors without crashing. The quote lists non-ECC unbuffered DIMMs. What should be ordered instead?",
    ["ECC memory the board supports", "A faster GPU", "A USB sound card", "A longer SATA cable"],
    0,
    "ECC detects and corrects single-bit errors, which is what this server is asking for. The board and CPU have to support it. A GPU, a sound card, and a SATA cable do not correct RAM errors.",
    ["Order ECC that the platform supports. Non-ECC will not correct the bit errors.",
     "A GPU does not correct system-memory bit errors.",
     "A sound card plays audio. It is not memory protection.",
     "A SATA cable connects storage. It does not add ECC."])

add(182, "3.3", "medium",
    "A camera system must store many terabytes of video and write it continuously. The quote contains only a small NVMe stick meant as a boot device. What should hold the video?",
    ["High-capacity hard disks sized for the retention window", "The small boot stick alone", "A stack of floppy disks", "The CPU cache"],
    0,
    "Continuous video is a capacity problem. Hard disks still hold that much data at a sensible cost, and the tiny NVMe stick is a boot device, not a month of cameras. Floppies and the CPU cache are not a video library.",
    ["Size the disk pool for how long the video must be kept.",
     "A small boot stick fills up on the first day of cameras.",
     "Floppy disks do not hold a camera system.",
     "CPU cache disappears when the power drops. It is not storage."])

add(183, "3.4", "hard",
    "A new CPU fits the socket, and the board stays dark at power-on until the firmware is updated from the vendor's site using the old CPU. After the update the new CPU posts. What was missing?",
    ["Firmware support for that CPU generation", "A matched pair of speakers", "An HDMI monitor as a power source", "A USB microphone"],
    0,
    "A socket can be physically compatible before the firmware knows the new stepping. The old CPU was how they applied that update. Speakers, a monitor, and a microphone do not teach a board a new CPU.",
    ["Update the firmware. The socket fit was not the missing piece.",
     "Speakers are not part of power-on self-test. The board was waiting on firmware.",
     "A monitor displays POST. It does not power or identify the CPU.",
     "A USB microphone does not teach the firmware a new processor."])

add(184, "3.5", "medium",
    "A server has two hot-swap power supplies on two circuits. One supply fails and the server stays up. What did the second supply provide?",
    ["Redundant power so one failure is survivable", "A second set of video outputs", "ECC for the CPU cache", "A wireless SSID"],
    0,
    "Two supplies on two circuits mean the server keeps running when one supply or one circuit dies. The second supply is not a GPU, not memory correction, and not a wireless network.",
    ["That is redundant power. Replace the failed module while the server stays up.",
     "A power supply does not add monitor outputs.",
     "ECC is a memory feature, not a second power supply.",
     "An SSID comes from a radio, not from a PSU bay."])

add(185, "3.6", "medium",
    "A multifunction printer copies and prints from USB. Scan-to-email fails, and the printer's gateway field is blank while every PC on that subnet has a gateway. What should be set on the printer?",
    ["The same default gateway the PCs use", "A new fuser because the gateway is a lamp", "A USB extension as the email path", "Landscape as the default orientation"],
    0,
    "Scan-to-email leaves the subnet, so the printer needs a gateway. Local USB printing does not. The fuser, a longer USB cable, and page orientation do not route mail.",
    ["Give the printer the subnet's gateway so the mail server is reachable.",
     "The fuser bonds toner. It is not an IP gateway.",
     "USB printing already works. Email is a network path.",
     "Orientation does not fill in a gateway address."])

add(186, "4.1", "medium",
    "One company owns the hosts and does not sell tenancy to outsiders. Employees reach that cloud over the company network. Which deployment is it?",
    ["Private", "Public, sold to anyone with a card", "A community shared by competing hospitals", "A coffee-shop hotspot"],
    0,
    "A private cloud serves one organization. A public cloud is multi-tenant and for sale. A community cloud is shared by a group of organizations. A hotspot is not a cloud deployment model.",
    ["Single-organization ownership is the private deployment.",
     "Public would let other customers buy in. This one does not.",
     "A community cloud has several member organizations, not one owner.",
     "A hotspot is a wireless network, not this cloud model."])

add(187, "4.2", "easy",
    "A technician runs a guest on a laptop by installing a hypervisor application on Windows. The laptop OS is still what boots. Which hypervisor type is that application?",
    ["Type 2, hosted on an existing operating system", "Type 1, because any guest makes the host bare metal", "A hardware RAID controller", "A DNS resolver"],
    0,
    "A type 2 hypervisor is an application on a host operating system. A type 1 hypervisor is the layer that boots on the hardware. RAID and DNS are not hypervisors.",
    ["The Windows boot plus a hypervisor app is type 2.",
     "A guest does not turn a Windows laptop into a bare-metal hypervisor.",
     "RAID groups disks. It does not host a guest OS.",
     "DNS resolves names. It does not run a virtual machine."])

add(188, "4.2", "hard",
    "A virtual machine should be reachable by other office PCs at an address on the office subnet. It can reach the internet, and office PCs cannot ping it. The virtual NIC is set to NAT. What change fixes the reachability?",
    ["Switch the virtual NIC from NAT to bridged", "Delete the virtual disk", "Give the guest no address at all", "Turn the host's disk into RAID 0"],
    0,
    "NAT hides the guest behind the host, which is why the guest can get out and the LAN cannot get in. Bridged puts the guest on the office subnet. Deleting the disk, removing the address, or striping the host disk does not publish the guest.",
    ["Bridged mode is what puts the guest on the office subnet.",
     "Deleting the disk destroys the guest. It does not add a LAN address.",
     "Removing the address leaves the guest with nothing for the office PCs to ping.",
     "RAID 0 on the host is a storage choice, not a virtual switch mode."])

add(189, "5.1", "medium",
    "The symptom is written down and nobody has a tested cause yet. In the CompTIA A+ troubleshooting method, what comes next?",
    ["Establish a theory of probable cause", "Reimage the PC before any theory", "Document a cause that was never tested", "Order a new motherboard as the first action"],
    0,
    "A+ troubleshooting goes from identifying the problem to a theory, then a test. Reimaging, writing an untested cause, or buying a board skips the theory.",
    ["The next step is a theory you can test. Identification is already done.",
     "Reimaging is a late, destructive action, not the step after the symptom is known.",
     "You cannot document a cause you have not established.",
     "A motherboard order is not the step that follows a written symptom."])

add(190, "5.2", "hard",
    "A desktop is unstable and a visual inspection shows several capacitors on the motherboard with bulging tops. What is the failed part to plan around?",
    ["The motherboard, because those capacitors are failing", "The monitor's OSD menu", "The mouse pad", "The printer tray"],
    0,
    "Bulging capacitor tops are a classic board failure. Plan on the motherboard or a qualified repair of that board, not the monitor menu, the mouse, or a printer tray.",
    ["Those bulging capacitors are on the board that has to be replaced or repaired.",
     "The on-screen menu did not swell the capacitors.",
     "A mouse pad is not an electronic failure.",
     "The paper tray is not on the motherboard."])

add(191, "5.3", "hard",
    "Two disks are in a RAID 0 volume. One disk stops spinning and the array will not mount. What can be rebuilt from the remaining disk?",
    ["Nothing. RAID 0 has no redundancy", "The entire volume, because RAID 0 mirrors", "Only the parity, because RAID 0 stores parity", "The volume, after the good disk is formatted"],
    0,
    "RAID 0 stripes with no mirror and no parity. Lose one disk and the stripe is gone. It does not mirror, it does not keep parity, and formatting the survivor erases what little is left.",
    ["There is nothing to rebuild. Restore from backup.",
     "A mirror is RAID 1. RAID 0 does not keep a second copy of the stripe.",
     "Parity is RAID 5 or RAID 6. RAID 0 has none.",
     "Formatting the remaining disk does not recreate the stripe."])

add(192, "5.4", "easy",
    "A laptop panel looks normal. The projector says no signal. The projector's input menu is set to HDMI and the cable is on DisplayPort. What is the first change?",
    ["Select the input that matches the connected cable", "Replace the laptop motherboard", "Reseat the laptop CPU", "Format the laptop"],
    0,
    "No signal with a healthy laptop screen and the projector sitting on the wrong input is an input mismatch. Match the input to the cable before you touch the board, the CPU, or the disk.",
    ["Change the projector input to the port the cable actually uses.",
     "The laptop panel works. The motherboard is not the first suspect.",
     "The CPU is running the laptop display. Do not reseat it for a wrong input.",
     "Formatting does not select a projector input."])

add(193, "5.5", "medium",
    "A phone shuts down while charging under a pillow, inside a thick case. On a table with the case off it stays on and charges. What is the practical fix?",
    ["Charge it on a hard surface with the case off so it can shed heat", "Replace the display because it dimmed once", "Jailbreak it so the thermal limit goes away", "Put it back under the pillow and ignore the shutdown"],
    0,
    "The pillow and the case trapped heat, and the phone protected itself. Let it cool and charge where air can move. A dim moment is not a dead panel. Removing the thermal limit and returning it to the pillow repeat the fault.",
    ["Give it airflow. The shutdown tracked the pillow and the case.",
     "The panel came back. Heat was the symptom, not a failed display.",
     "Defeating the thermal shutdown risks the battery.",
     "The pillow is the condition that caused the shutdown."])

add(194, "5.6", "medium",
    "A new toner cartridge prints blank pages. The sealing tape tab is still sticking out of the cartridge. What is the fix?",
    ["Pull the sealing tape and reseat the cartridge", "Replace the pickup rollers first", "Change the paper to legal size", "Set the queue to print duplex"],
    0,
    "The sealing tape keeps a new cartridge from shipping with loose toner, and it also blocks the image until it is removed. Rollers, paper size, and duplex do not explain a blank page with the tape still in place.",
    ["Remove the tape. A sealed cartridge cannot lay down an image.",
     "Pickup rollers affect whether paper moves, not a sealed cartridge.",
     "Legal paper does not remove a tape over the drum opening.",
     "Duplex prints both sides. It does not unseal a cartridge."])

add(195, "5.7", "medium",
    "Every lunch period, 2.4 GHz clients near the break room drop, and 5 GHz clients in the same seats stay up. A microwave in that room runs at lunch. What is the likely interference?",
    ["The microwave overlapping 2.4 GHz", "A DNS suffix on the 5 GHz clients", "The printer's fuser", "A VGA cable in another building"],
    0,
    "Microwave ovens leak energy in the 2.4 GHz band and leave 5 GHz alone. The timing matches the oven. DNS, a fuser, and a VGA cable do not jam one band at lunch.",
    ["Move the AP, move the oven, or use 5 GHz there. The band and the clock match the oven.",
     "A DNS suffix does not drop only the 2.4 GHz radio at noon.",
     "The fuser is a printer heater, not a 2.4 GHz jammer.",
     "VGA is analog video. It is not this lunchtime pattern."])

add(196, "5.7", "hard",
    "Wireless clients associate to the AP and can ping the AP. None of them can reach the internet, and the AP's WAN cable is unplugged. Where is the fault?",
    ["The AP has no uplink to the rest of the network", "Every client needs a new battery", "The SSID is too long", "The clients are using too little transmit power to ping the AP"],
    0,
    "Association and a ping to the AP mean the radio works. The unplugged WAN cable is why nothing beyond the AP answers. Batteries, the length of the name, and client power are contradicted by the successful ping.",
    ["Plug the uplink back in. The wireless hop is already proven.",
     "The clients reached the AP. A dead battery would not do that.",
     "SSID length does not unplug a WAN cable.",
     "They had enough power to ping the AP. The missing piece is the cable."])

add(197, "5.3", "medium",
    "A new disk is installed and Disk Management shows it as Not Initialized. The system disk is healthy. What is the safe next action?",
    ["Initialize the new disk, and do not touch the system disk", "Format the system disk", "Delete the EFI partition on the boot drive", "Run a low-level wipe of every disk"],
    0,
    "A brand-new disk has no partition table until it is initialized. Do that to the new disk only. Formatting or wiping the boot disk, or deleting its EFI partition, is how you lose the PC.",
    ["Initialize the disk you just added. Leave the boot disk alone.",
     "The system disk is the one that is already working. Formatting it is the outage.",
     "The EFI partition is how the PC boots. Deleting it is not disk initialization.",
     "Wiping every disk destroys the installation to label one new drive."])

add(198, "5.5", "easy",
    "A laptop shuts down under load and the exhaust air is hot. The fan is packed with dust and barely spins. After the dust is cleared the fan spins and the shutdowns stop. What was wrong?",
    ["Dust was blocking the cooling path", "The HDMI cable was too short", "The touchpad driver was missing", "The webcam slider was closed"],
    0,
    "A hot exhaust, a stalled fan, and a shutdown that ends when the dust is gone is a cooling failure. The video cable, the touchpad, and the webcam do not pack a fan with lint.",
    ["Clean the fan and the fins. The dust was the fault this time.",
     "A short HDMI cable cannot pack a fan with dust or make the exhaust air hot.",
     "A touchpad driver does not make the exhaust air hot.",
     "A closed webcam slider does not overheat the chassis."])

if __name__ == "__main__":
    found = collisions("220-1101", Q)
    if PROBLEMS or found:
        raise SystemExit("\n".join(PROBLEMS + found))
    dump("220-1101", {"q-fresh.json": Q})
