def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        if next in ")]}":
            try:
                left = opening_brackets_stack.pop()
            except IndexError as err:
                return "Incorrect"
            if are_matching(left, next):
                continue
            else:
                return "Incorrect"
    if len(opening_brackets_stack) > 0:
        return "Incorrect"
    else:
        return "Correct"
