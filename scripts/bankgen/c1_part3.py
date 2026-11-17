from common import item

P = "c1"
Q = []

Q.append(item(P, 90, "5.1", "easy",
    "A user says the PC is 'broken' and asks for a new motherboard. The technician has not asked what happens, when it started, or what changed. Company policy says hardware is replaced only after diagnosis. What comes first?",
    ["Identify the problem, including what changed, and respect the policy before any replacement", "Order the motherboard because the user used the word broken", "Document a replacement that has not happened", "Install the new board and identify the problem afterward"],
    0,
    "The A+ method starts by identifying the problem: question the user, find the scope, and ask what changed. It also says to consider policy before you change anything. A motherboard replacement is a late step, after a theory, a test, and a plan. Documentation records the real outcome.",
    ["Identify first, and do not skip the policy that forbids swap-first repairs.",
     "The word broken is not a diagnosis. Ordering a board skips every earlier step.",
     "You cannot document a fix you have not performed. Notes come with the work, and the closeout comes at the end.",
     "Installing first and thinking later is how working parts get replaced and the real fault stays."]))

Q.append(item(P, 91, "5.1", "medium",
    "A theory that the monitor cable is loose was tested by reseating both ends. The image is still missing, and a flashlight test shows no faint panel. What does the method say when the theory fails?",
    ["Form a new theory or escalate", "Reseat the same cable indefinitely", "Skip to documentation and close the ticket as fixed", "Replace the user's chair"],
    0,
    "A failed test means the theory was wrong or incomplete. Establish a new one, or escalate if you are past your skill or authority. Repeating the same reseat is not a new theory. Closing the ticket leaves the user with a blank screen. The chair was never evidence.",
    ["New theory or escalation is the branch after a disproven cause.",
     "The cable was already reseated. Doing it again does not honor the result of the test.",
     "The screen is still blank. There is nothing honest to close as fixed.",
     "The chair does not drive the panel. It is not a theory about this symptom."]))

Q.append(item(P, 92, "5.1", "medium",
    "The cause is a failed stick of RAM. The technician is about to power off, replace it, and then confirm the PC boots and the application runs. In the A+ six-step method, which step combines the plan and the actual replacement?",
    ["Establish a plan of action and implement the solution", "Identify the problem, which is already done", "Document findings before the RAM is replaced", "Test a theory that was already confirmed"],
    0,
    "On the A+ list, step 4 is both the plan and the implementation. You decide the replacement, watch for side effects such as losing the other channel's population, and then do the work. Identification and the theory test are already behind you. Documentation is the last step, after you verify the boot and the application.",
    ["Plan and implement are one A+ step. Do the replacement carefully, then verify, then document.",
     "Identification already happened. Going back to it does not put the RAM in the slot.",
     "Documentation is step 6. Writing the closeout before the swap leaves an unfinished repair.",
     "The theory was confirmed. The next work is the fix, not another test of a loose cable."]))

Q.append(item(P, 93, "5.1", "easy",
    "A RAM replacement fixed the crashes. The user opens the original application and it stays up. The technician updates the ticket with the symptom, the bad module, and the new part number. Which two end steps are those? (Choose two.)",
    ["Verify full system functionality", "Document findings, actions, and outcomes", "Skip verification because the user smiled", "Leave the ticket blank so the next technician can practice"],
    [0, 1],
    "Verification is the user actually doing the work that used to crash, not only a successful POST. Documentation is the ticket that tells the next person what the cause was. A smile is not a test. An empty ticket throws away the diagnosis.",
    ["Verification is the application staying up. POST alone would have been a weaker test.",
     "The ticket is the documentation step: symptom, cause, and the action you took.",
     "A smile does not prove the crashing application is fixed.",
     "A blank ticket fails the documentation step and makes the next incident start from zero."]))

Q.append(item(P, 94, "5.2", "medium",
    "A PC beeps and does not display after a RAM upgrade. The modules were pushed in until the side clips almost latched. What is the first hardware check?",
    ["Reseat the RAM fully and try one module at a time", "Replace the CPU immediately", "Reinstall Windows", "Change the monitor's color profile"],
    0,
    "A beep code and no display right after a memory install points at memory seating or a bad module. Fully latch each stick, and test one at a time so a single bad module is obvious. The CPU and Windows were working before the upgrade. A color profile does not prevent POST.",
    ["Reseat and isolate. The upgrade is the change, and the RAM is the part your hands were just on.",
     "The CPU did not change. Replacing it first ignores the beeps that followed the memory work.",
     "Windows is not running yet. There is no display and no POST. Reinstalling it is not possible or useful.",
     "A color profile is an operating-system setting. The PC has not reached the OS."]))

Q.append(item(P, 95, "5.2", "easy",
    "A burning smell comes from a tower, and a wisp of smoke leaves the power supply. What is the first action?",
    ["Power it off and unplug it, then do not open the supply", "Keep it running to see if the smell fades", "Spray water into the vents", "Format the disk"],
    0,
    "Smoke and a burning smell mean stop feeding it power. Unplug it. Do not open the power supply. The capacitors inside can hurt you, and the supply is a replaceable unit, not a field-repair project. Water makes a short worse. Formatting a disk does not put out a fire.",
    ["Kill the power and leave the supply closed. Replace it. Do not probe inside it.",
     "Leaving it on is how a smell becomes a fire.",
     "Water on live or recently live electronics is a shock and a short.",
     "The disk is not the burning part. Formatting it is irrelevant and destroys data."]))

Q.append(item(P, 96, "5.2", "medium",
    "A PC loses the date every time it is unplugged. The operating system time is correct until the next power loss. What component should be replaced?",
    ["The CMOS battery", "The toner cartridge", "The Wi-Fi antenna", "The printer fuser"],
    0,
    "The motherboard keeps firmware settings and the clock with a small battery, usually a CR2032, while wall power is absent. A dead cell explains a clock that dies only when unplugged. Toner, a Wi-Fi antenna, and a fuser are not the real-time clock.",
    ["Replace the CMOS battery and then reset the clock. The symptom is specific to power loss.",
     "Toner is a laser-printer supply. It does not keep time.",
     "The antenna is a radio lead. It does not power the firmware clock.",
     "The fuser melts toner. It is not on the motherboard."]))

Q.append(item(P, 97, "5.2", "medium",
    "Capacitors on a motherboard are domed on top and a few are leaking. The PC crashes randomly. What is the reasonable conclusion?",
    ["The motherboard is failing and should be replaced, not recapped in the field as a casual repair", "Domed capacitors are the normal factory shape", "Replace the mouse", "Add more USB devices"],
    0,
    "A healthy electrolytic capacitor has a flat top, often with a scored vent. A dome or a leak means the part has failed, and the board will be unstable. Replacing the board is the practical repair. Recapping is a specialized repair, not a desk-side first move. The mouse and extra USB devices do not swell capacitors.",
    ["Swollen, leaking capacitors are a failed board. Replace the motherboard.",
     "A dome is damage. Factory tops are flat.",
     "The mouse cannot swell a capacitor on the board.",
     "More USB load does not restore a leaking capacitor."]))

Q.append(item(P, 98, "5.2", "easy",
    "A laptop sitting on a blanket shuts down when the GPU gets busy. The same laptop on a hard desk, with the vents clear, stays up. What is the cause?",
    ["The blanket blocked the intake and the laptop overheated", "The blanket changed the SSID", "The GPU forgot its driver only while on cloth", "The CMOS battery falls out on soft surfaces"],
    0,
    "Soft surfaces block laptop intakes and the heat has nowhere to go. The thermal protection then shuts the machine down under load. A desk lets the fans breathe. Blankets do not edit wireless names, drivers, or the CMOS battery.",
    ["Airflow was the missing piece. Keep the laptop on a hard surface and confirm the fan actually spins.",
     "An SSID does not change because the laptop was set on cloth.",
     "The driver is still installed. The pattern follows the surface, not a driver reinstall.",
     "The CMOS battery is screwed inside the machine. A blanket does not eject it."]))

Q.append(item(P, 99, "5.2", "hard",
    "A desktop randomly reboots only in 3D games. Temperatures are normal, the event log shows kernel power loss, and the supply is well below the GPU's required wattage. Memory tests pass. Which component is the best suspect?",
    ["The power supply", "The keyboard", "The printer driver", "The monitor stand"],
    0,
    "A supply that cannot hold the 12 volt rail under GPU load drops the PC and leaves a kernel-power event. Normal temperatures argue against a simple dust problem, and a passed memory test argues against RAM. The keyboard, the printer driver, and the monitor stand do not brown out a 12 volt rail.",
    ["The undersized supply matches the load-only reboot and the power event. Replace it with a supply that meets the GPU requirement.",
     "A keyboard does not reboot a PC when the GPU draws current.",
     "A printer driver is not in the 3D path and does not cut power.",
     "The stand holds the panel. It is not an electrical source."]))

Q.append(item(P, 100, "5.3", "easy",
    "A mechanical drive starts clicking and the PC no longer sees it consistently. SMART also reports a failing status. What should the technician do before trying heroic repairs on that drive?",
    ["Copy the data off now, if it still mounts, and replace the drive", "Defragment it for several hours", "Run a full format to clear the click", "Disable SMART so the warning stops"],
    0,
    "Clicking plus a SMART failure means the mechanics are going. The priority is the data: copy what you can, then replace the disk. Defragmenting and formatting beat a dying drive harder. Turning SMART off hides the warning and saves nothing.",
    ["Back up immediately and retire the drive. The click is a failing actuator, not a software setting.",
     "Defragmenting a dying mechanical drive spends the little life it has left.",
     "A format writes the whole disk and destroys the files you were trying to save.",
     "SMART is the warning. Silencing it does not heal the platter."]))

Q.append(item(P, 101, "5.3", "medium",
    "A RAID 5 array is degraded. One disk's LED shows a failure, and the other two are healthy. Users can still read data. What is the correct next action?",
    ["Replace the failed disk and let the array rebuild. Do not pull a healthy disk", "Delete the array and create a new one on the remaining disks", "Convert it to RAID 0 to make the rebuild faster", "Format all three disks"],
    0,
    "A degraded RAID 5 is still serving data and can survive only this one failure. Replace the bad disk so the parity can rebuild. Pulling a healthy disk, or rewriting the array, destroys the volume. RAID 0 has no redundancy and is not a rebuild target. Formatting erases the users' data.",
    ["Replace the failed member and rebuild. Leave the healthy disks in place until the new disk has joined.",
     "Creating a new array on the survivors throws away the degraded volume that is still readable.",
     "RAID 0 cannot rebuild anything. Converting now is how you lose the array.",
     "Formatting the members erases the data the degraded array was still providing."]))

Q.append(item(P, 102, "5.3", "hard",
    "A two-disk RAID 0 boot volume loses one disk. The user asks for a rebuild. What is the honest answer?",
    ["RAID 0 cannot rebuild. The data is gone unless a backup exists", "RAID 0 rebuilds from parity on the surviving disk", "Replace the disk and the stripe repairs itself overnight", "Convert the survivor to RAID 5 without the lost data"],
    0,
    "RAID 0 stripes with no parity and no mirror. Either disk dying loses the volume. There is nothing to rebuild from. Backups are the only recovery. RAID 5 and RAID 1 are the layouts that survive a single disk, and they had to be chosen before the failure.",
    ["No parity and no mirror means no rebuild. Restore from backup and then choose a redundant layout.",
     "RAID 0 has no parity. The surviving disk holds only stripes, not a complete copy.",
     "A new disk does not know the missing stripes. The array will not heal overnight.",
     "You cannot invent the lost stripes by renaming the survivor as RAID 5."]))

Q.append(item(P, 103, "5.3", "medium",
    "A new disk appears in the firmware and does not appear in File Explorer. Disk Management says the disk is not initialized. There is no data on it. What should the technician do?",
    ["Initialize it, create a volume, and format it", "Run a low-level wipe of a different disk that already has data", "Replace the CPU", "Delete the user's profile"],
    0,
    "A brand-new disk has no partition table until it is initialized. GPT is the right choice for a modern disk, especially over 2 TB. Then it needs a volume and a format. Do not initialize a disk that used to have data and is only missing a drive letter. That is a different symptom. The CPU and the profile are unrelated.",
    ["Initialize, partition, and format. Explorer has nothing to show until those exist.",
     "Wiping some other disk destroys data that was not part of this problem.",
     "The CPU is not why a new disk has no partition table.",
     "A user profile does not initialize storage."]))

Q.append(item(P, 104, "5.3", "easy",
    "A 4 TB disk shows about 2 TB in Windows. It was initialized as MBR. The firmware is UEFI. What is the limitation?",
    ["MBR cannot address the whole disk past about 2 TB. Use GPT", "UEFI cannot boot any disk larger than 2 TB", "NTFS is limited to 2 TB", "The disk is a DVD"],
    0,
    "MBR's partition table is the reason a large disk appears as about 2 TB. GPT is the partition style for disks of this size, and UEFI boots from GPT. NTFS itself can hold far more than 2 TB. The disk is not an optical disc. Converting the partition style destroys existing partitions, so back up first if there is anything on it.",
    ["Initialize it as GPT if you need the other 2 TB. MBR is the ceiling.",
     "UEFI is exactly the firmware that likes GPT. It is not the reason the disk looks small.",
     "NTFS is not capped at 2 TB. The partition table is.",
     "A 4 TB hard disk is not a DVD. Optical media does not show up as an MBR disk of 2 TB."]))

Q.append(item(P, 105, "5.4", "easy",
    "A projector says no signal. The laptop's own screen works, and the projector input menu is set to HDMI while the cable is on VGA. What are the two checks? (Choose two.)",
    ["Select the projector input that matches the cable", "Use the laptop's display-output toggle so it actually sends a picture", "Replace the projector lamp before checking inputs", "Reseat the memory, because no signal is a RAM code"],
    [0, 1],
    "No signal is often the wrong input or a laptop that is still showing only its internal panel. Match the input to the cable, then use the display toggle, Windows+P on Windows, to extend or duplicate. The lamp is a later suspect when the input is correct and the picture is dim or absent. RAM does not choose a projector input.",
    ["The menu is on HDMI and the cable is VGA. Change the input before you condemn the projector.",
     "The laptop may not be sending anything out the external port. Toggle the output.",
     "A lamp replacement is money spent before the free checks. The menu already shows the mismatch.",
     "Memory errors do not present as a projector input mismatch."]))

Q.append(item(P, 106, "5.4", "medium",
    "A projector runs for ten minutes and shuts off. The filter is packed with dust and the intake is hot. The lamp hour counter is low. What is the likely cause?",
    ["Overheating from a clogged filter", "A lamp at the end of its life, given the low hour count", "A wrong SSID", "A depleted CMOS battery in the projector's remote"],
    0,
    "Projectors shut down to protect themselves when they cannot move air. A packed filter and a hot intake explain a ten-minute run with a young lamp. Clean the filter and give it the clearance the manual shows. A low lamp count argues against an exhausted bulb. Wireless names and the remote's battery do not thermal-shutdown the lamp.",
    ["Clean the airflow path. The heat and the dirty filter match the timed shutdown.",
     "The hour counter says the lamp is young. Do not buy a bulb before the filter is clean.",
     "An SSID is a wireless name. The projector is overheating, not joining the wrong network.",
     "The remote battery would stop the remote. It would not heat the intake."]))

Q.append(item(P, 107, "5.4", "hard",
    "An external monitor is fine, and the laptop panel shows lines that change when the lid moves. What does that pattern isolate?",
    ["The internal display cable or the panel, not the graphics adapter", "A dead CPU", "A failed printer spooler", "The office DHCP scope"],
    0,
    "A good external picture means the GPU is producing video. Lines that track the hinge point at the cable that flexes there, or at the panel if the cable tests good. Replacing the CPU, restarting a spooler, or editing DHCP does not change a hinge-related line.",
    ["External good, internal bad, worse when the lid moves: cable or panel. Start with the cable.",
     "The CPU is running the external monitor. It is not the cracked path in the hinge.",
     "The spooler prints. It does not draw lines on a laptop panel.",
     "DHCP hands out addresses. It does not follow the hinge."]))

Q.append(item(P, 108, "5.4", "easy",
    "A VGA monitor is missing all of the blue. Wiggling the VGA plug changes the color. What is the likely fault?",
    ["A bent or broken pin in the VGA connector", "A failed fuser", "An incorrect POP3 port", "A RAID 5 rebuild"],
    0,
    "VGA carries analog color on separate pins. A bent pin drops one color, and wiggling the plug makes it come and go. HDMI usually fails more completely rather than dropping a single clean color. A fuser, a mail port, and a RAID rebuild do not remove blue from a VGA cable.",
    ["Inspect and carefully straighten, or replace the cable. One color plus a loose plug is the pin.",
     "The fuser is inside a laser printer. It does not drive a monitor.",
     "POP3 is a mail port. It is not a video pin.",
     "A RAID rebuild is a disk operation. It does not subtract blue."]))

Q.append(item(P, 109, "5.5", "easy",
    "A phone battery is swollen and the case is splitting. The user wants to finish charging it overnight under a pillow. What is the safe guidance?",
    ["Power it off, do not charge it, do not puncture it, and replace the battery", "Keep charging it so the battery smooths itself flat", "Press the swelling back into the case with a clamp", "Put the phone in a freezer"],
    0,
    "A swollen lithium battery is a fire risk. Stop charging it, do not squeeze or puncture it, and replace it through the vendor or a battery recycling path. Charging it under a pillow adds heat. A freezer does not make a damaged cell safe.",
    ["Off, no charger, no puncture, replace and recycle. That is the safe path.",
     "More charge on a swollen cell is how it gets worse, not how it flattens.",
     "Clamping the case punctures or stresses the cell. Do not force it shut.",
     "Cold does not repair a swollen cell and can add condensation. Replace the battery."]))

Q.append(item(P, 110, "5.5", "medium",
    "A phone fell in a sink. The user has already plugged it into a charger because someone said charging dries electronics. What should the technician say?",
    ["Power it off and do not apply power. Dry it properly and do not trust rice as the repair", "Leave it charging so the heat drives the water out", "Put it in a bag of rice and promise the water is gone by morning", "Run it in the oven on low"],
    0,
    "Water plus power is a short. The professional step is power off, disconnect the battery if the model allows, and dry the phone before it sees a charger again. Rice is a folk remedy that leaves starch in the ports and does not prove the board is dry. An oven melts things. Corrosion can show up later even if it boots tomorrow.",
    ["No power until it is actually dry. That is the first rule after a liquid spill.",
     "Charging a wet phone is how a recoverable spill becomes a dead board.",
     "Rice is not a repair. It does not reach the water under a shield, and it makes a mess.",
     "An oven is uncontrolled heat. It is not a drying procedure for a battery."]))

Q.append(item(P, 111, "5.5", "medium",
    "A phone will not charge. A different cable and a different brick work on another phone, and they fail on this one. The port is packed with lint. What is the first physical fix?",
    ["Power it off and carefully remove the lint so the plug can seat", "Replace the motherboard before looking in the port", "Install more RAM", "Change the wallpaper"],
    0,
    "Lint in a Lightning or USB-C port keeps the plug from making contact. With the phone off, a non-metal pick or the vendor's method clears it, and then the known-good cable can be tried again. The motherboard is a last resort after the port and the battery have been ruled out. RAM and wallpaper do not charge a phone.",
    ["Clean the port carefully and retest with the known-good cable. That is the cheap, likely fix.",
     "A packed port explains the symptom. Do not replace the board while you can still see the lint.",
     "Adding phone memory does not clear a packed charge port or move current into the battery.",
     "Wallpaper is cosmetic. It does not move current into the battery."]))

Q.append(item(P, 112, "5.5", "easy",
    "A laptop trackpad cursor drifts across the screen by itself. An external mouse is steady. What is the likely fix?",
    ["Clean or replace the trackpad, or disable it while a mouse is used, after checking for a palm-rest pressure problem", "Replace the fuser", "Change the DNS server", "Flash the printer firmware"],
    0,
    "Cursor drift with a good external mouse isolates the problem to the trackpad: dirt, a swollen battery pressing the pad, or a failing digitizer. Clean it, make sure nothing is pressing it, and replace it if it still wanders. A fuser, DNS, and a printer have nothing to do with the pointer.",
    ["The trackpad is the unsteady device. Clean, relieve pressure, or replace it. The external mouse already proved the system pointer works.",
     "A fuser is a printer part. It does not move a cursor.",
     "DNS resolves names. It does not drift a pointer.",
     "Printer firmware does not calibrate a laptop trackpad."]))

Q.append(item(P, 113, "5.5", "medium",
    "A phone drops from 80 percent to 5 percent in a few minutes and then shuts off, even with the screen dim. Battery health in the settings is marked poor. What should be replaced?",
    ["The battery", "The SIM card, because health is a cellular setting", "The screen protector only", "The headphone jack as the power source"],
    0,
    "A sudden percentage cliff plus a poor-health reading is a worn battery that can no longer hold a charge. Replace it with the correct part and recycle the old one. The SIM identifies the subscriber. A screen protector and the headphone jack do not store the charge.",
    ["Replace the battery. The health reading and the cliff agree.",
     "The SIM is identity and network access. It does not store the battery percentage.",
     "A protector is plastic on the glass. It does not hold current.",
     "The headphone jack is not the battery. Replacing it will not make the percentage stay at 80."]))

Q.append(item(P, 114, "5.6", "easy",
    "Lines appear on copies only when the automatic document feeder is used. Flatbed copies of the same page are clean. What should be cleaned?",
    ["The narrow ADF glass strip", "The laser fuser", "The DHCP scope", "The toner, because the flatbed is also dirty"],
    0,
    "The ADF has its own thin glass strip. A mark there is scanned into every fed page and never touches a flatbed copy. Clean that strip. The fuser and the toner would mark computer prints and flatbed copies too. DHCP is unrelated.",
    ["Clean the ADF glass. The flatbed result already proved the rest of the scanner and the printer are fine.",
     "The fuser would smear printed output from every source, not only the feeder.",
     "DHCP only hands out addresses. It does not draw lines on copies from the feeder.",
     "The flatbed copies are clean, so the toner is not drawing this line."]))

Q.append(item(P, 115, "5.6", "medium",
    "A laser printer feeds several sheets at once and then jams. The pickup roller looks glossy. Which maintenance part is worn?",
    ["The separation pad or the pickup roller", "The formatter's IP address", "The scanner lamp", "The Ethernet cable"],
    0,
    "A glossy pickup roller no longer grips one sheet, and a worn separation pad no longer holds the rest of the stack back. The result is multifeed and jams. Replace those wear items. The IP address, the scanner lamp, and the network cable do not separate paper.",
    ["The pickup and the separation pad are the paper-handling parts that match a glossy roller and a multifeed.",
     "An IP address does not grab extra sheets.",
     "The scanner lamp lights a copy. It does not feed the printer tray.",
     "The cable delivers jobs. It does not change roller friction."]))

Q.append(item(P, 116, "5.6", "medium",
    "Jobs sit in the Windows queue and nothing comes out. The printer is online, and a direct test print from the printer's panel works. What should be restarted?",
    ["The Print Spooler service, and clear any stuck job", "The CMOS battery", "The DHCP relay on a different subnet with no evidence", "The laptop inverter"],
    0,
    "A panel test print proves the printer can mark paper. A stuck Windows queue points at the spooler on the PC or the print server. Restart the Print Spooler service and delete the jammed job. The CMOS battery, a relay, and an inverter are not holding the queue.",
    ["Restart the spooler and clear the stuck document. The printer itself already passed its own test.",
     "The CMOS battery keeps the clock. It does not store print jobs.",
     "A DHCP relay is an addressing feature. Nothing here says addresses are failing.",
     "An inverter lights an old laptop screen. It does not queue prints."]))

Q.append(item(P, 117, "5.6", "hard",
    "A laser page shows a faint copy of the previous page's image. The printer has been doing this on every job today. Which part is failing to clear the drum?",
    ["The cleaning stage, often the cleaning blade or a worn drum", "The pickup roller's gloss", "The NIC", "The paper tray size sensor only"],
    0,
    "After the image is transferred, the drum has to be cleaned before the next page. A ghost of the previous page means that cleaning failed, or the drum is worn. The imaging process ends with cleaning for this reason. A glossy pickup roller multifeeds. The NIC and the tray sensor do not leave a ghost image.",
    ["Ghosting points at the cleaning blade or the drum. Replace the cartridge or the drum.",
     "A pickup roller problem grabs extra paper. It does not reprint the last image faintly.",
     "The NIC moves packets. It does not wipe the drum.",
     "The size sensor selects a tray. It does not leave toner from the previous page."]))

Q.append(item(P, 118, "5.6", "easy",
    "An impact printer produces faint characters on multipart forms. There is no toner cartridge. What supply is worn out?",
    ["The ribbon", "The laser fuser", "The inkjet head", "The thermal paper"],
    0,
    "Impact printers strike a ribbon against the form. A faint multipart form means the ribbon is exhausted or dried out. There is no toner, no inkjet head, and no thermal paper in this design. Replacing the ribbon is the maintenance step.",
    ["Replace the ribbon. Impact printing has nothing else to put ink on the form.",
     "A fuser belongs to a laser printer. This device has no toner to melt.",
     "An inkjet head is a different technology. An impact printer does not have one.",
     "Thermal paper would be blank without a ribbon in an impact printer, and this printer uses forms, not thermal rolls."]))

Q.append(item(P, 119, "5.6", "medium",
    "A trainee has the seven laser-printer stages on flash cards and needs them in the order the page actually takes. Which order is the laser imaging process?",
    ["Processing, charging, exposing, developing, transferring, fusing, cleaning", "Fusing, cleaning, processing, exposing, charging, developing, transferring", "Charging, fusing, processing, cleaning, exposing, developing, transferring", "Developing, processing, fusing, charging, exposing, transferring, cleaning"],
    0,
    "The page is processed into a raster, the drum is charged, the laser exposes the image, toner develops it, the image transfers to paper, the fuser melts it, and the drum is cleaned for the next page. If you remember that fusing is near the end and cleaning is last, the earlier steps fall into place: you cannot develop toner onto a drum you have not charged and exposed.",
    ["That is the process order. Processing first, cleaning last, fusing just before the clean.",
     "Fusing and cleaning are the end, not the beginning. Paper cannot be fused before it has an image.",
     "Fusing before the image exists does not make sense, and charging is not after cleaning.",
     "Developing cannot lead the list. The drum has not been charged or exposed yet."]))

Q.append(item(P, 120, "5.7", "easy",
    "A PC shows 169.254.5.9 and cannot reach the internet. Other PCs on the same switch are fine. What does the address mean, and what is a reasonable first configuration check?",
    ["DHCP failed for this PC. Confirm it is set to obtain an address and that its port can reach the server", "The address is a public web server and the PC is fine", "169.254 means the DNS server is authoritative", "The PC is running RAID 1"],
    0,
    "169.254 is APIPA. This PC did not get a lease. If neighbors did, the DHCP server exists, so check this PC's setting, cable, port VLAN, and whether a firewall on the PC is irrelevant to DHCP. It is not a public address, not a DNS statement, and not a disk array.",
    ["APIPA plus healthy neighbors narrows it to this PC's path to a working DHCP server.",
     "169.254 is not a public address and is not routed to the internet.",
     "The address does not say anything good about DNS. The PC never got that far.",
     "RAID is storage. It does not assign 169.254."]))

Q.append(item(P, 121, "5.7", "hard",
    "Users can browse by IP address and cannot browse by name. Ping to 8.8.8.8 works. Ping to a name fails. What is the fault?",
    ["DNS", "The default gateway, because IP ping already failed", "The NIC, because a numeric ping worked", "The subnet mask, because names and numbers use different masks"],
    0,
    "Numbers working and names failing is DNS. The gateway is fine, because a public IP answered. The NIC is fine for the same reason. Masks do not have a separate value for names. Check the configured DNS server, and check whether that server can resolve.",
    ["DNS is the missing translation from name to number. The numeric path already works.",
     "The gateway test succeeded. A public address replied, so the gateway is not the broken piece.",
     "The NIC carried the numeric ping. Replacing it ignores the evidence.",
     "There is one mask. Names do not get a different one."]))

Q.append(item(P, 122, "5.7", "medium",
    "A laptop on the conference-room Wi-Fi shows full signal and no internet. A browser immediately asks the user to accept a network policy. What is between the user and the internet?",
    ["A captive portal", "A failed fuser", "A RAID rebuild", "A missing CMOS battery"],
    0,
    "A captive portal intercepts the first web request until the user accepts or signs in. Full signal only means the radio associated. It does not mean the portal has been satisfied. A fuser, a RAID set, and a CMOS battery do not insert a policy page.",
    ["Open the page, accept or sign in, and the internet path should follow. The radio is already up.",
     "A fuser is in a laser printer. It does not gate Wi-Fi.",
     "A RAID rebuild is a disk task. It does not present a policy page.",
     "The CMOS battery keeps a clock on a motherboard. It is not the conference-room login."]))

Q.append(item(P, 123, "5.7", "hard",
    "A link light on a switch port flaps every few seconds. A known-good PC was moved to this port and the flap followed the port, not the PC. A different patch cord stops the flap. What was at fault?",
    ["The patch cord", "The PC's NIC, which was proven good", "DNS", "The printer driver on a server"],
    0,
    "The flap followed the port until the cord was changed, and the known-good PC ruled out the NIC. The cord is the failed part. DNS and a printer driver do not toggle a link light. If a new cord had not helped, the next suspect would have been the switch port itself.",
    ["Replace the patch cord. The test already isolated it: good PC, bad behavior, new cord, stable link.",
     "The known-good PC moved the symptom off itself. The NIC is not the flap.",
     "DNS does not drop link. Link is electrical or optical.",
     "A printer driver does not bounce a switch port's link light."]))

Q.append(item(P, 124, "5.7", "medium",
    "Voice calls over the office Wi-Fi break up. A speed test shows plenty of megabits, and the delay swings wildly. Wired desks do not have the problem. What is the impairment, and what is a reasonable change?",
    ["Jitter on the wireless. Prefer wired phones or improve the wireless with less interference and proper QoS", "Zero bandwidth, because the speed test was high", "A bad fuser", "APIPA on phones that have working addresses"],
    0,
    "Jitter is delay that keeps changing, and voice suffers even when a speed test looks fine. Wireless contention is a common source. Put desk phones on Ethernet where you can, and treat the wireless with a cleaner channel plan and voice prioritization. The speed test already disproves 'no bandwidth.' A fuser and APIPA are the wrong symptoms.",
    ["Jitter is the swing. Move voice off a busy radio or engineer the radio so voice is not waiting on bulk traffic.",
     "The speed test showed capacity. The problem is variation, not a zero-megabit link.",
     "A fuser smears toner. It does not break up a call.",
     "APIPA would mean the phones had no lease. The stem says calls are happening, just badly."]))

Q.append(item(P, 125, "5.7", "medium",
    "A SOHO user on a satellite link complains that web pages load but every click in a remote desktop feels late. The installer offers a faster plan with the same satellite technology. What should the technician explain?",
    ["The delay is latency from the satellite path. More megabits will not remove the distance", "A faster plan removes the orbit", "Satellite latency means the HDMI cable is too long", "The remote desktop needs a new fuser"],
    0,
    "Satellite latency comes from the distance the signal travels. A bigger download number does not move the satellite closer, so the remote desktop will still feel late. This is a reason to prefer a terrestrial link for that application. HDMI and a fuser are not in the path.",
    ["Explain the latency. If the work depends on snappy clicks, satellite is the wrong access type regardless of the speed tier.",
     "The orbit stays. Bandwidth and latency are different limits.",
     "HDMI is a local video cable. It does not add orbital delay.",
     "A fuser is a printer part. It does not sit on the satellite path."]))

if __name__ == "__main__":
    from common import dump
    dump("220-1101", {"q-d5.json": Q})
