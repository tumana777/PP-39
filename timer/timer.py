import time
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
import pyfiglet
from playsound3 import playsound
from pathlib import Path

current_dir = Path(__file__).parent

console = Console()
seconds = 10 * 60


def create_timer(remaining):
    mins, secs = divmod(remaining, 60)
    color = "red" if remaining <= 10 else "green"

    digits = pyfiglet.figlet_format(
        f"{mins:02d}:{secs:02d}",
        font="big",
    )

    timer = Text(digits, style=f"bold {color}")

    return Panel(
        Align.center(timer, vertical="middle"),
        title="[bold]COUNTDOWN TIMER[/bold]",
        border_style=color,
        padding=(1, 2),
    )


with Live(
    create_timer(seconds),
    console=console,
    screen=False,
    auto_refresh=False,
) as live:
    for remaining in range(seconds, -1, -1):
        live.update(create_timer(remaining), refresh=True)
        time.sleep(1)

console.print("[bold red]TIME IS UP![/bold red]")
playsound(current_dir / "alarm.wav")
