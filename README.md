# Bad-Pdf

Bad-PDF create malicious PDF to steal NTLM Hashes from windows machines, it utilize vulnerability disclosed by checkpoint team to create the malicious PDF file. Bad-Pdf reads the NTLM hashes using Responder listener.

This method work on all PDF readers(Any version) and java scripts are not required for this attack.

Reference : https://research.checkpoint.com/ntlm-credentials-theft-via-pdf-files/

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

#### Author : Deepu TV Contact me @twitter.com/DeepZec 

