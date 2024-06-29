def contains_substring(main_str, sub_str):
    if len(sub_str) > len(main_str):
        return False

    # Loop through each character in the main string
    for i in range(len(main_str)):
        # If the first character of the substring matches the current character in the main string
        if sub_str[0] == main_str[i]:
            if len(main_str) - i >= len(sub_str):
                match_found = True
                # Check the remaining characters of the substring
                for j in range(1, len(sub_str)):
                    if main_str[i + j] != sub_str[j]:
                        match_found = False
                        break
                if match_found:
                    return True

    # If the substring is not find, return False
    return False

# Test cases
print(contains_substring("hello", "llo"))  #Output: True
print(contains_substring("hello", "olh"))  #Output: False
