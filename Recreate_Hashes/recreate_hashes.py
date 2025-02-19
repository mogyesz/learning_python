import binascii
import base64
import sys

def hex_to_base(hex_string):
    byte_data = binascii.unhexlify(hex_string)
    return base64.b64encode(byte_data).decode()

def recreate_hash(name, passwd, salt, output_file):
    digest = hex_to_base(passwd)
    salt_base64 = hex_to_base(salt)
    
    hash = f"{name}:sha256:50000:{salt_base64}:{digest}"
    output_file.write(hash + '\n')
    
def parse_db_line(line):
    name, passwd, salt = line.strip().split('|')
    return name, passwd, salt

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 titanic_hash.py <filename>")
        sys.exit(1)
        
    filename = sys.argv[1]
    output_filename = filename + ".hashes"
    
    try:
        with open(filename, 'r') as file, open(output_filename, 'w') as output_file:
            for line in file:
                name, passwd, salt = parse_db_line(line)
                recreate_hash(name, passwd, salt, output_file)
        print(f"Hashes written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()