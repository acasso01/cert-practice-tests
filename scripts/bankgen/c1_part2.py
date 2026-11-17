from common import item

P = "c1"
Q3, Q4 = [], []

Q3.append(item(P, 45, "3.1", "easy",
    "A new office run will sit in an air-return ceiling and must carry 1 Gbps Ethernet for 80 meters. The cheapest cable on the cart is a PVC-jacket Category 5e. What is wrong with using it there?",
    ["The air-return space needs plenum-rated cable, even though Category 5e can carry the speed", "Category 5e cannot carry 1 Gbps at any length", "Plenum cable is only for outdoors", "PVC is required in plenums because it smokes less"],
    0,
    "Category 5e is electrically fine for 1 Gbps at 80 meters. The jacket is the problem. An air-return ceiling is a plenum, and the cable there must be plenum rated so a fire does not fill the ventilation system with thick smoke. Ordinary PVC is the wrong jacket. Plenum is an indoor air-space rating, not an outdoor rating.",
    ["Speed is fine. The plenum rating is the missing piece, because this ceiling moves building air.",
     "Category 5e does carry 1 Gbps to 100 meters. The speed is not why this pull is wrong.",
     "Outdoor cable is a different jacket problem. Plenum is specifically for indoor air-handling spaces.",
     "PVC is the higher-smoke jacket. It is what you avoid in a plenum, not what you require."]))

Q3.append(item(P, 46, "3.1", "medium",
    "Both ends of a cable were terminated to the T568B color order, and the wire map passes. A coworker says one end should have been T568A or the link will not carry Ethernet. What is true?",
    ["Both ends the same, either A or B, makes a straight-through cable. B on both ends is correct", "Ethernet requires A on one end and B on the other for every PC-to-switch cable", "T568B is only legal for telephone pairs", "A straight-through cable uses different colors on pins 4 and 5 at each end"],
    0,
    "A straight-through cable uses the same standard on both ends. T568B on both ends is the common choice in the United States, and T568A on both ends is also straight-through. A on one end and B on the other is a crossover, which modern NICs with auto-MDIX rarely need. Pins 4 and 5 are the blue pair in both standards.",
    ["Matching ends are straight-through. This cable is built correctly for a PC-to-switch run.",
     "A-to-B is a crossover. It is not the requirement for a normal switch link.",
     "T568B is an Ethernet pinout. Telephone-only wiring is a different, simpler use of the cable.",
     "The blue pair stays on pins 4 and 5 in both A and B. You do not swap it to make a straight-through cable."]))

Q3.append(item(P, 47, "3.1", "medium",
    "A monitor has a VGA connector, and the new laptop only has HDMI and USB-C. The picture must stay analog all the way into that old monitor. Which statement is accurate?",
    ["VGA is the analog video connector. An adapter from HDMI or USB-C must actively convert to analog", "VGA and HDMI are the same signal, so a passive pin adapter always works", "DisplayPort is the analog standard and VGA is digital", "DVI-D carries analog and is identical to VGA"],
    0,
    "VGA is analog. HDMI and DisplayPort and USB-C video are digital. A cheap passive pin swap does not turn digital into analog. You need an active converter. DVI-D is digital only. DVI-A and DVI-I are the DVI flavors that can carry analog, which is a different connector from DVI-D.",
    ["The laptop's digital output needs an active conversion to feed an analog VGA monitor. A passive adapter is the usual disappointment.",
     "HDMI is digital and VGA is analog. They are not the same signal with different shells.",
     "DisplayPort is digital. VGA is the analog one. The names are reversed in that choice.",
     "DVI-D is digital only. It does not carry the analog pins that a VGA monitor needs."]))

Q3.append(item(P, 48, "3.1", "easy",
    "A technician is choosing a connector for an internal power lead to an older drive that is not SATA. The plug is a four-pin white connector from the power supply. What is that connector called?",
    ["Molex", "Lightning", "RJ11", "LC"],
    0,
    "The four-pin peripheral power connector is Molex. SATA power is the newer flat connector. Lightning is an Apple data and charge port. RJ11 is a telephone plug. LC is a fiber connector. None of those power an internal legacy drive.",
    ["Molex is the four-pin drive power connector. That is the white plug on older power supplies.",
     "Lightning is a phone and tablet connector. It does not power an internal hard drive.",
     "RJ11 is the small telephone modular plug. It is not a power connector.",
     "LC is a small fiber-optic connector. It carries light, not drive power."]))

Q3.append(item(P, 49, "3.1", "medium",
    "A run next to a bank of large motors shows CRC errors on unshielded cable. Fiber is available, and so is shielded twisted pair. Which choice is immune to the motors' electrical noise?",
    ["Fiber", "Unshielded twisted pair pulled even closer to the motors", "A longer VGA cable used as Ethernet", "Coax with an F connector pretending to be a switch uplink"],
    0,
    "Fiber carries light, so magnetic and electrical noise from the motors does not couple into the signal. Shielded copper can help if it is grounded correctly, but it is not immune. More unshielded cable closer to the motors is worse. VGA and F-type coax are the wrong media for an Ethernet uplink between switches.",
    ["Fiber is the immune choice. Use it through the motor room instead of hoping the copper improves.",
     "Moving unshielded pairs closer to the noise source increases the errors.",
     "VGA is an analog video cable. It is not an Ethernet uplink.",
     "F-type coax is for RF and cable modems. It is not how these switches should be linked."]))

Q3.append(item(P, 50, "3.2", "easy",
    "A desktop will not POST after a memory upgrade. The new module is DDR5 and the board's slots are DDR4. The technician is about to push harder. What is the correct stop?",
    ["DDR4 and DDR5 are keyed differently and are not interchangeable. Do not force the module", "DDR5 is backward compatible if you remove the notch with a file", "DDR4 boards accept DDR5 at a lower voltage automatically", "The module is SODIMM and every desktop uses SODIMM"],
    0,
    "Each DDR generation has a different notch and pinout so you cannot plug the wrong one in. Forcing it breaks the slot and the module. Filing the notch defeats the safety and still lands the pins in the wrong places. Desktops use DIMMs. SODIMMs are the laptop modules. Get DDR4 for this board.",
    ["The keying is intentional. Stop, and install the generation the board was built for.",
     "Cutting a notch does not remap the pins or the voltage. It destroys the module and can destroy the board.",
     "The board does not negotiate a DDR5 module down to DDR4. The generations do not mix.",
     "This is a desktop. Even a DDR4 SODIMM would be the wrong form factor. The generation is already wrong."]))

Q3.append(item(P, 51, "3.2", "hard",
    "A board supports dual channel. Two identical DDR4 modules are installed in the two slots next to each other, and the firmware reports single-channel mode. The manual colors one slot in each channel. What should change?",
    ["Move one module into the matching slot so the pair occupies both channels", "Install a third module of a different size and speed", "Enable the modules in Device Manager after Windows boots, because the firmware cannot see RAM", "Replace the modules with ECC sticks the board does not support"],
    0,
    "Dual channel needs the modules in the slots the manual pairs, often one of each color, not the two slots that happen to be adjacent. Adjacent slots are often the same channel, which is why the firmware fell back to single channel. The PC still works. It is just not using the width you paid for. Mixed random modules and unsupported ECC are not the fix.",
    ["Follow the color or the manual. The pair has to sit on both channels before the firmware will report dual channel.",
     "A mismatched third module makes the population harder, not cleaner.",
     "If the firmware sees the RAM and reports a mode, Windows is not hiding it. Device Manager is the wrong tool.",
     "ECC that the board does not support will be rejected or will run without ECC. It does not fix slot placement."]))

Q3.append(item(P, 52, "3.2", "medium",
    "A workstation manual says the memory controller supports ECC only with registered ECC modules, and this gaming board does not. A user wants ECC sticks from a server for 'fewer crashes.' What is the likely result?",
    ["The gaming board may refuse the registered ECC modules or ignore the ECC function", "ECC modules are required for every Windows install", "Registered ECC is slower DDR and always fits a laptop SODIMM slot", "ECC removes the need for a supported CPU and motherboard"],
    0,
    "ECC corrects single-bit memory errors, and registered modules add a buffer the memory controller must understand. A board and CPU that do not support them will not boot, or will not actually correct errors. ECC is not a Windows requirement, it is not a laptop SODIMM by default, and it does not bypass the compatibility list.",
    ["Check the board's memory support list. Server ECC is often the wrong electrical type for a consumer board.",
     "Windows does not require ECC. Most desktops run non-ECC memory for their whole lives.",
     "Registered ECC DIMMs are a server form, not a way to fill a laptop slot, and they are not just 'slower DDR.'",
     "The memory controller has to support ECC. The stick does not create that support."]))

Q3.append(item(P, 53, "3.2", "hard",
    "A heavy application is using the page file constantly, the disk is busy, and the PC has 8 GB of RAM while the application vendor requires 32 GB. Adding a larger page file stops the crashes but the machine stays slow. What is the right fix?",
    ["Install more physical RAM. The page file is disk, and it is only a safety net", "Delete the page file and add no RAM", "More virtual memory is faster than real RAM", "Replace the CMOS battery so the page file moves into the CPU cache"],
    0,
    "Virtual memory is the page file on disk. It prevents some crashes by giving Windows somewhere to put idle pages, and it is much slower than DRAM. This workload needs 32 GB and has 8 GB, so the disk is thrashing. Add RAM. Deleting the page file removes the safety net. The CMOS battery does not relocate the page file.",
    ["The vendor's 32 GB requirement is physical memory. The page file is why it is slow, not why it should stay slow.",
     "No page file plus too little RAM turns a slow machine into a crashing one.",
     "Disk is not faster than DRAM. A bigger page file does not outrun real memory.",
     "The CMOS battery keeps firmware settings and the clock. It is not a memory upgrade."]))

Q3.append(item(P, 54, "3.3", "easy",
    "A technician is explaining drive types to a user who wants the fastest general-purpose internal drive. Which pairing is accurate?",
    ["NVMe over PCIe is faster than a SATA SSD, which is faster than a 5400 rpm hard drive", "A 5400 rpm hard drive is faster than NVMe", "M.2 and NVMe mean the same thing, so every M.2 drive is NVMe", "mSATA and M.2 share one connector"],
    0,
    "NVMe is the fast protocol that rides on PCIe. A SATA SSD is limited by SATA. A spinning 5400 rpm drive is slower than both for general use. M.2 is a form factor: an M.2 drive can be SATA or NVMe, so the names are not synonyms. mSATA is an older connector and does not mate with M.2.",
    ["That order matches the protocols and the mechanics. NVMe, then SATA SSD, then a slow spinner.",
     "A 5400 rpm drive is the low-power spinning option. It is not faster than NVMe.",
     "M.2 describes the stick shape. You still have to read whether the slot and the drive speak NVMe or SATA.",
     "mSATA is a different small SATA connector. It does not plug into an M.2 slot."]))

Q3.append(item(P, 55, "3.3", "hard",
    "A motherboard manual says the M.2 slot shares lanes with SATA port 1. After an NVMe drive is installed, the SSD on SATA port 1 disappears. The data cable is seated. What happened?",
    ["The M.2 drive disabled that SATA port, which the manual warned about", "NVMe erased the SATA drive's data by being installed", "SATA port 1 only works if the M.2 slot is occupied", "The drive disappeared because RAID 5 needs three disks"],
    0,
    "Many boards steal the lanes or the port from a SATA connector when an M.2 device is populated. The SATA drive is still fine. Move its cable to a port the manual says stays active. Installing NVMe does not wipe another drive. The port did not require the M.2 device. RAID 5 is a different configuration and was not described.",
    ["Shared lanes are the documented behavior. Use a different SATA port and the drive should reappear.",
     "The SATA drive was not erased by the presence of another slot. It lost its port.",
     "The manual says the opposite: occupying M.2 turns that SATA port off.",
     "Nothing in the symptom is a RAID array. One missing port is the lane-sharing rule."]))

Q3.append(item(P, 56, "3.3", "medium",
    "A user wants the family photos on two disks so that one disk can fail and the photos remain. They also want as much speed as a stripe would give, and they have only two drive bays. Which RAID level fits, and which common wish does it not grant?",
    ["RAID 1 mirrors the disks. It survives one failure. It does not give RAID 0 write speed and a full two-disk capacity", "RAID 0, because a stripe survives a single disk failure", "RAID 5, because it can be built on two disks", "RAID 10, because it needs only two disks"],
    0,
    "RAID 1 is the two-disk mirror. Capacity is one disk, reads can be quick, and either disk can fail. RAID 0 stripes and dies when either disk dies, so it is the wrong place for the only copy of family photos. RAID 5 needs at least three disks. RAID 10 needs at least four. With two bays, the redundancy choice is the mirror.",
    ["RAID 1 is the fit. Say out loud that they get one disk of space, not two, so the expectation is honest.",
     "RAID 0 has no redundancy. One failure loses the stripe, which is the photos.",
     "RAID 5 parity needs three or more disks. Two bays cannot build it.",
     "RAID 10 is a stripe of mirrors and wants four disks. Two bays are not enough."]))

Q3.append(item(P, 57, "3.3", "hard",
    "A four-bay server holds a database that needs both speed and the ability to lose one disk. The admin is comparing RAID 5 and RAID 10. Which trade is accurate?",
    ["RAID 10 uses half the raw capacity and generally writes faster than RAID 5. RAID 5 keeps more usable capacity and survives one failure", "RAID 5 survives two disk failures and uses two disks", "RAID 10 can be built on three disks and keeps 75 percent capacity", "RAID 0 and RAID 5 are the same layout"],
    0,
    "RAID 10 mirrors pairs and stripes across those pairs. With four disks you get two disks of usable space, and a write does not have the parity read-modify-write penalty of RAID 5. RAID 5 on four disks keeps three disks of space and survives one failure. It does not survive two. RAID 10 is not a three-disk layout. RAID 0 has no parity.",
    ["That is the real trade: RAID 10 spends capacity to avoid parity writes. RAID 5 spends write performance to keep more capacity.",
     "RAID 5 survives one failure, not two. Two-disk survival is RAID 6, which is not the A+ set, or a lucky RAID 10 pair.",
     "RAID 10 wants four disks here. Three disks do not make a stripe of mirrors with 75 percent usable space.",
     "RAID 0 is a stripe with no parity. RAID 5 is a stripe with parity. They are not the same."]))

Q3.append(item(P, 58, "3.3", "easy",
    "A camera card must move files larger than 4 GB onto both Windows and macOS without extra software. Which file system avoids the 4 GB file limit and is writable on both?",
    ["exFAT", "FAT32", "NTFS, which macOS can always write without help", "ext4, which Windows mounts natively"],
    0,
    "FAT32 stops at about 4 GB per file, so a long video fails. exFAT removes that limit and is the exchange format both operating systems write. NTFS is native to Windows. macOS can read it and often cannot write it without extra software. ext4 is a Linux file system and is not a native Windows volume.",
    ["exFAT is the cross-platform choice for large files. Format the card with it and both computers can write.",
     "FAT32 is compatible and too small per file. A video over 4 GB will not copy.",
     "Treat NTFS as Windows-native. Do not promise a stock Mac can write it.",
     "ext4 is not a file system Windows understands out of the box. The card would look unreadable."]))

Q3.append(item(P, 59, "3.4", "medium",
    "An ITX motherboard is being installed in an ATX case. The board lines up with only some of the standoffs, and four extra standoffs sit under empty areas of the board. What should the technician do?",
    ["Remove the extra standoffs so they cannot short the board, and confirm the form factor still mounts safely", "Add more standoffs under the board until every hole in the case is filled", "Force an ATX board into the ITX tray by drilling the traces", "Skip standoffs and let the board rest on the metal tray"],
    0,
    "Standoffs must match the board's holes. An extra standoff under a trace or a solder point can short the board the moment you power it. ITX is smaller than ATX. It can mount in many ATX cases if the right standoffs are the only ones present. No standoffs at all lets the solder side touch the case. Drilling the board destroys it.",
    ["Extra standoffs are a short. Take them out, use the holes the ITX board actually has, and then seat the board.",
     "Filling every case hole puts metal where the board did not ask for it. That is the short.",
     "You do not drill a motherboard to change its form factor. Use a case and a board that match, or the correct subset of standoffs.",
     "The tray is conductive. Standoffs are what keep the solder from becoming a short."]))

Q3.append(item(P, 60, "3.4", "medium",
    "A builder bent a pin in an LGA socket by dropping the CPU in at an angle. On a different AMD AM4 build, the pins are on the processor instead. Which statement is accurate?",
    ["Intel LGA puts the pins in the socket. AM4 puts the pins on the CPU. Either way, do not force a bent pin", "Both designs put the pins on the motherboard and the CPU is a pad grid", "AM4 is LGA and Intel desktop chips of that era are PGA", "Bent pins can be ignored because the socket only uses half of them"],
    0,
    "LGA means the lands are on the CPU and the pins are in the socket. That is the Intel desktop pattern and also AMD AM5. AM4 is PGA, so the pins are on the chip and a bend is on the chip. Forcing either one breaks the contact. You do not get to ignore pins. If you are not practiced at straightening them, stop and replace the damaged part.",
    ["That is the pin location difference. Treat a bent pin as damage, not as something the socket will work around.",
     "Only LGA puts the pins in the socket. AM4 is the design with pins on the processor.",
     "The labels are reversed. AM4 is pin-grid, and the Intel desktop sockets people mean by LGA have pins in the socket.",
     "Every pin that the design uses matters. A bent one is an open or a short, not a spare."]))

Q3.append(item(P, 61, "3.4", "easy",
    "A new PC boots, fans spin, and then it shuts off within a few seconds. The cooler still has the plastic film on its cold plate, and there is no thermal paste. What is the fault?",
    ["The CPU is overheating because the cooler is not actually touching it", "The plastic film is required and should stay on", "The shutdown proves the SSD is the wrong form factor", "Windows Update caused a shutdown before Windows was installed"],
    0,
    "The cold plate has to meet the CPU heat spreader with a thin layer of paste. A plastic shipping film prevents that contact, so the CPU hits its thermal limit and the firmware shuts the PC off to save the chip. Remove the film, apply a small amount of paste, and reseat the cooler evenly. The SSD and Windows are not in this story. The film is trash, not a part.",
    ["No contact, no paste, immediate thermal shutdown. Remove the film and install the cooler properly.",
     "The film is packaging. Leaving it on is the reason the cooler cannot do its job.",
     "An SSD form-factor problem would show up as a missing drive, not as a thermal shutdown at first power-on.",
     "Windows is not installed yet in this build story. The firmware is protecting the CPU."]))

Q3.append(item(P, 62, "3.4", "medium",
    "Task Manager on a four-core CPU shows eight logical processors. The user thinks the shop sold an eight-core chip. What is the accurate explanation?",
    ["The chip has four cores and multithreading presents eight logical processors", "Logical processors are always separate physical sockets", "Eight logical processors means the board has eight CPUs installed", "Multithreading doubles the RAM"],
    0,
    "A core is a physical processor. Multithreading, such as Intel Hyper-Threading or AMD SMT, lets one core present two logical processors to the OS. Four cores therefore show as eight. That is not eight sockets and it does not double the memory. Software that licenses physical cores should not be told this is an eight-core part.",
    ["Four physical cores with two threads each is eight logical processors. The chip was described honestly.",
     "Logical processors are scheduling targets. They are not extra sockets on the board.",
     "A normal desktop has one CPU package. Eight logical processors do not mean eight packages.",
     "Threads do not add DIMMs. Memory size is a separate specification."]))

Q3.append(item(P, 63, "3.4", "medium",
    "A hypervisor says hardware virtualization is disabled, and a Windows Pro feature that needs it will not install. The CPU supports the feature. Where is the setting?",
    ["In the firmware, enable VT-x or AMD-V", "In the printer preferences", "On the VGA jumpers", "In the DHCP scope"],
    0,
    "Intel VT-x and AMD-V are firmware switches. A CPU can support them while the firmware still has them turned off, which is how a hypervisor ends up refusing to start. Printer preferences, display jumpers, and DHCP do not enable the virtualization bit. After you enable it, a full power cycle is sometimes required before the OS sees it.",
    ["The firmware setup is where VT-x or AMD-V is enabled. That matches a capable CPU and a hypervisor that still says disabled.",
     "Printer preferences do not change CPU features.",
     "VGA jumpers are an ancient display configuration. They are not the virtualization switch.",
     "A DHCP scope hands out addresses. It cannot toggle a CPU feature."]))

Q3.append(item(P, 64, "3.4", "hard",
    "BitLocker is being planned for a fleet. The laptops have a TPM, and the desktops in a lab do not. Secure Boot is also available in the firmware. Which statement keeps the three ideas separate?",
    ["The TPM stores measurements and can hold BitLocker keys. Secure Boot checks signatures at startup. A password is neither of those", "Secure Boot encrypts the disk", "The TPM is a network firewall", "BitLocker works only on FAT32 and does not use the TPM"],
    0,
    "The TPM is a small secure chip used for measured boot and for protecting keys. Secure Boot refuses a bootloader whose signature is not trusted. BitLocker is the disk encryption that can seal its key to the TPM. A firmware password is just a password. Mixing the three names up is how a fleet gets a control that does not actually encrypt anything.",
    ["TPM, Secure Boot, and a password are three different controls. BitLocker can use the TPM. Secure Boot does not encrypt the volume.",
     "Secure Boot authenticates the boot path. BitLocker is what encrypts the disk.",
     "A TPM is not a firewall and it does not filter packets.",
     "BitLocker encrypts NTFS volumes. FAT32 is not its file system, and the TPM is a supported key protector."]))

Q3.append(item(P, 65, "3.5", "medium",
    "A gaming PC shuts off only when the graphics card is under load. The supply is a no-name 300 watt unit and the card's requirement plus the CPU already exceeds that before you add drives. What is the likely cause?",
    ["The power supply wattage is too small for the load", "The card needs a longer HDMI cable", "The shutdown is a DNS timeout", "300 watts is more than any single GPU can draw, so the supply is not the cause"],
    0,
    "Idle does not reveal a supply that is too small. The moment the CPU and the GPU both ask for their design power, a 300 watt unit browns out and the PC resets or dies. Add the draw and leave headroom, then replace the supply with one that meets it. HDMI length and DNS do not power a GPU. Modern cards can draw more than 300 watts by themselves.",
    ["The symptom follows the load, and the arithmetic says the supply is undersized. Replace it with a correctly sized unit.",
     "A longer display cable does not make a power supply hold the rail.",
     "DNS does not reset a PC when the GPU gets busy.",
     "High-end GPUs can exceed 300 watts on their own. The premise that no card can is false."]))

Q3.append(item(P, 66, "3.5", "hard",
    "A builder is short one PCIe power cable and takes a modular cable from a different brand's supply. The pinout looks similar. What is the risk?",
    ["Modular cables are not universal. The other brand's pinout can destroy the card or the supply", "All modular cables use one standard pinout, so brand never matters", "The cable only affects the wall voltage selector", "A wrong modular cable is safe because the connector is keyed against every mistake"],
    0,
    "The connector shape is not a promise about which pin is 12 volts and which is ground. Vendors have shipped modular cables with different pinouts. Using another brand's cable is a known way to kill a GPU or a drive. Use the cables that shipped with this supply, or a cable the supply vendor explicitly lists for this model.",
    ["Do not mix modular cables across brands. The similar plug can still be wired differently, and the damage is immediate.",
     "There is no single safe pinout shared by every modular supply. Brand and model matter.",
     "The wall-voltage selector is a separate switch on some old supplies. A PCIe cable does not set it.",
     "Keying stops some wrong plugs and does not stop a same-shape cable with a different pinout."]))

Q3.append(item(P, 67, "3.5", "easy",
    "A desktop will not power on. The 24-pin motherboard connector is seated, and the 8-pin CPU power connector near the socket is dangling. Fans twitch and the board never POSTs. What is missing?",
    ["The CPU power connector", "A second HDMI cable", "The VGA jumper from a 1990s board", "A USB flash drive"],
    0,
    "The main 24-pin connector feeds the board, and the 4-pin or 8-pin connector beside the socket feeds the CPU. Leave that one off and the board can light up, twitch the fans, and never POST. Seat the CPU power connector. Display cables, ancient jumpers, and a USB stick do not feed the socket.",
    ["The dangling 8-pin lead is CPU power. Plug it in before you replace the motherboard.",
     "HDMI carries video. It does not power the CPU.",
     "Modern boards do not use a VGA jumper to start the CPU. The missing piece is the power plug.",
     "A flash drive is storage. It is not the CPU power rail."]))

Q3.append(item(P, 68, "3.6", "easy",
    "A new laser printer grinds on first power-up and will not pull paper. Bright orange tabs are still fitted on the cartridge and inside the paper path, exactly where the manual shows shipping locks. What is the first fix?",
    ["Remove every shipping lock and piece of packing tape", "Replace the formatter board", "Change the IP address", "Install a duplex unit before removing the locks"],
    0,
    "Shipping locks and tape hold moving parts still during transit. Leaving them in is the classic first-day grind. Take them all out, install the cartridge properly, and then power the printer. A formatter, an IP address, and a duplex unit are not the first guess while the orange tabs are still visible.",
    ["The locks are still installed. Remove them before you diagnose motors or boards.",
     "The formatter is the printer's controller. A grinding new unit with the locks still in does not need that part yet.",
     "The printer has not even fed a page. Addressing is not the grind.",
     "A duplex unit is optional equipment. It does not replace removing the shipping hardware."]))

Q3.append(item(P, 69, "3.6", "hard",
    "One Windows PC prints a page of nonsense characters to a shared laser printer. Two other PCs print the same document correctly. The nonsense PC was set up with a driver the user downloaded for a different model. What should be replaced?",
    ["The incorrect driver on that one PC", "The printer's fuser, because one PC is affected", "The building's DHCP server", "The toner, because the other PCs are lucky"],
    0,
    "Garbled text from a single computer is a driver or spooler problem on that computer. A bad fuser or empty toner would affect every sender. DHCP did not rewrite the page. Install the driver that matches this model and this operating system, and remove the mismatched one.",
    ["One PC, wrong driver, garbage page. Fix that driver. The printer has already proved it can print.",
     "A fuser fault marks every page, from every PC. It would not spare two computers.",
     "DHCP hands out addresses. It does not choose a printer language.",
     "Toner does not behave differently per sending PC. The other pages are not luck."]))

Q3.append(item(P, 70, "3.6", "medium",
    "Pay stubs are sitting in the output tray of a hallway printer where anyone can read them. The printer can hold a job until the user enters a PIN or badges in. Which feature should be turned on?",
    ["Secure print, or badge release", "Economy mode", "A public open tray with no hold", "APIPA"],
    0,
    "Secure print and badge release keep the page in the printer until the person who owns it is standing there. That is the control for pay stubs in a hallway. Economy mode saves toner and does not provide privacy. An open tray is the current problem. APIPA is an IP addressing failure.",
    ["Hold the job until the user authenticates at the printer. That is secure print or badging.",
     "Economy mode thins the toner. The stub is still readable by whoever walks past.",
     "Leaving the tray open is how the stubs are exposed. It is not a feature to enable.",
     "APIPA is a 169.254 address. It does not hold a print job."]))

Q3.append(item(P, 71, "3.6", "hard",
    "Scan-to-folder worked until the file server's service account password was changed last night. Scan-to-email still works. What should be updated?",
    ["The saved credential the scanner uses for the SMB share", "The fuser temperature", "The printer's IPv6 SLAAC address as the only possible cause", "The display language"],
    0,
    "Scan-to-folder is an SMB connection with a username and a password stored on the device. When that password changes, the scan fails and email, which uses a different path, keeps working. Update the stored credential. The fuser, SLAAC, and the panel language do not authenticate to a file share.",
    ["The scanner is logging into the share with the old password. Put the new credential on the device.",
     "The fuser melts toner. It does not log into a file server, and email still scanning proves the device is up.",
     "IPv6 addressing would break more than one protocol if it were the outage. Email still works.",
     "The panel language does not store the SMB password."]))

Q3.append(item(P, 72, "3.7", "easy",
    "Toner rubs off a laser page when you touch it. Text is dark enough, and the image is in the right place. Which part is not doing its job?",
    ["The fuser", "The formatter, because the page is blank", "The scanner glass", "The Ethernet cable"],
    0,
    "The fuser melts and presses the toner into the paper. If the image is present and smears, the toner never fused. A formatter problem would garble or drop the job. The scanner glass matters for copies, not for a computer print that smears. The cable delivered the job, because there is an image.",
    ["The fuser is heat and pressure at the end of the path. Smear means that stage failed.",
     "The page is not blank. The formatter got an image onto the drum and onto the paper.",
     "Scanner glass affects copies and scans. A smeared computer print has already passed the drum.",
     "The cable is not a heat source. The job arrived."]))

Q3.append(item(P, 73, "3.7", "medium",
    "Every laser page has a dark vertical line in the same place, including pages from every tray and every PC. Cleaning the glass is not relevant because nobody is copying. What is the usual cause?",
    ["A scratched or dirty imaging drum", "A wrong printer driver on one PC", "Economy mode", "A DHCP reservation"],
    0,
    "A line that repeats in the same horizontal position, on every page, from every source, is on the drum or another roller that touches every page. Many lasers put the drum in the toner cartridge, so replacing that cartridge is the practical test. A driver would not spare no PC. Economy mode fades the page. DHCP does not scratch a line.",
    ["The drum is the common cause of a consistent vertical line. Replace the cartridge or the drum.",
     "Every PC prints the line, so it is not one workstation's driver.",
     "Economy mode lightens the whole page. It does not draw one dark line.",
     "A reservation fixes an address. It does not mark the paper."]))

Q3.append(item(P, 74, "3.7", "medium",
    "An inkjet page has bands of missing color. The vendor utility has a head-cleaning cycle. What is the first maintenance step?",
    ["Run the cleaning cycle, then print a nozzle check", "Replace the fuser", "Degauss the print head", "Install a tractor feed"],
    0,
    "Inkjet heads clog. The cleaning cycle purges them, and a nozzle check shows whether the bands are gone. If a couple of cleanings fail, replace the cartridge or the head, depending on whether the head is built into the cartridge. Lasers have fusers. Degaussing is for old magnetic displays and drives. Tractor feed belongs to impact printers.",
    ["Clean, then verify with the nozzle pattern. That is the inkjet maintenance order.",
     "There is no fuser in an inkjet. That part is in a laser printer.",
     "Degaussing is not inkjet maintenance and will not clear a nozzle.",
     "Tractor feed pulls continuous forms through an impact printer. It is the wrong technology."]))

Q3.append(item(P, 75, "3.7", "easy",
    "A thermal receipt printer suddenly prints blank pages. The paper is ordinary copy paper that was loaded when the special rolls ran out. What is the requirement?",
    ["Thermal printers need heat-sensitive paper. Ordinary paper has nothing to darken", "Thermal printers use a ribbon and cannot use coated paper", "The receipt printer needs a laser fuser", "Copy paper is required, and thermal paper is the mistake"],
    0,
    "A thermal head heats spots on coated paper, and those spots darken. Plain copy paper has no coating, so the head writes invisibly. Do not look for a ribbon. That is the impact printer. There is no fuser. And do not store the real thermal rolls in a hot place, or they darken in the box.",
    ["Put the correct thermal paper back in. Plain paper will not mark.",
     "Impact printers use ribbons. Direct thermal receipts do not.",
     "A fuser is a laser part. A receipt printer does not have one.",
     "Copy paper is why the page is blank. Thermal paper is the supply this printer needs."]))

Q4.append(item(P, 76, "4.1", "easy",
    "A company uses a web mail suite. Employees do not patch a server, and the provider runs the application. Which cloud model is the mail suite?",
    ["SaaS", "IaaS", "A private VLAN", "RAID 0"],
    0,
    "Software as a service is the finished application. Web mail is the example. Infrastructure as a service would be a virtual machine the company still patches. A VLAN and a RAID level are not service models.",
    ["SaaS is the application you simply use. The provider patches the mail platform.",
     "IaaS would leave the guest operating system in the company's hands. That is not this mail suite.",
     "A VLAN is a Layer 2 segment. It is not a cloud service model.",
     "RAID 0 is disk striping. It is not SaaS."]))

Q4.append(item(P, 77, "4.1", "medium",
    "Developers deploy an application and do not manage the operating system underneath it. The provider patches that OS and the runtime. The developers still own the application code. Which model is this?",
    ["PaaS", "SaaS, because the developers wrote the application", "IaaS, because somebody patched an OS", "A community cloud, regardless of who manages the OS"],
    0,
    "Platform as a service gives you a place to run code while the provider keeps the platform and the OS. SaaS would mean the provider also owns the application. IaaS would mean your team patches the guest. Community cloud describes who shares the cloud, not who patches the OS.",
    ["PaaS is the split in the question: you bring the app, they run the platform.",
     "If the developers own the code, it is not SaaS. SaaS is the provider's application.",
     "IaaS is the model where your administrators patch the guest. The stem says they do not.",
     "Community cloud means several organizations share a cloud for a common purpose. It can be IaaS, PaaS, or SaaS."]))

Q4.append(item(P, 78, "4.1", "medium",
    "A tax office needs ten times the servers in April and almost none in June, and it wants the June bill to shrink with the June load. Which two cloud characteristics are those? (Choose two.)",
    ["Rapid elasticity", "Metered utilization", "A single physical RAID 0 as the whole design", "A requirement to buy the peak hardware and keep it all year"],
    [0, 1],
    "Rapid elasticity is the grow-and-shrink behavior. Metered use is paying for what you consume, so June is cheap. Buying the April hardware and keeping it all year is the opposite of both. RAID 0 is a disk layout and is not a cloud characteristic.",
    ["Elasticity is the April surge and the June release of capacity.",
     "Metered utilization is why the bill follows the load instead of the peak.",
     "RAID 0 is striping. It does not scale an application in April.",
     "Owning the peak hardware all year is the cost the cloud characteristics are supposed to avoid."]))

Q4.append(item(P, 79, "4.1", "easy",
    "Several hospitals share a cloud built for their compliance needs. It is not the hospital chain's own data center, and it is not the general public region anyone can buy. Which deployment model is it?",
    ["Community", "Public, because more than one customer exists", "Private, because hospitals are involved", "Hybrid, because two hospitals means two models"],
    0,
    "A community cloud is shared by organizations with a common concern, such as hospitals or universities. Public is the provider's general multi-customer region. Private is dedicated to one organization. Hybrid is a mix of private and public, or on-premises and cloud, not merely 'more than one hospital.'",
    ["Community is the shared, purpose-built cloud. The hospitals are the community.",
     "Public means the general cloud anyone purchases. A compliance-specific shared cloud is narrower than that.",
     "Private would be one organization's own environment. Several independent hospitals sharing is community.",
     "Hybrid is a mix of deployment models. Two customers do not define it."]))

Q4.append(item(P, 80, "4.1", "medium",
    "Payroll stays on servers in the company basement. The public website runs in a public cloud. A VPN connects the two. What is the deployment called?",
    ["Hybrid", "Community only", "Public only, because a VPN is involved", "Private only, because payroll did not move"],
    0,
    "Hybrid is the mix: some workloads remain private, some run in the public cloud, and they are connected. Leaving payroll in the basement does not make the whole design private, because the website is public. The VPN is the connection, not a separate deployment model.",
    ["Hybrid is the combination of the basement and the public cloud. The VPN is how they reach each other.",
     "Community would be several organizations sharing one cloud. This is one company using two places.",
     "The website is public and payroll is not. Calling the whole design public ignores the basement.",
     "Calling it private ignores the public website. The mix is the point."]))

Q4.append(item(P, 81, "4.1", "medium",
    "A desktop folder is set to sync to a cloud drive. A user deletes the folder locally and the cloud copy disappears too. They say the sync was their backup. What did they misunderstand?",
    ["Sync keeps copies the same, including deletions. A backup keeps a separate restorable history", "Sync stores an unlimited number of old versions by definition", "A cloud sync cannot delete anything", "RAID 1 on the PC is the same product as the sync client"],
    0,
    "File sync is a mirror of the current folder. Delete it in one place and the deletion propagates. A backup is a separate copy you can restore, preferably with versions and an offsite copy that a delete does not immediately destroy. Some products add version history. You do not assume that unless you have turned it on and tested a restore.",
    ["Sync is not a backup. The delete did what sync is supposed to do. They need a real backup with history.",
     "Version history is a feature you configure and pay for on some products. It is not the definition of sync.",
     "Sync can absolutely delete the other copy. That is the incident.",
     "RAID 1 is a local mirror of disks. It is not the cloud sync client, and it also is not an offsite backup."]))

Q4.append(item(P, 82, "4.1", "easy",
    "Users can knock over a cup on their desk and not lose the spreadsheet they had open, because the desktop they see is running in the data center. The desk only has a small client. What is that design?",
    ["VDI", "A local FAT32 install with no network", "RAID 0 on the desk", "A KVM switch"],
    0,
    "Virtual desktop infrastructure runs the desktop on a server, on premises or in the cloud, and the device on the desk displays it. A lost or soaked laptop does not hold the files if the work never lived there. FAT32, local RAID, and a KVM do not move the desktop into the data center.",
    ["VDI is the remote desktop running in the data center. The cup cannot reach the files.",
     "A local install keeps the files on the desk. That is the risk VDI removes.",
     "RAID 0 is local striping with no redundancy. It is not a data-center desktop.",
     "A KVM switches one keyboard and monitor between local PCs. It does not host the desktop elsewhere."]))

Q4.append(item(P, 83, "4.1", "medium",
    "A cloud design shares physical hosts among customers and relies on the provider to isolate them. A noisy neighbor can still affect performance if the isolation is weak. What is the sharing called?",
    ["Shared resources, or multitenancy", "A private dedicated host by definition", "RAID 1", "A loopback plug"],
    0,
    "Multitenancy means several customers share the provider's resources. It is one of the reasons cloud can be cheap, and it is why isolation matters. A dedicated host is the opposite product. RAID 1 and a loopback plug are local hardware ideas, not the sharing model.",
    ["Multitenancy is the shared infrastructure. The noisy neighbor is the risk that comes with it.",
     "A dedicated host is reserved for one customer. The stem describes sharing.",
     "RAID 1 mirrors two disks. It is not a cloud tenancy model.",
     "A loopback plug tests a NIC. It does not describe customers sharing a host."]))

Q4.append(item(P, 84, "4.2", "easy",
    "A technician wants to open a suspicious attachment without letting it onto the office file shares. A virtual machine with no network adapter is available. What is that VM being used as?",
    ["A sandbox", "A production domain controller", "A DHCP server for the floor", "A print server"],
    0,
    "A sandbox is an isolated place to try something you do not trust. No network adapter means the attachment cannot walk onto the file shares even if it is malicious. You still do not use that VM for ordinary browsing afterward. It is not your domain controller, your DHCP server, or your print server.",
    ["The isolated VM is a sandbox. That is the purpose that matches the objective.",
     "A domain controller is production identity. You do not open suspicious attachments on it.",
     "DHCP is a network service. This VM has no adapter on purpose.",
     "A print server is production. It is the wrong place for an untrusted file."]))

Q4.append(item(P, 85, "4.2", "medium",
    "A Type 2 hypervisor on a technician's Windows laptop will not start a VM. The firmware message it quotes says virtualization is disabled. The laptop has enough RAM. What is the first change?",
    ["Enable virtualization in the firmware", "Add a second laptop battery and leave the firmware alone", "Format the host as FAT32", "Disable the TPM"],
    0,
    "Client hypervisors need the CPU's virtualization extensions turned on in firmware, and they need enough RAM and disk. The error already named the firmware switch, and RAM is sufficient, so enable VT-x or AMD-V and power-cycle. FAT32, the battery, and the TPM are not the quoted error.",
    ["Turn the feature on in firmware. The hypervisor told you it is off.",
     "Another battery does not enable a CPU feature.",
     "FAT32 is a poor host file system choice and is not why the hypervisor refuses to start.",
     "The TPM is not the switch the error named. Leave it alone."]))

Q4.append(item(P, 86, "4.2", "medium",
    "An old accounting app runs only on Windows 7. The shop standard is a current Windows version. The app must keep running for one department, and it must not be reachable from the internet. What is the client-virtualization approach?",
    ["Run Windows 7 in a VM that has no path to the internet, and keep the host current", "Put Windows 7 on every PC in the company", "Expose the Windows 7 VM directly on the internet so vendors can help", "Replace the VM with RAID 0"],
    0,
    "Client virtualization is how you keep a legacy operating system for one application without installing that unsupported OS on the whole fleet. The VM should be isolated, because Windows 7 no longer gets public security fixes. Putting it on the internet, or on every desk, spreads an unsupported system. RAID is storage, not an operating system.",
    ["One isolated VM is the contained way to keep the legacy app. The host OS can stay current.",
     "Installing an unsupported OS everywhere maximizes the exposure the VM was meant to avoid.",
     "An unsupported OS on the internet is the opposite of containment.",
     "RAID 0 does not run Windows 7 and does not isolate an application."]))

Q4.append(item(P, 87, "4.2", "easy",
    "A laptop with 8 GB of RAM is asked to run three VMs that each want 4 GB, plus the host OS. The host becomes unusable. What resource ran out?",
    ["RAM", "The VGA connector", "The number of USB ports", "The print spooler"],
    0,
    "Client virtualization is usually limited by memory. Three guests at 4 GB plus a host do not fit in 8 GB, so the host pages itself to death. Add RAM or run fewer guests. The VGA port, USB count, and the print spooler are not the resource the guests are fighting over.",
    ["Memory is the scarce resource. 8 GB cannot back three 4 GB guests and the host.",
     "The video connector carries a picture. It does not allocate memory to a guest VM.",
     "USB ports do not size a virtual machine's RAM, so adding ports would not help.",
     "The print spooler queues print jobs. It does not fund guest memory."]))

Q4.append(item(P, 88, "4.2", "hard",
    "A security note says a guest VM is not automatically safe just because it is virtual. The host is unpatched, and the guest has no antivirus. Which statement matches the objective's security caution?",
    ["Guests need patches and malware protection, and a VM is not a complete security boundary", "Virtual machines cannot be attacked, so guests need no patches", "The host's patches cover every guest even when guest updates are off", "A snapshot replaces antivirus"],
    0,
    "A VM is another computer. It needs the same patching and endpoint protection as a physical one, especially if it can reach a network. The host must be patched too, because a compromise of the host is a compromise of the guests. Snapshots are a convenience for rolling back, and they are not a malware control. They can even preserve the malware.",
    ["Treat the guest as a real system. Isolation helps, and it does not replace patches or antivirus.",
     "Guests are attacked every day. Virtualization is not invisibility.",
     "Host patches fix the host. The guest operating system has its own update cycle.",
     "A snapshot can roll back a test. It does not detect malware, and a snapshot taken after infection keeps the infection."]))

Q4.append(item(P, 89, "4.2", "medium",
    "A developer needs a Linux tool on a Windows laptop for an afternoon, without repartitioning the disk. Client virtualization is approved. What is the least disruptive approach?",
    ["Run a Linux VM on the Windows host", "Wipe Windows and install Linux on the bare hardware", "Boot a second physical laptop the developer does not have", "Convert the file system to ext4 and hope Windows still boots"],
    0,
    "A Type 2 hypervisor on the existing Windows install runs Linux for the afternoon and leaves the disk layout alone. Wiping the laptop destroys the workstation. Another physical machine may be fine and is not what they have. Converting the Windows volume to ext4 makes Windows unbootable.",
    ["A VM is the client-side virtualization answer. The Windows install stays, and Linux runs as a guest.",
     "Reinstalling the host is the opposite of least disruptive.",
     "A second computer is a different project, and the stem says they are using the laptop they have.",
     "ext4 is not a Windows system volume. That conversion is a rebuild, not an afternoon tool."]))

if __name__ == "__main__":
    from common import dump
    dump("220-1101", {"q-d3.json": Q3, "q-d4.json": Q4})
