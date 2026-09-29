from pysros.management import connect
from pysros.exceptions import *
import sys

def get_connection():
    try:
        c = connect(host="172.20.20.13",
                    username="admin",
                    password="admin", hostkey_verify=False)
    except RuntimeError as e1:
        print("Failed to connect.  Error:", e1)
        sys.exit(-1)
    except ModelProcessingError as e2:
        print("Failed to create model-driven schema.  Error:", e2)
        sys.exit(-2)
    return c

if __name__ == "__main__":
    c = get_connection()
