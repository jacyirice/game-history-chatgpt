import openai
import os
from dotenv import load_dotenv
from gpt_story import GPTStory

load_dotenv()


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    limit_scenes = 2

    gpt_story = GPTStory(limit_scenes=limit_scenes)
    gpt_story.run()
    gpt_story.save_messages()


if __name__ == "__main__":
    main()
