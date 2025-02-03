def extract_initial_from_List(input_list):
    """
    This function takes a list of names and returns a list of initials
    for example
    input_list = ['John', 'Jane Doe']
    output_list = ['J', 'JD']
    """
    return [" ".join([x[0] for x in name.split()]) for name in input_list]

print(extract_initial_from_List(['John', 'Jane Doe']))

