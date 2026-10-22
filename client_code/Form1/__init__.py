from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from .. import Prevodilac


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.server_je_budan = False
    
    # Uklanjamo "card" ulogu kako bi bijelo polje postalo nevidljivo
    self.column_panel_1.role = None
    self.column_panel_1.visible = True
    
    # Kreiramo FlowPanel koji se ravna udesno
    self.flow_desno = FlowPanel(align="right")
    
    # Kreiramo plavo dugme sa dodatnim razmakom na kraju teksta ("🥣 ") da ikonica ne bude odsječena
    self.coffee_lnk = Link(
        text="Podrži nas 🥣 ",  # Dodat razmak na kraju da se osigura ivica
        icon="fa:bowl-rice",
        url="https://buymeacoffee.com",  # <-- Unesi svoje korisničko ime
        role="button",
        foreground="#ffffff",
        background="#226096",
        bold=True
    )
    
    # Dodajemo mali unutrašnji razmak sa desne strane direktno kroz HTML/CSS stil komponente
    self.coffee_lnk.style = "padding-right: 12px !important; display: inline-flex; align-items: center;"
    
    # Slažemo komponente
    self.flow_desno.add_component(self.coffee_lnk)
    self.column_panel_1.add_component(self.flow_desno)
    

  @handle("text_area_1", "change")
  def text_area_1_change(self, **event_args):
    """Ova metoda se poziva automatski dok korisnik kuca u text_area_1"""
    if not self.server_je_budan and len(self.text_area_1.text.strip()) >= 2:
      self.server_je_budan = True
      Prevodilac.probudi_server()

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.text_area_1.text.strip():
      return

    self.button_1.enabled = False
    result = Prevodilac.ijekavizuj_tekst(self.text_area_1.text)

    self.text_area_2.text = result
    self.button_1.enabled = True
    self.server_je_budan = False
