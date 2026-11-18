"""New 220-1201 topics that the V14 bank did not cover."""

from common import PROBLEMS, dump, item
from gate import collisions

P = "c1"
Q = []


def add(*args):
    Q.append(item(P, *args))


add(199, "1.1", "medium",
    "A laptop has weak Wi-Fi only when the lid is open past a certain angle. The antenna leads were pinched under a replaced panel. Where do those leads belong?",
    ["Along the path to the antennas in the display housing",
     "Wrapped around the CMOS battery",
     "Plugged into the SATA port",
     "Left disconnected because Wi-Fi uses the battery"],
    0,
    "Laptop Wi-Fi antennas sit in the display housing, and the leads have to reach them without being crushed. A pinched lead explains a signal that changes with the lid. The CMOS battery, a SATA port, and the battery itself are not the antenna path.",
    ["Route the leads back to the antennas in the lid and do not pinch them.",
     "The CMOS battery keeps the clock. It is not an antenna.",
     "SATA connects storage. It does not carry the Wi-Fi leads.",
     "The battery powers the radio. It does not replace the antenna."])

add(200, "2.2", "hard",
    "A new access point advertises 2.4 GHz, 5 GHz, and 6 GHz. Which two statements describe that radio? (Choose two.)",
    ["6 GHz is the band Wi-Fi 6E adds",
     "2.4 GHz is still the band that uses channels 1, 6, and 11 in most regions",
     "6 GHz passes through walls better than 2.4 GHz",
     "NFC is the name of the 5 GHz band"],
    [0, 1],
    "Wi-Fi 6E is the generation that adds 6 GHz. The 2.4 GHz band still uses the familiar non-overlapping channel plan. Higher frequency does not travel through walls better. NFC is a separate short-range technology, not a Wi-Fi band.",
    ["6 GHz is the extra band. That is what 6E means on this access point.",
     "Channels 1, 6, and 11 are the usual non-overlapping 2.4 GHz plan.",
     "6 GHz is more easily blocked by walls than 2.4 GHz. It does not travel farther.",
     "NFC is tap-to-pay range. It is not the 5 GHz Wi-Fi band."])

add(201, "2.5", "medium",
    "A ceiling access point powers on from the switch cable and has no power brick. The switch port is marked 802.3at. What is feeding the access point?",
    ["Power over Ethernet from the switch",
     "A USB-C charger hidden in the ceiling",
     "The fiber strand itself, with no copper pairs",
     "A CR2032 taped to the access point"],
    0,
    "802.3at is a Power over Ethernet standard. The switch puts power on the copper Ethernet pairs, which is why there is no brick. Fiber has no pairs to carry that power. A USB charger and a coin cell are not what the port marking describes.",
    ["The switch is the power source. 802.3at is PoE.",
     "Nothing in the story describes a USB charger. The cable to the switch is the lead.",
     "Fiber does not carry 802.3at power. This link is copper.",
     "A coin cell does not run a ceiling access point."])

add(202, "3.1", "medium",
    "A laptop panel is an LCD with a dense grid of small LEDs behind it for local dimming. The pixels themselves are not organic emitters. Which panel type is that?",
    ["Mini-LED", "OLED", "A CRT", "A plasma panel"],
    0,
    "Mini-LED is an LCD backlight made of many small LEDs so zones can dim. OLED pixels emit their own light and do not need that backlight. CRT and plasma are older display types this laptop is not using.",
    ["A dense LED backlight behind an LCD is Mini-LED, not a self-lit pixel.",
     "OLED would be the pixel emitting light, not a backlight behind an LCD.",
     "A CRT is a tube. It is not a laptop backlight.",
     "Plasma is not the backlight technology in this panel."])

add(203, "4.1", "medium",
    "A host runs twenty copies of one service. Each copy has its own files and processes, and they all share the host kernel. There is no separate guest operating system per copy. What are the copies?",
    ["Containers", "Type 1 hypervisors stacked twenty deep", "RAID 0 members", "CMOS batteries"],
    0,
    "Containers isolate processes and files while sharing the host kernel. A virtual machine would bring a guest operating system. RAID is disks. A CMOS battery is a clock cell. Neither of those is a twenty-copy service.",
    ["Shared kernel, separate processes: those are containers.",
     "A type 1 hypervisor is the layer under virtual machines, not each copy of the service.",
     "RAID 0 stripes disks. It does not run twenty services.",
     "A CMOS battery does not host an application."])

if __name__ == "__main__":
    found = collisions("220-1201", Q)
    if PROBLEMS or found:
        raise SystemExit("\n".join(PROBLEMS + found))
    dump("220-1201", {"q-v15.json": Q})
