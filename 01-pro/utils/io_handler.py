import os

TEST_FILE_PATH = os.path.join(os.path.dirname(__file__), "..","..", "test","01-pro", "test_cases.txt")


def read_test_passwords():
    if not os.path.exists(TEST_FILE_PATH):
        raise FileNotFoundError("❌ test_cases.txt not found.")
    
    with open(TEST_FILE_PATH, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
