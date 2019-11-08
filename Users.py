class User:
    
    def __init__(self, user_id, user_password, user_name, user_age):
        self.__user_id = user_id
        self.__user_password = user_password
        self.__user_name = user_name
        self.__user_age = user_age
        self.__user_role = None
        self.__user_action_type=None
    
    def get_user_id(self):
        return self.__user_id
    
    def get_user_name(self):
        return self.__user_name
    
    def get_user_age(self):
        return self.__user_age
    
    def get_user_password(self):
        return self.__user_password
    
    def get_user_role(self):
        return self.__user_role
    
    def get_user_action_type(self):
        return self.__user_action_type    
    
    def set_user_role(self,user_role):
        self.__user_role=user_role
        
    def set_user_action_type(self,user_action_type):
        self.__user_action_type=user_action_type  