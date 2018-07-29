class Employee(object):
    def __init__(self,fname=None,lname=None):
        self.fname = fname
        self.lname = lname
        self.email = fname+"_"+lname+"@abc.com"
    @property
    def newemail(self):
        return  '{}_{}@gmail.com'.format(self.fname,self.lname)

    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)


emp1 = Employee('shreyansh','sinha')

emp1.fname = "sushant"

print(emp1.fname)
print(emp1.lname)
print(emp1.email)
print(emp1.newemail)
print(emp1.fullname())


#The output is:
#sushant
#sinha
#shreyansh_sinha@abc.com
#sushant sinha

#to resolve this we use @property
