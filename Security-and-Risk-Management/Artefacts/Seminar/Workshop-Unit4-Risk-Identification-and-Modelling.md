# Unit 4 Seminar workshop : Threat modelling for Industrial Cyber-Physical Systems (ICPS)


## Context 
This workshop is based on : Jbair, M., Ahmad, B., Maple, C. and Harrison, R. (2022) Threat modelling for industrial cyber physical systems in the era of smart manufacturing, Computers in Industry, 137, p.103611
<br>

## 1) What are the key elements and interdependencies in a cyber-physical system that must be captured in a comprehensive threat model, and why are they critical for accurate risk analysis?
A complete CPS threat model must capture the full chain: threat actor (insider/outsider + skills/resources), assets (with criticality), vulnerabilities, attacks/TTPs, attack impact (availability, integrity, confidentiality, safety), attack detection, and likelihood. The interdependencies matter because attacks propagate across layers (IT,OT) and can turn a “cyber” event into a real physical impact. If you model only one layer, your risk analysis becomes unrealistic. 

## 2) How can threat modelling help identify attack entry points and system vulnerabilities in cyber-physical energy systems, and what are the challenges in doing so effectively?
Threat modelling helps by mapping attack scenarios/attack trees using adversary techniques (ex ICS ATT&CK): reconnaissance/scanning ,exploit ,lateral movement, control logic changes / MitM / DoS, ... That’s how you expose entry points and “reachable” assets. The challenge is that CPS mixes legacy OT, complex architectures, and physical process constraints so you need good system knowledge to build realistic scenarios.

## 3) In the context of CPS threat modelling, how can scenario-specific metrics and risk assessment methodologies be used to prioritise vulnerabilities and guide the development of targeted security countermeasures?
Use scenario metrics to rank what matters. In this paper the authors use **Attack Vector (AV)** (window of exposure: actor capability, vulnerabilities, asset value, detection, impact) and Attack Likelihood (AL) (history/trends), then compute risk as R = AV × AL, and place it on a risk matrix to prioritise treatment. That gives a clear shortlist of “fix first” scenarios and lets you select targeted technical + management controls.
