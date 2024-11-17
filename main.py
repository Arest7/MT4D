import random
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.animation import Animation
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]
def average_fibonacci(numbers, fibonacci_nums):
    fib_numbers = [num for num in numbers if num in fibonacci_nums]
    if len(fib_numbers) > 0:
        return sum(fib_numbers) / len(fib_numbers)
    return 0
class FibonacciApp(MDApp):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.regenerate_button = MDRaisedButton(
            text="List generatsiya qilish",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=self.regenerate
        )
        self.input_button = MDRaisedButton(
            text="Listni kiritish",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            on_release=self.show_input_dialog
        )
        self.list_label = MDLabel(
            text="Random list: ",
            theme_text_color="Secondary",
            halign="center"
        )
        self.average_label = MDLabel(
            text="Fibonachchi sonlarini o'rta arifmetigi: ",
            theme_text_color="Secondary",
            halign="center"
        )
        self.layout.add_widget(self.list_label)
        self.layout.add_widget(self.average_label)
        self.layout.add_widget(self.regenerate_button)
        self.layout.add_widget(self.input_button)
        self.random_list = generate_random_list(20, 0, 100)
        self.fibonacci_nums = fibonacci(max(self.random_list))
        self.update_ui()
        return self.layout
    def update_ui(self):
        self.list_label.text = f"Random list: {self.random_list}"
        average = average_fibonacci(self.random_list, self.fibonacci_nums)
        self.average_label.text = f"Fibonachchi sonlarini o'rta arifmetigi: {average:.2f}"
        animation = Animation(opacity=0, duration=0.5)
        animation.bind(on_complete=self.show_updated_list)
        animation.start(self.layout)
    def show_updated_list(self, *args):
        self.list_label.text = f"Random list: {self.random_list}"
        average = average_fibonacci(self.random_list, self.fibonacci_nums)
        self.average_label.text = f"Fibonachchi sonlarini o'rta arifmetigi: {average:.2f}"
        fade_in_animation = Animation(opacity=1, duration=0.5)
        fade_in_animation.start(self.layout)
    def regenerate(self, instance):
        self.random_list = generate_random_list(20, 0, 100)
        self.update_ui()
    def show_input_dialog(self, instance):
        self.input_field = MDTextField(
            hint_text="Raqamlarnni kiriting",
            multiline=False,
            size_hint=(0.9, None),
            height="40dp",
        )
        self.dialog = MDDialog(
            title="Input List",
            type="custom",
            content_cls=self.input_field,  
            buttons=[
                MDRaisedButton(
                    text="Kiritish",
                    on_release=self.submit_input, 
                ),
                MDRaisedButton(
                    text="Bekor qilish",
                    on_release=lambda x: self.dialog.dismiss(),  
                ),
            ],
        )
        self.dialog.open()
    def submit_input(self, instance):
        try:
            user_input = list(map(int, self.input_field.text.replace(" ", "").split(",")))
            self.random_list = user_input
            self.update_ui()
            self.dialog.dismiss()  
        except ValueError:
            self.input_field.text = "Faqat raqamlarni vergul bilan ajratilgan holda kiriting."
if __name__ == "__main__":
    FibonacciApp().run()
