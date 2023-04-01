
def format_errors(validation_errors):
    """
    Formats validation errors into a dictionary.
    """
    formatted_errors = {}
    for field, error in validation_errors.items():
        formatted_errors[field] = error
    return {'errors': formatted_errors}
