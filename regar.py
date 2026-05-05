import reflex as rx

class State(rx.State):
    texto = "Bienvenido a mi página web"

    def cambiar_texto(self):
        self.texto = "¡Gracias por hacer clic!"

def index():
    return rx.center(
        rx.vstack(
            rx.heading("Mi primera página con Reflex"),
            rx.text(State.texto),
            rx.button("Haz clic aquí", on_click=State.cambiar_texto)
        )
    )

app = rx.App()
app.add_page(index)
