class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
            }
        },
    }

lst=dict()
def count_items(d,iter):
    for k, v in d.items():
        lst[k] = lst.get(k, iter)
        if isinstance(v, dict):
            count_items(v,iter+1)


def depth_print(x):
    count_items(x,1)
    b=sorted(lst.items())

    for i,v in b : 
        print(i+'',v) 
    
    print(person_a.__dict__)
    print(person_b.__dict__)

depth_print(a)



