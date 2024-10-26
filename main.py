from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock  # Import Clock for scheduling
from kivy.core.window import Window

class VotingApp(BoxLayout):
    candidate_1_votes = NumericProperty(0)
    candidate_2_votes = NumericProperty(0)
    candidate_3_votes = NumericProperty(0)

    # Track users who have already voted
    voters = set()
    # Property to toggle admin mode
    is_admin = BooleanProperty(False)
    # Variable to keep track of the currently active popup
    current_popup = None

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
        # Create a label for the message
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))

        # Create an OK button
        ok_button = Button(text='OK', size_hint_y=None, height=40)
        content.add_widget(ok_button)

        # Create the popup
        popup = Popup(title='Alert', content=content, size_hint=(None, None), size=(400, 200))
        self.current_popup = popup  # Set the current popup reference

        # Bind the button to dismiss the popup
        ok_button.bind(on_press=lambda x: self.dismiss_popup(popup))

        popup.open()

        # Schedule focusing on the password input after the popup opens
        Clock.schedule_once(lambda dt: self.password_input.focus == True, 0.1)

    def dismiss_popup(self, popup):
        popup.dismiss()
        self.current_popup = None  # Clear the current popup reference

    def reset_votes(self):
        self.candidate_1_votes = 0
        self.candidate_2_votes = 0
        self.candidate_3_votes = 0
        self.voters.clear()  # Clear voter tracking

    def open_admin_login(self):
        # Create a popup for admin login
        self.login_popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.password_input = TextInput(hint_text='Enter Admin Password', password=True, multiline=False)
        self.login_button = Button(text='Login', size_hint_y=None, height=40)

        self.login_popup_content.add_widget(self.password_input)
        self.login_popup_content.add_widget(self.login_button)

        self.login_popup = Popup(title='Admin Login', content=self.login_popup_content, size_hint=(None, None), size=(400, 200))

        # Bind the login button and Enter key
        self.login_button.bind(on_press=lambda x: self.admin_login(self.password_input.text, self.login_popup))
        self.password_input.bind(on_text_validate=lambda x: self.admin_login(self.password_input.text, self.login_popup))

        self.login_popup.open()

        # Schedule focusing on the password input after the popup opens
        Clock.schedule_once(lambda dt: self.password_input.focus == True, 0.1)

    def admin_login(self, password, popup):
        # Check password (you can change it to whatever you like)
        if password == "admin123":
            self.is_admin = True
            self.show_popup("Admin mode enabled")
            popup.dismiss()  # Dismiss the login popup
        else:
            self.show_popup("Incorrect password!")

    def admin_logout(self):
        self.is_admin = False
        self.show_popup("Admin mode disabled")

# Function to handle key events
def on_key_down(window, key, scancode, codepoint, modifier):
    if key == 13:  # Check if Enter key is pressed (key code 13)
        if VotingApp.current_popup:  # Check if there is an active popup
            # Find the OK button and trigger its action
            for child in VotingApp.current_popup.content.children:
                if isinstance(child, Button) and child.text == 'OK':
                    child.trigger_action()  # Simulate button press
                    break

class VotingAppApp(App):
    def build(self):
        Window.bind(on_key_down=on_key_down)  # Bind the key down event
        return VotingApp()

if __name__ == "__main__":
    VotingAppApp().run()
