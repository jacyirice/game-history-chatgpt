import openai
import json
from antlr.enter_player.syntax import valid as valid_syntax_enter_user
from antlr.data_story.syntax import valid as valid_syntax_data_story


def get_multi_line_input(default_message: str, num_lines: int = 3):
    lines = []
    lines.append(input(default_message))
    for _ in range(num_lines - 1):
        lines.append(input())
    return "\n".join(lines)


class GPTStory:
    def __init__(
        self, base_scenes: dict, messages: list = [], limit_scenes: int = 5, player_name: str = ""
    ):
        self.model = "gpt-3.5-turbo-0301"
        self.base_scenes = base_scenes
        self.messages = messages
        self.limit_scenes = limit_scenes
        self.player_name = player_name
        self.base_messages = []

    def prepare_initial_messages(self) -> None:
        with open("data/messages.json", "r") as f:
            messages = f.read()

            if not self.player_name:
                self.player_name = input("Qual o seu nome? ")

            messages = messages.replace("PLAYER_NAME", self.player_name)
            messages = messages.replace("LIMIT_SCENES", str(self.limit_scenes))
            messages = messages.replace("BASE_CENA_1", self.base_scenes["cena_1"])
            messages = messages.replace("BASE_CENA_FINAL", self.base_scenes["cena_final"])
            self.base_messages = json.loads(messages)

        if self.messages:
            if not valid_syntax_data_story(json.dumps(self.messages)):
                raise Exception("Invalid syntax in data/messages.json")

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

    def get_action_from_user(self, default_message: str = "Resposta:") -> str:
        action = get_multi_line_input(default_message)
        while not valid_syntax_enter_user(action):
            action = get_multi_line_input("\n" + default_message)
        return action

    def generate_next_scene(self, user_action: bool = True) -> dict:
        if user_action:
            self.messages.append(
                {
                    "role": "user",
                    "content": self.get_action_from_user(),
                }
            )
        prompt = self.generate_prompt()
        self.messages.append(prompt)
        return prompt

    def print_last_scene(self) -> None:
        print()
        print(self.messages[-1]["content"])

    def save_messages(self) -> None:
        self.messages.append(
            {
                "role": "user",
                "content": "Crie um nome curto para a historia, me retorne APENAS o nome utilizando snack_case",
            }
        )
        file_name = self.generate_prompt()["content"]
        with open(f"data/{file_name}.json", "w") as f:
            txt = json.dumps(self.messages[2:-1])
            txt = txt.replace(self.player_name, "PLAYER_NAME")
            f.write(txt)

    def run(self) -> None:
        self.prepare_initial_messages()
        scene_count = 0
        prompt = {}

        while (
            scene_count <= self.limit_scenes
            and "Fim da história".lower() not in prompt.get("content", "").lower()
        ):
            prompt = self.generate_next_scene(user_action=scene_count > 0)
            self.print_last_scene()
            scene_count += 1
