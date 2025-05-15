from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        positions = [
            {'x': 0.05, 'y': 0.55},
            {'x': 0.55, 'y': 0.55},
            {'x': 0.05, 'y': 0.05},
            {'x': 0.55, 'y': 0.05}
        ]

        images = [
            r"C:\Users\Hubi\Downloads\A photo with a black background and white elements inside, illustrating the concept of photos..png",
            r"C:\Users\Hubi\Downloads\A photo with a black background and white elements inside, illustrating the concept of time management and victory..png",
            r"C:\Users\Hubi\Downloads\A photo with a black background and white elements inside, illustrating the concept of time management and victory..png",
            r"C:\Users\Hubi\Downloads\A photo with a black background and white elements inside, illustrating the concept of technology. (1).png"
        ]

        button_texts = ['Pictures', 'Quotes',
                        'All you need to know', 'Bill Gates & time']

        for i in range(4):
            box = BoxLayout(orientation='vertical',
                            size_hint=(0.4, 0.4),
                            pos_hint=positions[i],
                            spacing=5)

            img = Image(source=images[i],
                        size_hint=(1, 0.8),
                        allow_stretch=True,
                        keep_ratio=True)
            btn = Button(text=button_texts[i],
                         size_hint=(1, 0.2),
                         background_color=(0.5, 0.5, 0.5, 1),
                         color=(1, 1, 1, 1))

            box.add_widget(img)
            box.add_widget(btn)
            self.add_widget(box)


class MyApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MyApp().run()
