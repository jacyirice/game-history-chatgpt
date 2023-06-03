import json
from .include.gpt_story import GPTStory


def get_gpt_story(request, create=True, messages=[]) -> GPTStory:
    if create:
        if messages:
            messages = json.loads(messages)
            messages[-1]["content"] = messages[-1]["content"].replace("Fim da história", "Qual a proxima ação?")

        base = {
            "base_scenes": {
                "cena_1": request.POST.get("cena_1"),
                "cena_final": request.POST.get("cena_final"),
            },
            "messages": messages,
            "limit_scenes": int(request.POST.get("limit_scenes")),
            "player_name": request.POST.get("player_name"),
            "is_family_friendly": request.POST.get("is_family_friendly", True)
        }
        gpt_story = GPTStory(**base)
        if messages:
            gpt_story.prepare_initial_messages()
        else:
            gpt_story.run()
        request.session["gpt_story"] = gpt_story.__dict__()
    else:
        base = request.session["gpt_story"]
        gpt_story = GPTStory(**base)
    return gpt_story
