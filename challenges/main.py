def find_common_elements(list1, list2):
    # TODO: use for loops to find values present in both list1 and list2, with no duplicates
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append (item)
    return common_elements