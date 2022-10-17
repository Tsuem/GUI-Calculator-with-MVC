'''
Created on 16 oct. 2022

@author: Tsue
'''

class Model:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.previous_value = ''
        self.value = ''
        self.operator = ''
    
    
    def calculate(self, caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''
        
        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
            
        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)

            self.value = str(self._evaluate())
        
        elif caption == '=':
            self.value = str(self._evaluate())
        
        elif caption == '.':
            if not caption in self.value:
                self.value += caption
        
        elif isinstance(caption, int):
            self.value += str(caption)
            
        else: 
            if self.value:
                self.operator = caption
            
                self.previous_value = self.value
            
                self.value = ''
            
        return self.value
    
    
    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)
    