def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# @singleton
# class MySingletonClass:
#     def __init__(self):
#         self.value = None

# # Example usage:
# singleton_instance1 = MySingletonClass()
# singleton_instance1.value = "Singleton Instance 1"

# singleton_instance2 = MySingletonClass()
# print(singleton_instance2.value)  # Output: "Singleton Instance 1"
