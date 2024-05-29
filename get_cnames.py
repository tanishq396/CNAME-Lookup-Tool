import subprocess
import argparse
import re

def clean_domain(domain):
    # Remove protocol prefixes
    if domain.startswith("http://"):
        domain = domain[len("http://"):]
    elif domain.startswith("https://"):
        domain = domain[len("https://"):]

    # Remove content within square brackets and the brackets themselves
    domain = re.sub(r'\[.*?\]', '', domain).strip()

    return domain

def get_cname(domain):
    try:
        domain = clean_domain(domain)
        # Execute the dig command and capture the output
        result = subprocess.run(['dig', domain, 'CNAME', '+short'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"

        cname = result.stdout.strip()
        return cname if cname else "No CNAME record found"
    except Exception as e:
        return f"Exception: {e}"

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    domains = [domain.strip() for domain in domains if domain.strip()]

    if not domains:
        print("Error: No valid domains found in the file.")
        return

    for domain in domains:
        cname = get_cname(domain)
        print(f"domain - {domain}\ncname - {cname}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get CNAME records for a list of subdomains using dig command.")
    parser.add_argument('-l', '--list', required=True, help="Path to the file containing the list of subdomains.")
    args = parser.parse_args()

    main(args.list)
