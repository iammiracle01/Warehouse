

# Warehouse API

Welcome to the Warehouse API, a robust API built with Flask to manage warehouse operations efficiently. This API supports full CRUD (Create, Read, Update, Delete) functionalities for managing sections and products within a warehouse.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [Sections](#sections)
  - [Products](#products)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Warehouse API provides endpoints to manage products and sections within a warehouse. It supports the addition, retrieval, updating, and deletion of both products and sections, ensuring that warehouse operations can be handled efficiently.

## Features

- **Create Section and Product**: Add new sections and products to the warehouse.
- **Read Sections and Products**: Retrieve details of all sections and products or specific ones.
- **Update Section and Product**: Update information of existing sections and products.
- **Delete Section and Product**: Remove sections and products from the warehouse.

## Installation

To get started with the Warehouse API, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/warehouse-api.git
    cd warehouse-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    flask run
    ```

## Usage

Once the application is running, you can interact with the API using tools like `curl`, `Postman`, or any HTTP client. The base URL for the API is `http://localhost:5000`.

## API Endpoints

### Sections

#### 1. Create a Section

- **URL**: `/sections`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "section_name": "Electronics"
    }
    ```
- **Response**:
    ```json
    {
        "section_id": 1,
        "section_name": "Electronics",
        "created_at": "2023-01-01T00:00:00"
    }
    ```

#### 2. Retrieve All Sections

- **URL**: `/sections`
- **Method**: `GET`
- **Response**:
    ```json
    [
        {"section_id": 1, "section_name": "Electronics"},
        {"section_id": 2, "section_name": "Food and Beverages"}
    ]
    ```

#### 3. Retrieve a Single Section

- **URL**: `/sections/<int:section_id>`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "section_id": 1,
        "section_name": "Electronics"
    }
    ```

#### 4. Update a Section

- **URL**: `/sections/<int:section_id>`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "section_name": "Updated Section Name"
    }
    ```
- **Response**:
    ```json
    {
        "section_id": 1,
        "section_name": "Updated Section Name"
    }
    ```

#### 5. Delete a Section

- **URL**: `/sections/<int:section_id>`
- **Method**: `DELETE`
- **Response**:
    ```json
    {
        "message": "Section deleted successfully."
    }
    ```

### Products

#### 1. Create a Product

- **URL**: `/products`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "section_id": 1,
        "product_name": "Laptop",
        "quantity_in_stock": 50,
        "price_per_unit": 1000,
        "is_product_available": true
    }
    ```
- **Response**:
    ```json
    {
        "product_id": 1,
        "section_id": 1,
        "product_name": "Laptop",
        "quantity_in_stock": 50,
        "price_per_unit": 1000,
        "is_product_available": true,
        "created_at": "2023-01-01T00:00:00"
    }
    ```

#### 2. Retrieve All Products

- **URL**: `/products`
- **Method**: `GET`
- **Response**:
    ```json
    [
        {
            "product_id": 1,
            "section_id": 1,
            "product_name": "Laptop",
            "quantity_in_stock": 50,
            "price_per_unit": 1000,
            "is_product_available": true
        },
        {
            "product_id": 2,
            "section_id": 2,
            "product_name": "Apple",
            "quantity_in_stock": 100,
            "price_per_unit": 2,
            "is_product_available": true
        }
    ]
    ```

#### 3. Retrieve a Single Product

- **URL**: `/products/<int:product_id>`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "product_id": 1,
        "section_id": 1,
        "product_name": "Laptop",
        "quantity_in_stock": 50,
        "price_per_unit": 1000,
        "is_product_available": true
    }
    ```

#### 4. Update a Product

- **URL**: `/products/<int:product_id>`
- **Method**: `PUT`
- **Request Body**:
    ```json
    {
        "section_id": 1,
        "product_name": "Updated Product Name",
        "quantity_in_stock": 60,
        "price_per_unit": 1200,
        "is_product_available": true
    }
    ```
- **Response**:
    ```json
    {
        "product_id": 1,
        "section_id": 1,
        "product_name": "Updated Product Name",
        "quantity_in_stock": 60,
        "price_per_unit": 1200,
        "is_product_available": true
    }
    ```

#### 5. Delete a Product

- **URL**: `/products/<int:product_id>`
- **Method**: `DELETE`
- **Response**:
    ```json
    {
        "message": "Product deleted successfully."
    }
    ```

This README provides a comprehensive overview of the Warehouse API, including installation steps, usage instructions, and detailed API endpoint documentation.
