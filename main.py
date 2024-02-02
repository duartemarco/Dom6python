def calculate_path_boost_for_masters(num_slaves):
    try:
        num_slaves = int(num_slaves)

        if num_slaves <= 0:
            return "Number of slaves must be a positive integer."

        max_path_boost = 6
        path_boost = 0

        while num_slaves >= 2 and path_boost < max_path_boost:
            num_slaves //= 2
            path_boost += 1

        return f"Path Boost for Masters: {path_boost}"

    except ValueError:
        return "Invalid input. Please enter a valid integer."

# Example usage:
num_slaves = input("Enter the number of magic slaves: ")
result = calculate_path_boost_for_masters(num_slaves)
print(result)