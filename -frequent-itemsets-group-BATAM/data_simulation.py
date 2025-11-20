# [Student: Aime] Import required libraries
from faker import Faker  # For generating fake names and dates
import random            # For random selection of items
import pandas as pd      # For creating and saving the dataset as CSV

# [Student: Aime] Initialize Faker instance for random date and customer information
fake = Faker()

# [Student: Aime] Create a list of at least 30 unique supermarket items
items_list = [
    'Milk', 'Bread', 'Eggs', 'Butter', 'Cheese', 'Chicken', 'Beef', 'Fish',
    'Rice', 'Pasta', 'Tomatoes', 'Onions', 'Potatoes', 'Carrots', 'Apples',
    'Bananas', 'Oranges', 'Grapes', 'Yogurt', 'Juice', 'Coffee', 'Tea',
    'Sugar', 'Salt', 'Oil', 'Flour', 'Cereal', 'Soap', 'Shampoo', 'Toothpaste'
]

# [Student: Aime] Define the number of transactions to simulate (minimum 3000 as required)
num_transactions = 5000

# [Student: Aime] Create an empty list to store generated transaction records
data = []

# [Student: Aime] Generate transaction data using a loop
for i in range(1, num_transactions + 1):

    # [Student: Aime] Generate a random transaction date (within the last year)
    transaction_date = fake.date_between(start_date='-1y', end_date='today')

    # [Student: Aime] Randomly choose how many items will be in the transaction (between 2 and 7)
    num_items = random.randint(2, 7)

    # [Student: Aime] Randomly select items from the list without duplicates
    selected_items = random.sample(items_list, num_items)
    
    # [Student: Aime] Append the transaction record (ID, Name, Date, Items) to the list
    data.append([
        i,                            # Unique Transaction ID
        fake.name(),                 # Fake Customer Name
        transaction_date,            # Simulated transaction date
        ','.join(selected_items)     # Convert list of items to comma-separated string
    ])

# [Student: Aime] Convert the list of transactions into a DataFrame
df_transactions = pd.DataFrame(data, columns=['TransactionID', 'CustomerName', 'Date', 'Items'])

# [Student: Aime] Save the DataFrame as a CSV file
df_transactions.to_csv('supermarket_transactions.csv', index=False)

# [Student: Aime] Display first few rows to verify dataset
df_transactions.head()
