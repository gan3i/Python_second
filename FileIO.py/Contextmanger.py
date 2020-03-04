"""Demonstrate raiding a refrigerator"""

class RefrigeratorRaider():
    """raide a refrigerator"""

    def open(self):
        print("open fridge door")

    
    def take(self, food):
        print(f"finding {food}...")
        if food == "deep fried pizza":
            raise RuntimeError("health warning")
        print(f"Taking {food}")


    def close(self):
        print("close fridge")


def raid(food):
    from contextlib import closing# closing calls the close method of the wrapped object before exiting.
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close().. removing explicit call to close.


raid("burger")
# raid("deep fried pizza")