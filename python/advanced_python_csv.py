import pandas as pd

faculty_data = pd.read_csv('faculty.csv')
cols = faculty_data.columns.tolist()
new_cols = [x.strip() for x in cols]
[faculty_data.rename(columns={cols[k]: new_col}, inplace=True) for k, new_col in enumerate(new_cols)]

# write list of emails to csv
emails_df = pd.DataFrame(faculty_data['email'], columns=['email'])

emails_df.to_csv('emails.csv', header=False, index=False)








