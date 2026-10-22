from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from .. import Prevodilac


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.server_je_budan = False
    self.column_panel_1.visible = False
    

  @handle("text_area_1", "change")
  def text_area_1_change(self, **event_args):
    if not self.server_je_budan and len(self.text_area_1.text.strip()) >= 2:
      self.server_je_budan = True
      Prevodilac.probudi_server()

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    if not self.text_area_1.text.strip():
      return

    self.button_1.enabled = False
    result = Prevodilac.ijekavizuj_tekst(self.text_area_1.text)

    self.text_area_2.text = result
    self.button_1.enabled = True
    self.server_je_budan = False
