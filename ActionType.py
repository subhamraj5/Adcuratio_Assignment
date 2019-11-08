class Action:
    
    def __init__(self,action_id,action_name):
        self.__action_id=action_id
        self.__action_name=action_name
        
        
    def get_action_id(self):
        return self.__action_id
    
    def get_action_name(self):
        return self.__action_name    
    
    def set_action_name(self,action_name):
        self.__action_name=action_name
        
    def set_action_id(self,action_id):
        self.__action_id=action_id    