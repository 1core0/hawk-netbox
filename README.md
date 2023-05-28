# NetBox Prefix Data Extraction

This script connects to a NetBox instance using the provided API key and URL from the `config.json` file. It retrieves prefixes with a specific tag and prepares a JSON file containing the prefix, tenant, site, and description information.

## Prerequisites

- Python 3.x
- `pynetbox` library (install using `pip install pynetbox`)

## Getting Started

1. Clone the repository or download the script.
2. Install the `pynetbox` library by running `pip install pynetbox` in your terminal.
3. Ensure you have a valid `config.json` file with the following structure:

```json
{
  "api_key": "YOUR_API_KEY",
  "url": "NETBOX_URL"
}
```

4. Replace `"YOUR_API_KEY"` with your NetBox API key. You can obtain your API key from your NetBox instance.
5. Replace `"NETBOX_URL"` with the URL of your NetBox instance.
6. Run the script by executing `python script.py` in your terminal.
