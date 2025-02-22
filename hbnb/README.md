
# HBnB - Technical Documentation

## Overview  
HBnB is a web-based platform designed to simplify the process of managing rental properties, user reviews, and available amenities. The system provides a structured way for users to register, list properties, leave reviews, and manage various amenities associated with rental places.
The application is built using a layered architecture, which helps separate different concerns within the system:

**Presentation Layer**  - Handles user interactions through APIs and ensures smooth communication with the backend.

**Business Logic Layer** – Implements the core functionality, such as processing user data, managing property listings, and enforcing system rules.

**Data Persistence Layer** – Responsible for storing and retrieving data efficiently, ensuring consistency and reliability.

This structured approach improves scalability, maintainability, and security, making it easier to extend the system with new features in the future. The design also follows object-oriented principles, making the codebase modular and easy to manage.

## Features  

### **User Management**  
- Users can **sign up, log in, and update their profile**.  
- Each user has a **first name, last name, email, and password**.  
- Some users can be designated as **administrators**.  
- Users have the ability to **delete their accounts**.  

### **Property Management**  
- Users can **create, update, and delete properties**.  
- Each property includes a **title, description, price, latitude, and longitude**.  
- Properties are linked to the **user (owner) who created them**.  
- Properties can have **multiple amenities**.  

### **Review System**  
- Users can **leave reviews and ratings** for properties they have visited.  
- Reviews are associated with both a **specific user and property**.  
- Reviews can be **created, updated, deleted, and viewed**.  

### **Amenity Management**  
- Amenities have a **name and description**.  
- Users can **add, modify, remove, and list** amenities associated with properties.

  ## UML Documentation and Diagrams  

### High-Level Package Diagram  

The HBnB application is structured using a **three-layered architecture**, ensuring a clear separation of concerns and maintainability. These layers define how the system handles user interactions, business logic, and data storage.  

### Architectural Layers  

#### **Presentation Layer**  
- Acts as the entry point for user interactions via APIs.  
- Manages requests for features like user authentication, property creation, and review management.  

#### **Business Logic Layer**  
- Contains the core functionalities and rules governing how data is processed.  
- Implements key operations such as validation, authorization, and interactions between different entities.  

#### **Persistence Layer**  
- Responsible for data storage and retrieval from the database.  
- Uses a structured approach to manage records efficiently.  

### **Facade Pattern for Layer Communication**  
To ensure a **clean separation of concerns**, the **Facade pattern** is used as an intermediary between layers. This approach simplifies interactions by allowing each layer to communicate in a structured manner without directly depending on lower-level implementations.  

A **high-level package diagram** is included in this repository to visually represent these three core layers, showcasing their roles and how they interact within the HBnB system.
![HBNB drawio](https://github.com/user-attachments/assets/9e723aea-567c-46b8-a5bd-68c45d3ead3c)


### **Detailed Class Diagram for Business Logic Layer**
The class diagram for the Business Logic Layer consists of four main entities: User, Place, Review, and Amenity.
![Baseclass drawio](https://github.com/user-attachments/assets/a7975db8-acfa-4c16-a328-2f18ff1cca85)
#### **1. Base Class**  
The `Base Class` serves as the foundation for all other entities. It provides the following common attributes:  
- `ID (uuid)`: A unique identifier for each object.  
- `created_at (datetime)`: Timestamp of object creation.  
- `updated_at (datetime)`: Timestamp of the last update.


#### **2. User Class**  
The `User` class represents individuals using the system. Each user has:  
- `first_name, last_name (str)`: Basic identity information.  
- `email (str)`: Unique email address for authentication.  
- `password (str)`: Encrypted password for login.  
- `is_admin (Boolean)`: Determines whether the user has administrative privileges.  

##### **Methods**:  
- `register()`: Creates a new user.  
- `update()`: Modifies user details.  
- `delete()`: Removes the user.  
- `list()`: Retrieves user records.

#### **3. Place Class**  
The `Place` class represents rental properties listed on the platform. Each place has:  
- `title, description (str)`: Basic details of the place.  
- `price (float)`: Cost per night.  
- `latitude, longitude (float)`: Geographical location.  
- `owner_id (uuid)`: Links the place to its owner (User).  
- `list_of_amenities (Amenity[])`: Stores associated amenities.  
- `list_of_reviews (Review[])`: Stores reviews related to the place.  

##### **Methods**:  
- `create()`: Adds a new place.  
- `update()`: Modifies place details.  
- `delete()`: Removes a place from the system.  
- `list()`: Displays available places.  
- `add_amenity()`: Associates an amenity with a place.  

#### **4. Review Class**  
The `Review` class allows users to leave feedback on places. Each review includes:  
- `user_id (uuid)`: The reviewer’s unique identifier.  
- `place_id (uuid)`: The place being reviewed.  
- `comment (str)`: The review text.  
- `rating (int)`: A numerical rating.  

##### **Methods**:  
- `create()`: Adds a new review.  
- `update()`: Modifies an existing review.  
- `delete()`: Removes a review.  
- `list()`: Displays reviews for a place.  

#### **5. Amenity Class**  
The `Amenity` class represents facilities or services available at a place, such as Wi-Fi, parking, or a swimming pool. It includes:  
- `name (str)`: The amenity’s title.  
- `description (str)`: A short explanation of the amenity.  

##### **Methods**:  
- `create()`: Adds a new amenity.  
- `update()`: Modifies an existing amenity.  
- `delete()`: Removes an amenity.  
- `list()`: Displays available amenities.

### **Relationships and Associations**  

- **User to Place (1 → *)**: A user can own multiple places.  
- **Place to Review (1 → *)**: A place can have multiple reviews.  
- **Place to Amenity (1 → *)**: A place can have multiple amenities.  
- **Review to User (1 → *)**: A user can write multiple reviews.


# User Registration Process
When a user wants to register on the application, they fill in their details such as name, email, and password and send a request to the API. The API receives this information and passes it to the business logic layer to verify if the data is valid and correctly formatted. Once everything is confirmed to be in order, the system sends the information to the database to be stored. When the storage process is successfully completed, the database returns a confirmation to the system, which then notifies the API that the registration has been successful. Finally, the API sends a response back to the user, informing them that their account has been created or notifying them of any errors that may have occurred during the process.
![User Registration-Page-4 drawio](https://github.com/user-attachments/assets/e6d8b0ca-b03e-4ec9-bbbb-d23eddd01380)


# Place Creation Flow
Once a user is registered and wants to create a new place, such as an apartment or a listing, they fill in the necessary details and send a request to the API. Before proceeding with the creation of the place, the API first verifies whether the user exists in the database. To do this, it queries the business logic layer, which then communicates with the database to check for the user's existence. If the user is found, the API continues with the creation process by passing the place details to the place management model, which then stores this information in the database. Once the place is successfully stored, the database sends back a confirmation, and the API notifies the user that the place has been created successfully or informs them of any errors that may have occurred.
![BusinessLogic drawio](https://github.com/user-attachments/assets/7f69631c-78cf-4c3a-aef9-0ec9bff86571)

# Review Submission Process
In the "Review Submission" process, a user submits a review for a place (e.g., an apartment or listing) in the HBnB application. The sequence of events unfolds as follows:
The user starts by filling out the review form and submitting a request with the review details, including text and rating for the place.
The API receives the request and validates the provided data, ensuring that all required fields are filled out and properly formatted.
If the data is valid, the API passes the request to the Business Logic Layer for further processing.
The Business Logic Layer verifies whether the user has permission to submit a review for the place and checks whether the place exists in the database.
If everything is in order, the Business Logic Layer creates a new review object and prepares it for storage.
The review object is then sent to the Persistence Layer (Database), where the review is stored, linking it to the relevant place.
After successfully storing the review, the database sends a confirmation response back to the Business Logic Layer.
The Business Logic Layer processes the confirmation and sends a success message back to the API.
Finally, the API responds to the user, confirming that their review has been successfully submitted and stored, or notifying them of any errors encountered during the process, such as missing data or an invalid place.
This process ensures that all interactions between the user, application layers, and database are handled securely and efficiently.

![ReviewSub drawio](https://github.com/user-attachments/assets/23490210-abef-46e5-9d08-7d6651e1fe46)

# Fetching a List of Places - Sequence Diagram
In the "Fetching a List of Places" process, a user requests a list of places from the HBnB application based on certain criteria, such as location, price range, or amenities. The sequence diagram illustrates the interaction between the Presentation Layer, Business Logic Layer, and Persistence Layer to handle this request.
The user interacts with the application interface (Presentation Layer) to specify the criteria for the list of places they are looking for, such as location or price. After the user submits the request, the API in the Presentation Layer receives it and validates the input data, ensuring that the criteria are properly formatted. Once validated, the request is forwarded to the Business Logic Layer for further processing.
The Business Logic Layer processes the criteria and may apply additional business rules, such as filtering based on availability or other constraints. It then queries the Persistence Layer (Database) to retrieve the list of places that match the criteria. The database processes the query and returns the relevant places back to the Business Logic Layer.
Once the Business Logic Layer receives the data, it formats it as needed and sends the list of places to the API. Finally, the API responds to the user with the list of places that match the specified criteria or informs them if no results were found.
This process ensures that the flow of information between the different layers of the application is smooth, efficiently handling user requests and delivering the appropriate data.

![Fetchinglist drawio](https://github.com/user-attachments/assets/49633450-c30d-4023-8284-b599715b3d20)

