import flet as ft


class AlertManager:
    def __init__(self, page: ft.Page):
        self._page = page
        self._title_text = ft.Text("")
        self._alert_dialog = ft.AlertDialog(
            title=self._title_text,
            actions=[ft.TextButton("OK", on_click=self.close)],
        )

    def show_alert(self, message: str):
        self._title_text.value = message
        if self._alert_dialog.open:
            self._alert_dialog.update()
        else:
            self._page.open(self._alert_dialog)

    def close(self, e):
        self._page.close(self._alert_dialog)