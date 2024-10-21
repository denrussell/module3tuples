'''
Objective: The aim of this assignment is to deepen your understanding of 
tuples in Python.

Task 1: Formatting Flight Itineraries 

Create a Python function that takes a 
list of tuples as an argument. Each tuple contains information about a 
flight itinerary: (traveler_name, origin, destination). The function should 
format and return a string that lists each itinerary. For example, if the 
input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
'''
# I just need to create a format that returns with name, origin, destination.
def format_itinerary(flight_itinerary):
    formatted_list = []

# I need a for loop to iterate each tuple and index location
    for i, (traveler_name, origin, destination) in enumerate(flight_itinerary, 1):
        formatted_list.append(f"Itinerary {i}: {traveler_name} – From {origin} to {destination}")
    
    return "\n".join(formatted_list)

# sample given list of tuples
flight_itinerary = [("Alice", "New York", "London"),
                    ("Bob", "Tokyo", "San Francisco")]


result = format_itinerary(flight_itinerary)
print (result)
# let's test and add another itinerary
more_flights =  flight_itinerary.append(("Dennis", "San Francisco", "Las Vegas"))
result = format_itinerary(flight_itinerary)
print (f"\n{result}")
