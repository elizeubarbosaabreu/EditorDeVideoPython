from datetime import datetime

def now():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

if __name__ == '__main__':
    print(now())