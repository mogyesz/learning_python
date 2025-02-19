## recreate_hashes.py
A Python script that reads a file containing user credentials (password and salt), recreates password hashes using the PBKDF2 algorithm with SHA-256, and outputs the resulting hashes to a new file.

#### Overview
This script processes a file with user credentials, converts the password and salt values to base64, and then generates a hash in the format used by Gitea's passwd_hash_algo. The resulting hashes are written to a new file.

#### Requirements
Python 3.x

#### Installation
Clone this repository to your local machine:

```shell
git clone https://github.com/yourusername/recreate_hashes.git
cd recreate_hashes
```

#### Usage:

To use the script, run it from the command line with the input file as an argument. The input file should contain lines of user credentials in the following format:

name|passwd|salt

name is the username.
passwd is the hashed password (hex encoded).
salt is the salt used during hashing (hex encoded).

Example
To run the script:

```bash
python3 recreate_hashes.py input
```
