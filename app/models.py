from . import db


class Section(db.Model):
    __tablename__ = "sections"

    section_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    section_name = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            "section_id": self.section_id,
            "section_name": self.section_name,
        }


class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    section_id = db.Column(
        db.Integer, db.ForeignKey("sections.section_id"), nullable=False
    )
    product_name = db.Column(db.String(80), nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    is_product_available = db.Column(db.Boolean, default=True)

    section = db.relationship("Section", backref=db.backref("products", lazy=True))

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "section_id": self.section_id,
            "product_name": self.product_name,
            "quantity_in_stock": self.quantity_in_stock,
            "price_per_unit": self.price_per_unit,
            "is_product_available": self.is_product_available,
            "section": self.section.section_name,
        }
