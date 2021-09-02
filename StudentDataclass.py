from dataclasses import dataclass, field

@dataclass
class Student:
    name:str
    college_id: int
    gpa: float = field(default=0.0)#testing field not sure why and how to set init or repr = false as descriped in the documentation
# init and repr are automatically genrated. to deactivate, we can make them false at the declaration step. 
def main():
    alice=Student('Alice', 12345, 3)
    bob=Student('Bob', 98765, 3.5)
    mo=Student('Mo',12222)

    print(alice)
    print(bob)
    print(mo)
    
main()