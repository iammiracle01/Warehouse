import logging
from .models import db, Section, Product
from .exceptions import (
    SectionNotFoundException,
    SectionAlreadyExistsException,
    ProductNotFoundException,
    ProductAlreadyExistsException,
    InvalidSectionException,
)


service_logger = logging.getLogger('service_logger')

class SectionService:
    @staticmethod
    def get_all_sections():
        service_logger.info("Fetching all sections from database")
        return Section.query.all()

    @staticmethod
    def get_section_by_id(section_id):
        section = Section.query.get(section_id)
        if not section:
            service_logger.error(f"Section with ID {section_id} not found")
            raise SectionNotFoundException(f"Section with ID {section_id} not found")
        service_logger.info(f"Found section with ID {section_id}")
        return section

    @staticmethod
    def create_section(section_name):
        existing_section = Section.query.filter_by(section_name=section_name).first()
        if existing_section:
            service_logger.error(f"Section with name {section_name} already exists")
            raise SectionAlreadyExistsException(
                f"Section with name {section_name} already exists"
            )
        new_section = Section(section_name=section_name)
        db.session.add(new_section)
        db.session.commit()
        service_logger.info(f"Created section with name {section_name}")
        return new_section

    @staticmethod
    def update_section(section_id, section_name):
        section = Section.query.get(section_id)
        if not section:
            service_logger.error(f"Section with ID {section_id} not found")
            raise SectionNotFoundException(f"Section with ID {section_id} not found")

        existing_section = Section.query.filter_by(section_name=section_name).first()
        if existing_section:
            service_logger.error(f"Section with name {section_name} already exists")
            raise SectionAlreadyExistsException(
                f"Section with name {section_name} already exists"
            )

        section.section_name = section_name
        db.session.commit()
        service_logger.info(f"Updated section with ID {section_id} to name {section_name}")
        return section

    @staticmethod
    def delete_section(section_id):
        section = Section.query.get(section_id)
        if not section:
            service_logger.error(f"Section with ID {section_id} not found")
            raise SectionNotFoundException(f"Section with ID {section_id} not found")
        Product.query.filter_by(section_id=section_id).delete()
        db.session.delete(section)
        db.session.commit()
        service_logger.info(f"Deleted section with ID {section_id}")
        return section


class ProductService:
    @staticmethod
    def get_all_products():
        service_logger.info("Fetching all products from database")
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        product = Product.query.get(product_id)
        if not product:
            service_logger.error(f"Product with ID {product_id} not found")
            raise ProductNotFoundException(f"Product with ID {product_id} not found")
        service_logger.info(f"Found product with ID {product_id}")
        return product

    @staticmethod
    def create_product(
        section_id,
        product_name,
        quantity_in_stock,
        price_per_unit,
        is_product_available,
    ):
        section = Section.query.get(section_id)
        if not section:
            service_logger.error(f"Section with ID {section_id} does not exist")
            raise InvalidSectionException(
                f"Section with ID {section_id} does not exist"
            )

        existing_product = Product.query.filter_by(
            product_name=product_name, section_id=section_id
        ).first()
        if existing_product:
            service_logger.error(f"Product with name {product_name} already exists in section ID {section_id}")
            raise ProductAlreadyExistsException(
                f"Product with name {product_name} already exists in section ID {section_id}"
            )

        new_product = Product(
            section_id=section_id,
            product_name=product_name,
            quantity_in_stock=quantity_in_stock,
            price_per_unit=price_per_unit,
            is_product_available=is_product_available,
        )
        db.session.add(new_product)
        db.session.commit()
        service_logger.info(f"Created product with name {product_name} in section ID {section_id}")
        return new_product

    @staticmethod
    def update_product(
        product_id,
        section_id,
        product_name,
        quantity_in_stock,
        price_per_unit,
        is_product_available,
    ):
        product = Product.query.get(product_id)
        if not product:
            service_logger.error(f"Product with ID {product_id} not found")
            raise ProductNotFoundException(f"Product with ID {product_id} not found")

        section = Section.query.get(section_id)
        if not section:
            service_logger.error(f"Section with ID {section_id} does not exist")
            raise InvalidSectionException(
                f"Section with ID {section_id} does not exist"
            )

        existing_product = Product.query.filter_by(
            product_name=product_name, section_id=section_id
        ).first()
        if existing_product and existing_product.product_id != product_id:
            service_logger.error(f"Product with name {product_name} already exists in section ID {section_id}")
            raise ProductAlreadyExistsException(
                f"Product with name {product_name} already exists in section ID {section_id}"
            )

        product.section_id = section_id
        product.product_name = product_name
        product.quantity_in_stock = quantity_in_stock
        product.price_per_unit = price_per_unit
        product.is_product_available = is_product_available
        db.session.commit()
        service_logger.info(f"Updated product with ID {product_id}")
        return product

    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if not product:
            service_logger.error(f"Product with ID {product_id} not found")
            raise ProductNotFoundException(f"Product with ID {product_id} not found")
        db.session.delete(product)
        db.session.commit()
        service_logger.info(f"Deleted product with ID {product_id}")
        return product
