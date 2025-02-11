
# HBnB - Technical Documentation

## Overview  
HBnB is a web-based application that allows users to manage rental properties, reviews, and amenities. This document outlines the system’s architecture, core functionalities, and design principles. The application follows a **layered architecture**, ensuring a clear separation between the presentation layer, business logic, and data persistence.  

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
![HBNB drawio](https://github.com/user-attachments/assets/9e723aea-567c-46b8-a5bd-68c45d3ead3c)
