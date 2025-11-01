class ListHelper:

    @staticmethod                                # Static method: no self, no cls needed
    def greatest_frequency(my_list):
        max_count = 0                            # Track the highest frequency found
        most_common = None                       # Track the item with the highest frequency

        for item in my_list:                     # Go through each item in the list
            freq = my_list.count(item)           # Count how many times this item appears
            if freq > max_count:                 # If this item appears more times than current max
                max_count = freq                 # Update the max_count
                most_common = item               # Update the most_common item
        return most_common                       # Return the item with greatest frequency

    @staticmethod
    def doubles(my_list):
        unique_items = set(my_list)              # Convert to set → only unique items
        doubles_count = 0                        # Counter for items appearing at least twice

        for item in unique_items:                # Check each unique item once
            if my_list.count(item) >= 2:         # If the item appears 2 or more times
                doubles_count += 1               # Increase counter
        return doubles_count                     # Return total count of such items

# --- Main Program ---
numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print()
print(ListHelper.greatest_frequency(numbers))   # → 5 (appears most often)
print(ListHelper.doubles(numbers))              # → 3 (items 1, 3, 5 each appear >=2 times)
