FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns a list of
     to-do items.
     """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos( todos_arg, filepath=FILEPATH):
    """ Writes a to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


