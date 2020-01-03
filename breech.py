from riposte import Riposte
from riposte.printer import Palette
from multiprocessing import Pool
import requests
import datetime
import time
import sys
import os

BANNER = """
██████╗ ██████╗ ███████╗███████╗ ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║
██████╔╝██████╔╝█████╗  █████╗  ██║     ███████║
██╔══██╗██╔══██╗██╔══╝  ██╔══╝  ██║     ██╔══██║
██████╔╝██║  ██║███████╗███████╗╚██████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝
   Made by Konradas Bunikis
   Please do not use this tool for malicious purposes."""

repl = Riposte('Breech > ', banner=BANNER)

class Application:
    def __init__(self):
        self.target = None
        self.payload = None

app = Application()

# Proxies to use when doing requests.
PROXIES = {}

# Extensions to use when doing requests.
EXTENSIONS = ['']

# How many CPU cores to use.
CORES = 4

def check_URL(lines):
    try:
        for line in lines:
            for extension in EXTENSIONS:
                url = str(app.target + '/' + line).strip('\n').strip(' ') + extension
                response = requests.get(url, headers={'User-Agent': 'XY'})
                if response.status_code == 200:
                    print(Palette.GREEN.format('[+]') + ' Found: %s ' % url)
    except KeyboardInterrupt:
        return

@repl.command('clear')
@repl.command('cls')
def clear_command():
    _ = os.system('clear')

@repl.command('exit')
@repl.command('quit')
def quit_command():
    exit()

@repl.command('run')
def run_command():
    mp = Pool(CORES)
    try:
        if os.path.exists(app.payload) == True:
            start_time = datetime.datetime.now()
            repl.info(Palette.YELLOW.format('[%s] Starting...' % start_time))
            with open(app.payload, 'r') as file:
                batch = []
                for line in file:
                    batch.append([line])
                    if len(batch) == CORES:
                        mp.map(check_URL, batch)
                        batch = []
                mp.map(check_URL, batch)
            end_time = datetime.datetime.now()
            total_time = end_time - start_time
            repl.info(Palette.YELLOW.format('[%s] Finished. Time: %ss' % (end_time, total_time.total_seconds())), end='')
            mp.close()
            mp.join()
            repl.info('')
        else:
            repl.error('Could not open %s' % app.payload)
    except KeyboardInterrupt:
        mp.close()
        mp.join()
        sys.stdout.writelines('\n')

@repl.command('add')
def add_command(variable: str):
    if variable == 'PROXY':
        # Protocol
        proxy_protocol = input('Protocol [HTTPS/HTTP] > ').lower()
        # Address
        proxy_address = input('Address > ')
        # Port
        proxy_port = input('Port > ')
        # Adding...
        PROXIES[proxy_protocol] = 'http://%s:%s' % (proxy_address, proxy_port)
        # Added...
        repl.success('Successfully added.')
    if variable == 'EXTENSION':
        extension = input('Extension [.php|.html|.asp] > ')
        if extension not in EXTENSIONS:
            EXTENSIONS.append(extension)
            repl.success('Successfully added.')

@repl.command('set')
def set_command(variable: str, value: str):
    if variable == 'TARGET':
        app.target = value
        repl.status('Setting TARGET as %s' % app.target)
    if variable == 'PAYLOAD':
        app.payload = value
        repl.status('Setting PAYLOAD as %s' % app.payload)

@repl.command('show')
def show_command(variable: str):
    if variable == 'TARGET':
        repl.status('TARGET = %s' % app.target)
    if variable == 'PAYLOAD':
        repl.status('PAYLOAD = %s' % app.payload)

@repl.command('unset')
def unset_command(variable: str):
    if variable == 'TARGET':
        repl.status('Successfully unset TARGET')
        app.target = None
    if variable == 'PAYLOAD':
        repl.status('Successfully unset PAYLOAD')
        app.payload = None

try:
    repl.run()
except KeyboardInterrupt:
    exit()