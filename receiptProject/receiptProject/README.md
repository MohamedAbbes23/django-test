# Receipt App

## Overview

The Receipt App is a simple web application designed to manage receipts. Users can perform CRUD (Create, Read, Update, Delete) operations on their receipts, view a list of all receipts on the home page, and manage their personal information through authentication and authorization using the built-in User model.

## Features

- **User Authentication and Authorization**
- **CRUD Operations on Receipts**
- **Home Page with List of Receipts**
- **Receipt Model with the Following Fields:**
  - User (foreign key to the built-in User model)
  - Store Name (char field)
  - Date of Purchase (date type)
  - Item List (text field)
  - Total Amount (float field)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/receipt-app.git
   cd receipt-app

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   
3. **Apply database migrations:**

   ```bash
   python manage.py migrate

4. **Create a superuser account for initial login:**

   ```bash
   python manage.py createsuperuser

5. **Start the development server:**

   ```bash
   python manage.py runserver

5. **Access the application at http://localhost:8000**


## Usage
1. **Visit the registration page to create a new user account.**
2. **Log in using your credentials.**
3. **Add, view, update, or delete your receipts from the respective pages.**

# Models 

## Receipt Model 
The Receipt model is the core entity in the app, representing individual receipts. It has the following fields: 
- **User**: Foreign key referencing the built-in User model. 
- **Store Name**: Char field for the name of the store. 
- **Date of Purchase**: Date field for the date of the purchase. 
- **Item List**: Text field to list the purchased items. 
- **Total Amount**: Float field for the total amount of the receipt.


## Contributing

If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch for your feature or bug fix.**
3. **Make your changes and submit a pull request.**

