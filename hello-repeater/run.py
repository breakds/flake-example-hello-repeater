import click
import time

@click.command()
@click.option('--interval', default = 5, help = 'Print every <interval> seconds')
@click.option('--name', default = 'Sir', help = 'The name to greet')
def hello(interval, name):
    while True:
        print(f'Hello, {name}')
        time.sleep(interval)

        
if __name__ == '__main__':
    hello()
