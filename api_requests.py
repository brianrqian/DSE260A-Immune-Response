import requests
import csv
from io import StringIO
import pandas as pd
import os

api_version = "4_1"  # latest version, should be updated as API changes
base_url = f"https://www.cmi-pb.org/api/v{api_version}/"
base_headers = {
    "Accept": "text/csv",
}


def create_subdirectory(subdirectory="data"):
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


def find_subjects_in_year(year="2020"):
    """Find all subjects ID in a given year. Also, Write filtered CSV contents."""
    subject_endpoint = f"/subject?dataset=eq.{year}_dataset"
    filtered_df = fetch_data(subject_endpoint)
    write_data_to_csv(filtered_df, f"{year}_subject.csv")
    df = pd.read_csv(StringIO(filtered_df))
    subject_ids = pd.Series(df["subject_id"])

    return subject_ids


def filter_data_by_subjects(data, subjects):
    df = pd.read_csv(data)
    filtered_df = df[df["subject_id"].isin(subjects)]
    return filtered_df


def find_specimens_in_year(subjects, year="2020"):
    specimen = fetch_data("specimen")
    filtered_df = filter_data_by_subjects(StringIO(specimen), subjects)
    write_data_to_csv(filtered_df.to_csv(), f"{year}BD_specimen.csv")
    specimen_ids = pd.Series(filtered_df["specimen_id"])
    return specimen_ids


def filter_data_by_specimens(data, specimens):
    filtered_df = data[data["specimen_id"].isin(specimens)]
    return filtered_df


def write_data_to_csv(text, filename):
    """Write the collected data to a CSV file."""
    path = f"data/{filename}"
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error writing data to {filename}: {e}")


def fetch_data(endpoint=""):
    """Fetch data from a single API endpoint."""

    current_url = f"{base_url}/{endpoint}"

    response = requests.get(current_url, headers=base_headers)

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}: {response.text}")
        response.raise_for_status()

    return response.text


def fetch_all_data(endpoints, specimens, year="2020"):
    """Fetch data from a list of API endpoints."""
    for endpoint in endpoints:
        print(f"Fetching data from {endpoint}")
        data = fetch_data(endpoint)
        df = pd.read_csv(StringIO(data))

        if "specimen_id" not in df.columns:
            raise Exception("specimen_id column not found")

        filtered_df = filter_data_by_specimens(df, specimens)
        filename = f"{year}_{endpoint.replace('/','')}.csv"
        write_data_to_csv(filtered_df.to_csv(), filename)


def main():
    create_subdirectory()

    # metadata_endpoints = ['/',
    #                       '/gene',
    #                       '/transcript',
    #                       '/protein',
    #                       '/cell_type']

    data_endpoints = [
        "/pbmc_cell_frequency",
        "/plasma_ab_titer",
        "/plasma_cytokine_concentration",
        "/pbmc_gene_expression?versioned_ensembl_gene_id=eq.ENSG00000277632.1",
    ]

    # years = [2020, 2021, 2022]
    subjects = find_subjects_in_year()
    specimens = find_specimens_in_year(subjects)

    fetch_all_data(data_endpoints, specimens)


if __name__ == "__main__":
    main()
