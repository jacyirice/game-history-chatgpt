import openai
import json
from antlr.entrada_usuario import validar_sintaxe_entrada


class GPTStory:
    def __init__(
        self, messages: list = [], limit_scenes: int = 5, player_name: str = ""
    ):
        self.model = "gpt-3.5-turbo-0301"
        self.messages = messages
        self.limit_scenes = limit_scenes
        self.player_name = player_name

    def prepare_initial_messages(self) -> None:
        if self.messages:
            return None

        with open("data/messages.json", "r") as f:
            messages = f.read()
            messages = messages.replace(
                "PLAYER_NAME", self.player_name or input("Qual o seu nome? ")
            )
            messages = messages.replace("LIMIT_SCENES", str(self.limit_scenes))
            self.messages = json.loads(messages)
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
        action = input(default_message)
        while not validar_sintaxe_entrada(action):
            action = input("\n"+default_message)
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
                "content": "Crie um nome curto para a historia e me retorne apenas o nome utilizando snack_case",
            }
        )
        file_name = self.generate_prompt()["content"]
        with open(f"data/{file_name}.json", "w") as f:
            f.write(json.dumps(self.messages))

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
