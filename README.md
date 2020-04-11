# Bad-Pdf

Bad-PDF create malicious PDF file to steal NTLM(NTLMv1/NTLMv2) Hashes from windows machines, it utilize vulnerability disclosed by checkpoint team to create the malicious PDF file. Bad-Pdf reads the NTLM hashes using Responder listener.

~~This method work on all PDF readers(Any version)~~  most of the EDR/Endpoint solution fail to detect this attack.

Reference : https://research.checkpoint.com/ntlm-credentials-theft-via-pdf-files/

##### Update: 14/5/2018

Adobe has released a security update(APSB18-09)to address this vulnerability and CVE-2018-4993 is assigned for this vulnerability.

 

### Disclaimer:

All the code provided on this repository is for educational/research purposes only. Any actions and/or activities related to the material contained within this repository is solely your responsibility. The misuse of the code in this repository can result in criminal charges brought against the persons in question. Author will not be held responsible in the event any criminal charges be brought against any individuals misusing the code in this repository to break the law.

### Dependency: 
Responder/Kali Linux

Usage:

python badpdf.py

#### Run Bad-PDF in Kali linux:

![alt text](https://github.com/deepzec/Bad-Pdf/blob/master/screenshots/bad-pdf.PNG "Bad-PDF")

#### Responder waiting for NTLM hash:

![alt text](https://github.com/deepzec/Bad-Pdf/blob/master/screenshots/responder.PNG "Bad-PDF")

#### Run generated Bad-PDF file on a windows machine and get NTLM hash: :)

![alt text](https://github.com/deepzec/Bad-Pdf/blob/master/screenshots/NTLM-hash.PNG "Bad-PDF")

#### Mitigations:

~~* Vendor patches are not available for this vulnerability~~

Adobe patch: https://helpx.adobe.com/security/products/acrobat/apsb18-09.html

* Microsoft issued an optional security enhancement [0] late last year that provides customers with the ability to disable NTLM SSO authentication as a method for public resources.

* Disable external SMB access in firewall to prevent NTLM hash leak to internet

##### Yara Rule:

https://github.com/InQuest/yara-rules/blob/master/NTLM_Credentials_Theft_via_PDF_Files.rule


#### Author : Deepu TV ; Feel free to contact me @twitter.com/DeepZec 

