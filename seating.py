classroom_seating = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def find_free_seats(classroom): 
    new_classroom = classroom 
    for row_index, row in enumerate(classroom):
        for col_index, column in enumerate(row):

            if not column: 
                print(f'Row {row_index+1} seat {col_index+1} is free. Do you want to sit there? (y/n)')
                sit_here = input().lower()

                if sit_here == 'y':
                    print('What is your name?')
                    new_classroom[row_index][col_index] = your_name

