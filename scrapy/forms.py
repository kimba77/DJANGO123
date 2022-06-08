from . import parser, models
from django import forms


class PerserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Watchs", "Watchs"),
        ("Lalafo", "Lalafo"),
        ("Technodom", "Technodom"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self):
        if self.data["media_type"] == "Watchs":
            watchs_parser = parser.parser_func_watch()
            for data in watchs_parser:
                models.Watchs.objects.create(**data)
        elif self.data["media_type"] == "Technodom":
            technodom_parser = parser.parser_func_technodom()
            for data in technodom_parser:
                models.Tehchnodom.objects.create(**data)

            # if models.Plants.objects.filter(user=user).exists():
            #     pass
            # else:
            #     models.Plants.objects.create(user=user, count=count_number)
