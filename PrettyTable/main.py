from prettytable import PrettyTable

my_table = PrettyTable()  # New table
my_table.add_column('Type', ['a', 'b', 'c'])
my_table.add_column('Value', [1, 2, 3])
print(my_table)
