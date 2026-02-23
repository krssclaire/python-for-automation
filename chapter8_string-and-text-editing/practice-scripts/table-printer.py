def print_table(data):
    cols_widths = [0] * len(data)
    
    for i in range(len(data)):
        cols_widths[i] = max(len(item) for item in data[i])    

    for row in range(len(data[0])):
        for col in range(len(data)):
            print(data[col][row].rjust(cols_widths[col]), end=' ')
        print()
    
table_data = [['apples', 'oranges', 'cherries', 'banana'], 
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
