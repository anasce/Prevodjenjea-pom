from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from .. import Prevodilac


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.server_je_budan = False
    
    # Omogućavamo da panel ispod rezultata bude vidljiv
    self.column_panel_1.visible = True
    
    # --- PLAVO DUGME ZA PODRŠKU ISPOD REZULTATA ---
    self.coffee_lnk = Link(
        text="Podrži nas 🥣",
        icon="fa:bowl-rice",  # Ikona činije
        url="https://buymeacoffee.com",  # <-- Ovdje upiši svoje korisničko ime
        role="button",
        foreground="#ffffff",
        background="#226096",  # Prelijepa plava boja koja se slaže sa podnaslovom aplikacije
        bold=True
    )
    # Dodajemo dugme direktno u panel koji se nalazi ispod text_area_2
    self.column_panel_1.add_component(self.coffee_lnk)
    # ----------------------------------------------
    

  @handle("text_area_1", "change")
  def text_area_1_change(self, **event_args):
    """Ova metoda se poziva automatski dok korisnik kuca u text_area_1"""
    if not self.server_je_budan and len(self.text_area_1.text.strip()) >= 2:
      self.server_je_budan = True
      # call_s (silent) budi server u pozadini bez prikazivanja indikatora učitavanja
      #anvil.server.call_s('probudi_server')
      Prevodilac.probudi_server()

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.text_area_1.text.strip():
      return

    # Vizuelno blokiramo dugme da spriječimo dupli klik tokom obrade
    self.button_1.enabled = False
    #self.button_1.text = "Prevođenje..."

    # Pošto je server pokrenut unaprijed dok je korisnik kucao, poziv je trenutan
    #result = anvil.server.call('ijekavizuj_tekst', ulazni_tekst=self.text_area_1.text)
    result = Prevodilac.ijekavizuj_tekst(self.text_area_1.text)

    # Prikazujemo rezultat i vraćamo dugme u funkciju
    self.text_area_2.text = result
    self.button_1.enabled = True
    #self.button_1.text = "Prevedi"
    
    # Resetujemo zastavu za sledeći unos
    self.server_je_budan = False
