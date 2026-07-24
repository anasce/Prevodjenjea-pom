from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #self.text_area_2.text=self.text_area_1.text
    # 2. Call the server function and store the returned value
    result = anvil.server.call('ijekavizuj_tekst', ulazni_tekst=self.text_area_1.text)

    # 3. Use the result in your UI
    self.text_area_2.text = result
