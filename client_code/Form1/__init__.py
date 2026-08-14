from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import Prevodilac

class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)
    self.server_je_budan = False

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
