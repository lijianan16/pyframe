import os
import sys
def pro_path():
    project_path = os.path.dirname(sys.argv[0])
    return project_path.split("com")[0]