import typer

def greet(name: str, age: int = 20):
    typer.echo(f"Hello, {name}, you are {age} years old!")

if __name__ == "__main__":
    typer.run(greet)
