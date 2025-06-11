# log_parser.py
# Simple log parser to extract failed login events (Event ID 4625)

def parse_log_file(file_path):
    try:
        with open(file_path, "r") as log:
            for line in log:
                if "4625" in line:
                    print("[!] Failed login detected:")
                    print(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'tested_log.txt' with your own test log file
    parse_log_file("tested_log.txt")
