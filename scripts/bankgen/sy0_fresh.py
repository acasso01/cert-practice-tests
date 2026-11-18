"""Original SY0-701 questions that do not restate the existing bank."""

from common import PROBLEMS, dump, item
from gate import collisions

P = "sy0"
Q = []


def add(*args):
    Q.append(item(P, *args))


add(183, "1.1", "medium",
    "An alert fires when a host speaks to a known-bad address. Nobody is standing at a door, and no policy document produced the alert. Which control category and type fit the alert?",
    ["Technical and detective", "Physical and deterrent only", "A paper policy with no sensor", "A generator that replaces the UPS"],
    0,
    "The alert is produced by a system, so it is technical, and it reports activity that already happened, so it is detective. A door, a policy with no sensor, and a generator do not raise that alert.",
    ["A sensor that reports bad traffic is a technical detective control.",
     "Nothing physical deterred anyone in this alert. The control is the detection system.",
     "A policy can require monitoring. It does not itself fire the alert.",
     "A generator supplies power. It does not watch network destinations."])

add(184, "1.2", "easy",
    "A directory records who signed in, what they opened, and when. It is not the check of the password and it is not the list of what they are allowed to open. Which part of AAA is the record?",
    ["Accounting", "Authentication doubled", "A firewall rule", "A checksum of a photo"],
    0,
    "Accounting is the log of activity. Authentication is the proof of identity. Authorization is what that identity may do. A firewall rule and a checksum are not the AAA record of access.",
    ["The record of the session is accounting.",
     "Authentication already happened when the password was checked. This question is the later record.",
     "A firewall rule allows or denies packets. It is not the AAA accounting log.",
     "A checksum tests a file. It does not record who opened it."])

add(185, "1.4", "hard",
    "A server's long-term private key is stolen today. Sessions recorded last year must stay unreadable. Which property of the key exchange provides that?",
    ["Perfect forward secrecy", "Using the same session key for every connection forever", "Storing the session keys next to the stolen private key on purpose", "Turning encryption off"],
    0,
    "Perfect forward secrecy derives session keys that cannot be reconstructed from a later theft of the long-term key. Reusing one session key, storing the session keys beside the stolen key, or disabling encryption all fail that goal.",
    ["Forward secrecy is why last year's sessions survive today's key theft.",
     "One permanent session key is the opposite of forward secrecy.",
     "Keeping the session keys next to the stolen key hands them over with it.",
     "No encryption means the recordings were never protected."])

add(186, "2.1", "medium",
    "A group defaces a site and posts a political statement. They do not ask for money and they do not take the customer database. Which actor's usual motivation matches?",
    ["A hacktivist", "A financially motivated criminal crew demanding a ransom", "A drive that failed on its own", "A scheduled backup job"],
    0,
    "Hacktivists act for a cause and often want the act seen. A ransom crew wants payment. A dead drive and a backup job are not actors with a manifesto.",
    ["The statement and the lack of a payment demand fit a hacktivist.",
     "A ransom crew's motivation is the money. This incident does not ask for any.",
     "A failed drive does not post a political statement.",
     "A scheduled backup copies data. It does not deface a website or post a statement."])

add(187, "2.2", "easy",
    "A text message claims to be the bank and includes a link to a login page. The user did not request a text. What is that message?",
    ["Smishing", "A fiber cut", "A warm spare", "A tape rotation"],
    0,
    "Smishing is phishing over SMS. The link is the trap. A fiber cut, a spare site, and a tape rotation do not send a bank login text.",
    ["Treat the text as smishing. Do not use the link.",
     "A fiber cut is an outage, not a text message.",
     "A warm spare is recovery hardware. It does not send SMS.",
     "Tape rotation is a backup schedule, not a phone message."])

add(188, "2.2", "medium",
    "Customers at one store report fraudulent card charges after using the register. A reader was clipped over the real card slot and has now been removed. What was that device doing?",
    ["Skimming card data", "Balancing the books", "Issuing TLS certificates", "Cooling the server room"],
    0,
    "A skimmer sits on a legitimate reader and copies card data. It is not accounting, not a certificate authority, and not the cooling system. Replace the reader path and notify the processor.",
    ["The overlay was a skimmer. Treat the cards used there as exposed.",
     "Balancing the books does not require a fake reader on the slot.",
     "A certificate is not captured by a clip-on card reader.",
     "The cooling system does not clip onto a card slot or copy track data."])

add(189, "2.3", "medium",
    "A build still links a library whose maintainer published a fix months ago. The application code around the library was written in-house and is not the buggy part. Where is the vulnerability?",
    ["In the outdated third-party library", "In the office wallpaper", "In a paper visitor log", "In the color of the server chassis"],
    0,
    "The known flaw is in the library that was not updated. The surrounding in-house code is not the component the maintainer fixed. Wallpaper, a visitor log, and chassis paint are not the vulnerable component.",
    ["Update or replace the library, then rebuild. That is the vulnerable component.",
     "Wallpaper does not execute as part of the application.",
     "A visitor log is not linked into the build.",
     "Chassis color does not contain the unfixed flaw."])

add(190, "2.4", "hard",
    "One password is tried against hundreds of accounts, and almost no account hits its lockout threshold. A later review shows the same password on the failures. What pattern is that?",
    ["Password spraying", "One account being guessed thousands of times until it locks", "A full disk backup", "A door propped open"],
    0,
    "Spraying uses a few passwords across many accounts so lockouts, which count per account, do not fire. A classic brute force hammers one account and usually locks it. A backup and a propped door are not this authentication pattern.",
    ["Many accounts, one password, few lockouts. That is spraying.",
     "Thousands of guesses at one account is the pattern that lockout is built to stop.",
     "A disk backup does not submit passwords.",
     "A propped door is a physical finding, not this log pattern."])

add(191, "2.5", "medium",
    "Users can run anything they download, and a new policy says only approved applications may execute. Which control enforces that policy?",
    ["An application allow list", "A longer mouse cord", "Disabling all logging", "Giving every user local administrator"],
    0,
    "An allow list executes known-good programs and blocks the rest. A mouse cord does not. Turning off logs and making everyone an administrator remove controls instead of adding one.",
    ["Allow only the approved binaries. That is the control the policy named.",
     "A mouse cord does not decide which programs run.",
     "No logs means you will not see the block or the bypass.",
     "Local administrator is how people walk around an allow list."])

add(192, "3.1", "medium",
    "A company runs its own cloud for daily load and rents public-cloud capacity when the daily load overflows. Which deployment is that combination?",
    ["Hybrid", "A single public region with no private capacity", "An air-gapped laptop", "A paper ledger"],
    0,
    "Hybrid uses both private and public capacity, which is what the overflow arrangement is. Public-only, an air gap, and a paper ledger do not burst from a private cloud into a public one.",
    ["Private for the baseline and public for the peak is hybrid.",
     "Public-only leaves out the company's own cloud.",
     "An air-gapped laptop is not a burst capacity plan.",
     "A paper ledger cannot rent extra compute when the private cloud fills up."])

add(193, "3.2", "hard",
    "A safety controller must not have a routed path to the office LAN or the internet. Operators carry updates in on reviewed media. Which design is that?",
    ["An air gap", "A flat network with the controller on the office VLAN", "Publishing the controller to the internet", "Reusing the office Wi-Fi password on the controller"],
    0,
    "An air gap is the absence of a network path. Putting the controller on the office VLAN, publishing it, or sharing the Wi-Fi password creates the path the design forbids. Carried media is a separate, reviewable route and does not make the gap a routed network.",
    ["No routed path is the air gap. Keep it that way and review any media.",
     "The office VLAN is a routed path. It breaks the requirement.",
     "Publishing the controller is the opposite of isolating it.",
     "A shared Wi-Fi password puts the controller on a network."])

add(194, "3.2", "medium",
    "Two servers sit on the same subnet and must not talk to each other unless a policy says so. A traditional subnet boundary is not enough. What adds that per-flow rule?",
    ["Microsegmentation", "One shared local administrator password", "Turning off the switch", "A public DNS resolver with no policy"],
    0,
    "Microsegmentation enforces policy between workloads even when they share a subnet. A shared password, a powered-off switch, and a DNS resolver do not express that allow rule.",
    ["Policy between the two servers, regardless of the subnet, is microsegmentation.",
     "A shared password gives both servers the same key. It does not separate them.",
     "Powering the switch off stops everything, including the traffic you still need.",
     "A DNS resolver answers names. It does not police server-to-server flows."])

add(195, "3.3", "medium",
    "A system must store passwords and must also store contracts that staff will read later. Which pair of protections matches those two needs?",
    ["Hash the passwords, and encrypt the contracts", "Encrypt the passwords with a key stored in the same field so anyone can reverse them", "Hash the contracts and throw away the only copy", "Post both in a world-readable share"],
    0,
    "Passwords should be verified with a slow hash, not stored so they can be decrypted. Contracts must be readable later, so they are encrypted and the key is protected, not hashed away. A world-readable share protects neither.",
    ["Hash what you only need to check. Encrypt what you need to read back.",
     "A reversible password next to its key is not password storage.",
     "Hashing the only copy of a contract destroys the contract.",
     "A world-readable share is the exposure both protections exist to prevent."])

add(196, "3.4", "medium",
    "A recovery site has servers racked and powered, and the latest payroll data is not there yet. Staff expect to restore data before they can work. Which site type is that?",
    ["Warm", "Hot, with current data and a live cutover", "Cold, with an empty room and no servers", "A desk drawer of unlabeled tapes and no hardware"],
    0,
    "A warm site has the hardware and still needs data or configuration before service returns. A hot site can take over with current data. A cold site is an empty space. A drawer of tapes without hardware is not a racked site.",
    ["Hardware ready, data still to restore: warm.",
     "Hot would already have the data and a short cutover.",
     "Cold would not have the servers racked and powered.",
     "Tapes in a drawer are not a powered recovery site."])

add(197, "4.1", "easy",
    "A user receives an unexpected attachment. The security team wants to see what it does without running it on the user's PC. Where should it run?",
    ["A sandbox isolated from the corporate network", "The finance file server", "The domain controller", "The user's laptop, because that is fastest"],
    0,
    "A sandbox detonates an untrusted file where it cannot reach production. The file server, the domain controller, and the user's laptop are the places you are trying to keep it out of.",
    ["Detonate it in the sandbox. That is the isolated place.",
     "The file server is production data. It is the wrong place to open a suspect file.",
     "The domain controller is the last machine to use as a test bench.",
     "The user's laptop is the machine the attachment was trying to reach."])

add(198, "4.2", "medium",
    "A discovery scan finds a server that is not in the asset inventory and has no owner. What should happen to that finding?",
    ["Treat it as an unmanaged asset and bring it under inventory or remove it", "Ignore it because it was not on the list", "Give it a domain-admin password so it feels included", "Publish its address on the internet"],
    0,
    "An unknown server is a gap in inventory and a likely gap in patching and ownership. Identify it, assign an owner, or take it off the network. Ignoring it, sharing an admin password, or publishing it makes the gap worse.",
    ["Put an owner on it or remove it. Unknown hardware is not a free pass.",
     "Missing from the list is the problem, not a reason to skip it.",
     "A shared domain-admin password is not how you adopt a server.",
     "Publishing the address exposes a machine you do not even own on paper."])

add(199, "4.3", "hard",
    "A critical service is patched and the process is never restarted. A rescan an hour later still reports the vulnerable version in memory. What is the likely remaining step?",
    ["Restart the service so it loads the patched code", "Declare the finding a false positive without looking", "Delete the asset record", "Turn off vulnerability scanning"],
    0,
    "Some fixes sit on disk until the process starts again. The rescan is telling you the running image is still old. Restart during the window. Pretending it is a false positive, deleting the asset, or blinding the scanner leaves the old code running.",
    ["Restart so the running process is the patched one, then rescan.",
     "The scanner agrees with the running version. That is not a false positive yet.",
     "Deleting the record hides the server. It does not load the patch.",
     "Stopping the scans removes the evidence and leaves the bug."])

add(200, "4.4", "medium",
    "A SIEM rule pages the on-call team every night when a known backup job runs. The pages are never incidents. What should the analysts change?",
    ["Tune the rule so the known backup does not page", "Page a larger group so more people see the backup", "Delete the backup", "Turn off the SIEM"],
    0,
    "A rule that fires on approved activity trains people to ignore pages. Exclude or raise the threshold for that job, and keep the rule for unexpected cases. More pages, no backups, or no SIEM do not fix the noise.",
    ["Tune it. The backup is known, and the page is not an incident.",
     "A larger page list spreads the same false alarm.",
     "The backup is the business process. Do not delete it to silence a rule.",
     "The SIEM is how you would see a real event. Keep it, and fix the rule."])

add(201, "4.5", "medium",
    "Receivers must be able to tell that a message body was signed by the company's mail system and not altered. The public key is in DNS. Which control is that?",
    ["DKIM", "A door badge", "A warm site", "A cable certifier"],
    0,
    "DKIM signs the message and publishes the key in DNS so receivers can check the signature. A badge, a recovery site, and a cable tester do not sign mail.",
    ["DKIM is the signature and the DNS key. That matches the requirement.",
     "A badge opens a door. It does not sign a message.",
     "A warm site is a recovery location, not a mail signature.",
     "A certifier tests cable. It does not publish a mail key."])

add(202, "4.6", "hard",
    "A caller asks the help desk to reset an executive's password. The caller ID shows an external number and the caller cannot answer the callback phrase on the account. What should the analyst do?",
    ["Refuse the reset until the caller's identity is verified", "Reset it and read the new password back to the caller", "Post the new password in a public channel", "Disable the executive's MFA to make the call shorter"],
    0,
    "A password reset is account takeover if the caller is not the user. The failed callback phrase is the stop sign. Reading a new password to an unverified caller, posting it, or removing MFA completes the social-engineering attempt.",
    ["Stop. Verification failed, so the reset does not happen.",
     "Reading a password to an unverified caller hands over the account.",
     "A public channel is not a password-reset destination.",
     "Removing MFA weakens the account the caller is trying to take."])

add(203, "4.7", "medium",
    "When a high-severity endpoint alert fires, the same isolation steps run every time without waiting for someone to remember them. Which system runs that repeatable response?",
    ["SOAR", "A printed poster that no process reads", "A shredded document", "A blank spreadsheet with no integration"],
    0,
    "SOAR connects the alert to a playbook and runs the response the same way each time. A poster, a shredded page, and an empty spreadsheet are not integrated with the alert.",
    ["The playbook runner is SOAR. That is the consistent response.",
     "A printed poster is not connected to the alert and cannot isolate a host.",
     "A shredded document cannot execute steps.",
     "A spreadsheet that is not connected to the alert does not run the response."])

add(204, "4.8", "hard",
    "An investigator needs what was in RAM on a running suspect host. The host is about to be powered off and shipped. What must happen first?",
    ["Capture memory while the host is still running", "Power it off so the RAM is easier to read later", "Reinstall the OS over the disk", "Factory-reset the machine"],
    0,
    "RAM contents disappear when power is lost. Capture memory before shutdown if that evidence matters. Powering off, reinstalling, or factory-resetting destroys it. Disk imaging is a separate step and does not replace the memory capture.",
    ["Take the memory image first. Shipping a powered-off host will not still have it.",
     "Powering off is how the RAM evidence is lost.",
     "Reinstalling overwrites the disk and does nothing useful for RAM you already lost.",
     "A factory reset is destruction, not collection."])

add(205, "5.1", "medium",
    "A team cannot meet a control this quarter. The security lead writes who accepted the gap, why, and the date the gap must close. What is that writing?",
    ["A time-bounded exception", "A permanent repeal of the control", "A CVE number", "A cable test"],
    0,
    "An exception names the owner, the reason, and the expiry. It is not permission to forget the control. A CVE and a cable test do not accept a governance gap.",
    ["Owner, reason, and end date make it an exception rather than a silent failure.",
     "A permanent repeal is not what a dated gap is.",
     "A CVE names a vulnerability. It is not this acceptance.",
     "A cable test does not accept a control gap."])

add(206, "5.2", "medium",
    "A risk treatment leaves residual risk. The business owner signs that the organization will live with what remains. Which treatment is the signature?",
    ["Acceptance", "Ignoring the risk with no owner", "Pretending the risk is zero", "Deleting the asset record so the risk disappears on paper"],
    0,
    "Acceptance is a conscious decision by someone who can accept it, with the residual risk still recorded. Silence, a fake zero, and deleting the asset are not acceptance. They are missing risk management.",
    ["The owner's signature on the residual risk is acceptance.",
     "Silence and a missing owner are not a signed acceptance of residual risk.",
     "Calling the risk zero does not make the residual go away.",
     "Deleting the record hides the asset. The risk remains."])

add(207, "5.3", "medium",
    "Every critical system is hosted by the same vendor. A one-day outage at that vendor would stop payroll, mail, and the customer portal together. Which third-party risk is that?",
    ["Concentration risk", "A diverse set of vendors with no shared failure", "A spare laptop in a closet", "A new logo"],
    0,
    "Concentration risk is depending on one provider for too many critical services, so one failure hits all of them. Diversity is the opposite. A spare laptop and a logo do not describe this single point of failure.",
    ["One vendor for payroll, mail, and the portal is concentration risk.",
     "Diversity would mean those services do not share one provider's outage.",
     "A closet laptop does not replace three critical services.",
     "A logo does not create or measure vendor concentration."])

add(208, "5.4", "easy",
    "A privacy regulation starts a clock when the company becomes aware of a qualifying breach. The clock ends at the regulator, not at a marketing meeting. What obligation is the clock?",
    ["Regulatory breach notification", "An optional social-media post", "A hardware refresh cycle", "A new office logo"],
    0,
    "Breach-notification rules require telling the regulator, and sometimes affected people, on a deadline that starts when you know. A social post, a hardware cycle, and a logo are not that legal duty.",
    ["The clock is the regulatory notification. Know when it starts.",
     "A social post is not the notice to the regulator.",
     "Refreshing hardware does not notify anyone of a breach.",
     "A logo is branding. It is not a notification deadline."])

add(209, "5.5", "hard",
    "A vendor offers a report in which an auditor tested whether security controls operated effectively across six months, not merely whether the controls were designed on a single day. Which report is that?",
    ["A SOC 2 Type II", "A SOC 2 Type I, which is a point in time", "A packing slip", "A birthday card"],
    0,
    "Type II reports on the operating effectiveness of controls over a period. Type I is a point-in-time design report. A packing slip and a birthday card are not assurance reports.",
    ["Six months of operating effectiveness is Type II.",
     "Type I does not cover a period of operation. It is the point-in-time report.",
     "A packing slip lists a shipment. It is not an audit opinion.",
     "A birthday card is not an assurance report."])

if __name__ == "__main__":
    found = collisions("sy0-701", Q)
    if PROBLEMS or found:
        raise SystemExit("\n".join(PROBLEMS + found))
    dump("sy0-701", {"q-fresh.json": Q})
