import argparse

import openai
from tqdm import trange

import config
from utils.open_ai import set_api_key
from utils.read_file import parse_pdf
from utils.save_file import save_txt
from utils.utils import parse_filename


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--filepath", required=True)
    parser.add_argument("--model_engine", default="gpt-3.5-turbo")
    parser.add_argument(
        "--max_tokens", default=300, help="maximum number of tokens for summarization"
    )
    return parser.parse_args()


def open_ai_send_request(text_to_summarize: str, engine: str, max_tokens: int) -> str:
    response = openai.ChatCompletion.create(
        model=engine,
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following text: '{text_to_summarize}'",
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )
    summary = response.choices[0].message.content.strip()
    return summary


def request_summary(text_to_summarize: str, args) -> str:
    # on evarage 100 tokens is ±75 words
    if len(text_to_summarize) * config.TOKE_WORD_COEF > config.MODEL_MAX_TOKENS:
        summary = list()
        for i in trange(0, len(text_to_summarize), config.MODEL_MAX_TOKENS):
            chunk = " ".join(text_to_summarize[i : i + config.MODEL_MAX_TOKENS])
            chunck_summary = open_ai_send_request(
                chunk, args.model_engine, args.max_tokens
            )
            summary.append(chunck_summary)
        summary = "\n".join(summary)
    else:
        summary = open_ai_send_request(
            text_to_summarize, args.model_engine, args.max_tokens
        )
    return summary


def summarize(args) -> None:
    # reading pdf file
    text = parse_pdf(args.filepath)
    filename = config.CACHE_DIR / parse_filename(args.filepath)
    save_txt(filename, text)

    print(
        "Estimated number of tokens in text: ", int(len(text) * config.TOKE_WORD_COEF)
    )
    # send for summarization
    summary = request_summary(text, args)
    save_txt(str(filename) + f'_summary_{args.max_tokens}_tokens', summary)


if __name__ == "__main__":
    args = parse_args()
    set_api_key(config.OPENAI_KEY_API)

    summarize(args)
