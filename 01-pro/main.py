import sys
from Core.enums import HashAlgorithm
from Core.hasher import HashManager
from utils.io_handler import read_test_passwords

def run_interactive():
    print("🔐 Password Hasher – PRO Edition")
    print("Choose algorithm: sha256 / sha512 / bcrypt")
    algo_input = input("Algorithm: ").strip().lower()

    try:
        algo = HashAlgorithm(algo_input)
    except ValueError:
        print("❌ Invalid algorithm.")
        return

    manager = HashManager(algo)
    password = input("Enter password: ").strip()
    hashed = manager.hash(password)
    print(f"\n🔒 {algo.name} Hash:\n{hashed}")

    if algo == HashAlgorithm.BCRYPT:
        check = input("\nEnter password again to verify: ").strip()
        if manager.verify(check, hashed):
            print("✅ Match!")
        else:
            print("❌ Not a match!")

def run_test_mode(algo_str: str):
    try:
        algo = HashAlgorithm(algo_str.lower())
    except ValueError:
        print("❌ Invalid algorithm for test mode.")
        return

    manager = HashManager(algo)
    passwords = read_test_passwords()

    for pwd in passwords:
        hashed = manager.hash(pwd)
        print(f"{pwd} → {algo.name} → {hashed}")

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--test":
        run_test_mode(sys.argv[2])
    else:
        run_interactive()
