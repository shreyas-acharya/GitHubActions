from sys import argv
from rich.console import Console
from rich.table import Table
from rich.live import Live
from art import text2art
import time

console = Console()
table = Table(title="Catalogue")
table.add_column("Word", ratio=10)
table.add_column("Result", ratio=80)

with Live(table, refresh_per_second=10):
    for index in range(len(argv)):
        table.add_row(argv[index], text2art(argv[index], "random"))
        time.sleep(3)
