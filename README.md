
# HBnB - Technical Documentation

## Overview  
HBnB is a web-based platform designed to simplify the process of managing rental properties, user reviews, and available amenities. The system provides a structured way for users to register, list properties, leave reviews, and manage various amenities associated with rental places.
The application is built using a layered architecture, which helps separate different concerns within the system:
## Presentation Layer  
- Handles user interactions through APIs and ensures smooth communication with the backend.
## Business Logic Layer 
– Implements the core functionality, such as processing user data, managing property listings, and enforcing system rules.
## Data Persistence Layer 
– Responsible for storing and retrieving data efficiently, ensuring consistency and reliability.
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

