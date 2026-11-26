
import gc

print("Garbage Collection Enabled:", gc.isenabled())

gc.disable()
print("Garbage Collection Disabled")

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = {"name": "Python", "age": 30}

print("Objects Created:")
print(a)
print(b)
print(c)

gc.enable()
print("Garbage Collection Enabled:", gc.isenabled())

collected = gc.collect()
print("Garbage Collected:", collected)
