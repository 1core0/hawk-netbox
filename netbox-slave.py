import json
import pynetbox
TAG = 'YOUR_TAG'
MASK_LENGTH = 16
def connect():
    with open('config.json') as config_file:
        config = json.load(config_file)

    api_key = config['api_key']
    url = config['url']
    try:
        nb = pynetbox.api(url=url, token=api_key)
        return nb
    except Exception as e:
        print(f"Exception has occurred during connection: {str(e)}")

def isNone(entry):
    if entry['site'] is None or entry['prefix'] is None:
        print(f"The site {entry} is missing fields. Skipping...")
        return True
    return False
def create_RepoJson(nb):
    repositories = []
    prefixes = nb.ipam.prefixes.filter(tag=TAG, mask_length=MASK_LENGTH)
    for prefix in prefixes:
        if prefix['site']['name'] is None:
            prefix['site']['name'] = input(f"Please enter Repository Name: ")

        dictionary = {
            'name': prefix['site']['name'],
            'ip' : prefix['prefix']
        }
        repositories.append(dictionary)
    with open('repositories.json', 'w') as file:
        json.dump(repositories, file, indent=4)
        return True
def create_ScanJson(nb):
    scans = []
    prefixes = nb.ipam.prefixes.filter(tag=TAG, mask_length=24)
    for prefix in prefixes:
        if prefix['description'] is None:
            prefix['description'] = input(f"Please enter Scan Name: ")
        dictionary = {
            'scan_name' : prefix['description'].upper(),
            'targets' : prefix['prefix']
        }
        scans.append(dictionary)
    with open('scans.json', 'w') as file:
        json.dump(scans, file, indent=4)
        return True
def create_AssetJson(nb):
    assets = []
    tenants = nb.tenancy.tenants.filter(tag=TAG)
    for tenant in tenants:
        prefixes = nb.ipam.prefixes.filter(tenant_id=tenant.id)
        ipv4 = []
        for prefix in prefixes:
            ipv4.append(str(prefix))       
        dictionary = {
                        'asset_name' : tenant['name'],
                        'ipv4' : ipv4
                    }
        assets.append(dictionary)
    with open('assets.json', 'w') as file:
        json.dump(assets, file, indent=4)
        return True

def main():
    nb = connect()
    if create_RepoJson(nb):
        print("File repositories.json created successfully!")
    if create_ScanJson(nb):
        print("File scans.json created successfully!")
    if create_AssetJson(nb):
        print("File assets.json created successfully!")


if __name__ == "__main__":
    main()
