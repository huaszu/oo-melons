"""Classes for melon orders."""

class AbstractMelonOrder:
    order_type= None 
    tax = 0
    
    

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty 
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        
        if self.order_type == "international" and self.qty <10:
            total += 5
        
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self):
        """Initialize melon order attributes."""
        
        pass

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
