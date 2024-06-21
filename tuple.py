# Lesson 2: Assignments | Tuples

# 1. Tuple Mastery in Python

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should loop through the list of itineraries and print a formatted string for each. 
# For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], 
# the output should be:

# "Itinerary 1: Alice - From New York to London"
#  "Itinerary 2: Bob - From Tokyo to San Francisco"



# def flight_itineraries(itineraries):    
#     for i, itinerary in enumerate(itineraries):        
#         traveler_name, origin, destination = itinerary        
#     print(f"Itinerary {i+1}: {traveler_name} - From {origin} to {destination}")
# Example usageitineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]flight_itineraries(itineraries)

itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]


def flight (itinerary):
   infos = 0 
   for traveler_name , origin, destination in itinerary: 
      infos = infos + 1
      print (f"Itinerary {infos}': {traveler_name} - From {origin} to {destination}")
       
flight(itinerary)


# ===================================================
# 2. Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancemen

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
  
book_titles = []
def books(newbook):    
  while True:        
 
   
    add_book = input('What book do you want to add? ')        
    if add_book in book_titles:            
          print('You cannot add a duplicate. Please type a different book.')        
    else:            
        library.append((add_book))    
        book_titles.append(add_book)        
        print(library)        
books(None)
