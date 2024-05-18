# beyondchats
# API Response Citation Finder

This project fetches data from a paginated API, identifies the sources for each response, and presents the citations through a user-friendly UI built with Streamlit.

## Features

- Fetch data from a paginated API.
- Identify citations for each response.

## Technologies Used
- Python
- Streamlit
- Requests

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/api-response-citation-finder.git
    cd api-response-citation-finder
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run citation_finder.py
    ```

2. The app will open in your web browser. It will fetch data from the API, process it, and display the citations for each response.

