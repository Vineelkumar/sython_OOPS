class Item:
    def __init__(self,name,price,category):
        self._name = name
        self._price = price
        self._category = category
        if self._price <= 0:
            raise ValueError("Invalid value for price, got {}".format(self._price))
        
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def category(self):
        return self._category    
        
            
    def __str__(self):
        return "{}@{}-{}".format(self._name,self._price,self._category)
        
        

class Query(Item):
    def __init__(self,field,operation,value):
      #  super().__init__(self._name,self._price,self._category)
        self._field = field
        self._operation = operation
        self._value = value
        operators = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if self._operation not in operators:
            raise ValueError("Invalid value for operation, got {}".format(self._operation))
    @property
    def field(self):
        return self._field
                
    @property
    def operation(self):
        return self._operation

    @property
    def value(self):
        return self._value

    def __str__(self):
        for i in range(6):
            return f'{self._field} {self._operation} {self._value}'


class Store:
    def __init__(self):
        self.lists = []
    
    def __str__(self):
        if len(self.lists) > 0:
            return '\n'.join(map(str,self.lists))
        else:
            return 'No items'
    
    def count(self):
        return len(self.lists)
        
        
    def add_item(self, item):
        self.lists.append(item)
       
    def filter(self,query):
        filter_item = Store()
        if query.operation == 'EQ':
            
            for i in self.lists:
                if query.field == 'name' and i.name == query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'price' and i.price == query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'category' and i.category == query.value:
                    filter_item.add_item(i)
      
            return filter_item      
        
        elif query.operation == 'GT':
            for i in self.lists:
                if i.price > query.value:
                    filter_item.add_item(i)
            return filter_item
        
        elif query.operation == 'LT':
            for i in self.lists:
                if i.price < query.value:
                    filter_item.add_item(i)
            return filter_item    
        
        elif query.operation == 'GTE':
            for i in self.lists:
                if i.price >= query.value:
                    filter_item.add_item(i)
            return filter_item    
        
        elif query.operation == 'LTE':
            for i in self.lists:
                if i.price <= query.value:
                    filter_item.add_item(i)
            return filter_item
            
        elif query.operation == 'STARTS_WITH':
            for i in self.lists:
                if query.field == 'name' and i.name.startswith(query.value):
                    filter_item.add_item(i)
                elif query.field == 'category' and i.category.startswith(query.value):
                    filter_item.add_item(i)
            return filter_item
        
        elif query.operation == 'ENDS_WITH':
            for i in self.lists:
                if query.field == 'name' and i.name.endswith(query.value):
                    filter_item.add_item(i)
                elif query.field == 'category' and i.category.endswith(query.value):
                    filter_item.add_item(i)    
            return filter_item    
            
        elif query.operation == 'IN':
            
            for i in self.lists:
                if query.field == 'name' and i.name in query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'price' and i.price in query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'category' and i.category in query.value:
                    filter_item.add_item(i)
      
            return filter_item          
            
        elif query.operation == 'CONTAINS':
            for i in self.lists:
                if query.field == 'name' and i.name.__contains__(query.value):
                    filter_item.add_item(i)
                
                elif query.field == 'category' and i.category.__contains__(query.value):
                    filter_item.add_item(i)
            
            return filter_item
        
    def exclude(self,query):

        exclude_item = Store()
        if query.operation == 'EQ':
            
            for i in self.lists:
                if query.field == 'name' and i.name != query.value:
                    exclude_item.add_item(i)
                
                elif query.field == 'price' and i.price != query.value:
                    exclude_item.add_item(i)
                
                elif query.field == 'category' and i.category != query.value:
                    exclude_item.add_item(i)
      
            return exclude_item      
        
        elif query.operation == 'GT':
            for i in self.lists:
                if i.price <= query.value:
                    exclude_item.add_item(i)
            return exclude_item
        
        elif query.operation == 'LT':
            for i in self.lists:
                if i.price >= query.value:
                    exclude_item.add_item(i)
            return exclude_item    
        
        elif query.operation == 'GTE':
            for i in self.lists:
                if i.price < query.value:
                    exclude_item.add_item(i)
            return exclude_item    
        
        elif query.operation == 'LTE':
            for i in self.lists:
                if i.price > query.value:
                    exclude_item.add_item(i)
            return exclude_item
            
        elif query.operation == 'STARTS_WITH':
            for i in self.lists:
                if query.field == 'name' and not(i.name.startswith(query.value)):
                    exclude_item.add_item(i)
                elif query.field == 'category' and not(i.category.startswith(query.value)):
                    exclude_item.add_item(i)
            return exclude_item
        
        elif query.operation == 'ENDS_WITH':
            for i in self.lists:
                if query.field == 'name' and not(i.name.endswith(query.value)):
                    exclude_item.add_item(i)
                elif query.field == 'category' and not(i.category.endswith(query.value)):
                    exclude_item.add_item(i)    
            return exclude_item    
            
        elif query.operation == 'IN':
            
            for i in self.lists:
                if query.field == 'name' and i.name not in query.value:
                    exclude_item.add_item(i)
                
                elif query.field == 'price' and i.price not in query.value:
                    exclude_item.add_item(i)
                
                elif query.field == 'category' and i.category not in query.value:
                    exclude_item.add_item(i)
      
            return exclude_item              
        
        elif query.operation == 'CONTAINS':
            
            for i in self.lists:
                if query.field == 'name' and not(i.name.__contains__(query.value)):
                    exclude_item.add_item(i)
                
                elif query.field == 'category' and not(i.category.__contains__(query.value)):
                    exclude_item.add_item(i)
            
            return exclude_item

        
================= OR =================



class Item:
    def __init__(self,name,price,category):
        self._name = name
        self._price = price
        self._category = category
        if self._price <= 0:
            raise ValueError("Invalid value for price, got {}".format(self._price))
        
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def category(self):
        return self._category    
        
            
    def __str__(self):
        return "{}@{}-{}".format(self._name,self._price,self._category)
        

class Query(Item):
    def __init__(self,field,operation,value):
        self._field = field
        self._operation = operation
        self._value = value
        operators = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if self._operation not in operators:
            raise ValueError("Invalid value for operation, got {}".format(self._operation))
    @property
    def field(self):
        return self._field
                
    @property
    def operation(self):
        return self._operation

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'


class Store:
    def __init__(self):
        self.lists = []
    
    def __str__(self):
        if len(self.lists) > 0:
            return '\n'.join(map(str,self.lists))
        else:
            return 'No items'
    
    def count(self):
        return len(self.lists)


    def add_item(self, item):
        self.lists.append(item)

    
    def filter(self,query):
        filter_item = Store()
        for items in self.lists:
            val = getattr(items,query.field)
            
            if query.operation == 'EQ' and val == query.value:
                filter_item.add_item(items)
                
            if query.operation == 'GT' and val > query.value:
                filter_item.add_item(items)
            
            if query.operation == 'LT' and val < query.value:
                filter_item.add_item(items)
            
            if query.operation == 'LTE' and val <= query.value:
                filter_item.add_item(items)
                
            if query.operation == "GTE" and val >= query.value:
                filter_item.add_item(items)    
            
            if query.operation == 'STARTS_WITH' and val.startswith(query.value):
                filter_item.add_item(items)
                
            if query.operation == 'ENDS_WITH' and val.endswith(query.value):
                filter_item.add_item(items)    
            
            if query.operation == 'IN' and val in query.value:
                filter_item.add_item(items)
            
            if query.operation == 'CONTAINS' and val.__contains__(query.value):
                filter_item.add_item(items)    
                
        return filter_item
        
        
    def exclude(self,query):
        exclude_item = Store()
        for items in self.lists:
            val = getattr(items,query.field)
            
            if query.operation == 'EQ' and val != query.value:
                exclude_item.add_item(items)
                
            if query.operation == 'GT' and val <= query.value:
                exclude_item.add_item(items)
            
            if query.operation == 'LT' and val >= query.value:
                exclude_item.add_item(items)
            
            if query.operation == 'LTE' and val > query.value:
                exclude_item.add_item(items)
                
            if query.operation == "GTE" and val < query.value:
                exclude_item.add_item(items)    
            
            if query.operation == 'STARTS_WITH' and not(val.startswith(query.value)):
                exclude_item.add_item(items)
                
            if query.operation == 'ENDS_WITH' and not(val.endswith(query.value)):
                exclude_item.add_item(items)    
            
            if query.operation == 'IN' and val not in query.value:
                exclude_item.add_item(items)
            
            if query.operation == 'CONTAINS' and not(val.__contains__(query.value)):
                exclude_item.add_item(items)    
                
        return exclude_item
