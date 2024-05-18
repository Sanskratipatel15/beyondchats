import time
import requests
import streamlit as st

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"

def fetch_data_from_api(url):
    results = []
    page = 1
    while True:
        response = requests.get(url, params={'page': page})
        if response.status_code == 429:
            st.error("Rate limit exceeded. Waiting for 1 minute before retrying...")
            time.sleep(60)  # Wait for 1 minute before retrying
            continue
        elif response.status_code != 200:
            st.error(f"Failed to fetch data from API. Status code: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        if isinstance(data, dict):
            results.append(data)
        else:
            results.extend(data)
        page += 1
        time.sleep(1)  # Add a delay between requests to avoid hitting rate limits
    return results

def find_citations(response_text, sources):
    citations = []
    for source in sources:
        if source['context'] in response_text:
            citations.append({
                "id": source['id'],
                "link": source.get('link', "")
            })
    return citations

def main():
    st.title("API Response Citation Finder")
    st.write("Fetching data from the API...")

    data = fetch_data_from_api(API_URL)

    if not data:
        st.write("No data found.")
        return

    all_citations = []
    for item in data:
        response_text = item.get('response', '')
        sources = item.get('sources', [])
        if not isinstance(sources, list):
            sources = []
        citations = find_citations(response_text, sources)
        all_citations.append(citations)

    st.write("Citations for each response:")
    for idx, citations in enumerate(all_citations):
        st.write(f"Response {idx+1}:")
        st.write(citations)

if __name__ == "__main__":
    main()