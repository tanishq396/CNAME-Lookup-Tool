## **CNAME Lookup Tool**

This script reads a list of subdomains from a file, uses the `dig` command to retrieve their CNAME records, and outputs the results in a simplified format.

## Features

- **Input File**: Reads domains from a specified file.
- **Domain Cleaning**: Automatically removes `http://`, `https://`, and any content within square brackets (`[]`).
- **CNAME Resolution**: Uses the `dig` command to find CNAME records for each domain.
- **Simplified Output**: Outputs each domain and its corresponding CNAME in a clear and easy-to-read format.

## Usage

1. **Install Requirements**:
   Ensure you have Python installed and `dig` command is accessible from your command line.

2. **Create a Subdomain List**:
   Create a text file (e.g., `subdomains.txt`) with each subdomain on a new line.

3. **Run the Script**:
   Execute the script using the following command:
   ```sh
   python get_cnames.py -l subdomains.txt
   ```

## Example

For an input file `subdomains.txt` containing:
```
http://example.com
https://sub.example.com
test.example.com [additional info]
```

The script will output:
```
domain - example.com
cname - cname.example.com

domain - sub.example.com
cname - cname.sub.example.com

domain - test.example.com
cname - cname.test.example.com
```
