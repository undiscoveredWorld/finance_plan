"""generate-env asks you for an environment variables and generates environment files.

Files will be created at 'src/docker.env' and at 'tests/docker.env'
"""


def ask_docker_variables() -> str:
    POSTGRES_PASSWORD = ask_variable("POSTGRES_PASSWORD", default="my-password")
    POSTGRES_USER = ask_variable("POSTGRES_USER", default="fp")
    POSTGRES_DB = ask_variable("POSTGRES_DB", default="Finance_plan")

    body = (f"POSTGRES_PASSWORD={POSTGRES_PASSWORD}\n" +
            f"POSTGRES_USER={POSTGRES_USER}\n" +
            f"POSTGRES_DB={POSTGRES_DB}\n")

    return body


def ask_variable(variable_name: str, default: any = None) -> str:
    """Ask user for an environment variable and return answer"""
    if default:
        text = f"{variable_name}({default}): "
    else:
        text = f"{variable_name}: "

    input_text = input(text)
    if input_text == "":
        return default
    return input_text


if __name__ == "__main__":
    body = ask_docker_variables()

    with open("./src/docker.env", "w") as file:
        file.write(body)

    with open("./tests/docker.env", "w") as file:
        file.write(body)
