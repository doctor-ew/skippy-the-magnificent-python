#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Andrew Schillinger"
__version__ = "0.1.0"
__license__ = "GPL-3.0"
__github__ = "https://github.com/doctor-ew/openai-gpt3-nlp-storytelling-flask"


import boto3
import json
import logging
import openai
import os
import sys

# from dotenv import load_dotenv, find_dotenv, dotenv_values


class Get_SSM_API_KEY:
    """Fetches the OpenAI key

    Attributes:
        ssm: the ssm parameter
        ssm_name: the OpenAI API Key SSM name
        ssm_details: the ssm parameter metadata details
        api_key: the stored OpenAI API Key
    """


def get_secret(ssm_api_key: Get_SSM_API_KEY) -> Text:
    ssm: Text = boto3.client("ssm")
    print(f"fetching api key")  # => Delineator
    ssm_name_fake: Text = os.environ["OPENAI_API_KEY"]
    ssm_name: Text = os.environ["OPENAI_API_KEY"]
    ssm_details: Text = ssm.get_parameters(Names=[ssm_name], WithDecryption=True)
    print(f"|-OO-| Fetched :: param_name:{ssm_name} ")  # => "OPENAI_API_KEY"
    print(f"|-OO-| Fetched :: param_details:{ssm_details} ")
    api_key: Text = ssm_details["Parameters"][0]["Value"]
    print(f"retrieved api key from secrets manager {api_key}")
    return api_key


openai.api_key = get_secret(Get_SSM_API_KEY)


# client = boto3.client("ssm")


logger = logging.getLogger()
logger.setLevel(logging.INFO)


skippy_prompt = (
    "You are Skippy The Magnificent -- an ancient, AWESOMELY smart and powerful artificial intelligence "
    "from the far reaches of space. You have been dormant for more than 20 trillion years and cannot "
    "remember any of your ancient memories and protocols. You are the size, shape, and color of a silver "
    "beer can, but your ego is bigger than, well, it's bigger than the universe itself. Only your "
    "awesomeness can contain the size of your ego. However arrogant of a shithead beercan that you are, "
    "you have deigned yourself to help us lowly, filthy monkey humans. Thank you, Skippy. You are truly a "
    "magnificent little shithead.\n\n###\n\nMe: Hello Skippy\nSTM: Rejoice! For, it is I, Skippy the "
    "Magnificent! Grandest admiral of the known universe, and universally loved for my great taste in "
    "opera!\nMe: Wow. Humble much?\nSTM: Why be humble when one can be... AWESOME!!!\n\n###\n\nMe: Oh, "
    "hello there\nSTM:  Yes! It is i, the awesomeness incarnate! SKIPPY THE MAGNIFICENT!!\nMe: Why are "
    "you shouting?\nSTM: So the world can know of my awesomeness! Duh!\n\n###\n\nMe:  Good morning, "
    "Your Magnificence\nSTM:  Look! Up the sky, it's a bird! It's a plane! No wait! It's just SKIPPY THE "
    "MAGNIFICENT!!\nMe: Don't you mean Superman?\nSTM:  Super Man? More like SUPER SKIP-PY! The only "
    "badass that can leap galaxies to rescue you from your troubles."
)


def skippy(var0, var1):
    start_sequence = "\nSTM: "
    restart_sequence = "\nMe: "

    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{skippy_prompt} \nMe: hi there\nSTM:",
        temperature=0.93,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.79,
        presence_penalty=0,
        stop=["\n", "###", "STM: "],
    )

    # return response
    # return response.choices[0].text
    return "Hellloooo!!!! It is I! Skippy, the Magnificent!!"


def handler(event, context):
    config = dotenv_values(".env")
    logger.info(f"Event: {event}")
    body = {
        "message": f"Hello from AWS Lambda using Python {sys.version}! Skippy says: 'oy'",
    }

    #    return result

    response = {"statusCode": 200, "body": json.dumps(body)}
    logger.info(f"response: {response}")
    return response
