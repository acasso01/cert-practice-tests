"""Original 220-1102 questions that do not restate the existing bank."""

from common import PROBLEMS, dump, item
from gate import collisions

P = "c2"
Q = []


def add(*args):
    Q.append(item(P, *args))


add(149, "1.4", "easy",
    "A laptop on battery is capped at a slow clock. Plugged in, the user wants full speed, and the current plan is Power saver. Where is that plan changed?",
    ["Power Options", "Mouse settings", "The credential manager", "Indexing Options"],
    0,
    "The power plan sets how aggressive the CPU is on battery and on AC. Power Options is where that plan is selected. The mouse, stored passwords, and the search index do not set the CPU cap.",
    ["Open Power Options and pick a plan that allows full speed on AC.",
     "Mouse settings do not change the processor power cap.",
     "Credential Manager stores secrets. It does not pick a power plan.",
     "Rebuilding the index does not raise a CPU that Power saver has capped."])

add(150, "1.5", "medium",
    "A PC has missed a month of patches. Windows Update shows updates are paused until a date next month. What should the technician do?",
    ["Resume updates and let the pending patches install", "Leave the pause because paused PCs are safer", "Delete the user profile to unpause updates", "Format the disk"],
    0,
    "A pause is a deliberate delay, not a successful patch cycle. Resume updates. Staying paused, rebuilding a profile, or formatting the disk does not install the missing fixes.",
    ["Resume the pause. The date on the screen is why the month was skipped.",
     "A paused PC is missing fixes. That is less safe, not more.",
     "The profile is not what paused Windows Update.",
     "Formatting is not how you end an update pause."])

add(151, "1.7", "medium",
    "A standard user runs an installer and it fails while writing under Program Files. An administrator account on the same PC can complete the same installer. What is the constraint?",
    ["The standard user may not write in Program Files", "The PC has no CPU", "The display is unplugged", "Program Files only accepts Linux packages"],
    0,
    "Program Files is protected. A standard user can install per-user apps and cannot write that directory. An administrator can. The CPU and the display are working if the installer got that far, and Windows is not rejecting the file for being a Linux package in this story.",
    ["Have an administrator install it, or use a per-user install. The right is the missing piece.",
     "The installer opened and failed on a folder. The CPU is present and working.",
     "The user could see the error. The display is connected.",
     "The failure is a Windows permission, not a Linux package format."])

add(152, "1.8", "easy",
    "A Linux server is handed a Windows setup.exe and told to run it natively to install a Windows-only service. What happens?",
    ["It will not run, because the binary is built for Windows", "Linux runs every .exe natively", "The file becomes a kernel module because of its name", "The server converts it into a shell script automatically"],
    0,
    "An .exe built for Windows needs a Windows environment. Linux does not run it just because the file was copied over. The extension does not make it a kernel module or a shell script.",
    ["Use a Windows host for that installer. The Linux server is the wrong operating system.",
     "Linux does not treat a Windows executable as a native program.",
     "The name .exe does not make a file a Linux kernel module.",
     "Nothing in the copy rewrites the binary into a shell script."])

add(153, "1.9", "medium",
    "A user is moving to a new PC. Accounting wants the profile, documents, and application settings moved, not a photograph of the old desktop. Which tool family does that migration?",
    ["User State Migration Tool", "A screenshot pasted into a slide", "A BIOS beep code", "A toner cartridge"],
    0,
    "The User State Migration Tool captures a profile and puts it on the new computer. A screenshot does not move settings. Beep codes diagnose hardware. A toner cartridge prints. None of those migrate a profile.",
    ["USMT is built to move user state from one PC to another.",
     "A screenshot leaves the real files on the old disk.",
     "A BIOS beep code diagnoses hardware. It does not copy a user profile.",
     "A toner cartridge prints pages. It does not capture or restore a user profile."])

add(154, "1.10", "medium",
    "Spotlight on a Mac cannot find files that are sitting in Documents. Documents is listed under Spotlight privacy exclusions. What should change?",
    ["Remove Documents from the Spotlight exclusion list", "Empty the Trash as the only search index", "Turn on the firewall and leave the exclusion", "Rename the Mac"],
    0,
    "Spotlight will not index a folder the user excluded. Take Documents off that list and let it index. The Trash, the firewall, and the computer name do not restore an excluded folder to the index.",
    ["Remove the exclusion. Spotlight was told to ignore that folder.",
     "Emptying the Trash does not put the Documents folder back into the Spotlight index.",
     "The firewall does not add a folder back into Spotlight.",
     "Renaming the Mac does not remove a folder from the Spotlight privacy list."])

add(155, "1.11", "medium",
    "An Ubuntu server needs its packages refreshed from the distribution repositories. The technician types a Windows command and gets 'command not found'. Which tool belongs on this server?",
    ["apt", "winver", "diskpart", "The Microsoft Store"],
    0,
    "Debian and Ubuntu use apt to refresh and install packages. winver and diskpart are Windows tools. The Microsoft Store is not the package manager on this server.",
    ["Use apt on Ubuntu. That is the package tool the distribution ships.",
     "winver is a Windows dialog. The shell already said the command is missing.",
     "diskpart partitions disks on Windows. It does not refresh apt repositories.",
     "The Store is a Windows app channel, not this server's package manager."])

add(156, "1.5", "easy",
    "A user changed the display language and cannot find the control to change it back. Which Windows app area holds language and region?",
    ["Settings, under Time and language", "The BIOS fan curve", "The printer's toner menu", "The monitor's color OSD only"],
    0,
    "Windows language and region live in Settings. The firmware fan curve, the toner menu, and a monitor OSD do not switch the Windows display language.",
    ["Open Time and language in Settings and add or select the language.",
     "A firmware fan curve controls cooling. It does not change the Windows display language.",
     "The toner menu reports a cartridge. It does not install a Windows language.",
     "The monitor OSD changes the panel, not the operating-system language."])

add(157, "2.2", "medium",
    "Guest wireless must not let one guest open a share on another guest's laptop. The company SSID is a different network. What should be enabled on the guest SSID?",
    ["Client isolation", "WPS with the printed PIN", "A shared key printed on the lobby wall", "A hidden SSID and no passphrase"],
    0,
    "Client isolation, or AP isolation, stops wireless clients on that SSID from talking to each other. WPS, a posted key, and a hidden name with no passphrase do not separate the guests.",
    ["Turn on client isolation for the guest SSID.",
     "A WPS PIN is a weak join method. It does not separate clients.",
     "A key on the wall publishes the secret. It does not isolate clients.",
     "Hiding the name without a passphrase makes the network easier, not safer."])

add(158, "2.3", "medium",
    "A console shows the last antivirus definition update was 400 days ago. A scan today reports a clean PC. How much trust does that scan deserve?",
    ["Little, until the definitions are current and the scan is repeated", "Complete trust, because any scan is final", "None of the files need definitions if the screen is green", "Trust it more because the definitions are older"],
    0,
    "A scanner only recognizes what its definitions describe. A year-old database misses a year of malware. Update the definitions and scan again before you call the PC clean.",
    ["Update first, then scan. The green result used an obsolete database.",
     "A scan is only as current as its definitions. Age matters.",
     "The green screen was produced by old definitions. It is not proof.",
     "Older definitions recognize less, not more."])

add(159, "2.4", "medium",
    "A finance director receives a mail that uses private project names and asks for a same-day wire. The address is one letter off the real vendor. What is that targeted mail?",
    ["Whaling, a spear-phishing attempt on an executive", "A routine all-staff newsletter", "A distributed denial of service", "A BIOS update"],
    0,
    "Whaling aims spear phishing at a senior person, often with real details and a payment ask. A newsletter does not demand a wire from a lookalike domain. A traffic flood and a BIOS update are not this message.",
    ["Treat it as whaling. Do not wire from a lookalike message.",
     "A newsletter does not ask an executive for a same-day wire.",
     "A denial of service floods a service. It does not send one mail.",
     "Nothing in the message is a firmware update."])

add(160, "2.6", "easy",
    "Users plug in found USB drives. Policy says the PC must not run content from those drives automatically. Which control matches?",
    ["Disable AutoPlay for removable media", "Turn AutoPlay on for every drive", "Email unknown executables to the whole company", "Write the local admin password on the drive"],
    0,
    "AutoPlay is how a USB drive starts something the moment it is inserted. Turn that off for removable media. Enabling it, mailing the files, or labeling the drive with an admin password spreads the risk.",
    ["Disable AutoPlay. Insertion should not execute anything.",
     "Turning AutoPlay on is the behavior the policy forbids.",
     "Mailing unknown executables is how the drive's contents travel further.",
     "An admin password on the drive is a credential leak, not a control."])

add(161, "2.7", "medium",
    "A company phone shows the subject lines of new mail on the lock screen. People standing nearby can read them. Which change stops that preview?",
    ["Hide notification content on the lock screen", "Turn the screen brightness to maximum", "Disable the PIN so the phone opens faster", "Forward every mail to an unlocked public mailbox"],
    0,
    "Lock-screen previews are a setting. Hide the content so a locked phone shows that mail arrived and not what it says. Brighter text, no PIN, and a public mailbox make the exposure worse.",
    ["Hide the content. The mail can still arrive without being readable by the room.",
     "More brightness makes the preview easier to read, not harder.",
     "Removing the PIN removes the lock the preview was sitting on.",
     "A public mailbox is a second copy of the same exposure."])

add(162, "2.8", "hard",
    "A drive failed so badly that a wipe utility cannot see it, and the data on it was confidential. Degaussing is not available. What destruction method still fits?",
    ["Physical destruction, such as shredding the platters", "A quick format that the drive cannot perform", "Putting it in the trash intact", "Renaming the volume"],
    0,
    "If the disk will not take a wipe, you destroy the media. A quick format cannot run on a drive the utility cannot see. Trash and a rename leave the platters readable by someone else.",
    ["Shred or otherwise destroy the platters, then keep the certificate.",
     "A format needs a drive the software can address. This one does not.",
     "An intact drive in the trash can still be read. That is not destruction.",
     "Renaming a volume leaves the platters readable. It is not destruction."])

add(163, "2.9", "medium",
    "A small-office router still has WPS enabled, and the PIN is printed on the bottom where visitors sit. What should change?",
    ["Turn WPS off and use a long WPA2 or WPA3 passphrase", "Turn WPS on a second time", "Publish the PIN on the guest portal", "Set the admin password to the WPS PIN"],
    0,
    "WPS PINs are short and are often brute-forced, and a printed PIN is already disclosed. Disable WPS and use a long passphrase. Repeating WPS, posting the PIN, or reusing it as the admin password keeps the weakness.",
    ["Disable WPS. The printed PIN is not a secret anymore.",
     "Enabling it again does not remove the PIN on the sticker.",
     "A portal that shows the PIN gives it to every guest.",
     "The admin password should not be the same short PIN."])

add(164, "2.10", "easy",
    "A browser tab the user did not open says the computer is infected and to call a toll number. No company security tool produced the page. What should the user do?",
    ["Close the site and do not call. Tell the help desk if it returns", "Call the number and buy the cleaner they sell", "Disable the browser's pop-up blocker", "Install the extension the page offers"],
    0,
    "A scare page with a phone number is a support scam, not an operating-system alert. Close it. Calling, allowing more pop-ups, or installing their extension is how the scam gets paid or gets a foothold.",
    ["Close it. A real company alert does not arrive as a random page with a toll number.",
     "The number belongs to the scam. Paying them does not clean anything.",
     "Turning off the pop-up blocker makes the next scare page easier.",
     "The extension is the payload the page is selling."])

add(165, "3.1", "medium",
    "A line-of-business app says its Windows service is not running. services.msc shows that service as Stopped and Startup type Disabled. What is the repair?",
    ["Set the service to Automatic or Manual and start it", "Delete the system32 folder", "Disable every other service", "Format the volume that holds the user profile"],
    0,
    "A disabled service will not start with the PC, and a stopped service is not serving the app. Set an appropriate startup type and start it. Deleting system files, stopping everything else, or formatting the profile destroys the PC to avoid one service.",
    ["Enable and start the service the application named.",
     "system32 is the operating system. Deleting it is not a service start.",
     "Other services are not the one the app asked for.",
     "The profile volume is not why this service is disabled."])

add(166, "3.2", "hard",
    "Only the company bank site resolves to a strange address. Other names resolve normally. The hosts file contains a line for that bank pointing at the strange address. What is the cause?",
    ["The hosts file is overriding DNS for that one name", "The monitor is color-blind", "The mouse polling rate", "A paused print queue"],
    0,
    "The hosts file is consulted before DNS and can pin one name to an attacker's address. Remove the line and find out how it was written. The monitor, the mouse, and the print queue do not rewrite one name.",
    ["Delete the bad hosts line and investigate how it arrived.",
     "Color vision does not change a DNS answer.",
     "The mouse rate does not insert a hosts entry.",
     "A print queue does not override one website name."])

add(167, "3.3", "medium",
    "The malware scan is clean, System Restore is back on, and a new restore point exists. The user is about to take the laptop. Which best-practice step is still left?",
    ["Educate the user on how the malware arrived and how to avoid a repeat", "Reconnect it to the network before the scan", "Create a restore point of the infected state", "Disable the antivirus to speed the next login"],
    0,
    "Education is the last malware-removal step, after the machine is clean and restore is healthy again. Reconnecting early, snapshotting the infection, and disabling the antivirus undo the work.",
    ["Tell the user what to stop doing. That is the remaining step.",
     "The network comes back after quarantine and cleanup, not before the scan.",
     "A restore point of the infection is what you avoided by disabling restore earlier.",
     "Turning the antivirus off is how the next sample lands."])

add(168, "3.4", "medium",
    "A phone sits on the vendor logo and reboots to the same logo after an OS update was interrupted. What is the sensible recovery path?",
    ["Use the vendor recovery mode to retry or reinstall the OS", "Keep rebooting until the logo changes by luck", "Drill the charging port", "Throw away the SIM and hope the OS returns"],
    0,
    "A boot loop after a broken update is a firmware or OS recovery problem. The vendor's recovery mode can retry the update or reinstall. Random reboots, a damaged port, and removing the SIM do not rewrite the OS.",
    ["Follow the vendor's recovery steps. The update did not finish.",
     "More reboots repeat the same broken boot.",
     "The charging port is not the interrupted update.",
     "The SIM is not the operating system that failed to start."])

add(169, "3.5", "medium",
    "A user installed a configuration profile from a text message so a free app would work. The phone now trusts a strange VPN. What should be removed?",
    ["The untrusted configuration profile", "The phone's legitimate mail profile that IT installed", "The screen lock", "The SIM tray"],
    0,
    "A profile from a text can install a VPN or a certificate the user never meant to trust. Remove that profile. The company mail profile, the lock, and the SIM are not the thing the message added.",
    ["Delete the profile the message installed, then change the account passwords.",
     "The company mail profile is not the text-message VPN.",
     "The screen lock is a control. Removing it does not remove the VPN.",
     "The SIM tray is hardware. The profile is software."])

add(170, "3.1", "easy",
    "Boot is slow. Task Manager's Startup tab shows a heavy updater set to launch at sign-in, and the user does not need it every morning. What is a reasonable change?",
    ["Disable that startup item and confirm the next boot", "Disable every Microsoft service", "Delete the user hive", "Turn off the disk"],
    0,
    "Startup apps are a common reason a healthy PC boots slowly. Disable the one heavy item and see if boot improves. Disabling Microsoft services, deleting the hive, or powering off the disk is not a startup cleanup.",
    ["Turn off the unneeded startup item and measure the next boot.",
     "Microsoft services are not the single updater on the Startup tab.",
     "The user hive is the profile. Deleting it is not how you disable one app.",
     "A disk that is off does not boot faster. It does not boot."])

add(171, "4.1", "easy",
    "A laptop is handed to a new hire. The asset list has no record of the serial number or who holds it. What should be recorded before it leaves the cage?",
    ["The asset tag or serial, the assignee, and the date", "Only the wallpaper color", "The user's personal email password", "Nothing, because assets track themselves"],
    0,
    "An asset record says what the device is, who has it, and when. Wallpaper is not an inventory. A personal password does not belong in an asset system. Devices do not inventory themselves.",
    ["Record the identifier, the person, and the date. That is the asset entry.",
     "Wallpaper is not an asset attribute you can audit.",
     "A personal password is a secret, not an inventory field.",
     "If nobody writes it down, the cage cannot say who has the laptop."])

add(172, "4.4", "medium",
    "A laser printer just jammed. The fuser is hot enough to burn, and the user wants the page pulled immediately. What should the technician do?",
    ["Wait until the fuser cools, then clear the jam", "Grab the metal fuser while it is still at operating temperature", "Spray water into the fuser", "Keep printing so the next page pushes the jam"],
    0,
    "A fuser is a burn hazard right after printing. Let it cool, then remove the paper. Grabbing it, adding water, or forcing more pages risks a burn and more damage.",
    ["Give the fuser time to cool. Then pull the jammed page.",
     "The metal is at fusing temperature. Grabbing it is how people get burned.",
     "Water in a hot fuser is a shock and a damage risk.",
     "Another page driven into a jam makes the jam worse."])

add(173, "4.5", "medium",
    "A server-room thermometer reads 95 F and the cooling unit has failed. Equipment is still running. What is the environmental priority?",
    ["Restore cooling or shut equipment down before heat damage", "Add more servers to warm the room evenly", "Open every chassis and leave the fans unplugged", "Cover the intake vents to keep dust out"],
    0,
    "95 F and a dead cooler is an overheat in progress. Restore cooling or power gear down in an orderly way. More heat, unplugged fans, and blocked intakes make it worse.",
    ["Get the temperature down. That is the failure in front of you.",
     "More servers add heat the room cannot remove.",
     "Chassis need their fans. Unplugging them removes the remaining cooling.",
     "Covered intakes starve the equipment of air."])

add(174, "4.6", "hard",
    "A drive may contain evidence. A manager asks the technician to browse the files and email the interesting ones before anyone logs custody. What should the technician do instead?",
    ["Stop and follow evidence handling, including chain of custody", "Browse it on a home PC over the weekend", "Quick-format it so the files are tidy", "Post a sample of the files in a team chat"],
    0,
    "Evidence handling means you do not go fishing through the disk and you can show who had it. Browsing at home, formatting, or posting samples destroys the custody and can destroy the evidence.",
    ["Stop. Custody and the incident process come before curiosity.",
     "A home PC is not a controlled evidence environment.",
     "A quick format is destruction, not preservation.",
     "A team chat is disclosure, not a case file."])

add(175, "4.8", "medium",
    "A repetitive file cleanup must run on a Linux server every night. The author starts the file with a bash shebang. Which kind of script is that?",
    ["A shell script", "A PowerShell script that Linux runs because of the shebang", "A BIOS macro", "A spreadsheet"],
    0,
    "A bash shebang marks a shell script. PowerShell is a different language and is not what that shebang invokes. The BIOS and a spreadsheet do not run the nightly cleanup.",
    ["The shebang selects the shell. That is a shell script.",
     "PowerShell does not start because a bash shebang is present.",
     "The BIOS does not run a nightly file cleanup script.",
     "A spreadsheet does not have a bash shebang."])

add(176, "4.9", "hard",
    "A user must approve a view of their screen before a technician can see it, and the technician must not have an unattended login. Which remote-support model matches?",
    ["Remote assistance that waits for the user's consent", "An always-on RDP session with a shared password", "Telnet to the user's desktop", "A VNC listener with no password"],
    0,
    "Remote assistance and Quick Assist style tools show the screen after the user agrees, and they do not leave an unattended back door. A shared RDP password, Telnet, and an open VNC listener fail that requirement.",
    ["Use the consent-based assist tool. The user stays in control of the session.",
     "A shared always-on login is unattended access. The stem forbids it.",
     "Telnet is clear text and is not a consented screen share.",
     "VNC with no password is an open console."])

if __name__ == "__main__":
    found = collisions("220-1102", Q)
    if PROBLEMS or found:
        raise SystemExit("\n".join(PROBLEMS + found))
    dump("220-1102", {"q-fresh.json": Q})
