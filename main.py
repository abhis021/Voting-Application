from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class VotingApp(BoxLayout):
    candidate_1_votes = NumericProperty(0)
    candidate_2_votes = NumericProperty(0)
    candidate_3_votes = NumericProperty(0)

    # Track users who have already voted
    voters = set()
    # Property to toggle admin mode
    is_admin = BooleanProperty(False)

    def vote_candidate(self, candidate, voter_id):
        if voter_id in self.voters:
            self.show_popup("You have already voted!")
            return

        if candidate == 'candidate_1':
            self.candidate_1_votes += 1
        elif candidate == 'candidate_2':
            self.candidate_2_votes += 1
        elif candidate == 'candidate_3':
            self.candidate_3_votes += 1

        # Add the voter to the set to prevent multiple voting
        self.voters.add(voter_id)

    def show_popup(self, message):
        popup = Popup(title='Alert',
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def reset_votes(self):
        self.candidate_1_votes = 0
        self.candidate_2_votes = 0
        self.candidate_3_votes = 0
        self.voters.clear()  # Clear voter tracking

    def open_admin_login(self):
        # Create a popup for admin login
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        password_input = TextInput(hint_text='Enter Admin Password', password=True, multiline=False)
        login_button = Button(text='Login', on_press=lambda x: self.admin_login(password_input.text))

        content.add_widget(password_input)
        content.add_widget(login_button)

        popup = Popup(title='Admin Login', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def admin_login(self, password):
        # Check password (you can change it to whatever you like)
        if password == "alpsandroid":
            self.is_admin = True
            self.show_popup("Admin mode enabled")
        else:
            self.show_popup("Incorrect password!")


class VotingAppApp(App):
    def build(self):
        return VotingApp()


if __name__ == "__main__":
    VotingAppApp().run()
