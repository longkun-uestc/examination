def match(s1, s2):
    if not s2:
        if not s1 or s1 == "*":
            return (0, 0)
    if not s1:
        return (-1, 0)
