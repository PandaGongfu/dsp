import pandas as pd
import re

faculty_data = pd.read_csv('faculty.csv')
cols = faculty_data.columns.tolist()
new_cols = [x.strip() for x in cols]
[faculty_data.rename(columns={cols[k]: new_col}, inplace=True) for k, new_col in enumerate(new_cols)]

faculty_data['last_name'] = faculty_data['name'].map(lambda x: x.split(' ')[-1])
faculty_data['first_name'] = faculty_data['name'].map(lambda x: x.split(' ')[0])
faculty_data['clean_degree'] = faculty_data['degree'].map(lambda x: x.strip())
faculty_data['clean_title'] = faculty_data['title'].map(lambda x: ''.join(re.findall('.*(?<=Professor)', x)))


def first_n(d, n):
    count = 0
    for k, v in list(d.items()):
        count += 1
        print(k, v)
        if count == n:
            break

# Q6
faculty_dict = {}
dict_f = lambda x: faculty_dict.setdefault(x.last_name, []).append([x.clean_degree, x.clean_title, x.email])
_ = faculty_data.apply(dict_f, axis=1)
first_n(faculty_dict, 3)

# Q7
professor_dict = {}
dict_f = lambda x: professor_dict.setdefault((x.first_name, x.last_name), []).extend([x.clean_degree, x.clean_title, x.email])
_ = faculty_data.apply(dict_f, axis=1)
first_n(professor_dict, 3)

# Q8
faculty_data['first_last_name'] = faculty_data.apply(lambda x: (x.first_name, x.last_name), axis=1)
names_list = faculty_data['first_last_name'].tolist()
names_sorted = sorted(names_list, key=lambda x: x[0])
names_sorted = sorted(names_sorted, key=lambda x: x[-1])
