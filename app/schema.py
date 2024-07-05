section_schema = {
    "type": "object",
    "properties": {
        "section_name": {"type": "string"},
    },
    "required": ["section_name"],
}

product_schema = {
    "type": "object",
    "properties": {
        "section_id": {"type": "integer"},
        "product_name": {"type": "string"},
        "quantity_in_stock": {"type": "integer"},
        "price_per_unit": {"type": "integer"},
        "is_product_available": {"type": "boolean"},
    },
    "required": [
        "section_id",
        "product_name",
        "quantity_in_stock",
        "price_per_unit",
        "is_product_available",
    ],
}