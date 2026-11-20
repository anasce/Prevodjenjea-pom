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
    
    izabrana_ikona = random.choice(["fa:coffee",   "fa:beer", "fa:glass", "fa:ik"])

    
    self.coffee_btn = Button(
        text="Podrži nas ",
        icon=izabrana_ikona,
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
import anvil.js

anvil.js.window.eval("""
(function() {
  if (document.getElementById('praznicni-prostor')) return;

  const style = document.createElement('style');
  style.textContent = `
    #praznicni-prostor {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 999999;
      overflow: hidden;
    }
    .lebdeci-elem {
      position: absolute;
      font-size: 24px;
      user-select: none;
      pointer-events: none;
      text-shadow: 0 0 6px rgba(0, 0, 0, 0.35);
      transition-property: top, left, transform;
      transition-timing-function: ease-in-out;
    }
  `;
  document.head.appendChild(style);

  const kontejner = document.createElement('div');
  kontejner.id = 'praznicni-prostor';
  document.body.appendChild(kontejner);

  const bijelaPahuljaSVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/><line x1="19.07" y1="4.93" x2="4.93" y2="19.07"/></svg>';

  const simboli = [
    '🤶','🎅', '🦌', '⛄', '🎄',
    bijelaPahuljaSVG, bijelaPahuljaSVG, bijelaPahuljaSVG,
    '🎅','🤶', '🦌', '⛄', '🎄',
    bijelaPahuljaSVG, bijelaPahuljaSVG, bijelaPahuljaSVG,
    '⭐', '🌟', '✨', '💫',
    '🎊', '🎉', '🎀', '🎁',
    '🥂', '🍾', '🎆', '🎇',
    '🔔', '🕯️', '❄️','🛷'
  ];

  simboli.forEach(function(simbol) {
    const el = document.createElement('div');
    el.className = 'lebdeci-elem';
    el.innerHTML = simbol;
    el.style.left = Math.random() * 95 + 'vw';
    el.style.top = Math.random() * 95 + 'vh';
    kontejner.appendChild(el);

    function pomjeriNasumicno() {
      const trajanje = 4 + Math.random() * 6;
      const novaLijeva = Math.random() * 94;
      const novaGornja = Math.random() * 94;
      const rotacija = (Math.random() * 60) - 30;

      el.style.transitionDuration = trajanje + 's';
      el.style.left = novaLijeva + 'vw';
      el.style.top = novaGornja + 'vh';
      el.style.transform = 'rotate(' + rotacija + 'deg)';

      setTimeout(pomjeriNasumicno, trajanje * 1000);
    }

    setTimeout(pomjeriNasumicno, 100);
  });
})();
""")
    
