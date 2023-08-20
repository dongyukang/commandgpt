def browse_file():
    try:
        file_path = input('Please input path of your local pc: ')

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content, True
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None, False
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return None, False

def load_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
