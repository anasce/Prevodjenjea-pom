import sys, os, re 
import anvil.server

EXACT = [
  
  ('doprineo', 'doprinio'),
  ('razboleo', 'razbolio'),
  ('sledeći', 'slijedeći'), 
  ('zamenik', 'zamjenik'),
  ('svideo', 'svidio'),
  ('uvideo', 'uvidio'),
  ('napred', 'naprijed'),
  ('pevac', 'kokot'),
  ('video', 'vidio'),
  ('vreme', 'vrijeme'),
  ('doneo', 'donijeo'),
  ('sreda', 'srijeda'),
  ('hteo', 'htio'),
  ('uspeo', 'uspio'),
  ('uvid', 'uvid'),
  ('dete', 'dijete'),
  ('plen', 'plijen'),
  ('žele', 'žele'),
  ('sme', 'smije'),
  ('smeo', 'smio'),
  ('dele', 'dijele'),
  ('dece', 'djece'),
  ('leta', 'ljeta'),
  ('dve', 'dvije'),
  ('pre', 'prije'),
  ('bes', 'bijes'),
  ('deo', 'dio'),
  ('dev', 'djev'),
  ('lek', 'lijek'),



]


STEMS = [
    ('četvoromeseč', 'četvoromjeseč'),
    ('devetomeseč', 'devetomjeseč'),
    ('desetomeseč', 'desetomjeseč'),
    ('pretpostavk', 'pretpostavk'),
    ('predstavnik', 'predstavnik'),
    ('jednomeseč', 'jednomjeseč'),
    ('petomeseč', 'petomjeseč'),
    ('šestomeseč', 'šestomjeseč'),
    ('sedmomeseč', 'sedmmjeseč'),
    ('osmomeseč', 'osmoomjeseč'),
    ('presecanj', 'presijecanj'),
    ('predvide', 'predvidje'),
    ('potpreds', 'potpredsj'),
    ('dragocen', 'dragocjen'),
    ('dvomeseč', 'dvomjeseč'),
    ('zakasnel', 'zakašnjel'),
    ('tromeseč', 'tromjeseč'),
    ('opredeli', 'opredijeli'),
    ('ponedelj', 'ponedjelj'),
    ('opredelj', 'opredjelj'),
    ('pregreja', 'pregrija'),
    ('povredi', 'povrijedi'),
    ('obavest', 'obavijest'),
    ('izbegav', 'izbjegav'),
    ('delegat', 'delegat'),
    ('osvedoč', 'osvjedoč'),
    ('poverlj', 'povjerlj'),
    ('obavešt', 'obavješt'),
    ('zabelež', 'zabiljež'),
    ('podsmeh', 'podsmjeh'),
    ('prebole', 'prebolje'),
    ('premešt', 'premješt'),
    ('premest', 'premjest'),
    ('dodelj', 'dodijelj'),
    ('odeljak', 'odjeljak'),
    ('doprinel', 'doprinijel'),
    ('doprinos', 'doprinios'),
    ('neizbež', 'neizbjež'),
    ('neizmer', 'neizmjer'),
    ('telefon', 'telefon'),
    ('letelic', 'letjelic'),
    ('nadžive', 'nadživje'),
    ('prosleđ', 'prosljeđ'),
    ('osvetli', 'osvijetli'),
    ('osvetlj', 'osvjetlj'),
    ('pobeg', 'pobjeg'),
    ('dodel', 'dodjel'),
    ('pobegl', 'pobjegl'),
    ('prevar', 'prevar'),
    ('povest', 'povijest'),
    ('prosle', 'proslije'),
    ('gnezdo', 'gnijezdo'),
    ('unapre', 'unaprije'),
    ('razbole', 'razbolje'),
    ('nalepn', 'naljepn'),
    ('zaplena', 'zapljena'),
    ('zaplenu', 'zapljenu'),
    ('zapleni', 'zaplijeni'),
    ('zaplene', 'zapljene'),
    ('proceni', 'procijeni'),
    ('procena', 'procjena'),
    ('procene', 'procjene'),
    ('procenu', 'procjenu'),
    ('bekstv', 'bjekstv'),
    ('napredo', 'napredo'),
    ('napredn', 'napredn'),
    ('proter', 'protjer'),
    ('nasled', 'naslijed'),
    ('pogreš', 'pogriješ'),
    ('dodeli', 'dodijeli'),
    ('promen', 'promjen'),
    ('izvesn', 'izvjesn'),
    ('izvest', 'izvijest'),
    ('pobedi', 'pobijedi'),
    ('porekl', 'porijekl'),
    ('posled', 'posljed'),
    ('razume', 'razumije'),
    ('razume', 'razumje'),
    ('predst', 'predst'),
    ('odeven', 'odjeven'),
    ('dospel', 'dospjel'),
    ('pešačk', 'pješačk'),
    ('posred', 'posred'),
    ('decemb', 'decemb'),
    ('namešt', 'namješt'),
    ('zaplen', 'zaplijen'),
    ('detinj', 'djetinj'),
    ('svugde', 'svugdje'),
    ('savest', 'savjest'),
    ('proleć', 'proljeć'),
    ('nalep', 'nalijep'),
    ('nalete', 'naletje'),
    ('svetsk', 'svjetsk'),
    ('povređ', 'povrijeđ'),
    ('neuspe', 'neuspje'),
    ('vaspit', 'vaspit'),
    ('podela', 'podjela'),
    ('smatra', 'smatra'),
    ('dožive', 'doživje'),
    ('preseć', 'presjeć'),
    ('preduz', 'preduz'),
    ('stalež', 'stalež'),
    ('obelež', 'obiljež'),
    ('izgore', 'izgorje'),
    ('prosek', 'prosijek'),
    ('proseč', 'prosječ'),
    ('nedelj', 'nedjelj'),
    ('razmer', 'razmjer'),
    ('primer', 'primjer'),
    ('menjač', 'mjenjač'),
    ('svetlo', 'svjetlo'),
    ('posled', 'posljed'),
    ('zaposl', 'zaposl'),
    ('zapose', 'zaposje'),
    ('vremen', 'vremen'),
    ('neretk', 'nerijetk'),
    ('usled', 'usljed'),
    ('devet', 'devet'),
    ('želel', 'željel'),
    ('pleni', 'plijeni'),
    ('posle', 'poslije'),
    ('greši', 'griješi'),
    ('delima', 'djelima'),
    ('prene', 'prenije'),
    ('letak', 'letak'),
    ('oceni', 'ocijeni'),
    ('detet', 'djetet'),
    ('strelj','strijelj'),
    ('kolev', 'kolijev'),
    ('podne', 'podne'),
    ('koren', 'korijen'),
    ('svide', 'svidje'),
    ('čovek', 'čovjek'),
    ('cveta', 'cvjeta'),
    ('ucena', 'ucjena'),
    ('ucene', 'ucjene'),
    ('ucenu', 'ucjenu'),
    ('uceni', 'ucijeni'),
    ('decem', 'decem'),
    ('zaver', 'zavjer'),
    ('savet', 'savjet'),
    ('podel', 'podijel'),
    ('lekar', 'ljekar'),
    ('zamen', 'zamijen'),
    ('mesec', 'mjesec'),
    ('levic', 'ljevic'),
    ('levič', 'ljevič'),
    ('posed', 'posjed'),
    ('poset', 'posjet'),
    ('poseć', 'posjeć'),
    ('negde', 'negdje'),
    ('najpr', 'najprij'),
    ('smešt', 'smješt'),
    ('smest', 'smjest'),
    ('živet', 'živjet'),
    ('živel', 'živjel'),
    ('živeo', 'živio'),
    ('nedel', 'nedjel'),
    ('odole', 'odolje'),
    ('uvide', 'uvidje'),
    ('pover', 'povjer'),
    ('dodel', 'dodjel'),
    ('svedo', 'svjedo'),
    ('never', 'nevjer'),
    ('venac', 'vijenac'),
    ('umest', 'umjest'),
    ('oseća', 'osjeća'),
    ('izmen', 'izmijen'),
    ('zamer', 'zamjer'),
    ('detalj', 'detalj'),
    ('belež', 'biljež'),
    ('osvet', 'osvjet'),
    ('obole', 'obolje'),
    ('teles', 'tjeles'),
    ('kolen', 'koljen'),
    ('uspeh', 'uspjeh'),
    ('predse', 'predsje'),
    ('izmer', 'izmjer'),
    ('izveš', 'izvješ'),
    ('izbeg', 'izbjeg'),
    ('lepot', 'ljepot'),
    ('vetar', 'vjetar'),
    ('sever', 'sjever'),
    ('nemač', 'njemač'),
    ('napad', 'napad'),
    ('izved', 'izved'),
    ('nared', 'nared'),
    ('smenj', 'smjenj'),
    ('zvezd', 'zvjezd'),
    ('delat', 'djelat'),
    ('devoj', 'djevoj'),
    ('beleg', 'biljeg'),
    ('zased', 'zasijed'),
    ('namer', 'namjer'),
    ('nemac', 'njemac'),
    ('delim', 'dijelim'),
    ('želet', 'željet'),
    ('ocenj', 'ocijenj'),
    ('greja', 'grija'),
    ('smeja', 'smija'),
    ('iznet', 'iznijet'),
    ('cenit', 'cijeniti'),
    ('sreds', 'sreds'),
    ('cvet', 'cvijet'),
    ('slep', 'slijep'),
    ('deca', 'djeca'),
    ('deci', 'djeci'),
    ('decu', 'djecu'),
    ('deco', 'djeco'),
    ('uteh', 'utjeh'),
    ('greh', 'grijeh'),
    ('mlek', 'mlijek'),
    ('deli', 'dijeli'),
    ('besv', 'besvj'),
    ('bled', 'blijed'),
    ('bled', 'blijed'),
    ('ubed', 'ubijed'),
    ('preć', 'prijeć'),
    ('pret', 'prijet'),
    ('smeh', 'smijeh'),
    ('sneg', 'snijeg'),
    ('svet', 'svijet'),
    ('sten', 'stijen'),
    ('odel', 'odijel'),
    ('retk', 'rijetk'),
    ('odne', 'odnije'),
    ('reši', 'riješi'),
    ('veća', 'veća'),
    ('veće', 'veće'),
    ('veći', 'veći'),
    ('zver', 'zvijer'),
    ('donel', 'donijel'),
    ('vred', 'vrijed'),
    ('deča', 'dječa'),
    ('delo', 'djelo'),
    ('dela', 'djela'),
    ('delo', 'djelo'),
    ('delu', 'djelu'),
    ('oseć', 'osjeć'),
    ('odeć', 'odjeć'),
    ('nemc', 'njemc'),
    ('vešt', 'vješt'),
    ('peva', 'pjeva'),
    ('venc', 'vijenc'),
    ('cent', 'cent'),
    ('ubeđ', 'ubjeđ'),
    ('nežn', 'nježn'),
    ('mesn', 'mjesn'),
    ('oset', 'osjet'),
    ('hleb', 'hljeb'),
    ('gnev', 'gnjev'),
    ('tera', 'tjera'),
    ('vide', 'vidje'),
    ('vest', 'vijest'),
    ('besn', 'bijesn'),
    ('dvem', 'dvjem'),
    ('uver', 'uvjer'),
    ('mese', 'mjese'),
    ('seti', 'sjeti'),
    ('ocen', 'ocjen'),
    ('smer', 'smjer'),
    ('pesm', 'pjesm'),
    ('ovde', 'ovdje'),
    ('mest', 'mjest'),
    ('lenj', 'lijen'),
    ('peša', 'pješa'),
    ('onde', 'ondje'),
    ('sled', 'sljed'),
    ('beža', 'bježa'),
    ('breg', 'brijeg'),
    ('lete', 'letje'),
    ('leto', 'ljeto'),
    ('letu', 'ljetu'),
    ('leti', 'ljeti'),
    ('uspe', 'uspje'),
    ('done', 'donije'),
    ('letnj', 'ljetnj'),
    ('odel', 'odjel'),
    ('smel', 'smjel'),
    ('venč', 'vjenč'),
    ('ceni', 'cijeni'),
    ('cena', 'cijena'),
    ('cenu', 'cijenu'),
    ('leko', 'ljeko'),
    ('leku', 'lijeku'),
    ('leka', 'lijeka'),
    ('leč', 'liječ'),
    ('rek', 'rijek'),
    ('lev', 'lijev'),
    ('vol', 'volj'),
    ('reč', 'riječ'),
    ('cev', 'cijev'),
    ('cep', 'cijep'),
    ('pes', 'pijes'),
    ('lep', 'lijep'),
    ('obe', 'obje'),
    ('une', 'unije'),
    ('bed', 'bijed'),
    ('tel', 'tijel'),
    ('cel', 'cijel'),
    ('ded', 'djed'),
    ('reš', 'rješ'),
    ('ver', 'vjer'),
    ('mle', 'mlje'),
    ('ređ', 'rjeđ'),
    ('več', 'vječ'),
    ('leš', 'lješ'),
    ('meš', 'mješ'),
    ('mer', 'mjer'),
    ('les', 'ljes'),
    ('pev', 'pjev'),
    ('gde', 'gdje'),
    ('sen', 'sjen'),
    ('seć', 'sjeć'),
    ('hte', 'htje'),


    ('bel', 'bijel'),

 
]


KONTEKST_MAPE = [
    {
        'ekavski': ['sedela', 'sedeli', 'sedeo', 'sedio', 'sede', 'sedu', 'sedi', 'sedog', 'sedoh'],
        'kljucevi1': ['kos', 'brad', 'zalisc', 'star', 'godin', 'glav', 'vlas', 'obrv', 'mrsi'],
        'kljucevi2': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć', 'ispred'],
        'mape_grupa1': {
            'sedela': 'sijedila', 'sedeli': 'sijedili', 'sedeo': 'sijedio', 'sedio': 'sijedio',
            'sede': 'sijede', 'sedu': 'sijedu', 'sedi': 'sijedi', 'sedog': 'sijedog', 'sedoh': 'sijedoh'
        },
        'mape_grupa2': {
            'sedela': 'sjedjela', 'sedeli': 'sjedjeli', 'sedeo': 'sjedio', 'sedio': 'sjedio',
            'sede': 'sjede', 'sedu': 'sjedu', 'sedi': 'sjedi', 'sedog': 'sjedog', 'sedoh': 'sjedoh'
        }
    },
   
    {
        'ekavski': ['svet'],
        'kljucevi1': ['zemlj', 'planet', 'ljud', 'narod', 'putov', 'obid', 'držav'],
        'kljucevi2': ['bog', 'crkv', 'otac', 'duh', 'krst', 'ikona', 'svešten', 'vjera'],
        'mape_grupa1': {'svet': 'svijet'},
        'mape_grupa2': {'svet': 'svet'}
    },
    {
        'ekavski': ['leci'],
        'kljucevi1': ['papir', 'prospekt', 'reklam', 'dijel', 'štamp', 'sto', 'kutij'],
        'kljucevi2': ['boles', 'doktor', 'bolnic', 'zdrav', 'lijek', 'pacijent', 'ran'],
        'mape_grupa1': {'leci': 'letci'},
        'mape_grupa2': {'leci': 'liječi'}
    },
    {
        'ekavski': ['bela', 'bele'],
        'kljucevi1': ['boj', 'papir', 'košulj', 'snijeg', 'haljin', 'zid', 'platn'],
        'kljucevi2': ['pladn', 'dan', 'zabel', 'platn', 'košulj', 'zid', 'boj'],
        'mape_grupa1': {'bela': 'bijela', 'bele': 'bijele'},
        'mape_grupa2': {'bela': 'bjelila', 'bele': 'bjelile'}
    }
]


IMENA_IZUZECI_KORIJENI = ['vera','veri','veru','sedić', 'seden', 'sedlar', 'razbolović', 'slepčević']

def _wb(rijec): return re.compile(r'(?<![^\W\d_])' + re.escape(rijec) + r'(?![^\W\d_])', re.UNICODE | re.IGNORECASE)
def _stem(korijen): return re.compile(r'(?<![^\W\d_])(' + re.escape(korijen) + r')(\w*)', re.UNICODE | re.IGNORECASE)

_EXACT = [(_wb(e), e, i) for e, i in EXACT]
_STEMS = [(_stem(e), e, i) for e, i in STEMS]

def da_li_je_pocetak_recenice(tekst, pozicija):
    p = tekst[:pozicija].strip()
    return True if not p or p[-1] in ['.', '!', '?', '\n', '"', '„', '(', '['] else False

def _sacuvaj_velika_slova(izvorna, zamjena, sufiks=""):
    if izvorna.isupper(): return zamjena.upper() + sufiks.upper()
    if izvorna.istitle(): return zamjena.capitalize() + sufiks
    return zamjena + sufiks

def _primijeni_exact(tekst):
    for pat, e, i in _EXACT:
        def _r(m):
            s = m.group(0)
            if da_li_je_pocetak_recenice(tekst, m.start()):
                if any(s.lower().startswith(korijen) for korijen in IMENA_IZUZECI_KORIJENI):
                    return s
            return s if (s[0].isupper() and not da_li_je_pocetak_recenice(tekst, m.start())) else _sacuvaj_velika_slova(s, i)
        tekst = pat.sub(_r, tekst)
    return tekst

def _primijeni_stems(tekst):
    TACNA_IMENA = ['vera', 'veri', 'veru']
    KORIJENI_PREZIMENA = ['sedić', 'seden', 'sedlar', 'razbolović', 'slepčević']
    TEHNICKI_IZUZECI = ['telefon', 'televiz', 'telegram', 'telefons', 'televizij', 'teleskop']
    
    for pat, e, i in _STEMS:
        def _r(m):
            s, suf = m.group(1), m.group(2)
            puna_rec = (s + suf).lower()
            
            if da_li_je_pocetak_recenice(tekst, m.start()):
                if puna_rec in TACNA_IMENA or any(puna_rec.startswith(k) for k in KORIJENI_PREZIMENA):
                    return m.group(0)
                    
            if any(puna_rec.startswith(izuzetak) for izuzetak in TEHNICKI_IZUZECI):
                return m.group(0)
                
            if s[0].isupper() and not da_li_je_pocetak_recenice(tekst, m.start()):
                return m.group(0)
                
            return _sacuvaj_velika_slova(s, i, suf)
            
        tekst = pat.sub(_r, tekst)
    return tekst

def _primijeni_kontekst_prozor(tekst):
    recenice = re.split(r'([.!?\n]+)', tekst)
    novi_delovi = []
    
    for recenica in recenice:
        if not recenica.strip() or re.match(r'^[...!?\n]+$', recenica):
            novi_delovi.append(recenica)
            continue
            
        tokeni = re.split(r'([^\W\d_]+)', recenica, flags=re.UNICODE)
        idx_p = [idx for idx, t in enumerate(tokeni) if re.match(r'^[^\W\d_]+$', t)]
        okolina = recenica.lower()
        
        for i, t_idx in enumerate(idx_p):
            trenutna_rijec = tokeni[t_idx]
            rijec_lower = trenutna_rijec.lower()
            
            if i == 0 and any(rijec_lower.startswith(korijen) for korijen in IMENA_IZUZECI_KORIJENI):
                continue
                
            for mapa in KONTEKST_MAPE:
                if rijec_lower in mapa['ekavski']:
                    skor1 = sum(1 for k in mapa['kljucevi1'] if k in okolina)
                    skor2 = sum(1 for k in mapa['kljucevi2'] if k in okolina)
                    
                    if skor1 > skor2:
                        baza_zamjene = mapa['mape_grupa1']
                    else:
                        baza_zamjene = mapa['mape_grupa2']
                    
                    if rijec_lower in baza_zamjene:
                        tokeni[t_idx] = _sacuvaj_velika_slova(trenutna_rijec, baza_zamjene[rijec_lower])
                        
        novi_delovi.append("".join(tokeni))
        
    return "".join(novi_delovi)

def zamijeni_rijeci(tekst):
    return _primijeni_kontekst_prozor(_primijeni_stems(_primijeni_exact(tekst)))

def obradi_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))
    print(f"Završeno: '{ulaz}' -> '{izlaz}'")

@anvil.server.callable
def ijekavizuj_tekst(ulazni_tekst):
    if not ulazni_tekst:
        return ""
    try:
        return zamijeni_rijeci(ulazni_tekst)
    except Exception as greska:
        print(f"Greška pri obradi teksta: {greska}")
        return ulazni_tekst

if __name__ == "__main__":
    if len(sys.argv) == 3:
        obradi_datoteku(sys.argv[1], sys.argv[2])
