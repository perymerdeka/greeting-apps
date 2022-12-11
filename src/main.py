from typer import Typer, Option
from typing import Optional

from greet import Greetings

app = Typer()

@app.command()
def main(
    name: str = Option("", help="Enter Your Name"),
    mode: Optional[str] = Option(
        "unformal", help="help you print greeting text with unformal format"
    ),
    address: Optional[str] = Option("", help="Your Address"),
    city: Optional[str] = Option("", help="Your City"),
    state: Optional[str] = Option("", help="Your State Address"),
):
    greeting: Greetings = Greetings(name=name, address=address, city=city, state=state)
    if mode == "unformal":
        greeting.intro()
    elif mode == "formal":
        greeting.intro()
    elif mode == "unformal":
        greeting.formal_event()
    elif mode == "indentity":
        greeting.identity()
    
if __name__ == "__main__":
    app()