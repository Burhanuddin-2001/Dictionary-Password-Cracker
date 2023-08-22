
import hashlib
from tqdm import tqdm


def read_file(path):
    # Function to read a file and return its content as a list of lines
    try:
        with open(path, "r") as f:
            # read().splitlines() remove newline character from each line
            temp_list = f.read().splitlines()
            return temp_list
# note: Instead of using readlines() to read the file, we can use read().splitlines() to avoid having to remove the newline character from each line later on.
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("The file is not available in the provided 'PATH'")
        return None


def hash_finder(value):
    # Function to compute the SHA-256 hash of a given value
    if isinstance(value, str):
        # If the value is a string, compute its hash and return it
        return hashlib.sha256(value.encode("utf-8")).hexdigest()
    elif isinstance(value, list):
        # If the value is a list, compute the hash of each element and return a list of hashes
        temp = []
        for word in tqdm(value, desc="Hashing values"):
            h = hashlib.sha256()
            h.update(word.encode("utf-8"))
            temp.append(h.hexdigest())
        return temp
    else:
        # If the value is neither a string nor a list, return None
        return None


def Compare_hashes(Target, wordlist):
 # Function to compare a target hash with a list of hashes and return the index of the matching hash if found
    try:
        if Target in wordlist:  # if the target is available in the wordlist return its index
            return wordlist.index(Target)
    except BaseException as hashproblem:  # Handle any exception that may occur during comparison
        print("Proper hashing is not done, exiting the program")
        exit()
    else:  # If no match is found, return None
        return None


def main():
    # Main function to run the password cracking program

    # Providing file_path implicitly
    file_path = "password list.txt"

    # User inputed file path
    # file_path = input(
    #     "Enter the file path of dictionary file(word list) for password cracking:\n")
    # file_path = file_path[file_path.find(":")+1:]
    # file_path = file_path.strip()

    Target_pass = input("Enter Target password: ").strip()
    target_hash = hash_finder(Target_pass)

    # #Hash-Password
    # target_hash= input("Enter Target password hash: ").strip()

    bin_word_list = read_file(file_path)
    word_list_hash = hash_finder(bin_word_list)
    ans = Compare_hashes(target_hash, word_list_hash)
    if ans != None:
        print(f"The Password is Cracked :)\n Password = {bin_word_list[ans]}")
    else:
        print("Password Not Found")


if __name__ == "__main__":
    main()
