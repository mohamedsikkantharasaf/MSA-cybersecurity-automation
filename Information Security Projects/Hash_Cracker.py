import hashlib
import sys
import pyfiglet
import requests
import os
import binascii

ascii_banner = pyfiglet.print_figlet("Hash Cracker", colors="Yellow", font="big")

print("\033[91mAlgorithms Available: MD5 | SHA1 | SHA224 | SHA384 | SHA512 | SHA256 | \033[0m\n")

print("\033[94mEnter no:1 for MD5\033[0m")
print("\033[94mEnter no:2 for SHA1\033[0m")
print("\033[94mEnter no:3 for SHA256\033[0m")
print("\033[94mEnter no:4 for SHA224\033[0m")
print("\033[94mEnter no:5 for SHA512\033[0m")
print("\033[94mEnter no:6 for SHA384\033[0m")
print("\033[94mEnter no:7 for CRC32 \033[0m")

hash_type = int(input("Enter the Hash Type (e.g., CRC32):"))
hash_value = str(input("Enter the Hash Value (as a hexadecimal string):"))

wordlist_file_path = 'wordlist.txt'

# Check if the wordlist file is already present locally
if not os.path.exists(wordlist_file_path):
    # New GitHub raw URL of the wordlist file
    wordlist_url = 'https://raw.githubusercontent.com/mohamedsikkantharasaf/MSA-cybersecurity-automation' \
                   '/c5b82db914f5e72d978d8d843d470a14d6116413/Information%20Security%20Projects/wordlist.txt'

    # Fetch the wordlist from GitHub
    response = requests.get(wordlist_url)

    if response.status_code == 200:
        with open(wordlist_file_path, 'w') as local_wordlist_file:
            local_wordlist_file.write(response.text)
        print("Wordlist downloaded and saved locally.")
    else:
        print(f"Failed to fetch wordlist. Status code: {response.status_code}")
        sys.exit()

# Read the wordlist from the local file
try:
    with open(wordlist_file_path, 'r', encoding='utf-8') as local_wordlist_file:
        word_list = local_wordlist_file.read().splitlines()
except UnicodeDecodeError:
    print("Error decoding as UTF-8. Trying to decode with errors ignored.")
    with open(wordlist_file_path, 'r', encoding='utf-8', errors='ignore') as local_wordlist_file:
        word_list = local_wordlist_file.read().splitlines()

for word in word_list:
    if hash_type == 1:
        hash_object = hashlib.md5(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash_value == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

    elif hash_type == 2:
        hash_object = hashlib.sha1(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash_value == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

    elif hash_type == 3:
        hash_object = hashlib.sha256(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash_value == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

    elif hash_type == 4:
        hash_object = hashlib.sha224(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash_value == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

    elif hash_type == 5:
        hash_object = hashlib.sha512(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash_value == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

    elif hash_type == 6:
        hash_object = hashlib.sha384(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash_value == hashed:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

    elif hash_type == 7:
        hash_object = binascii.crc32(word.encode('utf-8')) & 0xFFFFFFFF
        hash_valued = int(hash_value, 16)
        if hash_valued == hash_object:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break

else:
    print(f"Hash is not Found in provide word list :\033[1;32m {hash_value}\n")

