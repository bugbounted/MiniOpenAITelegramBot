import openai


def openai_request(prompt: str) -> str:
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3800,
        temperature=0,    # TODO: add user control and random option
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
    )["choices"][0]["text"].strip()
