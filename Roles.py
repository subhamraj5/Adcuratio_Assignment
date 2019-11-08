class Role:
    
    def __init__(self,role_id,role_name):
        self.__role_id=role_id
        self.__role_name=role_name
        
        
    def get_role_id(self):
        return self.__role_id
    
    def get_role_name(self):
        return self.__role_name    
    
    def set_role_name(self,role_name):
        self.__role_name=role_name
        
    def set_role_id(self,role_id):
        self.__role_id=role_id    