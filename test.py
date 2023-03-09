from rich.table import Table
from rich.console import Console

table = Table()
console = Console()

table.add_column("Id")
table.add_column("Job")
table.add_column("Status")
table.add_row("1", "job1", "done")
table.add_row("2", "job2", "done")
table.add_row("3", "job3", "not completed")
table.add_row("4", "job4", "done")

console.print(table)
