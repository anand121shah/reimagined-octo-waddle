import os
import subprocess
from datetime import datetime

def log_login_time():
    # Change to the repository directory
    os.chdir('/path/to/reimagined-octo-waddle')

    # Get the current date and time
    now = datetime.now()
    formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')

    # Append the login time to a file
    with open('log.txt', 'a') as file:
        file.write(f'{formatted_time}\n')

    # Commit the change to Git
    os.system('git add log.txt')
    os.system(f'git commit -m "Logged login at {formatted_time}"')
    os.system('git push')

if __name__ == '__main__':
    # Check for internet connection
    response = subprocess.run(['ping', '-c', '1', 'github.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if response.returncode == 0:
        log_login_time()
    else:
        print("No internet connection. Login time not logged.")
