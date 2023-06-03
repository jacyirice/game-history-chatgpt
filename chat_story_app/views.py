from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views import View

from .include.antlr.enter_player.syntax import valid as valid_syntax_enter_user
from .include.antlr.data_story.syntax import valid as valid_syntax_data_story
from .utils import get_gpt_story
from .models import ChatStory
# Create your views here.


@method_decorator(login_required, name="dispatch")
class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        if "gpt_story" in request.session:
            del request.session["gpt_story"]

        return render(request, self.template_name)

    def post(self, request):
        cena_1 = request.POST.get("cena_1")
        cena_final = request.POST.get("cena_final")
        limit_scenes = request.POST.get("limit_scenes")
        player_name = request.POST.get("player_name")

        if cena_final and limit_scenes and player_name:
            messages = request.FILES.get("messages")
            url = "chat_view"

            if messages:
                messages = messages.read().decode("utf-8")
                status, error = valid_syntax_data_story(messages)

                if not status:
                    context = {"error_input_file": error}
                    return render(request, self.template_name, context)

                url = reverse(url) + f"?scene_num=0"

            gpt_story = get_gpt_story(request, messages=messages)
            return redirect(url)

        return redirect("home_view")


@method_decorator(login_required, name="dispatch")
class ChatView(View):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        if "gpt_story" not in request.session:
            return redirect("home_view")

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        scene_num = request.GET.get("scene_num", None)
        if scene_num is not None:
            scene_num = int(scene_num)
            gpt_story = get_gpt_story(request, create=False)
            context = {
                "texto": gpt_story.messages[scene_num]["content"],
                "scene_num": str(scene_num),
                "last_scene_num": len(gpt_story.messages)-1,
            }
        else:
            gpt_story = get_gpt_story(request, create=False)
            if gpt_story.messages[-1]["role"] == "user":
                gpt_story.run()
                request.session["gpt_story"] = gpt_story.__dict__()

            context = {
                "texto": gpt_story.get_last_scene(),
                "has_next_scene": gpt_story.has_next_scene(),
                "last_scene_num": str(len(gpt_story.messages) - 1),
            }
        return render(request, self.template_name, context)

    def post(self, request):
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
            return render(request, self.template_name, context)
        
        gpt_story_session = request.session["gpt_story"].copy()
        gpt_story_session["messages"].append(
            {
                "role": "user",
                "content": action,
            }
        )
        request.session["gpt_story"] = gpt_story_session

        return redirect("chat_view")


@login_required
def download_story(request):
    if not "gpt_story" in request.session:
        return redirect("home_view")

    gpt_story = get_gpt_story(request, create=False)
    file_name, txt = gpt_story.save_messages()
    response = HttpResponse(txt, content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'
    
    ChatStory.objects.create(
        title=file_name,
        description=txt,
        user=request.user
    )
    
    return response
