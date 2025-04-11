# Jopek-backend
corresponding frontend: https://github.com/Hakkene/Jopek-frontend  
[![Coverage Status](https://coveralls.io/repos/github/Hakkene/Jopek-backend/badge.svg?branch=main)](https://coveralls.io/github/Hakkene/Jopek-backend?branch=main)



This is a back-end eCommerce web app built using **Django**, deisgned for a board game shop with rental service and powered by a **PostgreSQL** db. Its highlight features include:
- Product Management: Fetch all products or filter by category, name, or rental availability. Retrieve product details by slug.
- User Authentication: Register new accounts and authenticate users via token-based login.
- Order Processing: Submit cart contents and order details, including pricing and shipping information.
- Rental System: Display available rental items and process rental requests.
- Comments & Reviews: Fetch product reviews and allow authenticated users to post comments.
- User Profiles: Retrieve user details, including order and rental history.
- Admin panel

# Endpoints
Full endpoint documentation available at https://jopek.docs.apiary.io/

- **Products**  
  - `GET /products` – Retrieve all products (filters: category, name, rental availability)  
  - `GET /products/{slug}` – Retrieve product details by slug  

- **User Accounts**  
  - `POST /register` – Register a new user (username, password)  
  - `POST /login` – Authenticate user, return token  

- **Orders**  
  - `POST /orders` – Create a new order (price, address, notes)  
  - `POST /orders/{order_id}/cart` – Submit cart contents (product, quantity)  

- **Rentals**  
  - `GET /rentals` – Retrieve available rental products  
  - `POST /rentals` – Rent a product (requires authentication)  

- **Comments**  
  - `GET /comments` – Retrieve all comments  
  - `POST /comments` – Post a new comment (requires authentication)  

- **User Profile**  
  - `GET /profile` – Retrieve user details, order, and rental history  


# Installation
This app contains relevant docker files allowing to launch it inside a container:

1. Install Docker/Docker desktop
2. Use "docker compose up" in console
3. http://localhost:8000/


#
![Diagram ER fizyczny bazy danych](https://github.com/user-attachments/assets/593afaf1-7a7a-42ea-a108-9ec13c63817b)

>db's entity relationship diagram (ERD)




