import hashlib

def generate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        content = f.read()
        hasher.update(content)
    return hasher.hexdigest()

def compare_file_hash(file_path, expected_hash):
    file_hash = generate_file_hash(file_path)
    if file_hash == expected_hash:
        print(f"File '{file_path}' is intact.")
    else:
        print(f"File '{file_path}' has been altered!")

file_path = input("Enter the file path: ")
expected_hash = input("Enter the expected hash: ")
compare_file_hash(file_path, expected_hash)
