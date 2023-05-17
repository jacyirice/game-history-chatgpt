import openai
import os
from dotenv import load_dotenv
from antlr.entrada_usuario import validar_sintaxe_entrada

load_dotenv()


def get_prompt(messages: list) -> dict:
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.7, max_tokens=500
    ).choices[0]["message"]


def get_initial_messages(player_name: str) -> list:
    return [
        {
            "role": "system",
            "content": f"""
Crie um historia com, no maximo, 4 cenas. 
1. Não quero cenas curtas e mal desenvolvidas, quero cenas com dialogos e que mantenham o interesse do jogador;
2. A historia deve começar apresentando um homem, que no caso é o jogador, em um ambiente aleatorio e terminar com a cena do homem encontrando a mulher traindo ele com 7 homens pelados, deixe explicito que ele encontrou os 7 homens e que o jogador é corno; 
3. Utilize palavras de baixo calao na historia para dar um mais realista e menos culto;
4. A cada cena você deve pedir para eu digitar uma ação e criar a proxima cena baseada nessa ação. Pergunte "qual a proxima ação?" e aguarde a resposta;
5. O nome do jogador é {player_name}, refira a ele utilizando a segunda pessoa do singular e apresente cada novo personagem com um nome novo.
6. Mostre o numero da cena no inicio e Não ultrapasse o limite de cenas
7. Finalize a ultima cena com a frase "Fim da historia"
""",
        },
        {
            "role": "user",
            "content": "Apresente a primeira cena mostrando o numero da cena no inicio",
        },
    ]


def get_next_scene(messages: list, user_action: bool = True) -> dict:
    if user_action:
        action = input("Resposta:")
        while not validar_sintaxe_entrada(action):
            action = input("\nResposta:")
        messages.append({"role": "user", "content": action})
    prompt = get_prompt(messages)
    messages.append(dict(prompt))
    return prompt


def show_scene(prompt: dict) -> None:
    print()
    print(prompt["content"])


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    player_name = input("Qual o seu nome? ")
    messages = get_initial_messages(player_name)
    prompt = get_next_scene(messages, False)
    show_scene(prompt)
    while (
        len(messages) < 10
        and "Fim da história".lower() not in prompt["content"].lower()
    ):
        prompt = get_next_scene(messages)
        show_scene(prompt)


if __name__ == "__main__":
    main()
