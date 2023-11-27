import pandas as pd
import csv


# Function to read data from CSV files
def read_csv(file_name):
    data = []
    with open(file_name, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_users():
  users = pd.read_csv('app/data/users.csv', index_col='user')
  users = users.to_dict(orient='index')

  return users

def get_transitions():
  trans = read_csv('app/data/transitions.csv')
  return trans

def get_inventory():
  trans = pd.read_csv('app/data/transitions.csv')
  inv = trans.groupby(['type', 'product']).sum()[['quantity', 'sub_total']]
  inv.columns = ['quantity', 'cost']
  inv = inv.xs('B', level='type').subtract(inv.xs('S', level='type'), fill_value=0)
  inv['quantity'] = inv['quantity'].astype(int)
  inv = inv.reset_index()
  inv_list = inv.to_dict(orient='records')

  return inv_list
