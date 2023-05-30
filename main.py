import openai
import os
from dotenv import load_dotenv
from gpt_story import GPTStory

load_dotenv()


messages = [
    {
        "role": "system",
        "content": """
Você é um escritor de historias e está criando uma historia em quadrinhos para um jogo de computador.

Crie um historia com, no maximo, LIMIT_SCENES cenas. 
1. A cada cena apresente com riqueza de detalhes os sentimentos do personagem, as caracteristicas fisicas e vestimentas do personagem e o ambiente;
2. Todos os personagens devem ter um nome;
3. Toda cena deve ter um dialogo;
4. Utilize palavras de baixo calao na historia;
5. Pergunte "qual a proxima ação?" e aguarde a resposta;
6. Utilize a ação para criar a proxima cena;
7. Finalize a ultima cena com a frase "Fim da historia";
8.O nome do jogador é PLAYER_NAME, refira a ele utilizando a segunda pessoa do singular;
9. Não ultrapasse o limite de cenas;

Base da cena 1: O jogador está em um ambiente aleatorio e feliz;
Base da cena final: O jogador encontra a conjuge traindo ele com 7 homens pelados, deixe explicito que ele encontrou os 7 homens e que o jogador é corno.
""",
    },
    {
        "role": "user",
        "content": "Apresente a primeira cena mostrando o numero da cena no inicio",
    },
]


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    player_name = input("Qual o seu nome? ")
    limit_scenes = 2
    messages[0]["content"] = messages[0]["content"].replace("PLAYER_NAME", player_name)
    messages[0]["content"] = messages[0]["content"].replace(
        "LIMIT_SCENES", str(limit_scenes)
    )

    gpt_story = GPTStory(messages, limit_scenes, player_name)
    gpt_story.run()
    gpt_story.save_messages()


if __name__ == "__main__":
    main()
