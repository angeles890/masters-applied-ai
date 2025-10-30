from time import time, sleep


def timer(func):
    def wrapper_time(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time

        print(f"total time: {total_time}")

        return result, total_time
    
    return wrapper_time


@timer
def sleep_test(seconds: int):
    print("Going to sleep")
    sleep(seconds)
    print("I'm back")
    return seconds

def format_seconds(tot_time: int) -> str:
    return str( int( (tot_time / 3600) ) ) + ":" + str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + str( int(  ( (tot_time % 3600) % 60 ) ) )

