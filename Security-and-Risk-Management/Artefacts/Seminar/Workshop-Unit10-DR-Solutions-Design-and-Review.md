# Unit 10 Seminar Workshop : DR Solutions Design and Review


## Context
This workshop is based on : Kumar, Aashish. "Cloud Vendor Lock-In: Identify, Strategies and Mitigate" (2024)

## Questions and answers

## 1) What are some of the main vendor lock-in issues the authors identify? How would you mitigate them?

Vendor lock-in happens when an organisation becomes too dependent on one cloud provider, making it difficult, costly, and time-consuming to move services elsewhere. 
The main issues identified by the authors include technical lock-in through proprietary technologies and APIs, data lock-in through provider-specific storage formats, service lock-in through strong integration of proprietary services, certification lock-in due to the need for re-evaluation of standards and compliance, contract lock-in through restrictive terms and exit penalties, economic lock-in from heavy investment in one ecosystem, and network lock-in caused by provider-specific network services and configurations. The paper also shows that poor interoperability, limited portability, compatibility issues, and vendor-specific security frameworks can make switching even harder. To mitigate these risks, organisations should plan an exit strategy early, use multi-cloud or hybrid cloud approaches where appropriate, improve data portability, adopt open standards, reduce dependence on proprietary services, and use containerisation and modular design to make applications easier to move between providers.

## 2) What are some security concerns with the modern cloud? How can these be mitigated?

According to the vendor lock-in paper, one security concern is that organisations often align their security controls and compliance measures with one provider’s architecture. 
If the provider uses a unique security framework, moving to another provider may create vulnerabilities during transition. The paper also links security risk with data protection differences, metadata handling, data governance constraints, and privacy/compliance requirements such as GDPR, which can complicate both secure use and migration.

Mitigation would include using open standards, reducing dependence on proprietary security models, planning migration and exit in advance, improving data portability, and carrying out regular audits and compliance checks as part of a broader cloud strategy.

