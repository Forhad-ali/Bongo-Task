lst=dict()
def count_items(d,iter):
    for k, v in d.items():
        lst[k] = lst.get(k, iter)
        if isinstance(v, dict):
            count_items(v,iter+1)

a = {
    "key1":1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
            }
        },
    }

def depth_print(x):
    count_items(x,1)
    b=sorted(lst.items())

    for i,v in b : 
        print(i+'',v) 

depth_print(a)
