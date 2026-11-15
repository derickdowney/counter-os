class DomainException(Exception):
    """Base class for all domain-specific exceptions"""

    pass


class CountCannotBeNegative(DomainException, ValueError):
    """Count value object cannot be constructed using a negative integer"""

    pass
