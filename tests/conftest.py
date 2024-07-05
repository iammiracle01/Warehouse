import pytest
from app import create_app
from app.models import db, Section, Product

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function', autouse=True)
def setup_database(app):
    with app.app_context():
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

        yield

        db.session.query(Product).delete()
        db.session.query(Section).delete()
        db.session.commit()
