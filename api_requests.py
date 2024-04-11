import requests
import os

api_version = '4_1' # latest version, should be updated as API changes
base_url = f'https://www.cmi-pb.org/api/v{api_version}/'
base_headers = {
    'Accept': 'text/csv',
}

def create_subdirectory(subdirectory='data'):
    """Create a subdirectory if it doesn't exist."""
    directory_path = os.path.join(os.getcwd(), subdirectory)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")
    else:
        print(f"Directory already exists: {directory_path}")
        print("Deleting existing files")
        for filename in os.listdir(directory_path):
            os.remove(os.path.join(directory_path, filename))

def write_data_to_csv(text, filename):
    """Write the collected data to a JSON file."""
    path = f'data/{filename}'
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error writing data to {filename}: {e}")


def fetch_data(endpoint=''):
    """Fetch data from a single API endpoint."""

    current_url = f'{base_url}/{endpoint}'

    response = requests.get(current_url, headers=base_headers)

    if response.status_code != 200: 
        print(f"Failed to fetch data: {response.status_code}: {response.text}")
        response.raise_for_status()
    else:
        filename = f"{endpoint.replace('/','')}.csv"
        write_data_to_csv(response.text, filename)


def fetch_all_data(endpoints):
    """Fetch data from a list of API endpoints."""
    for endpoint in endpoints:
        print(f"Fetching data from {endpoint}")
        data = fetch_data(endpoint)


def fetch_and_write_data_in_chunks(endpoint=''):
    """Fetch data from a single API endpoint with pagination."""

    current_url = f'{base_url}/{endpoint}'

    range_start = 0
    range_step = 5000 
    range_end = range_start + range_step - 1

    filename = f"{endpoint.replace('/', '')}.csv"
    path = f'data/{filename}'

    with open(path, 'wb') as file:
        while True:
            chunked_headers = {
                'Accept': 'text/csv',
                'Range': f'{range_start}-{range_end}'
            }
            response = requests.get(current_url, headers=chunked_headers)

            if response.status_code == 200:
                if not response.content.strip() or len(response.content.splitlines()) < range_step:
                    print("Reached the end of the data.")
                    break

                file.write(response.content)
                range_start += range_step
                range_end = range_start + range_step - 1
            else:
                print(f"Failed to fetch data: {response.status_code}: {response.text}")
                break 

    print(f"Data successfully written to {filename}")


def find_subject_years(year='2020'):
    """Find all subjects that were tested in a given year."""
    subject_endpoint = f'{base_url}/subject?dataset=eq.{year}_dataset'

def main():
    create_subdirectory()

    metadata_endpoints = ['/',
                          '/gene',
                          '/transcript',
                          '/protein',
                          '/cell_type']

    data_endpoints = ['/pbmc_cell_frequency',
                      '/plasma_ab_titer',
                      '/plasma_cytokine_concentration',
                      '/specimen',
                      '/subject',
                      '/pbmc_gene_expression?versioned_ensembl_gene_id=eq.ENSG00000277632.1'
                      ]

    fetch_all_data(data_endpoints)

if __name__ == "__main__":
    main()