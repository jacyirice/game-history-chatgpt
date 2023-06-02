import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .include.antlr.enter_player.syntax import valid as valid_syntax_enter_user
from .include.antlr.data_story.syntax import valid as valid_syntax_data_story
from .utils import get_gpt_story
from .models import StoryCount

# Create your views here.


@login_required
def home_view(request):
    if request.method == "POST":
        if (
            request.POST.get("cena_1")
            and request.POST.get("cena_final")
            and request.POST.get("limit_scenes")
            and request.POST.get("player_name")
        ):
            messages = request.FILES.get("messages", [])
            if messages:
                messages = messages.read().decode("utf-8")
                status, error = valid_syntax_data_story(messages)
                if not status:
                    context = {"error_input_file": error}
                    return render(request, "home.html", context)

            gpt_story = get_gpt_story(request, messages=messages)
            return redirect("chat_view")
        else:
            return redirect("home_view")
    else:
        if "gpt_story" in request.session:
            del request.session["gpt_story"]

        return render(request, "home.html")


@login_required
def chat_view(request):
    if not "gpt_story" in request.session:
        return redirect("home_view")

    if request.method == "POST":
        action = request.POST.get("input_action")
        status, error = valid_syntax_enter_user(action)

        if not status:
            context = {"input_value": action, "error_input": error}
            gpt_story = get_gpt_story(request, create=False)
            gpt_story.prepare_initial_messages()
            context.update(
                {
                    "texto": gpt_story.get_last_scene(),
                    "has_next_scene": gpt_story.has_next_scene(),
                }
            )
            return render(request, "index.html", context)

        request.session["gpt_story"]["messages"] += [
            {
                "role": "user",
                "content": action,
            }
        ]

    gpt_story = get_gpt_story(request, create=False)
    if gpt_story.messages[-1]["role"] == "user":
        gpt_story.run()
        request.session["gpt_story"] = gpt_story.__dict__()

    context = {
        "texto": gpt_story.get_last_scene(),
        "has_next_scene": gpt_story.has_next_scene(),
    }
    return render(request, "index.html", context)


@login_required
def download_story(request):
    if not "gpt_story" in request.session:
        return redirect("home_view")

    gpt_story = get_gpt_story(request, create=False)
    file_name, txt = gpt_story.save_messages()
    response = HttpResponse(txt, content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    return response
