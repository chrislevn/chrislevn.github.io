# Part 2: High performance code 
We know that Python is slow due to GIL (Global Interpreter Lock). It means that only one thread can execute at a time. However, there are ways to overcome this limitation, and we will cover later in this section. The question is to whether choose a language that easy to learn and faster to develop or a language that is harder to learn but faster to run. The choice is varied depending on the use cases. For me, using Python is a no-brainer for data science and machine learning. It is redudant to use another language to reinvent the wheel just for the sake of speed. 

First of all, let's construct a wrap function to measure the time of a function: 

```python
from functools import wraps
import time 

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time
```

The trade-off of this function is that it will add a small speed overhead to the function. You can also consider `timeit` module. 

Use `cProfile` to profile the code: 
Use `snakeviz` to visualize the profile: 


