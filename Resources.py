class Resource:
    
    def __init__(self,resource_id,resource_name):
        self.__resource_id=resource_id
        self.__resource_name=resource_name
        
        
    def get_resource_id(self):
        return self.__resource_id
    
    def get_resource_name(self):
        return self.__resource_name    
    
    def set_resource_name(self,resource_name):
        self.__resource_name=resource_name
        
    def set_action_id(self,resource_id):
        self.__resource_id=resource_id    