import hashlib
import bcrypt
import sys
import os

TEST_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "test","00-basic", "test_cases.txt")

def hash_sha256(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def hash_sha512(password: str) -> str:
    return hashlib.sha512(password.encode()).hexdigest()

def hash_bcrypt(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_bcrypt(password: str, hashed_password: str) -> bool:
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode()
    return bcrypt.checkpw(password.encode(), hashed_password)

def run_test_mode(algorithm: str):
    print(f"🔍 Running test mode with {algorithm.upper()}...\n")
    if not os.path.exists(TEST_FILE_PATH):
        print("❌ Test file not found!")
        return
    with open(TEST_FILE_PATH, "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()]    
    for pwd in passwords:
        if algorithm == "sha256":
            h = hash_sha256(pwd)
        elif algorithm == "sha512":
            h = hash_sha512(pwd)
        elif algorithm == "bcrypt":
            h = hash_bcrypt(pwd)
        else:
            print(f"❌ Unknown algorithm: {algorithm}")
            return        
        
        print(f"{pwd} → {algorithm.upper()} → {h}\n")



def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--test":
        run_test_mode(sys.argv[2].lower())
        return    
    print("🔐 Password Hasher (Basic Crypto)")
    print("Select hashing algorithm:")
    print("1️⃣  SHA256")
    print("2️⃣  SHA512")
    print("3️⃣  bcrypt (with salt + verification)")
    
    choice = input("Your choice (1/2/3): ").strip()
    password = input("Enter password: ").strip()

    if choice == "1":
        result = hash_sha256(password)
        print(f"\n🔒 SHA256 Hash:\n{result}")
    elif choice == "2":
        result = hash_sha512(password)
        print(f"\n🔒 SHA512 Hash:\n{result}")
    elif choice == "3":
        hashed = hash_bcrypt(password)
        print(f"\n🔒 bcrypt Hash:\n{hashed}")
        
        check = input("\nEnter password again to verify: ").strip()
        if verify_bcrypt(check, hashed):
            print("✅ Match!")
        else:
            print("❌ Not a match!")
    else:
        print("❗ Invalid choice. Please select 1, 2, or 3.")
    
if __name__ == "__main__":
    main()        