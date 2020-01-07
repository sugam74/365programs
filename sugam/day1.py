#Remove duplicate item/number from an array
duplicate_lists = [1, 4, 4, 1, 5, 7, 3, 5, 9]
no_duplicate = []
for row in duplicate_lists:
    if not row in no_duplicate:
        no_duplicate.append(row)

print(no_duplicate)

# how simple is this