def safe_cast(val, to_type, default=None):
    """
    Used for casting values safely, returning a defult value on casting errors
    """
    try:
        if to_type == int:
            return to_type(double(val))
        return to_type(val)
    except (ValueError, TypeError):
        return default


def ldap_to_datetime(timestamp: float):
    """
    Takes an LDAP timestamp and converts it to a datetime object
    """
    from datetime import datetime, timedelta
    return datetime(1601, 1, 1) + timedelta(timestamp/10000000)


def get_files_in_dir(dir, ext):
    """
    Gets all files in a directory and returns them as a generator
    Optionally takes an extension and returns only files with that extension
    """
    import os

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.split('.')[1].lower() == ext.lower() or not ext:
                file_full_path = os.path.join(root, file)
                yield file_full_path


def compare_lists(firstlist, secondlist):
    """
    Takes two lists and compares them
    Returns a set of common fields and two lists of differences in a tuple
    """
    common = set(firstlist).intersection(secondlist)
    first_difference = [item for item in firstlist if item not in common]
    second_difference = [item for item in secondlist if item not in common]
    return (common, first_difference, second_difference)
