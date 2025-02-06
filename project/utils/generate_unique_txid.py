from datetime import datetime
import random
import string


def generate_unique_txid():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    min_length = 26
    max_length = 35
    random_length = random.randint(min_length, max_length) - len(timestamp)  
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random_length))  
    txid = timestamp + random_string
        
    return txid
