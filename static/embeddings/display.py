import pickle
with open("EC002.dat","rb") as f:
    obj = pickle.load(f)
    #del obj["EC002_IC001"]
    print(obj)
