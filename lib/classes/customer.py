class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    def orders(self):
        from classes.order import Order

        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        from classes.coffee import Coffee

        return [*set([order.coffee for order in self.orders()])]
