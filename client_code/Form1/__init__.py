import random
from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from .. import Prevodilac


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.server_je_budan = False
    
    self.column_panel_1.role = None
    self.column_panel_1.visible = True
    
    self.donji_razmak = Spacer(height=55)
    self.column_panel_1.add_component(self.donji_razmak)
    
    self.flow_desno = FlowPanel(align="right")
    
    # Napravite listu u kojoj miješate nazive Font Awesome ikona i nazive vaših PNG slika iz Assets-a
    izbor = random.choice(["fa:coffee", "fa:birthday-cake", "fa:cutlery", "spagete.png", "pirinac.png"])
    
    # Ako izabrana stavka završava na .png, tretiramo je kao sliku iz Assets-a
    if izbor.endswith(".png"):
      trenutna_ikona = f"_/theme/{izbor}" # Putanja do fajla u Anvil Assets-u
    else:
      trenutna_ikona = izbor # Standardna Font Awesome tekstualna ikona
    
    self.coffee_btn = Button(
        text="Podrži nas ",
        icon=trenutna_ikona,
        icon_align="right",
        role="primary-button",
        bold=True
    )

    self.coffee_btn.set_event_handler("click", self.otvori_buymeacoffee)
    
    self.flow_desno.add_component(self.coffee_btn)
    self.column_panel_1.add_component(self.flow_desno)
    

  def otvori_buymeacoffee(self, **event_args):
    import anvil.js
    anvil.js.window.open("https://www.patreon.com/c/E2IPREVODILAC/shop", "_blank")
    

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
