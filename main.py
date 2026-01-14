from info import print_ascii_art

def handle_command(command: str) -> bool:
    command = command.strip().lower()

    match command:
        case "help":
            print("Available commands:")
            print("  help  - show this message")
            print("  greet - say hello")
            print("  exit  - quit the program")
        
        case "info": 
            print_ascii_art()

        case "greet":
            print("Hello! 👋")

        case "exit" | "quit":
            print("Goodbye!")
            return False

        case "":
            # Ignore empty input
            pass

        case _:
            print(f"Unknown command: '{command}'")

    return True


def main():
    print("Command-line app started. Type 'help' for commands.")

    running = True
    while running:
        try:
            command = input("> ")
            running = handle_command(command)
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break
        except EOFError:
            print("\nEOF received. Exiting.")
            break


if __name__ == "__main__":
    main()
