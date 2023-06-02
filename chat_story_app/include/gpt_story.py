import openai
import json
from .antlr.enter_player.syntax import valid as valid_syntax_enter_user
from .antlr.data_story.syntax import valid as valid_syntax_data_story


def get_multi_line_input(default_message: str, num_lines: int = 3):
    lines = []
    lines.append(input(default_message))
    for _ in range(num_lines - 1):
        lines.append(input())
    return "\n".join(lines)


class GPTStory:
    def __init__(
        self,
        base_scenes: dict,
        messages: list = [],
        limit_scenes: int = 5,
        player_name: str = "",
        scene_count = 0
    ):
        self.model = "gpt-3.5-turbo-0301"
        self.base_scenes = base_scenes
        self.messages = messages
        self.limit_scenes = limit_scenes
        self.player_name = player_name
        self.base_messages = []
        self.scene_count = scene_count

        

    def prepare_initial_messages(self) -> None:
        with open("data/messages.json", "r") as f:
            messages = f.read()

            if not self.player_name:
                self.player_name = input("Qual o seu nome? ")

            messages = messages.replace("PLAYER_NAME", self.player_name)
            messages = messages.replace("LIMIT_SCENES", str(self.limit_scenes))
            messages = messages.replace("BASE_CENA_1", self.base_scenes["cena_1"])
            messages = messages.replace(
                "BASE_CENA_FINAL", self.base_scenes["cena_final"]
            )
            self.base_messages = json.loads(messages)

        if self.messages:
            self.messages = self.base_messages + self.messages
        else:
            self.messages = self.base_messages.copy()
        return None

    def generate_prompt(self) -> dict:
        prompt = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=1,
            max_tokens=2048,
            top_p=0.5,
            frequency_penalty=0.5,
            presence_penalty=0,
        )
        return dict(prompt.choices[0]["message"])

    def generate_next_scene(self) -> dict:
        prompt = self.generate_prompt()
        self.messages.append(prompt)
        return prompt

    def get_last_scene(self) -> None:
        return self.messages[-1]["content"]

    def save_messages(self) -> None:
        self.messages.append(
            {
                "role": "user",
                "content": "Crie um nome curto para a historia, me retorne APENAS o nome utilizando snack_case",
            }
        )
        file_name = self.generate_prompt()["content"] + ".json"
        self.messages = self.messages[:-1]
        txt = json.dumps(self.messages)
        txt = txt.replace(self.player_name, "PLAYER_NAME")

        return file_name, txt
        
    def has_next_scene(self) -> bool:
        return self.scene_count <= self.limit_scenes and "Fim da história".lower() not in self.messages[-1]["content"].lower()
    
    def next_scene(self) -> None:
        if self.has_next_scene():
            self.generate_next_scene()
            self.scene_count += 1


    def run(self) -> None:
        self.prepare_initial_messages()
        return self.next_scene()
        
    def __dict__(self) -> dict:
        return {
            "base_scenes": self.base_scenes,
            "messages": self.messages[2:],
            "limit_scenes": self.limit_scenes,
            "player_name": self.player_name,
            "scene_count": self.scene_count,
        }