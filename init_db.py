from app import create_app
from app.models import db, Section, Product

app = create_app()

with app.app_context():
    db.create_all()

    section1 = Section(section_name="Electronics")
    section2 = Section(section_name="Food and Drinks")

    db.session.add_all([section1, section2])
    db.session.commit()

    product1 = Product(
        section_id=section1.section_id,
        product_name="Laptop",
        quantity_in_stock=50,
        price_per_unit=1000,
        is_product_available=True,
    )
    product2 = Product(
        section_id=section1.section_id,
        product_name="Smartphone",
        quantity_in_stock=200,
        price_per_unit=500,
        is_product_available=True,
    )
    product3 = Product(
        section_id=section2.section_id,
        product_name="Canned Beans",
        quantity_in_stock=100,
        price_per_unit=2,
        is_product_available=True,
    )
    product4 = Product(
        section_id=section2.section_id,
        product_name="Soda",
        quantity_in_stock=300,
        price_per_unit=1,
        is_product_available=True,
    )

    db.session.add_all([product1, product2, product3, product4])
    db.session.commit()
