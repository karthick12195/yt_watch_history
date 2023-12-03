from bs4 import BeautifulSoup
import pandas as pd

# Read HTML content from file
file_path = 'data/Takeout/YouTube and YouTube Music/history/watch-history.html'  # Replace with the actual path to your HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

div_elements = soup.find_all('div', class_='content-cell')

# Initialize lists to store data
titles = []
channels = []
timestamps = []

# Extract information from each div
for div_element in div_elements:
    title = div_element.find('a').text
    channel = div_element.find_all('a')[1].text
    timestamp = div_element.find_all('br')[-1].next_sibling.strip()

    titles.append(title)
    channels.append(channel)
    timestamps.append(timestamp)

# Create a pandas DataFrame
df = pd.DataFrame({
    'Title': titles,
    'Channel': channels,
    'Timestamp': timestamps
})

# Display the DataFrame
print(df)