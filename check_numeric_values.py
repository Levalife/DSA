def validate(text):
    """
    >>> validate('abc_123')
    True
    >>> validate('_-=*')
    False

    if there is a character that is not alphanumeric or _ return False
    check for unbalanced parenthesis

    >>> validate("abc_(123)")
    True
    >>> validate("a((bc)")
    False
    >>> validate(")(()")
    False

    otherwise return True
    """
    result = True
    i = 0
    brackets = []
    while i < len(text) and result:
        if not text[i].isalnum() and text[i] not in {'_', '(', ')'}:
            result = False
        if text[i] == '(':
            brackets.append(text[i])
        if text[i] == ')':
            try:
                brackets.pop()
            except IndexError:
                result = False
        i += 1

    if len(brackets) > 0:
        result = False

    print
    result


def validate(text):
    """
    >>> validate('abc_123')
    True
    >>> validate('_-=*')
    False

    if there is a character that is not alphanumeric or _ return False
    check for unbalanced parenthesis

    >>> validate("abc_(123)")
    True
    >>> validate("a((bc)")
    False
    >>> validate(")(()")
    False

    otherwise return True
    """

    # Time: O(n)
    # Space: O(1)

    d = {"(": 0, ")": 0}

    result = True
    for i in text:
        if i == "(" or i == ")":
            if d["("] == d[")"] and i == ")":
                result = False
                break
            d[i] += 1

        if i != "_" and not i.isalnum() and i not in d:
            result = False

    if d["("] != d[")"]:
        result = False

    return result
