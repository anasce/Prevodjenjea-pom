import sys, os, re 
import anvil.server


import sys, os, re 
import anvil.server


EXACT = [
  
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
    ('odeljak', 'odjeljak'),
    ('doprine', 'doprinije'),
    ('neizbež', 'neizbjež'),
    ('neizmer', 'neizmjer'),
    ('letelic', 'letjelic'),
    ('nadžive', 'nadživje'),
    ('prosleđ', 'prosljeđ'),
    ('osvetli', 'osvijetli'),
    ('osvetlj', 'osvjetlj'),
    ('pobeg', 'pobjeg'),
    ('pobegl', 'pobjegl'),
    ('prevar', 'prevar'),
    ('povest', 'povijest'),
    ('prosle', 'proslije'),
    ('gnezdo', 'gnijezdo'),
    ('unapre', 'unaprije'),
    ('razbole', 'razbolje'),
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
    ('obe', 'obje'),
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
    ('sreds', 'sreds'),
    ('cvet', 'cvijet'),
    ('slep', 'slijep'),
    ('deca', 'djeca'),
    ('deci', 'djeci'),
    ('decu', 'djecu'),
    ('deco', 'djeco'),
    ('sede', 'sjedje'),
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
    ('iznet', 'iznijet'),
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
    ('leč', 'liječ'),
    ('rek', 'rijek'),
    ('leko', 'ljeko'),
    ('leku', 'lijeku'),
    ('leka', 'lijeka'),
    ('lev', 'lijev'),
    ('vol', 'volj'),
    ('reč', 'riječ'),
    ('cev', 'cijev'),
    ('cep', 'cijep'),
    ('pes', 'pijes'),
    ('lep', 'lijep'),
    ('une', 'unije'),
    ('bed', 'bijed'),
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
    ('ceni', 'cijeni'),
    ('cena', 'cijena'),
    ('cenu', 'cijenu'),
    ('cenit', 'cijeniti'),
    ('bel', 'bijel'),

 
]


# KONTEKST sada radi sa tačnim mapiranjem celih reči bez rizičnog sečenja sufiksa
KONTEKST_MAPE = [
    {
        'ekavski': [ 'sede', 'sedi', 'seda'],
        'ako_je_grupa1': 'sijed',  # npr. sijeda
        'kljucevi1': ['kos', 'brad', 'zalisc', 'star', 'godin', 'glav', 'vlas', 'obrv'],
        'ako_je_grupa2': 'sjed',   # npr. sjedi
        'kljucevi2': ['stolic', 'fotelj', 'klup', 'mest', 'sto', 'sof', 'park', 'sati', 'mirn', 'prozor', 'pod', 'kuć']
    }
]

def _wb(word): return re.compile(r'(?<![^\W\d_])' + re.escape(word) + r'(?![^\W\d_])', re.UNICODE | re.IGNORECASE)
def _stem(stem): return re.compile(r'(?<![^\W\d_])(' + re.escape(stem) + r')(\w*)', re.UNICODE | re.IGNORECASE)

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
            return s if (s.isupper() and not da_li_je_pocetak_recenice(tekst, m.start())) else _sacuvaj_velika_slova(s, i)
        tekst = pat.sub(_r, tekst)
    return tekst

def _primijeni_stems(tekst):
    for pat, e, i in _STEMS:
        def _r(m):
            s, suf = m.group(1), m.group(2)
            return m.group(0) if (s.isupper() and not da_li_je_pocetak_recenice(tekst, m.start())) else _sacuvaj_velika_slova(s, i, suf)
        tekst = pat.sub(_r, tekst)
    return tekst

def _primijeni_kontekst_prozor(tekst):
    tokeni = re.split(r'([^\W\d_]+)', tekst, flags=re.UNICODE)
    idx_p = [idx for idx, t in enumerate(tokeni) if re.match(r'^[^\W\d_]+$', t)]
    
    for i, t_idx in enumerate(idx_p):
        rijec = tokeni[t_idx]
        rijec_lower = rijec.lower()
        
        for mapa in KONTEKST_MAPE:
            if rijec_lower in mapa['ekavski']:
                # Pronalaženje okoline (3 reči pre i posle)
                prozor = [tokeni[idx_p[j]].lower() for j in range(max(0, i-3), i)] + [tokeni[idx_p[j]].lower() for j in range(i+1, min(len(idx_p), i+4))]
                okolina = " ".join(prozor)
                
                skor1 = sum(len(re.findall(re.escape(k), okolina)) for k in mapa['kljucevi1'])
                skor2 = sum(len(re.findall(re.escape(k), okolina)) for k in mapa['kljucevi2'])
                
                # Izvlačenje originalnog nastavka iz ekavske reči (npr. 'ede' iz 'sede' -> 'ije' + 'de' = 'sijede')
                nastavak = rijec_lower[3:] # seče sve posle prva 3 slova ('sed')
                
                if skor1 > skor2:
                    koren_zamene = mapa['ako_je_grupa1']
                else:
                    koren_zamene = mapa['ako_je_grupa2']
                
                prava_zamjena = koren_zamene + nastavak
                tokeni[t_idx] = _sacuvaj_velika_slova(rijec, prava_zamjena)
                
    return "".join(tokeni)

def zamijeni_rijeci(tekst):
    # Prvo proveravamo kontekstualne reči, pa tek onda opšte filtere
    tekst = _primijeni_kontekst_prozor(tekst)
    tekst = _primijeni_stems(tekst)
    tekst = _primijeni_exact(tekst)
    return tekst

def obradi_datoteku(ulaz, izlaz):
    if not os.path.isfile(ulaz): print(f"Greška: '{ulaz}'..."); sys.exit(1)
    with open(ulaz, encoding="utf-8") as f: t = f.read()
    with open(izlaz, "w", encoding="utf-8") as f: f.write(zamijeni_rijeci(t))

@anvil.server.callable
def ijekavizuj_tekst(ulazni_tekst):
    return zamijeni_rijeci(ulazni_tekst) if ulazni_tekst else ""
