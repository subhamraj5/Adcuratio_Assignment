from RbasApp.ActionType import Action
from RbasApp.Resources import Resource
from RbasApp.Roles import Role
from RbasApp.Users import User
import warnings
warnings.filterwarnings("ignore")

class Main:
    
    def create_resource(self,r_id,r_name):
        return Resource(r_id,r_name)
        
    def create_user(self,u_id,u_pwd,u_name,u_age):
        return User(u_id,u_pwd,u_name,u_age)
    
    def create_role(self,r_id,r_name):
        return Role(r_id,r_name)
    
    def create_action_type(self,a_id,a_name):
        return Action(a_id,a_name)
    
    def check_user_access(self,user):
        if user.get_user_role().get_role_name()=="admin":
            print(user.get_user_name()+" has Access to all resources with READ, WRITE and DELETE permission")
        elif user.get_user_role().get_role_name()=="viewer":
            print(user.get_user_name()+" has Access to all resources with READ only permission") 
        else:
            print(user.get_user_name()+" has Access to all resources with WRITE only permission")      
        
driver=Main()
    
#Creating Role
    
admin=driver.create_role(1, "admin")
member=driver.create_role(1, "member")
viewer=driver.create_role(1, "viewer")
    
    
#Creating Resource
    
R1=driver.create_resource(1,"R1")
R2=driver.create_resource(2,"R2")
R3=driver.create_resource(3,"R3")
R4=driver.create_resource(4,"R4")
R5=driver.create_resource(5,"R5")
    
    
#Creating Acion Type
    
read=driver.create_action_type(1,"Read")
write=driver.create_action_type(2,"Write")
delete=driver.create_action_type(3,"Delete")
rwd=driver.create_action_type(4,"RWD")
    
#Creating RBAS
    
u1=driver.create_user(1, "pwd","Raj",26)
u2=driver.create_user(1, "pwd","Rohan",25)
u3=driver.create_user(1, "pwd","Shruti",24)
u4=driver.create_user(1, "pwd","Tuba",25)    
    
u1.set_user_role(admin)
u1.set_user_action_type(rwd)
    
u2.set_user_role(member)
u2.set_user_action_type(write)
    
u3.set_user_role(viewer)
u3.set_user_action_type(read)


driver.check_user_access(u1)
driver.check_user_access(u2)
driver.check_user_access(u3)    
    
    
        