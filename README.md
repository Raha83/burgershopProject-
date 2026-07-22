# Online Burger Shop – Django

A modular online burger shop website developed using Django. This project provides an online food ordering experience where users can browse the burger menu, add products to their shopping cart, manage product quantities, and view the total price based on updated product prices.

The project is currently **In Progress** and is being developed with a modular and maintainable architecture to ensure clean code organization and scalability.

## Features

- User registration and login
- Email account activation
- Secure password hashing
- Password recovery via email
- Authentication-based access control
- Browse burger products and menu items
- Add products to the shopping cart
- Manage product quantities in the shopping cart
- Calculate and display the total cart price
- Dynamic price calculation based on updated product prices
- Django Admin Panel for managing:
  - Users
  - Products
  - Website settings
  - Other website data
- Comprehensive error handling
- Modular and maintainable project architecture
- Responsive user interface

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- Bootstrap

## Project Structure

The project follows a modular architecture to keep the code organized, maintainable, and scalable. Different parts of the application are separated into dedicated Django apps based on their functionality.

## Installation

Clone the repository:

```bash
git clone https://github.com/Raha83/burgershopProject-.git
```

Navigate to the project directory:

```bash
cd burgershopProject-
```

Install the required dependencies:

```bash
pip install -r req.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open the project in your browser:

```text
http://127.0.0.1:8000/
```

## Admin Panel

The Django Admin Panel is used to manage users, burger products, website settings, and other project data.

## Project Status

**In Progress**

New features and improvements are currently being developed.

## Author

Developed as a Django online burger shop project to practice and demonstrate backend web development, user authentication, database management, shopping cart functionality, and modular application architecture.
