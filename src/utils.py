def filter_data(data, criteria):
    return [item for item in data if criteria(item)]

def format_string(s):
    return s.strip().capitalize()

def handle_error(error):
    print(f"An error occurred: {error}")