# Collaborative Discussion (Units 7–9) – CVSS Critique and Alternatives (Wunder et al., 2024)

## Activity overview
Discussion topic: Critical analysis of CVSS limitations and evaluation of alternative vulnerability scoring systems (based on Wunder et al., 2024). Duration: 3 weeks (Units 7–9). One peer response received and one peer response given. No summary post produced due to limited peer engagement.


## Initial Post

The authors examine whether CVSS v3.1 scoring is consistent when used by professionals. The main criticism made by the authors is that CVSS scores are not always reliable. 
Different professionals can give different scores for the same vulnerability, and even the same person can give a different score later for that same vulnerability. 
The authors also show that some metrics, especially **Attack Vector**, **User Interaction** and **Scope**, are difficult to interpret in a consistent way.

I agree with this critique. In my opinion, a vulnerability scoring system should be as clear and consistent as possible because organisations use it to decide what to fix first. 
If the score changes depending on the evaluator, then the prioritisation may also change. This idea is supported by Howland (2023), who argues that CVSS is widely used but still flawed, especially when it is treated as a tool for real-world risk prioritisation rather than only technical severity.

Among the alternatives discussed by the authors, I think **SSVC** is the most interesting one. Unlike CVSS, SSVC is more decision-focused and takes context into account. 
It helps organisations decide what action to take based on stakeholder needs instead of only producing a severity number. For this reason, I believe SSVC is a better approach and could replace CVSS for vulnerability prioritisation.

## Peer Response 1

Hi,

I found your analysis of the inter-rater inconsistency highlighted by Wunder et al. (2024) particularly insightful. 
Your point regarding the same professional potentially scoring the same vulnerability differently over time underscores the inherent subjectivity in CVSS, which is often masked by its numerical output. You rightly identified that metrics like **Scope** and **User Interaction** are often the primary culprits of this variance.

I also agree with your selection of **Stakeholder-Specific Vulnerability Categorisation (SSVC)**. While CVSS acts as a "one-size-fits-all" thermometer, SSVC functions more like a triage protocol. 
To build on your point about decision-making, the use of a decision-tree model helps eliminate the "magic number" ambiguity that Howland (2023) criticises.

In terms of preventing the inconsistencies you mentioned, organisations should implement scoring rubrics or internal "gold standards" for specific system architectures. 
By pre-defining what "Network" or "Physical" access looks like within the specific company infrastructure, firms can reduce the subjectivity of the Attack Vector metric. Additionally, integrating automated threat intelligence feeds to verify **Exploit Status** (a key component of SSVC) can prevent reliance on outdated or subjective manual assessments (Spring et al., 2021).

Moving toward a context-aware model like SSVC not only improves consistency but ensures that resources are directed toward vulnerabilities that actually pose a credible threat to the organisation's mission.

## References (UoEO Harvard)

Howland, H. (2023) ‘CVSS: Ubiquitous and Broken’, *Digital Threats: Research and Practice*, 4(1). Available at: <https://dl.acm.org/doi/epdf/10.1145/3491263> (Accessed: February 2022).

Spring, J.M. et al. (2021) *Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization (Version 2.0).* Software Engineering Institute, Carnegie Mellon University. Available at: <https://www.sei.cmu.edu/documents/606/2021_019_001_653461.pdf> (Accessed: April 2021).

Wunder, J., Kurtz, A., Eichenmüller, C., Gassmann, F. and Benenson, Z. (2024) ‘Shedding Light on CVSS Scoring Inconsistencies: A User-Centric Study on Evaluating Widespread Security Vulnerabilities’. Available at: <https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10646847> (Accessed: September 2024).
