class DomainError(Exception):
    """Base class for all domain-specific exceptions"""

    pass


class CountCannotBeNegative(DomainError, ValueError):
    """Count value object cannot be constructed using a negative integer"""

    pass


class CountCannotBeGreaterThan100(DomainError, ValueError):
    """Count value object cannot be constructed with a number greater than 100"""
