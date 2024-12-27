/*

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

*/

class Restaurant {
  private _name: string;
  private _location: string;
  private _cuisine: string;

  /**
   * A base class representing a restaurant.
   * @param {string} name - The name of the restaurant.
   * @param {string} location - The location of the restaurant.
   * @param {string} cuisine - The type of cuisine served at the restaurant.
   */
  constructor(name: string, location: string, cuisine: string) {
    this._name = name;
    this._location = location;
    this._cuisine = cuisine;
  }

  /**
   * Gets the name of the restaurant.
   * @return {string} The name of the restaurant.
   */
  get name(): string {
    return this._name;
  }

  /**
   * Sets the name of the restaurant.
   * @param {string} name - The name to set for the restaurant.
   */
  set name(name: string) {
    this._name = name;
  }

  /**
   * Gets the location of the restaurant.
   * @return {string} The location of the restaurant.
   */
  get location(): string {
    return this._location;
  }

  /**
   * Sets the location of the restaurant.
   * @param {string} location - The location to set for the restaurant.
   */
  set location(location: string) {
    this._location = location;
  }

  /**
   * Gets the type of cuisine served at the restaurant.
   * @return {string} The type of cuisine.
   */
  get cuisine(): string {
    return this._cuisine;
  }

  /**
   * Sets the type of cuisine.
   * @param {string} cuisine - The cuisine to set.
   */
  set cuisine(cuisine: string) {
    this._cuisine = cuisine;
  }

  /**
   * Returns the menu of the restaurant.
   * @return {string} A sample menu of the restaurant.
   */
  getMenu(): string {
    return `Menu of ${this._name}: \n- Dish 1\n- Dish 2\n- Dish 3`;
  }

  /**
   * Books a table for a given number of people.
   * @param {number} numPeople - The number of people to book the table for.
   * @return {string} Confirmation of the table booking.
   * @throws {Error} Throws an error if the number of people is less than or equal to 0.
   */
  bookTable(numPeople: number): string {
    if (numPeople <= 0) {
      throw new Error(
        "Invalid number of people. Please provide a positive number."
      );
    }
    return `Table booked for ${numPeople} people at ${this._name}.`;
  }

  /**
   * Returns the reviews for the restaurant.
   * @return {string} Reviews for the restaurant.
   */
  getReviews(): string {
    return `Reviews for ${this._name}: \n- Excellent food!\n- Great ambiance!`;
  }
}

class FastFoodRestaurant extends Restaurant {
  private _specialOffers: string[];

  /**
   * A subclass representing a fast-food restaurant.
   * @param {string} name - The name of the restaurant.
   * @param {string} location - The location of the restaurant.
   * @param {string} cuisine - The type of cuisine served at the restaurant.
   * @param {Array<string>} specialOffers - List of special offers available at the restaurant.
   */
  constructor(
    name: string,
    location: string,
    cuisine: string,
    specialOffers: string[]
  ) {
    super(name, location, cuisine);
    this._specialOffers = specialOffers;
  }

  /**
   * Gets the special offers available at the fast food restaurant.
   * @return {string} A string representation of the menu with special offers.
   */
  getMenu(): string {
    return `Menu of ${
      this.name
    }: \n- Burger\n- Fries\n- Soft Drink\nSpecial Offers: ${this._specialOffers.join(
      ", "
    )}`;
  }

  /**
   * Books a table for a fast food restaurant.
   * @param {number} numPeople - The number of people to book the table for.
   * @return {string} Confirmation of the table booking.
   * @throws {Error} Throws an error if the number of people is less than or equal to 0.
   */
  bookTable(numPeople: number): string {
    if (numPeople <= 0) {
      throw new Error(
        "Fast food restaurant does not accept bookings for 0 or negative people."
      );
    }
    return `Fast food seating for ${numPeople} people at ${this.name}.`;
  }

  /**
   * Returns the reviews for the fast food restaurant.
   * @return {string} Reviews for the fast food restaurant.
   */
  getReviews(): string {
    return `Reviews for ${this.name}: \n- Quick service!\n- Affordable prices!`;
  }
}

class FineDiningRestaurant extends Restaurant {
  private _wineList: string[];

  /**
   * A subclass representing a fine dining restaurant.
   * @param {string} name - The name of the restaurant.
   * @param {string} location - The location of the restaurant.
   * @param {string} cuisine - The type of cuisine served at the restaurant.
   * @param {Array<string>} wineList - List of wines available at the restaurant.
   */
  constructor(
    name: string,
    location: string,
    cuisine: string,
    wineList: string[]
  ) {
    super(name, location, cuisine);
    this._wineList = wineList;
  }

  /**
   * Gets the menu of the fine dining restaurant.
   * @return {string} A string representation of the menu with wine selection.
   */
  getMenu(): string {
    return `Menu of ${
      this.name
    }: \n- Steak\n- Lobster\n- Risotto\nWine List: ${this._wineList.join(
      ", "
    )}`;
  }

  /**
   * Books a table for a fine dining restaurant.
   * @param {number} numPeople - The number of people to book the table for.
   * @return {string} Confirmation of the table booking.
   * @throws {Error} Throws an error if the number of people is less than or equal to 0.
   */
  bookTable(numPeople: number): string {
    if (numPeople <= 0) {
      throw new Error(
        "Fine dining restaurant requires at least one person for booking."
      );
    }
    return `Exclusive table booked for ${numPeople} people at ${this.name}.`;
  }

  /**
   * Returns the reviews for the fine dining restaurant.
   * @return {string} Reviews for the fine dining restaurant.
   */
  getReviews(): string {
    return `Reviews for ${this.name}: \n- Outstanding service!\n- Gourmet experience!`;
  }
}

class Cafe extends Restaurant {
  private _outdoorSeating: boolean;

  /**
   * A subclass representing a cafe.
   * @param {string} name - The name of the cafe.
   * @param {string} location - The location of the cafe.
   * @param {string} cuisine - The type of cuisine served at the cafe.
   * @param {boolean} outdoorSeating - Whether the cafe offers outdoor seating.
   */
  constructor(
    name: string,
    location: string,
    cuisine: string,
    outdoorSeating: boolean
  ) {
    super(name, location, cuisine);
    this._outdoorSeating = outdoorSeating;
  }

  /**
   * Gets the menu of the cafe.
   * @return {string} A string representation of the menu with beverage options.
   */
  getMenu(): string {
    return `Menu of ${
      this.name
    }: \n- Coffee\n- Tea\n- Pastries\nOutdoor Seating: ${
      this._outdoorSeating ? "Available" : "Not Available"
    }`;
  }

  /**
   * Books a table at the cafe, considering outdoor seating.
   * @param {number} numPeople - The number of people to book the table for.
   * @return {string} Confirmation of the table booking.
   * @throws {Error} Throws an error if the number of people is less than or equal to 0.
   */
  bookTable(numPeople: number): string {
    if (numPeople <= 0) {
      throw new Error("Cafe bookings require at least one person.");
    }
    const seating = this._outdoorSeating ? "outdoor" : "indoor";
    return `${
      seating.charAt(0).toUpperCase() + seating.slice(1)
    } seating booked for ${numPeople} people at ${this.name}.`;
  }

  /**
   * Returns the reviews for the cafe.
   * @return {string} Reviews for the cafe.
   */
  getReviews(): string {
    return `Reviews for ${this.name}: \n- Cozy atmosphere!\n- Best coffee in town!`;
  }
}

// Test cases
function testRestaurantClasses(): void {
  // Create instances of each restaurant type
  const restaurant = new Restaurant("The Gourmet Place", "New York", "Italian");
  const fastFood = new FastFoodRestaurant(
    "Quick Bites",
    "Chicago",
    "American",
    ["Discount Combo", "Free Fries"]
  );
  const fineDining = new FineDiningRestaurant("Le Luxe", "Paris", "French", [
    "Chardonnay",
    "Cabernet Sauvignon",
  ]);
  const cafe = new Cafe("Coffee Corner", "Seattle", "Cafe", true);

  try {
    console.log(restaurant.getMenu());
    console.log(restaurant.bookTable(4));
    console.log(restaurant.getReviews());

    console.log(fastFood.getMenu());
    console.log(fastFood.bookTable(2));
    console.log(fastFood.getReviews());

    console.log(fineDining.getMenu());
    console.log(fineDining.bookTable(2));
    console.log(fineDining.getReviews());

    console.log(cafe.getMenu());
    console.log(cafe.bookTable(3));
    console.log(cafe.getReviews());
  } catch (error) {
    console.error("Error:", (error as Error).message);
  }
}

// Run the test cases
testRestaurantClasses();
