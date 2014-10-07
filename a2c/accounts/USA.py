"""
This is Taxation Policy for Django Plan which is required. It will just return fixed tax rate 8.75% (NYS sales tax rate)
"""

from plans.taxation import TaxationPolicy

class USATaxationPolicy(TaxationPolicy):
    
    @classmethod
    def get_tax_rate(cls, tax_id, country_code):
        return cls.get_default_tax() 