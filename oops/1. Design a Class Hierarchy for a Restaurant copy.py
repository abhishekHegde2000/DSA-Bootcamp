'''

1. Design a Class Hierarchy for a Restaurant

Requirements:

Create a base class Restaurant with properties like name, location, cuisine, and methods like getMenu(), bookTable(), getReviews().
Create subclasses like FastFoodRestaurant, FineDiningRestaurant, and Cafe that inherit from Restaurant and have their own specific properties and methods (e.g., FastFoodRestaurant might have a property specialOffers).
Consider using interfaces to define common behavior (e.g., an interface for Order with methods like placeOrder(), getOrderStatus()).
Implement methods to handle order placement, customer reviews, and table reservations.
Focus Areas:

Inheritance and Polymorphism
Class Composition (if applicable)
Encapsulation and Data Hiding
Method Overriding
2. Implement a Singleton Pattern for a Logger

Requirements:

Design a Logger class that ensures only one instance of the class exists throughout the application.
The Logger should have methods for logging different levels of information (e.g., logInfo(), logWarning(), logError()).
Consider using different logging strategies (e.g., console logging, file logging, database logging) and allowing users to configure the logging level.
Focus Areas:

Singleton Design Pattern
Encapsulation
Flexibility and Configurability
3. Implement a Strategy Pattern for Sorting Algorithms

Requirements:

Create an interface for a SortingStrategy with a method like sort(data).
Implement different sorting algorithms (e.g., Bubble Sort, Quick Sort, Merge Sort) as classes that implement the SortingStrategy interface.
Create a Sorter class that accepts a SortingStrategy object and uses it to sort an array of data.
Focus Areas:

Strategy Design Pattern
Interface-Based Programming
Algorithm Implementation and Efficiency
4. Design a Class for a Shopping Cart

Requirements:

The ShoppingCart class should have methods for adding items, removing items, calculating the total price, applying discounts, and handling checkout.
Consider using the Decorator pattern to add features like taxes, shipping costs, and gift wrapping.
Implement proper error handling and validation for invalid inputs.
Focus Areas:

Object-Oriented Design Principles
Decorator Pattern (if applicable)
Error Handling and Validation
5. Implement a State Machine for a Traffic Light

Requirements:

Design a TrafficLight class that models the behavior of a traffic light using a state machine.
The TrafficLight should have states like Red, Yellow, Green and transitions between these states.
Consider using the State pattern to represent the different states and transitions.
Focus Areas:

State Design Pattern
Finite State Machines
Behavioral Modeling
Tips for Solving These Problems:

Focus on Clean Code: Use meaningful variable names, proper indentation, and comments to make your code readable and maintainable.
Write Unit Tests: Write unit tests to verify the correctness of your implementations.
Consider Performance: Analyze the time and space complexity of your solutions.
Explain Your Design Choices: Be prepared to explain your design decisions and trade-offs during an interview.
I'm ready when you are! Choose a problem, and let's see your solution. I'll provide feedback and help you refine your code. Good luck!

'''


# 1 Design a Class Hierarchy for a Restaurant

# Base class Restaurant


class Restaurant:
    """A base class representing a restaurant."""

    def __init__(self, name, location, cuisine):
        """Initializes the restaurant with its name, location, and cuisine type."""
        self.name = name
        self.location = location
        self.cuisine = cuisine

    def get_menu(self):
        """Returns a menu of the restaurant."""
        return f"Menu of {self.name}: \n- Dish 1\n- Dish 2\n- Dish 3"

    def book_table(self, num_people):
        """Books a table at the restaurant for a given number of people."""
        if num_people <= 0:
            return "Invalid number of people. Please provide a positive number."
        return f"Table booked for {num_people} people at {self.name}."

    def get_reviews(self):
        """Returns the reviews for the restaurant."""
        return f"Reviews for {self.name}: \n- Excellent food!\n- Great ambiance!"


class FastFoodRestaurant(Restaurant):
    """A subclass representing a fast-food restaurant."""

    def __init__(self, name, location, cuisine, special_offers):
        """Initializes the fast food restaurant with special offers."""
        super().__init__(name, location, cuisine)
        self.special_offers = special_offers

    def get_menu(self):
        """Returns the fast food menu with special offers."""
        return f"Menu of {self.name}: \n- Burger\n- Fries\n- Soft Drink\nSpecial Offers: {', '.join(self.special_offers)}"

    def book_table(self, num_people):
        """Books a table for a fast-food restaurant, with limited options."""
        if num_people <= 0:
            return "Fast food restaurant does not accept bookings for 0 or negative people."
        return f"Fast food seating for {num_people} people at {self.name}."

    def get_reviews(self):
        """Returns the reviews for the fast food restaurant."""
        return f"Reviews for {self.name}: \n- Quick service!\n- Affordable prices!"


class FineDiningRestaurant(Restaurant):
    """A subclass representing a fine dining restaurant."""

    def __init__(self, name, location, cuisine, wine_list):
        """Initializes the fine dining restaurant with a wine list."""
        super().__init__(name, location, cuisine)
        self.wine_list = wine_list

    def get_menu(self):
        """Returns the fine dining menu with wine selection."""
        return f"Menu of {self.name}: \n- Steak\n- Lobster\n- Risotto\nWine List: {', '.join(self.wine_list)}"

    def book_table(self, num_people):
        """Books a fine dining table with exclusive options."""
        if num_people <= 0:
            return "Fine dining restaurant requires at least one person for booking."
        return f"Exclusive table booked for {num_people} people at {self.name}."

    def get_reviews(self):
        """Returns the reviews for the fine dining restaurant."""
        return f"Reviews for {self.name}: \n- Outstanding service!\n- Gourmet experience!"


class Cafe(Restaurant):
    """A subclass representing a cafe."""

    def __init__(self, name, location, cuisine, outdoor_seating):
        """Initializes the cafe with outdoor seating information."""
        super().__init__(name, location, cuisine)
        self.outdoor_seating = outdoor_seating

    def get_menu(self):
        """Returns the cafe menu with a focus on beverages."""
        return f"Menu of {self.name}: \n- Coffee\n- Tea\n- Pastries\nOutdoor Seating: {'Available' if self.outdoor_seating else 'Not Available'}"

    def book_table(self, num_people):
        """Books a table at the cafe, considering outdoor seating."""
        if num_people <= 0:
            return "Cafe bookings require at least one person."
        seating = "outdoor" if self.outdoor_seating else "indoor"
        return f"{seating.capitalize()} seating booked for {num_people} people at {self.name}."

    def get_reviews(self):
        """Returns the reviews for the cafe."""
        return f"Reviews for {self.name}: \n- Cozy atmosphere!\n- Best coffee in town!"

# Test cases


def test_restaurant_classes():
    """Test the behavior of the restaurant subclasses."""

    # Create instances of each restaurant type
    restaurant = Restaurant("The Gourmet Place", "New York", "Italian")
    fast_food = FastFoodRestaurant("Quick Bites", "Chicago", "American", [
                                   "Discount Combo", "Free Fries"])
    fine_dining = FineDiningRestaurant("Le Luxe", "Paris", "French", [
                                       "Chardonnay", "Cabernet Sauvignon"])
    cafe = Cafe("Coffee Corner", "Seattle", "Cafe", True)

    # Test methods for Restaurant
    print(restaurant.get_menu())
    print(restaurant.book_table(4))
    print(restaurant.get_reviews())

    # Test methods for FastFoodRestaurant
    print(fast_food.get_menu())
    print(fast_food.book_table(2))
    print(fast_food.get_reviews())

    # Test methods for FineDiningRestaurant
    print(fine_dining.get_menu())
    print(fine_dining.book_table(2))
    print(fine_dining.get_reviews())

    # Test methods for Cafe
    print(cafe.get_menu())
    print(cafe.book_table(3))
    print(cafe.get_reviews())


# Run the test cases
test_restaurant_classes()
