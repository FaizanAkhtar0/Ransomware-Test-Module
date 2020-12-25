# Ransomware-Test-Module
A ransomware with limited functionality  and is limited to a folder. Can encrypt a limited files with provided extensions in the code. This is for educational purposes.

STEPS:
1) python -m virtualenv venv
2) windows: venv/Scripts/activate.bat | linux: venv/Scripts/activate
3) place files to encrypt in "Local_root", allowed extension provided in file_test.py
4) python main.py


# WELCOME TO TEST VERSION OF DUMMY RANSOMWARE PROJECT

Given:
ransomware_test.exe
exts.PNG => 
Local_root => Folder

Usage Instructions:
1) This test is only limited to "Local_root" folder, outside it everything is safe!
2) ransomware_test.exe must be placed in the same parent folder as Local_root (i.e: both must be in same directory in order to work)
3) All the files that you want to test ransomware on, must be placed inside of "Local_root" folder.
4) Initially this dummy project allows the extentions displayed in 'exts.PNG' image.
5) Either the test files must have any of allowed extentions or no extentions at all.
6) After placing of test files, RUN => "ransomware_test.exe", Let it run untill it closes by itself.
7) Go inside "Local_root" folder to see encrypted files.

Most Important INFO!!!
8) It will generate 3 files on your desktop as follows:
	1) YourEncrypted_Private_key.key
	2) YourPublic_key.PEM
	3) AES_encrypted_keys.txt
9) These are the files that will be used to decrypt your test files, do not delete them!
10) Upon deletion of these files you'll loose all the hopes of recovering test files.


General INFO!!!
1) If you are able to reverse engineer this 'ransomware_test.exe' you'll see my public key inside of variables.py file on variable name "hacker_public_key".
2) But without my "PRIVATE KEY" You can't decrypt the test files!

POSSIBLE SOLUTIONS!!!
1) Try a recovery software on "Local_root" folder to see if you can get back your files.
	=> Even if you recover them, it'd be of no use 'cuz they are shredded. Means It's data was overwriten multiple times before encryption.
	=> So this means you won't be getting your data back even if you recover the files.
2) Try reverse engineering to see if you can find some overlooked weakness that can help you decrypt your files. :)



ENJOY!
