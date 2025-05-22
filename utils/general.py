def convert_if_whole(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n