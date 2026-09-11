# this is an example of a re-try loop

from time import sleep

def progress(delay: int):
    TOKENS = ["-", "\\", "|", "/"]
    for i in range(delay):
        token = i % len(TOKENS)
        print(TOKENS[token], end="", flush=True)
        sleep(1)
        print("\b", end="", flush=True)    

TIMES = 5
BACKOFF = 5

print("Starting the retry loop...")
for attempt in range(TIMES):
    print(f"Attempt {attempt + 1} of {TIMES}")
    delay = BACKOFF*attempt
    print(f"Sleeping for {delay} seconds...")
    progress(delay)
    print("Retrying now...")
    