#
# Write a function that flattens a nested dictionary, converting it to a single-level dictionary with compound keys. Example: flatten_dict({"a": 1, "b": {"c": 2}}) should return {"a": 1, "b.c": 2}.
def flatten_dict(d):
    """
    Recursively flattens a nested dictionary into a single-level dictionary.

    Args:
        d (dict): The dictionary to be flattened.

    Returns:
        dict: A new dictionary with all nested keys concatenated with a '.' separator.
    """
    flat_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for subkey, subvalue in flatten_dict(value).items():
                flat_dict[f"{key}.{subkey}"] = subvalue
        else:
            flat_dict[key] = value
    return flat_dict

print(flatten_dict({"a": 1, "b": {"c": 2}}))
