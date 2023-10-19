### Step 1: Clone the GitHub Repository

1. Open a terminal on your computer.
2. Run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/anand121shah/reimagined-octo-waddle.git
   ```

### Step 2: Set Up Git

1. If Git is not already installed on your machine, download and install it from the [official website](https://git-scm.com/downloads).
2. Configure Git with your username and email by running the following commands in the terminal:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

### Step 3: Create the Python Script

1. Create a new file named `log_login.py` in the cloned repository directory (`reimagined-octo-waddle`).
2. Open `log_login.py` in a text editor and paste the following code into it:

```python
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
```

Replace `/path/to/reimagined-octo-waddle` with the actual path to the `reimagined-octo-waddle` directory on your machine.

### Step 4: Automate the Script Execution

#### On Windows (using Task Scheduler):

1. Search for "Task Scheduler" in the Start menu and open it.
2. In the Actions pane on the right, click "Create Basic Task."
3. Name the task and provide a description if desired, then click "Next."
4. Select "When I log on" as the trigger, then click "Next."
5. Choose "Start a program" as the action, then click "Next."
6. Browse to the location of your Python interpreter (e.g., `python.exe` or `python3.exe`), and in the "Add arguments" field, enter the path to `log_login.py`. For example:
   - Program/script: `C:\Python39\python.exe`
   - Add arguments: `C:\path\to\reimagined-octo-waddle\log_login.py`
7. Click "Next," review your settings, then click "Finish."

#### On macOS (using launchd):

1. Create a file named `com.user.log_login.plist` with the following content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.log_login</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/reimagined-octo-waddle/log_login.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

Replace `/path/to/reimagined-octo-waddle` with the actual path to the `reimagined-octo-waddle` directory on your machine.

2. Move the `plist` file to `~/Library/LaunchAgents`.
3. Load the job using `launchctl`:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.log_login.plist
   ```

#### On Linux (using cron):

1. Open a terminal.
2. Run `crontab -e` to edit the crontab file.
3. Add the following line to the end of the file:
   ```bash
   @reboot /usr/bin/python3 /path/to/reimagined-octo-waddle/log_login.py
   ```

### Step 5: Install Necessary Libraries

In the provided script, there are no additional libraries required as it uses only built-in Python libraries. However, if you decide to enhance the script or add more features, you might need to install additional libraries using pip:

```bash
pip install library-name
```

This complete guide should help you set up the system to log your login times to the specified GitHub repository.
