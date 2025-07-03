import gc
import time

class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"Created object: {self.name}")

    def __del__(self):
        print(f"Destroyed object: {self.name}")

def simple_gc_demo():
    obj = MyObject("A") 
    print("Using object...")
    time.sleep(2)

    print("Delete object...")
    del obj       

    print("Garbage collector...")
    gc.collect()         

simple_gc_demo()
