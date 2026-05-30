import random
import platform
import psutil
import time
from datetime import datetime

def print_ascii_art():
    art = """
    ____             ____            
   / __ \\___ _   __/ __ \\____  _____
  / / / / _ \\ | / / / / / __ \\/ ___/
 / /_/ /  __/ |/ / /_/ / /_/ (__  ) 
/_____/\\___/|___/\\____/ .___/____/  
                     /_/            
    """
    print(art)

def get_random_quote():
    quotes = [
        "First, solve the problem. Then, write the code. – John Johnson",
        "Code is like humor. When you have to explain it, it's bad. – Cory House",
        "The best error message is the one that never shows up. – Thomas Fuchs",
        "It's not a bug – it's an undocumented feature. – Anonymous",
    ]
    return random.choice(quotes)

def system_health_check():
    return {
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent,
        'boot_time': datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        'platform': platform.platform()
    }

def loading_animation(duration=3):
    animation = "|/-\\"
    for i in range(duration * 10):
        print(f"\rLoading {animation[i % len(animation)]}", end="")
        time.sleep(0.1)
    print("\rDone!           ")

if __name__ == "__main__":
    print_ascii_art()
    print("\nQuote of the moment:")
    print(get_random_quote())
    print("\nChecking system health...")
    loading_animation()
    health = system_health_check()
    print("\nSystem Information:")
    for key, value in health.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
