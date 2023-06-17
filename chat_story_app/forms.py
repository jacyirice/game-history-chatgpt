from django import forms
from django.core.exceptions import ValidationError
from .include.antlr.data_story.syntax import valid as valid_syntax_data_story


class HomeForm(forms.Form):
    cena_1 = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2}),
    )
    cena_final = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 2})
    )
    limit_scenes = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        initial=2,
        label="Número de Cenas",
    )
    player_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Nome do Jogador",
    )
    family_friendly = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="História Family Friendly",
    )
    messages = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control-file"}),
        label="Arquivo de Mensagens",
    )

    def clean(self):
        cleaned_data = super().clean()
        cena_final = cleaned_data.get("cena_final")
        limit_scenes = cleaned_data.get("limit_scenes")
        player_name = cleaned_data.get("player_name")
        cena_1 = cleaned_data.get("cena_1")
        messages = self.files.get("messages")

        if not (cena_final and limit_scenes and player_name):
            raise ValidationError("Preencha todos os campos obrigatórios.")

        if not (cena_1 or messages):
            raise ValidationError(
                "Preencha a Cena Inicial ou envie um arquivo de mensagens."
            )
        return cleaned_data

    def clean_messages(self):
        messages = self.files.get("messages")
        if messages:
            if messages.content_type != "application/json":
                raise ValidationError(
                    "O arquivo de mensagens deve ser um arquivo de texto (application/json)."
                )

            messages = messages.read().decode("utf-8")
            status, error = valid_syntax_data_story(messages)

            if not status:
                raise ValidationError(error)
        return messages
