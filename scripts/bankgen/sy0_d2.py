from common import item

P = "sy0"
Q = []

def add(*args):
    Q.append(item(P, *args))

add(20, "2.1", "easy",
    "A well-funded group quietly steals aircraft designs over many months and shows no interest in a ransom. The activity aligns with a government's intelligence goals. Which actor fits best?",
    ["A nation-state", "An unskilled attacker looking for an easy public server", "A hacktivist defacing a website for publicity", "Shadow IT, a team inside the company that bought a cloud tool"],
    0,
    "Nation-states have funding, patience, and an espionage motive. Quiet theft of designs over months matches that more than a loud defacement, a quick opportunistic scan, or an employee who signed up for an unsanctioned app. Shadow IT is a governance problem. It is not a foreign intelligence service.",
    ["Espionage, patience, and resources point at a nation-state. Ransom was never the goal.",
     "An unskilled attacker typically uses well-known tools against easy targets and does not run a months-long design theft.",
     "Hacktivists want attention for a cause. A quiet theft with no manifesto is a poor fit.",
     "Shadow IT is unsanctioned technology inside the organization. It does not describe a foreign theft of aircraft designs."])

add(21, "2.1", "medium",
    "An employee with legitimate access copies the customer database onto a personal drive the week after a poor performance review. No external malware is found. Which actor and motivation fit?",
    ["An insider, with revenge or personal gain as a plausible motivation", "A nation-state that had no access and no account", "Organized crime that brute-forced the front door with no credentials", "An unskilled attacker with no relationship to the company"],
    0,
    "An insider already has an account and a reason to be on the network. The timing with the review suggests revenge, and the copy suggests personal gain or a handoff. The absence of malware matters: the abuse used real access. The other choices require an outsider who was not needed for this story.",
    ["The employee is the insider. The review and the copy are the motive and the action.",
     "A nation-state story would not start with a local performance review and a personal drive.",
     "No brute force was required. The account was already valid.",
     "An outsider with no relationship does not match a person who already had the database rights."])

add(22, "2.1", "medium",
    "A criminal group encrypts a hospital's files and demands payment. The operation looks like a business: affiliates, a payment site, and a support chat for victims. What is the best actor and motivation pair?",
    ["Organized crime motivated by financial gain", "A hacktivist motivated by a public political statement and no payment", "Shadow IT motivated by convenience", "An ethical researcher who stops when asked"],
    0,
    "Organized crime runs extortion as a business. Ransomware with affiliates and a payment flow is financial. Hacktivists want a message more than a invoice. Shadow IT is unsanctioned internal tech. An ethical researcher works under rules and does not encrypt a hospital for ransom.",
    ["The payment demand and the business-like operation are organized crime seeking money.",
     "A political defacement without a ransom would fit hacktivism better. This story is a bill.",
     "Shadow IT is someone installing Dropbox, not a crew encrypting a hospital.",
     "Ethical research is authorized and stops at the agreed boundary. Extortion is the opposite."])

add(23, "2.1", "easy",
    "Marketing buys a cloud design tool on a credit card. IT and security never reviewed it, and customer artwork is now stored there. What is that practice called?",
    ["Shadow IT", "A nation-state intrusion", "A hardware keylogger", "A tabletop exercise"],
    0,
    "Shadow IT is technology the business adopts outside the approved process. The risk is data in a place with no review of identity, retention, or the vendor. It is not proof of a nation-state, a physical logger, or a planned exercise. The fix is to find it, decide whether to sanction it, and bring it under policy.",
    ["Unreviewed cloud use is shadow IT. The artwork is now outside the controls IT thought it had.",
     "A nation-state is an external actor. This started with a credit card in marketing.",
     "A keylogger is a device or program that records keystrokes. A design subscription is not one.",
     "A tabletop is a discussion exercise. Nobody scheduled this purchase as a drill."])

add(24, "2.1", "hard",
    "Two incidents look similar in the logs, but the responders disagree about sophistication. One used a single well-known phishing kit against a public webmail portal and gave up after a lockout. The other maintained access for months, moved between internal systems, and avoided noisy tools. Which comparison is fair?",
    ["The first is a less sophisticated, likely opportunistic effort. The second shows higher capability and patience",
     "Both are unskilled because both wanted access",
     "The months-long intrusion is less sophisticated because it was quiet",
     "Sophistication cannot be discussed without naming a country"],
    0,
    "Capability shows up in how long the actor stays, whether they adapt, and whether they are noisy. A kit and a quick lockout is low sophistication. A quiet, patient move through internal systems is higher. Quiet is not the same as unskilled. You can describe sophistication without attributing a nation.",
    ["The kit-and-quit attempt is the lower-capability case. The long internal activity is the higher one.",
     "Wanting access is not a sophistication rating. Almost every actor wants access.",
     "Quiet, sustained access is a sign of skill and planning, not of a lack of it.",
     "Attribution to a country is a separate question. Capability can be described from the behavior."])

add(25, "2.2", "easy",
    "An email pretends to be the CEO and asks finance to wire money today and not to call. A second case is a text message with a link that looks like the bank. What are the two vectors? (Choose two.)",
    ["Business email compromise, a form of phishing", "Smishing, phishing by text message", "A missing bollard", "A RAID rebuild"],
    [0, 1],
    "Business email compromise is a targeted payment fraud that arrives as email, often impersonating an executive. Smishing is the same kind of lure over SMS. Both are message-based social engineering. A bollard and a RAID rebuild are physical and storage topics.",
    ["The wire request impersonating the CEO is business email compromise, which rides on phishing.",
     "A texted bank link is smishing. The channel is the short message.",
     "A bollard stops vehicles. It does not send email.",
     "A RAID rebuild repairs disks. It is not a message vector."])

add(26, "2.2", "medium",
    "Attackers register a domain one letter off from the company's payroll site and host a lookalike login there. Employees who mistype the address enter credentials. What is that technique called?",
    ["Typosquatting", "A watering-hole compromise of a site the employees already trust", "Shoulder surfing", "Tailgating"],
    0,
    "Typosquatting relies on a near-miss name. The user makes the error and lands on the attacker's site. A watering hole is a site the victims already use, compromised so the real audience gets hit. Shoulder surfing watches a screen. Tailgating follows someone through a door. None of those is a lookalike domain.",
    ["The misspelled domain is typosquatting. The trap is the name, not a hacked legitimate server.",
     "A watering hole is the real site people meant to visit. Here the site itself is the fake.",
     "Shoulder surfing is looking over a shoulder at a screen or a keypad.",
     "Tailgating is a physical follow-through at a door."])

add(27, "2.2", "medium",
    "A contractor finds a network device still using the vendor's admin password and an old protocol exposed to the internet. No one sent a phishing email. Which attack surface is this?",
    ["Default credentials and an exposed service", "Vishing", "A honeyfile", "A tabletop exercise"],
    0,
    "Default credentials and open management services are a classic exposure. The attacker does not need to trick a person if the device still answers with the manual's password. Vishing is a phone pretext. A honeyfile is a decoy you planted. A tabletop is a meeting.",
    ["The unchanged password and the exposed service are the surface. Close the service and change the credential.",
     "Vishing needs a voice conversation. Nothing was phoned in this story.",
     "A honeyfile is a decoy document. This is a real device with a real default password.",
     "A tabletop does not leave a management port on the internet."])

add(28, "2.2", "hard",
    "A software update from a trusted vendor arrives signed and is installed everywhere. The update later turns out to contain an unauthorized backdoor added before the vendor shipped it. Which vector is this?",
    ["A supply-chain compromise", "Shoulder surfing of the installers", "Smishing of each laptop individually", "Tailgating into each office"],
    0,
    "The supply chain is the path the software took before you installed it. Trust in the vendor and the signature did not help if the vendor's build was the thing that was changed. That is not a person reading screens, a text to each user, or a door in each lobby. The response is to pull the update, preserve evidence, and work the vendor incident. This question does not describe how to insert a backdoor.",
    ["The malicious code arrived inside a legitimate update. That is the supply chain.",
     "Shoulder surfing watches a person. It does not alter a vendor build.",
     "Smishing would be a message to users. The laptops installed a normal update.",
     "Tailgating is physical access at a door. It does not explain a signed vendor package."])

add(29, "2.2", "easy",
    "A USB drive labeled 'salary data' is left in the parking lot. The risk is that someone plugs it into a company PC. Which vector is the drive?",
    ["Removable media", "A voice call", "An open TCP port on a firewall", "A cloud misconfiguration"],
    0,
    "Removable media is a delivery path that bypasses the network perimeter. The label is bait. The control is to disable unnecessary USB storage, train people not to plug in found drives, and investigate the drive on an isolated system if it must be examined. A voice call, a firewall port, and a cloud setting are different surfaces.",
    ["The drive is removable media. The parking lot is just where it was left.",
     "A voice call is vishing or a normal phone call. There is no call in this story.",
     "An open port is a network service. The attack arrives in someone's hand.",
     "A cloud misconfiguration is a console or an API setting. This object is a USB drive."])

add(30, "2.2", "medium",
    "Attackers compromise a news site that engineers read every morning, and only then deliver a malicious script to those visitors. The company's own website is untouched. What is the technique?",
    ["A watering-hole attack", "Typosquatting of the company's own domain", "Dumpster diving", "A brute-force attack on email passwords"],
    0,
    "A watering hole is a site the targets already visit. Compromise that site and you meet them there. Typosquatting would be a lookalike of the company's own name. Dumpster diving is physical trash. Password guessing is not how this story delivers the script.",
    ["The news site is the watering hole. The engineers came to it on their own.",
     "Typosquatting would involve a fake company domain. The news site is real and unrelated in name.",
     "Dumpster diving searches discarded paper and hardware. It is not a compromised news site.",
     "Brute force tries passwords. This delivery was a script from a site they already trusted."])

add(31, "2.3", "easy",
    "A server is missing a patch that the vendor released six weeks ago. A different server is being attacked with a flaw the vendor has never heard of and for which no patch exists. Which is which?",
    ["The first is an unpatched known vulnerability. The second is a zero-day",
     "Both are zero-days because both are dangerous",
     "The unpatched server is a zero-day because six weeks have passed",
     "The unknown flaw is not a vulnerability until a patch exists"],
    0,
    "A zero-day is a vulnerability that is being used before a fix is available, often before the vendor knows. A missing patch for a published flaw is ordinary vulnerability management debt. Age does not turn a known patch into a zero-day. The unknown flaw is a vulnerability now. The lack of a patch is what makes it a zero-day, not what makes it harmless.",
    ["Known bug plus an available patch is unpatched. No patch and active use is the zero-day.",
     "Danger is not the definition. A zero-day is about the absence of a fix and prior knowledge, not about severity alone.",
     "Six weeks of ignoring a published patch is a process failure. The flaw was not unknown on day one.",
     "Attackers can use a flaw before a patch exists. Waiting for the patch to call it real is backwards."])

add(32, "2.3", "medium",
    "A web form builds a database query by gluing the user's typed text into the command. A researcher demonstrates that unexpected input changes which rows come back. No sample payload is needed to classify this. What vulnerability class is it?",
    ["SQL injection", "A hardware failure of the disk", "Shoulder surfing", "A certificate expiration"],
    0,
    "SQL injection is untrusted input treated as part of a database command. The fix is parameterized queries and validation, which is application work, plus a review of database permissions. A disk failure, someone watching a screen, and an expired certificate do not describe this input handling. The classification does not require a working exploit string.",
    ["The query is being built from user text. That is SQL injection, and the repair is in the application.",
     "A failed disk loses availability. It does not change the meaning of a query.",
     "Shoulder surfing is visual. The form is accepting hostile structure, not a glance.",
     "An expired certificate breaks trust in a connection. It is not why the query changed."])

add(33, "2.3", "medium",
    "A guest virtual machine can read memory that belongs to the hypervisor or to another guest. What is that class of failure called?",
    ["VM escape", "A successful snapshot", "Load balancing", "A salt"],
    0,
    "VM escape breaks the boundary the hypervisor is supposed to enforce. It is one of the reasons guest and host patching both matter, and why untrusted code does not belong on the same host as sensitive guests. A snapshot saves state. Load balancing spreads traffic. A salt is a password-hashing value.",
    ["Escape is the guest reaching outside its sandbox. Patch the hypervisor and do not treat the guest boundary as perfect.",
     "A snapshot is a point-in-time copy. It is not a boundary failure.",
     "Load balancing distributes requests. It does not let one guest read another.",
     "A salt is mixed into a password hash. It has nothing to do with hypervisor isolation."])

add(34, "2.3", "hard",
    "An application checks a user's role, then later performs the privileged action. Another request can slip in between those two steps and change the role that is actually used. What vulnerability is that timing window?",
    ["A race condition", "A weak password", "Cross-site scripting stored in a comment field", "An expired CRL"],
    0,
    "A race condition is a flaw that depends on the order or timing of events. Time-of-check to time-of-use is the pattern where the thing you checked is not the thing you use. The fix is to make the check and the use atomic, which is a development problem. A weak password, stored script in a page, and a revocation list are different issues. This question names the window. It does not explain how to win the race.",
    ["The gap between the check and the action is the race. Close the window in code rather than hoping timing stays lucky.",
     "A weak password is an authentication problem. The story is about order of operations.",
     "Stored cross-site scripting is a browser-side script in content other users view. It is not this timing bug.",
     "A CRL is a list of revoked certificates. It does not sit between a role check and an action."])

add(35, "2.3", "easy",
    "A file server still runs an operating system the vendor stopped patching two years ago. It is on the production network because one old application needs it. What vulnerability category is the operating system itself?",
    ["End-of-life, unsupported software", "A zero-day in a fully supported product", "A biometric failure", "A hot site"],
    0,
    "End-of-life software no longer gets fixes. New flaws stay open. The compensating path is to isolate it, limit who can reach it, and plan the replacement. It is not a zero-day in a supported product, not a fingerprint reader, and not a recovery site.",
    ["Unsupported and unpatched by the vendor is end of life. Isolate it and replace it.",
     "A zero-day is an unknown or unfixed flaw in something you could otherwise maintain. This OS will not be maintained at all.",
     "Biometrics are an authentication factor. They are not an old operating system.",
     "A hot site is a ready recovery location. It does not describe the server's patch status."])

add(36, "2.3", "medium",
    "A cloud storage bucket is left readable by anyone on the internet. The files were not stolen by malware on a laptop. The configuration simply allowed anonymous access. What is the vulnerability?",
    ["A misconfiguration", "A hardware keylogger", "A watering hole", "Cross-site scripting in the bucket's encryption"],
    0,
    "Misconfiguration is a correct product used in an unsafe way. Anonymous access on a bucket is the textbook case. The fix is to remove public access, turn on logging, and check whether data was taken. A keylogger, a compromised third-party site, and a script-injection flaw are different causes. Encryption is not what made the bucket public.",
    ["The unsafe setting is the vulnerability. Close the anonymous access and review the access logs.",
     "A keylogger records keystrokes on a device. It did not set the bucket policy.",
     "A watering hole is a site the victims already visit. This is the company's own storage setting.",
     "Cross-site scripting is injected script in a web page. Public read on a bucket is an access-control setting."])

add(37, "2.4", "easy",
    "A user account logs in from New York and, four minutes later, from a country on the other side of the world. The user is in a meeting in New York. What indicator is that?",
    ["Impossible travel", "A normal VPN split tunnel", "A successful backup", "A planned tabletop"],
    0,
    "Impossible travel means two authentications are too far apart in geography for the time between them. It is a reason to challenge or disable the session and contact the user, not to assume the user is lying. A split tunnel, a backup, and a tabletop do not create two distant logins.",
    ["Four minutes is not a flight. Treat the distant login as hostile until the user confirms otherwise.",
     "A split tunnel chooses which traffic uses a VPN. It does not place one person in two countries.",
     "A backup job does not authenticate as the user from another country.",
     "A tabletop is a discussion. It does not create authentication events."])

add(38, "2.4", "medium",
    "CPU use on a server stays near 100 percent. The process is unknown, outbound connections go to a mining pool, and there is no ransom note. What is the most likely activity?",
    ["Cryptomining malware", "A healthy nightly backup", "Full-disk encryption doing its job", "A camera recording the lobby"],
    0,
    "A miner spends compute and talks to a pool. The fan noise and the bill are the symptoms. Isolate the host, identify the process, and follow the malware-removal and incident process. A backup finishes. Disk encryption is not a permanent 100 percent CPU with a pool connection. A lobby camera does not mine.",
    ["The unknown process plus the pool is mining. Contain the host before you chase the electricity bill.",
     "A backup is scheduled, identifiable, and done. It does not phone a mining pool all day.",
     "Encryption of a disk is a storage feature. It does not maintain a pool connection.",
     "A camera is a physical sensor. It is not this server's CPU."])

add(39, "2.4", "medium",
    "Security logs that used to record administrator logins on a server now have a gap covering the hour of a suspected intrusion. The logging service is running and the disk is not full. What indicator is the gap?",
    ["Logs were cleared or logging was paused by the intruder", "The gap proves no one logged in", "A full disk, even though the disk is not full", "Normal log rotation, which deletes the exact hour of every incident by design"],
    0,
    "A hole in a log that should be continuous is itself an indicator. Attackers delete or stop logs to hide. You do not read a gap as innocence. Check other sources, such as the SIEM copy if it was shipped off the server before the gap, and treat the host as suspect. Rotation should not surgically remove the incident hour.",
    ["A missing hour is evidence of tampering until you can explain it. Look for an off-box copy of those events.",
     "Absence of a record is not proof the login did not happen. It is a reason to distrust the local log.",
     "The stem says the disk is not full. Do not invent that cause.",
     "Rotation is predictable and documented. A gap that matches an intrusion is not routine rotation."])

add(40, "2.4", "hard",
    "A workstation encrypts files and drops a note demanding payment. The same note appears on a file share the workstation had open. What is the activity, and what is the first containment move?",
    ["Ransomware. Disconnect the workstation from the network so it cannot keep encrypting shares",
     "A routine backup. Leave the share mounted",
     "Patch management. Reboot and ignore the note",
     "A honeypot working as designed"],
    0,
    "Ransomware encrypts data and demands payment. A mapped share lets it travel. Isolation comes before forensics and before any talk of paying. A backup does not drop a payment note. A reboot does not decrypt files. A honeypot is a decoy you deployed, not a surprise note on a real share.",
    ["Pull the network. The share is how the encryption spreads. Then start the incident process and use offline backups if you have them.",
     "Backups do not ransom the original files. Leaving the share connected continues the damage.",
     "A patch will not restore encrypted documents, and ignoring the note does not contain the host.",
     "A honeypot is intentional. This is production data being encrypted."])

add(41, "2.4", "medium",
    "Users report that an internal website sometimes loads a script that asks for their password, and the page source contains content a customer typed into a review box yesterday. What class of malicious activity is indicated?",
    ["Stored cross-site scripting", "A physical tailgating incident", "A failed disk", "A salt in the password database"],
    0,
    "Stored cross-site scripting is attacker-controlled content saved by the site and later sent to other browsers, where it runs. A review box is a common place it hides. The fix is to encode output, validate input, and clean the stored content. Tailgating is a door. A disk failure and a password salt do not inject a script into other users' browsers. No sample script is required to recognize the pattern.",
    ["The review was stored and later executed in other browsers. That is stored cross-site scripting.",
     "Tailgating is following someone through a door. It does not alter a web page.",
     "A failed disk removes data. It does not add a password prompt to a review.",
     "A salt is a hashing input. It is not a script stored in a product review."])

add(42, "2.4", "easy",
    "Many machines on the internet send traffic to a company's public site at once, and the site becomes unreachable for real customers. A single lab PC doing the same thing yesterday was a smaller event. What are yesterday and today?",
    ["Yesterday was a denial of service. Today is distributed",
     "Both are impossible travel",
     "Today is a CRL publication",
     "Yesterday was a honeynet"],
    0,
    "Denial of service makes a system unavailable. When many sources do it together, it is distributed. The useful response is upstream filtering and the provider, not a new password on the web server. Impossible travel is an authentication clue. A CRL is a revocation list. A honeynet is a set of decoys.",
    ["One source is denial of service. Many sources are distributed denial of service.",
     "Impossible travel is two logins too far apart. It is not a traffic flood.",
     "Publishing a CRL does not knock a website over with volume.",
     "A honeynet is infrastructure you deploy to watch attackers. It is not this flood."])

add(43, "2.5", "easy",
    "Guest Wi-Fi, point-of-sale systems, and the corporate file servers currently share one flat network. A guest laptop can see server broadcasts. Which mitigation is the structural fix?",
    ["Segment the networks so guests cannot reach the servers, and only allow the paths you intend",
     "Give every guest domain-admin rights so the traffic is 'accounted for'",
     "Turn off all logging to improve speed",
     "Use the same local administrator password on the servers and the guests"],
    0,
    "Segmentation puts untrusted devices in a place where they cannot wander. Firewall rules then allow only what a business process needs. Domain admin for guests, no logs, and shared local passwords all make the blast radius larger. Segmentation is the mitigation the flat network is missing.",
    ["Separate the guest, payment, and corporate networks. Then permit only the flows you can name.",
     "Domain admin on a guest laptop is the opposite of least privilege.",
     "Turning off logs removes detection. It does not create a boundary.",
     "A shared local password means one guest compromise is every server."])

add(44, "2.5", "medium",
    "A server must keep running, but a patch for a high-severity flaw will not be approved until next month. Which mitigation is appropriate in the meantime?",
    ["A compensating control, such as isolating the service and restricting who can reach the vulnerable port",
     "Ignore the flaw because the patch window is later",
     "Disable the vulnerability scanner so the finding disappears",
     "Publish the server on the internet to see if anyone notices"],
    0,
    "If you cannot patch yet, you reduce exposure: limit source addresses, disable the vulnerable feature if you can, and watch the service. That is compensation, not a cure. Hiding the scanner finding leaves the hole. Putting the server on the internet widens it. The patch is still the planned fix.",
    ["Restrict and watch until the patch lands. Write down that the control is temporary.",
     "A later window does not make this month safe. Something has to hold the risk.",
     "Stopping the scanner removes your visibility. The flaw remains.",
     "Publishing the server on the internet increases exposure. It is not a mitigation for an unpatched flaw."])

add(45, "2.5", "medium",
    "An allow list on an application control product permits only signed binaries from the approved directory. A user downloads a 'cleaner' and it will not run. Why is that the intended outcome, compared with a deny list of known bad file names?",
    ["An allow list blocks everything that was not approved, including new malware the deny list has never seen",
     "A deny list is stronger because attackers cannot change a file name",
     "Allow lists exist to let every download run once",
     "The cleaner should be added immediately because the user wants it"],
    0,
    "Deny lists fail open against anything you have not cataloged, and names are trivial to change. Allow lists fail closed: if it is not on the list, it does not run. That will block some legitimate tools, so you need a request path. You do not add a random cleaner because it was blocked. The block is the control working.",
    ["Unknown malware is stopped because it was never approved. That is the point of an allow list.",
     "Attackers rename files to slip past deny lists. A name is a weak indicator.",
     "An allow list that runs every download is not an allow list.",
     "User convenience is not approval. The request process exists so security can say no."])

add(46, "2.5", "hard",
    "A workstation is suspected of calling an attacker every few minutes. The incident lead says to isolate it, not to power it off and not to let it keep talking to the office. Which outcome matches that instruction?",
    ["The host cannot reach other internal systems or the attacker, and its memory is still available if forensics needs it",
     "The host is wiped immediately so the talking stops",
     "The host stays on the production VLAN and only the user is told to stop clicking",
     "The power cable is pulled before anyone records the running processes"],
    0,
    "Isolation contains the host: no more lateral movement and no more command channel, while the machine can stay up for memory capture if policy wants that. Wiping and pulling power destroy evidence you may need. Leaving it on the production VLAN is not containment. Telling the user to stop clicking does not stop a process that is already running.",
    ["Network isolation is the containment that matches the lead's instruction. Evidence can still be collected.",
     "A wipe is eradication, and it is early. You may destroy the very artifacts the investigation needs.",
     "The production VLAN is how the host reaches the rest of the office. That is the path to cut.",
     "Pulling power loses memory. The lead asked not to do that yet."])

add(47, "2.5", "medium",
    "Which mitigation most directly reduces what a compromised user account can do, even after the attacker has the password?",
    ["Least privilege, so the account cannot administer systems it does not need",
     "A longer screensaver timeout",
     "Disabling all monitoring",
     "Sharing one administrator password so lockouts are rarer"],
    0,
    "Least privilege assumes the password may be stolen and limits the damage. An account that cannot change firewalls or read payroll cannot do those things for the attacker either. A longer timeout leaves sessions open. No monitoring hides the abuse. A shared administrator password makes one theft everyone's admin.",
    ["The stolen password is only as powerful as the rights behind it. Take away the rights the job does not need.",
     "A longer timeout keeps a session available longer. It does not shrink the account's rights.",
     "Turning off monitoring does not remove privileges. It removes your chance to see them used.",
     "A shared admin password is a force multiplier for the attacker, not a mitigation."])

add(48, "2.1", "medium",
    "A group defaces the public website and posts a manifesto about an environmental policy. They do not steal the customer database and they do not demand money. Which actor and motivation fit?",
    ["Hacktivists motivated by political or philosophical beliefs", "Organized crime motivated only by a ransom", "An unskilled attacker who accidentally reformatted a disk", "A business partner performing a contracted penetration test"],
    0,
    "Hacktivists use attacks to promote a cause. A public defacement and a manifesto are the signature, not a quiet theft or an invoice. Organized crime wants money. An accident is not a manifesto. A contracted test would be authorized, scoped, and would not be how you learn about it from the homepage.",
    ["The cause and the public message are hacktivism. Financial theft was not the point.",
     "There is no ransom. Organized crime's usual motive is missing.",
     "A manifesto is intent. An accidental format does not publish a policy statement.",
     "A real test is agreed in advance and does not surprise the company on its own homepage."])

add(49, "2.2", "medium",
    "A caller claims to be the help desk, knows the employee's name from a public staff page, and asks for a one-time code that just arrived by text. What combination is this?",
    ["Vishing that uses open-source information, aiming at a multi-factor code",
     "A legitimate help-desk process, because they knew the name",
     "A CRL check",
     "A salt"],
    0,
    "Vishing is social engineering by voice. A name from a public page is not proof of identity. A one-time code is a possession factor, and reading it to a caller gives that factor away. Help desks do not ask users to read those codes back. A revocation list and a password salt are not phone calls.",
    ["Hang up. The code is the second factor, and a public name does not authenticate the caller.",
     "Knowing a name from a website is reconnaissance, not authentication of the caller.",
     "A CRL is a certificate list. It does not phone employees.",
     "A salt is stored with a password hash. It is not a texted login code."])

add(50, "2.3", "medium",
    "A mobile device management report shows phones still running an operating system release with known, patched flaws. The phones are corporate-owned. What vulnerability are they carrying?",
    ["Missing patches on a managed platform", "A zero-day that no vendor has fixed", "A physical bollard failure", "An unrelated mainframe job-control language bug"],
    0,
    "If a fix exists and the phones do not have it, the vulnerability is the missing patch and the slow ring. Push the update, and quarantine phones that stay behind if policy says so. A zero-day would have no fix yet. Bollards and an unrelated mainframe are not this fleet.",
    ["The flaws are known and fixed upstream. The phones are behind. That is patch latency, not a zero-day.",
     "A zero-day has no patch. These flaws are described as already patched by the vendor.",
     "A bollard is a vehicle barrier. It does not version a phone OS.",
     "A mainframe language bug is not the mobile operating system in the report."])

add(51, "2.4", "hard",
    "A decoy administrator password, never used by any real person, is attempted against a VPN every night. What does the attempt tell you, and what should you avoid?",
    ["Someone found a honeytoken. Investigate the source. Do not turn the decoy into a real privileged password",
     "The password is safe to assign to a new administrator because it is being 'tested'",
     "Nightly attempts against a fake password are a successful backup",
     "Disable alerting on that account so the noise stops"],
    0,
    "A honeytoken is a credential that should never authenticate. Any use means it leaked from wherever you planted it, or someone is guessing a value you also published as bait. Trace the source. Do not promote the token into a real admin password, and do not silence the one alert that is working.",
    ["The attempt is the detection. Find where the token was exposed and leave it fake.",
     "Assigning it to a person turns a tripwire into a real key that is already in an attacker's hands.",
     "Backups do not authenticate to the VPN with a decoy password.",
     "The alert is the control. Turning it off blinds you to the next attempt."])

add(52, "2.5", "easy",
    "Which mitigation removes a service that is no longer used, instead of leaving it patched 'just in case'?",
    ["Decommission the system and delete the accounts and firewall rules that existed only for it",
     "Add the server to the domain admin group so it is 'monitored'",
     "Document the server and leave the old rules forever",
     "Disable encryption so decommissioning is faster"],
    0,
    "Decommissioning is a mitigation because an unused service is still an attack surface. Remove the host, the rules, and the accounts, and keep a record that you did. Domain admin does not monitor anything. Leftover rules are how the next person reopens a path. Encryption is unrelated to retiring the box.",
    ["Turn it off, remove the access that existed for it, and record the retirement. That is decommissioning.",
     "Domain admin is privilege, not monitoring, and it is the wrong direction.",
     "A document that says the server is unused, while the firewall rule remains, leaves the surface in place.",
     "Encryption is not what makes a retired server dangerous. The listening service is."])

add(53, "2.4", "medium",
    "Endpoint software quarantines a file and the user can no longer open it. The file arrived as an email attachment and matches a known malware signature. What did the quarantine accomplish?",
    ["It stopped the file from running while someone decides whether to delete it",
     "It sent the file to every user so they can compare copies",
     "It decrypted the user's hard drive",
     "It proved the file is safe to restore immediately"],
    0,
    "Quarantine moves a suspect object out of the path of execution and holds it. It is containment of that file, not a verdict that it is safe, and not a broadcast. Restoring it without analysis puts the malware back. Disk decryption is a different operation.",
    ["The file cannot run from quarantine. That pause is the point, until you delete it or confirm a false positive.",
     "Sending malware to everyone is distribution, not quarantine.",
     "Quarantine does not decrypt disks. It isolates a file.",
     "A signature match is a reason to keep it isolated, not to put it back in the inbox."])

if __name__ == "__main__":
    from common import dump
    dump("sy0-701", {"q-d2.json": Q})
