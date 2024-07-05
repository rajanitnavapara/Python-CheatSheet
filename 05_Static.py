'''
5.Static 
1. Define a static variable and access that through a class  
2. Define a static variable and access that through a instance 
3. Define a static variable and change within the instance 
4. Define a static variable and change within the class
'''

class Static:
    static_var = 10

    # 1. Define a static variable and access that through a class
    def access_static_var_through_class(self):
        print(Static.static_var)

    # 2. Define a static variable and access that through a instance
    def access_static_var_through_instance(self):
        print(self.static_var)

    # 3. Define a static variable and change within the instance
    def change_static_var_within_instance(self):
        self.static_var = 20
        print(self.static_var)

    # 4. Define a static variable and change within the class
    def change_static_var_within_class(self):
        Static.static_var = 30
        print(Static.static_var)

s = Static()
s.access_static_var_through_class() # 10
s.access_static_var_through_instance() # 10
s.change_static_var_within_instance() # 20
s.access_static_var_through_class() # 10
s.change_static_var_within_class() # 30
s.access_static_var_through_instance() # 30
s.access_static_var_through_class() # 30

# End of 05_Static.py
# # Date: 04/07/2024