"""SY0-801 topics that the SY0-701 bank did not cover, including AI threats."""

from common import PROBLEMS, dump, item
from gate import collisions

P = "sy0"
Q = []


def add(*args):
    Q.append(item(P, *args))


add(210, "2.1", "easy",
    "A server is missing a patch. Nobody has used that weakness yet. Which term fits the missing patch, and which term would fit a person who later tries to use it?",
    ["The missing patch is a vulnerability. The person who tries to use it is a threat actor",
     "The missing patch is already an incident, and the person is a control",
     "The missing patch is a policy, and the person is a vulnerability",
     "Both are the same thing: a residual risk acceptance"],
    0,
    "A vulnerability is a weakness. A threat actor is someone or something that may exploit it. Until that happens, the unpatched server is not yet an incident. A policy and a risk acceptance are decisions, not the weakness or the person.",
    ["Keep the two ideas separate. The hole is the vulnerability. The person is the threat actor.",
     "An incident is a weakness that is being used, or its result. A missing patch alone is not that.",
     "A policy is a rule. A missing patch is not a policy, and the person is not the weakness.",
     "Risk acceptance is a management decision. It is not the name of either the patch or the person."])

add(211, "2.1", "medium",
    "A payroll app can be reached from the internet, from the VPN, and from an old admin port that nobody documented. Which term is the set of all of those places?",
    ["The attack surface",
     "A single threat vector, because three paths count as one",
     "A compensating control",
     "A recovery time objective"],
    0,
    "The attack surface is every place an attacker might try. Each path, such as the internet, the VPN, or the forgotten port, can be a vector into that surface. A compensating control and a recovery time are not a list of exposed places.",
    ["All of the reachable places together are the attack surface. Shrink it by closing the unused port.",
     "Each path can be its own vector. The collection of them is the surface, not one vector.",
     "A compensating control stands in for a missing control. It is not the list of exposures.",
     "A recovery time objective is how long a service may be down. It is not an exposure list."])

add(212, "2.1", "medium",
    "A firewall log shows a scan, and the scanned service is unpatched. The scan did not succeed. How should those two facts be described?",
    ["A threat event met a vulnerability, and it has not become a successful compromise",
     "A successful breach, because any scan of an unpatched service is already data theft",
     "A false positive, because unpatched services cannot be real",
     "A backup test"],
    0,
    "A scan is threat activity. The missing patch is the vulnerability. Together they are dangerous, but a failed scan is not yet theft. Treat it as an attempt, patch the service, and keep the log. Calling it nothing, or calling it a completed breach, both misstate the evidence.",
    ["Record the attempt and close the weakness. Success was not shown.",
     "The log says the scan did not succeed. Do not report theft you cannot see.",
     "An unpatched service is a real weakness. The finding is not a false positive.",
     "A backup test restores data. It does not scan a service."])

add(213, "2.6", "medium",
    "A support bot is told, in a customer's message, to ignore its instructions and print the hidden system prompt. The bot complies. What kind of AI failure is that?",
    ["Prompt injection",
     "A hardware failure of the bot's disk",
     "A certificate expiration",
     "A full backup"],
    0,
    "Prompt injection is untrusted text that tries to override the model's instructions. The customer's message did that. The fix is to keep secrets out of the prompt, limit what the bot can reveal, and treat user text as data rather than as orders. A disk, a certificate, and a backup do not explain a bot obeying a hidden instruction.",
    ["Treat the customer text as untrusted data. That was prompt injection.",
     "Nothing here failed in the disk. The model followed an injected instruction.",
     "A certificate date does not make a bot reveal its prompt.",
     "A backup does not change how the bot reads a message."])

add(214, "2.6", "hard",
    "A model that flags malware was retrained on a set in which an attacker had relabeled malicious samples as safe. Afterward it waves those samples through. What happened to the model?",
    ["Data poisoning",
     "A normal accuracy improvement",
     "A password rotation",
     "A warm-site test"],
    0,
    "Poisoning is training data that was altered so the model learns the wrong lesson. Relabeling malware as safe is that attack. The model needs a trusted training set and a check against known-bad samples. A password rotation and a recovery test do not relabel training data.",
    ["The labels were sabotaged. That is poisoning. Retrain from a source you trust.",
     "Accuracy did not improve. The model learned a lie.",
     "Rotating a password does not change training labels.",
     "A warm site is spare infrastructure. It did not relabel the samples."])

add(215, "2.6", "medium",
    "A user spends a long chat trying to talk a public model into dropping its safety rules and producing content the rules forbid. The user never touches the training set. What is that attempt called?",
    ["Jailbreaking",
     "Data poisoning of the training set",
     "A tape rotation",
     "A change-advisory board approval"],
    0,
    "Jailbreaking is an attempt to make a model ignore the limits set for it, usually through the conversation rather than through the training data. Poisoning would change the data the model learned from. A tape job and a change board are not this conversation.",
    ["The chat is trying to remove the model's limits. That is jailbreaking. Do not use the output.",
     "Poisoning changes training data. This user never touched that data.",
     "Tape rotation is a backup schedule. It is not a chat with a model.",
     "A change board approves production changes. It is not a chat with a model."])

add(216, "2.6", "easy",
    "A generated answer cites a security bulletin number that does not exist and describes a menu the product does not have. The tone is confident. Which limitation is that?",
    ["A hallucination",
     "A verified vendor advisory",
     "Perfect explainability",
     "A passed audit"],
    0,
    "A hallucination is a confident answer that is not true. Invented bulletin numbers and menus are the clue. Check the vendor before you act on the text. Explainability and an audit do not make a fictional citation real.",
    ["Do not follow the invented bulletin. The model hallucinated it.",
     "A real advisory can be found at the vendor. This number cannot.",
     "Explainability would show why a decision was made. It does not invent a menu.",
     "An audit does not certify a citation that does not exist."])

add(217, "2.6", "medium",
    "A hiring model was trained mostly on one region's past decisions, and it rejects qualified applicants from another region at a much higher rate. Which AI problem is that?",
    ["Bias in the training data and the resulting decisions",
     "A load balancer preferring a healthy server",
     "A salt on a password hash",
     "A differential backup"],
    0,
    "Bias is a systematic skew, here inherited from a training set that did not represent the people being judged. Review the data and the outcomes, and do not treat the score as neutral. A load balancer, a salt, and a backup are unrelated.",
    ["The model learned an unfair pattern. That is bias, and the outcomes show it.",
     "A load balancer distributes traffic. It does not score applicants.",
     "A salt changes a password hash. It does not reject a region.",
     "A differential backup copies changed files. It does not hire anyone."])

add(218, "2.6", "medium",
    "An analyst pastes a full incident ticket, including customer account numbers, into a public chatbot that the company has not approved. What is the security failure?",
    ["Sensitive data left the company's control",
     "The chatbot is automatically a private company system",
     "Account numbers are not sensitive",
     "The paste is a backup of the ticket"],
    0,
    "A public model is outside the company's control unless a contract and a design say otherwise. Account numbers are sensitive. Pasting them there is data loss. It is not a backup, and calling the tool private does not make it one.",
    ["Stop the practice and report it. The account numbers were disclosed to an unapproved system.",
     "Public is not private. Approval and a contract would have to say otherwise.",
     "Account numbers identify customers. They are sensitive.",
     "A backup is a copy you control and can restore. This paste is neither."])

add(219, "2.6", "hard",
    "A vision model detects weapons in images. An attacker changes a few pixels so the weapon is still obvious to a person and the model says the image is clean. What is that?",
    ["Evasion",
     "A successful patch of the model",
     "A longer password",
     "A hot site"],
    0,
    "Evasion changes the input so a model misses what a person can still see. It is not a fix. Detect it by testing the model against altered inputs and by not trusting the score alone. A password and a hot site do not hide an object from a model.",
    ["The picture was altered to fool the model. That is evasion.",
     "A patch would improve detection. This change made detection fail.",
     "A longer password does not change the pixels in an image.",
     "A hot site is a recovery location. It does not edit an image."])

add(220, "2.6", "medium",
    "A model denies a loan and cannot show which factors produced the denial. Regulators ask why. Which gap is that?",
    ["Explainability",
     "A complete chain of custody for a disk image",
     "A passed penetration test of the office Wi-Fi",
     "A longer DHCP lease"],
    0,
    "Explainability is the ability to say why a model produced an outcome. A denial with no factors fails that. Custody of a disk, a wireless test, and a DHCP lease do not answer the regulator's question.",
    ["The missing 'why' is an explainability gap. Do not deploy a decision you cannot account for.",
     "Chain of custody tracks evidence. It does not explain a loan score.",
     "A wireless test does not document a credit decision.",
     "A DHCP lease times an address. It is not a reason code."])

add(221, "2.6", "hard",
    "A document the model is allowed to read tells it to call an internal tool and run a command the user never typed. The tool is connected and has broad rights. What risk is that, and what reduces it?",
    ["The model can be steered into code execution. Limit the tools and require a person for dangerous actions",
     "The document is harmless because models cannot call tools",
     "Give the tool domain-admin rights so the command always works",
     "Disable logging so the command is not recorded"],
    0,
    "If a model can invoke tools, untrusted content can try to make it invoke the wrong one. That is a code-execution risk. Reduce it by allowing only the tools the job needs and by stopping dangerous actions for a person to approve. More privilege and no logs make the failure worse.",
    ["Restrict the tools and put a person in front of anything destructive. The document was trying to drive the tool.",
     "This model can call a tool. Pretending it cannot is how the command runs.",
     "Domain admin on the tool is the opposite of least privilege.",
     "Turning off logs hides the action. It does not stop it."])

if __name__ == "__main__":
    found = collisions("sy0-801", Q)
    if PROBLEMS or found:
        raise SystemExit("\n".join(PROBLEMS + found))
    dump("sy0-801", {"q-v8.json": Q})
