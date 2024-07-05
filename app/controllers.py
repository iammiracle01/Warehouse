import logging
from flask import Blueprint, jsonify, request, render_template
from flasgger import swag_from
from jsonschema import validate, ValidationError
from .services import SectionService, ProductService
from .exceptions import (
    SectionNotFoundException,
    SectionAlreadyExistsException,
    ProductNotFoundException,
    ProductAlreadyExistsException,
    InvalidSectionException,
)
from .schema import section_schema, product_schema

controller_logger = logging.getLogger('controller_logger')
main = Blueprint("main", __name__)


def handle_exception(e, status_code):
    controller_logger.error(str(e))
    return jsonify({"error": str(e)}), status_code

@main.route("/")
def home():
    controller_logger.info("Home page accessed")
    return render_template(
        "index.html",
        sections=SectionService.get_all_sections(),
        products=ProductService.get_all_products(),
    )

@main.route("/sections", methods=["GET"])
@swag_from(
    {
        "parameters": [],
        "responses": {
            "200": {
                "description": "List of all sections",
                "examples": {
                    "application/json": [
                        {"section_id": 1, "section_name": "Electronics"},
                        {"section_id": 2, "section_name": "Food and Beverages"},
                    ]
                },
            }
        },
    }
)
def get_sections():
    """
    Get all sections.
    """
    sections = SectionService.get_all_sections()
    controller_logger.info("Fetching all sections")
    return jsonify([section.to_dict() for section in SectionService.get_all_sections()]), 200

@main.route("/sections/<int:section_id>", methods=["GET"])
@swag_from(
    {
        "parameters": [
            {
                "name": "section_id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the section to retrieve",
            }
        ],
        "responses": {
            "200": {
                "description": "Details of a section",
                "examples": {
                    "application/json": {"section_id": 1, "section_name": "Electronics"}
                },
            },
            "404": {"description": "Section not found"},
        },
    }
)
def get_section(section_id):
    """
    Get a section by its ID.
    """
    controller_logger.info(f"Fetching section with ID {section_id}")
    try:
        section = SectionService.get_section_by_id(section_id)
        return jsonify(section.to_dict()), 200
    except SectionNotFoundException as e:
        return handle_exception(e, 404)

@main.route("/sections", methods=["POST"])
@swag_from(
    {
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": section_schema,
                "description": "Section data",
            }
        ],
        "responses": {
            "201": {"description": "Section created"},
            "400": {"description": "Section already exists or invalid data"},
        }
    }
)
def add_section():
    """
    Create a new section.
    """
    data = request.get_json()
    try:
        validate(instance=data, schema=section_schema)
        section = SectionService.create_section(data["section_name"])
        controller_logger.info(f"Created new section with name {data['section_name']}")
        return jsonify(section.to_dict()), 201
    except ValidationError as e:
        return handle_exception(f"Invalid data: {e.message}", 400)
    except SectionAlreadyExistsException as e:
        return handle_exception(e, 400)

@main.route("/sections/<int:section_id>", methods=["PUT"])
@swag_from(
    {
        "parameters": [
            {
                "name": "section_id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the section to update",
            },
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": section_schema,
                "description": "Section data",
            },
        ],
        "responses": {
            "200": {"description": "Section updated"},
            "400": {"description": "Invalid data or section already exists"},
            "404": {"description": "Section not found"},
        },
    }
)
def update_section(section_id):
    """
    Update a section.
    """
    data = request.get_json()
    try:
        validate(instance=data, schema=section_schema)
        section = SectionService.update_section(section_id, data["section_name"])
        controller_logger.info(f"Updated section with ID {section_id}")
        return jsonify(section.to_dict())
    except ValidationError as e:
        return handle_exception(f"Invalid data: {e.message}", 400)
    except SectionNotFoundException as e:
        return handle_exception(e, 404)
    except SectionAlreadyExistsException as e:
        return handle_exception(e, 400)

@main.route("/sections/<int:section_id>", methods=["DELETE"])
@swag_from(
    {
        "parameters": [
            {
                "name": "section_id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the section to delete",
            }
        ],
        "responses": {
            "200": {"description": "Section deleted"},
            "404": {"description": "Section not found"},
        },
    }
)
def delete_section(section_id):
    """
    Delete a section.
    """
    try:
        section = SectionService.delete_section(section_id)
        controller_logger.info(f"Deleted section with ID {section_id}")
        return jsonify(section.to_dict()), 200
    except SectionNotFoundException as e:
        return handle_exception(e, 404)

@main.route("/products", methods=["GET"])
@swag_from(
    {
        "parameters": [],
        "responses": {
            "200": {
                "description": "List of all products",
                "examples": {
                    "application/json": [
                        {
                            "product_id": 1,
                            "section_id": 1,
                            "product_name": "Laptop",
                            "quantity_in_stock": 50,
                            "price_per_unit": 1000,
                            "is_product_available": True,
                        },
                        {
                            "product_id": 2,
                            "section_id": 2,
                            "product_name": "Apple",
                            "quantity_in_stock": 100,
                            "price_per_unit": 2,
                            "is_product_available": True,
                        },
                    ]
                },
            }
        },
    }
)
def get_products():
    """
    Get all products.
    """
    controller_logger.info(f"Fetching all products from IP: {request.remote_addr}")
    products = ProductService.get_all_products()
    return jsonify([product.to_dict() for product in ProductService.get_all_products()]), 200

@main.route("/products/<int:product_id>", methods=["GET"])
@swag_from(
    {
        "parameters": [
            {
                "name": "product_id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the product to retrieve",
            }
        ],
        "responses": {
            "200": {
                "description": "Details of a product",
                "examples": {
                    "application/json": {
                        "product_id": 1,
                        "section_id": 1,
                        "product_name": "Laptop",
                        "quantity_in_stock": 50,
                        "price_per_unit": 1000,
                        "is_product_available": True,
                    }
                },
            },
            "404": {"description": "Product not found"},
        },
    }
)
def get_product(product_id):
    """
    Get a product by its ID.
    """
    try:
        product = ProductService.get_product_by_id(product_id)
        controller_logger.info(f"Fetched product with ID {product_id}")
        return jsonify(product.to_dict()), 200
    except ProductNotFoundException as e:
        return handle_exception(e, 404)

@main.route("/products", methods=["POST"])
@swag_from(
    {
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": product_schema,
                "description": "Product data",
            }
        ],
        "responses": {
            "201": {"description": "Product created"},
            "400": {"description": "Product already exists or invalid data"},
        },
    }
)
def add_product():
    """
    Create a new product.
    """
    data = request.get_json()
    try:
        validate(instance=data, schema=product_schema)
        product = ProductService.create_product(
            data["section_id"],
            data["product_name"],
            data["quantity_in_stock"],
            data["price_per_unit"],
            data["is_product_available"],
        )
        controller_logger.info(f"Created new product with name {data['product_name']}")
        return jsonify(product.to_dict()), 201
    except ValidationError as e:
        return handle_exception(f"Invalid data: {e.message}", 400)
    except (InvalidSectionException, ProductAlreadyExistsException) as e:
        return handle_exception(e, 400)

@main.route("/products/<int:product_id>", methods=["PUT"])
@swag_from(
    {
        "parameters": [
            {
                "name": "product_id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the product to update",
            },
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": product_schema,
                "description": "Product data",
            },
        ],
        "responses": {
            "200": {"description": "Product updated"},
            "400": {"description": "Invalid section or product not found"},
            "404": {"description": "Product already exists"},
        },
    }
)
def update_product(product_id):
    """
    Update a product.
    """
    data = request.get_json()
    try:
        validate(instance=data, schema=product_schema)
        product = ProductService.update_product(
            product_id,
            data["section_id"],
            data["product_name"],
            data["quantity_in_stock"],
            data["price_per_unit"],
            data["is_product_available"],
        )
        controller_logger.info(f"Updated product with ID {product_id}")
        return jsonify(product.to_dict()), 200
    except ValidationError as e:
        return handle_exception(f"Invalid data: {e.message}", 400)
    except (ProductNotFoundException, InvalidSectionException) as e:
        return handle_exception(e, 404)
    except ProductAlreadyExistsException as e:
        return handle_exception(e, 404)

@main.route("/products/<int:product_id>", methods=["DELETE"])
@swag_from(
    {
        "parameters": [
            {
                "name": "product_id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the product to delete",
            }
        ],
        "responses": {
            "200": {"description": "Product deleted"},
            "404": {"description": "Product not found"},
        },
    }
)
def delete_product(product_id):
    """
    Delete a product.
    """
    try:
        product = ProductService.delete_product(product_id)
        controller_logger.info(f"Deleted product with ID {product_id}")
        return jsonify(product.to_dict()), 200
    except ProductNotFoundException as e:
        return handle_exception(e, 404)
