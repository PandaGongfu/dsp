import re
import pandas as pd
from collections import Counter

faculty_data = pd.read_csv('faculty.csv')
cols = faculty_data.columns.tolist()
new_cols = [x.strip() for x in cols]
[faculty_data.rename(columns={cols[k]: new_col}, inplace=True) for k, new_col in enumerate(new_cols)]

# Find degree frequencies
degrees = faculty_data['degree'].tolist()
clean_degrees = [d.replace('.', '') for s in degrees for d in s.split(' ') if len(d)]
Counter(clean_degrees)

# Find title frequencies
titles = faculty_data['title']
clean_titles = [''.join(re.findall(r".*Professor", title)) for title in titles]
Counter(clean_titles)

# Print list of emails
emails = faculty_data['email'].tolist()
print(emails)

# Find domains
domains = [''.join(re.findall(r"(?<=\@).*", email)) for email in emails]
print(list(Counter(domains).keys()))





