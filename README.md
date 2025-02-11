HBnB - Technical Documentation

Overview and Purpose

This document provides a detailed overview of the technical architecture of the HBnB application. It outlines the system’s structure, key components, and interactions. The application allows users to manage properties, reviews, and amenities while maintaining a well-organized and scalable design. UML diagrams are included to illustrate how different system layers interact.

Problem Statement

HBnB is a web-based platform that enables users to list, manage, and review rental properties. The main features of the system include:
User Management – Users can register, log in, and modify their profiles.
Property Management – Property owners can create and update listings with details such as title, description, and available amenities.
Review System – Users can leave reviews and ratings for properties they have visited.
Amenity Management – Various amenities (e.g., Wi-Fi, parking) can be added to properties.
The application is built using a layered architecture, ensuring a clear separation between the user interface, business logic, and data storage.

System Requirements and Business Rules

User Model

Users have a first name, last name, email, and password.
A user can be assigned an administrator role using a boolean flag.
Users can register, update profile details, and delete their accounts.

Property (Place) Model

Each property has a title, description, price per night, latitude, and longitude.
Properties are linked to the user who created them (owner).
Users can add, update, remove, and view property listings.
Properties can be associated with multiple amenities.
Review Model

Reviews are linked to both a specific user and property.
Each review includes a rating and a written comment.
Users can create, update, delete, and view reviews for properties.

Amenity Model

Amenities have a name and description.
Users can add, modify, remove, and list amenities for properties.