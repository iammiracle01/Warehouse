class SectionException(Exception):
    pass


class SectionNotFoundException(SectionException):
    pass


class SectionAlreadyExistsException(SectionException):
    pass


class ProductException(Exception):
    pass


class ProductNotFoundException(ProductException):
    pass


class ProductAlreadyExistsException(ProductException):
    pass


class InvalidSectionException(ProductException):
    pass
