import openai
import sys
import textwrap
from pathlib import Path

openai.api_key_path = Path(__file__).parent.parent / ".env"

def gpt(content, conversation=[], model="gpt-3.5-turbo") -> str:
    if not conversation:
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            *conversation,
            {"role": "user", "content": content},
        ],
    )
    return response["choices"][0]["message"]["content"]


def main(args: list[str] = sys.argv[1:]):
    #TODO: format response nicely
    # wrapped_response = textwrap.fill(
    #     gpt(args[0]),
    #     width=80,
    #     replace_whitespace=False,
    # )
    model = 'gpt-3.5-turbo'
    # set the model if '-v' is in args
    if '-v' in args:
        version = args[args.index('-v') + 1]
        if version == '3':
            model = 'gpt-3.5-turbo'
        elif version == '4':
            model = 'gpt-4'

    sys.stdout.write(gpt(args[-1], model=model) + "\n")


if __name__ == "__main__":
    main()
