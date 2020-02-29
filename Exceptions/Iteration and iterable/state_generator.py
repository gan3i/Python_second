def take(count, iterable):
    counter = 0
    for i in iterable:
        if counter==count:
            return
        counter +=1
        yield i



def distinct(iterable):
    seen=set()
    for i in iterable:
        if i in seen:
            continue
        yield i
        seen.add(i)

        
# def distinct_set(iterable):
#     print(set(iterable))
#     return set(iterable)

def run_pipeline():
    items = [8,9999,2,1,1,5,6,5,2,7]
    for i in take(3,distinct(items)):
        print (i)

if __name__== "__main__":
    run_pipeline()