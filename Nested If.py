# Q1 Task 1

place = input("Choose a place: forest or cave? ")

# Fix 1: Use == for comparison
if place == "forest":
    action = input("Climb a tree or cross a river? ")
    # Fix 2: Use == for comparison
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:  # No need to re-assign, use else for the opposite case
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("That's not an option! Choose between forest or cave.")

# Task 2

place = input("Choose a place: forest or cave? ")

# Fix 1: Use == for comparison
if place == "forest":
    action = input("Climb a tree or cross a river? ")
    # Fix 2: Use == for comparison
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:  # No need to re-assign, use else for the opposite case
        print("You found a boat!")
elif place == "cave":
    # Ask about torch
    torch_choice = input("You enter the cave. Do you want to light a torch or proceed in the dark? ")
    # Check torch choice
    if torch_choice == "light a torch":
        print("The torch illuminates strange paintings on the cave walls!")
    else:
        print("You stumble in the darkness and find a hidden passage!")
else:
    print("That's not an option! Choose between forest or cave.")


#Task 3

place = input("Choose a place: forest or cave? ")

# Fix 1: Use == for comparison
if place == "forest":
    action = input("Climb a tree or cross a river? ")
    # Fix 2: Use == for comparison
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:  # No need to re-assign, use else for the opposite case
        print("You found a boat!")
elif place == "cave":
    # Ask about torch
    torch_choice = input("You enter the cave. Do you want to light a torch or proceed in the dark? ")
    # Check torch choice
    if torch_choice == "light a torch":
        print("The torch illuminates strange paintings on the cave walls!")
    else:
        print("You stumble in the darkness and find a hidden passage!")
else:
    # Handle invalid place choice
    pass  # For now, do nothing (placeholder)

# Handle invalid action choice within forest (optional for now)
if place == "forest" and (action != "climb a tree" and action != "cross a river"):
    pass  # Placeholder for future feedback or alternative path


#Q2 Task 1

attendees = int(input("Enter number of attendees: "))  # Convert input to integer
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2

attendees = int(input("Enter number of attendees: "))

# Venue selection
venue = "large hall" if attendees > 100 else "conference room"

# Facility recommendations
facilities = "basic"  # Base assumption
if attendees > 50:
    facilities = "audio system"  # Recommend for medium gatherings
if attendees > 100:
    facilities = "audio system, projector"  # Recommend both for large events

print(f"Venue: {venue}")
print(f"Recommended facilities: {facilities}")


#Task 3

attendees = int(input("Enter number of attendees: "))

# Venue selection
venue = "large hall" if attendees > 100 else "conference room"

# Facility recommendations
facilities = "basic"  # Base assumption
if attendees > 50:
    facilities = "audio system"  # Recommend for medium gatherings
if attendees > 100:
    facilities = "audio system, projector"  # Recommend both for large events

# Catering selection
vegetarian = input("Do you want vegetarian food (yes/no)? ").lower()  # Convert to lowercase for easier comparison

caterer = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"

print(f"Venue: {venue}")
print(f"Recommended facilities: {facilities}")
print(f"Recommended caterer: {caterer}")
