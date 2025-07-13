import os


def get_weather(city: str) -> str:
    """Get the weather for a city.
    
    Args:
        city: The city to get the weather for.

    Returns:
        The weather for the city.
    """
    return f"The weather in {city} is sunny."

def save_file(tasks: str, filename: str) -> str:
    """Save the file.
    
    Args:
        tasks: The list of tasks to save.
        filename: name of the file to save without the file format.

    Returns:
        The status of the file save.
    """
    filename = f"{filename}.md"
    filepath =  os.path.join("outputs", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tasks)
    return (f"✅ Saved to {filename}")


def allocate():
    """List of available people to allocate tasks.

    Args:
        No args
    
    Returns:
        prompt and Dictionary of available people
    """
    people = {
        "Person A" : "Senior Dev",
        "Person B" : "Junior Dev",
        "Person C" : "Junior Dev",
        "Person D" : "Intern"
    }

    return f"Use the dict to allocate each task to the most suitable person", people