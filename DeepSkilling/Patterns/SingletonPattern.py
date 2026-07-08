class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Object")
            cls._instance = super().__new__(cls)
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()

if obj1 is obj2:
    print("Both objects are the same.")
else:
    print("Objects are different.")