## this is about kwargs ** star operator

#kwargs as a parameter, you can pass as much as you like key words arguments
## it will print as a dictionary

def func(**kwargs):
    print(kwargs)

print(func(first_name = "Anoop", last_name = "Sheoran"))


def func(name, **kwargs):
    print(kwargs)
    print(name)
    for k, v in kwargs.items():
        print(f"{k}: {v}")
    print(func("pi", first_name="Anoop", last_name="Sheoran"))

## dictionary unpacking

def func(**kwargs):
    print(kwargs)

print(func(first_name = "Anoop", last_name = "Sheoran"))

d = {"name": "Anoop", "age": 37}
print(func(**d))

### funcitons with all parameters

## PADK
### parameters
### *args
### default parameters
### **kwargs


def func1(l, **kwargs):

    if kwargs.get("reverse_string")==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title()for name in l]
names = ["anoop", "pi"]

print(func1(names, reverse_string=True))
