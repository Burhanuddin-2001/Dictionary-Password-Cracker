# Dictionary-Password-Cracker
This program is a simple dictionary-based password cracker for educational purposes. It reads a list of words from a file, computes their SHA-256 hashes, and compares them with the hash of a target password entered by the user. If a match is found, it prints the cracked password.

# Requirements
- Python 3.x
- hashlib module (included in Python standard library)
- tqdm module (pip install tqdm)

# Usage
* Clone this repository or download the password_cracker.py file.
* A common passwords word list (named password list.txt) is provided with the program. You can use this file as the dictionary for password cracking, or prepare your * own text file containing a list of words (one word per line).
* Run the program using python password_cracker.py.
* When prompted, enter the path to the dictionary file and the target password.
* The program will compute the SHA-256 hashes of the words in the dictionary and compare them with the hash of the target password. If a match is found, it will print the cracked password.

If you have a SHA-256 hash instead of the target password, you can uncomment the Hash-Password block in the code and input your target password hash there for password cracking using the provided dictionary.

If you want to use your own custom dictionary, just uncomment the user input part of the code and provide your dictionary file path there.

# Disclaimer
This program is intended for educational purposes only. The author does not condone or encourage any illegal activities related to password cracking or unauthorized access to computer systems.
