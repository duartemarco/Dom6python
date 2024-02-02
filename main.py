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
    

def spell_fatigue_cost(spell_level, base_fatigue, caster_level):
    try:
        spell_level = int(spell_level)
        base_fatigue = int(base_fatigue)
        caster_level = int(caster_level)

        final_fatigue = base_fatigue / (1 + caster_level - spell_level)

        return f"Fatigue cost: {final_fatigue}"
    
    except ValueError:
        return "Invalid input. Please enter a valid integer."

    

# Example usage:
# num_slaves = input("Enter the number of magic slaves: ")
# result = calculate_path_boost_for_masters(num_slaves)
# print(result)
    
spell_level = input("Inform the spell level:")
base_fatigue = input("Inform the base fatigue for the spell:")
caster_level = input("Inform the caster level:")
print(spell_fatigue_cost(spell_level, base_fatigue, caster_level))
