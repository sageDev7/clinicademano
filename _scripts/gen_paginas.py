"""Páginas internas de Clínica de Mano. Toma head, header/menú y footer del index (se puede volver a correr).
Uso: python _scripts/gen_paginas.py"""
import re
from pathlib import Path
D = Path(__file__).resolve().parent.parent
idx = (D / "index.html").read_text(encoding="utf8")

head = idx[:idx.index("</head>")]
head = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", head, flags=re.S)
hdr = idx[idx.index("<!-- ============ HEADER ============ -->"):idx.index("<main>")]
ftr = idx[idx.index("<!-- ============ FOOTER ============ -->"):idx.index('<script src="./main.js">')]
def local(h):  # anclas del index -> ./index.html#ancla
    h = h.replace('href="#inicio"', 'href="./index.html"')
    return re.sub(r'href="#([a-z][\w-]*)"', r'href="./index.html#\1"', h)
hdr, ftr = local(hdr), local(ftr)

WA = 'class="btn btn-dark js-wa" href="#" data-msg="Hola, quisiera solicitar un turno."'

def ph(titulo, sub, foto, nombre):
    return f'''<section class="ph" style="--ph:url('./img/{foto}')">
  <div class="wrap ph-in">
    <nav class="crumb rise" aria-label="Ruta"><a href="./index.html">Inicio</a><i class="ti ti-chevron-right" aria-hidden="true"></i><span>{nombre}</span></nav>
    <h1 class="ph-h1 rise d1">{titulo}</h1>
    <p class="ph-sub rise d2">{sub}</p>
  </div>
</section>'''

def cta(t, p, msg="Hola, quisiera solicitar un turno."):
    return f'''<section class="sec cta-sec">
  <div class="wrap cta-in reveal">
    <span class="tile" aria-hidden="true">M</span>
    <h2 class="h2">{t}</h2>
    <p class="lead">{p}</p>
    <div class="cta-btns"><a class="btn btn-dark js-wa" href="#" data-msg="{msg}">Pedir turno por WhatsApp</a><a class="btn btn-line" href="./index.html#contacto">Ver horarios y dirección</a></div>
  </div>
</section>'''

def rows(items):
    return "\n".join(f'          <li><h3>{t}</h3><p>{d}</p></li>' for t, d in items)

# ---------------- LA CLÍNICA ----------------
clinica = ph("La clínica", "Cuarenta años dedicados a la mano y el miembro superior, en Mendoza.", "cirugia_mano_2.jpg", "La clínica") + f'''

<section class="sec" id="historia">
  <div class="wrap hist-grid">
    <div class="reveal">
      <p class="eyebrow">Nuestra historia</p>
      <h2 class="h2">Pioneros en cirugía de la mano</h2>
      <p class="lead">Clínica de Mano empezó a atender en 1986 y fue uno de los primeros centros de la Argentina dedicados a las enfermedades de la mano y el miembro superior.</p>
      <p>Hoy diagnosticamos y tratamos afecciones de la mano, la muñeca, el codo y el hombro, y recibimos pacientes de toda la región de Cuyo.</p>
    </div>
    <ol class="timeline reveal">
      <li><b>1986</b><h3>Primeros pacientes</h3><p>La clínica abre en Mendoza, dedicada desde el inicio a la mano y el miembro superior.</p></li>
      <li><b>2013</b><h3>Nuevo edificio</h3><p>El 14 de enero nos mudamos a Garibaldi 394, en la Ciudad de Mendoza.</p></li>
      <li><b>Hoy</b><h3>Referencia en Cuyo</h3><p>Cirugía, tratamiento del dolor y rehabilitación en un mismo lugar.</p></li>
    </ol>
  </div>
</section>

<section class="sec sec-dark" id="como-trabajamos">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2 class="h2">Cirugía ambulatoria</h2>
      <p class="lead">Elegimos la técnica según cada caso, después de la consulta y los estudios.</p>
    </div>
    <div class="tec-grid">
      <article class="proc reveal"><i class="ti ti-door-exit" aria-hidden="true"></i><h3>Sin internación</h3><p>Operamos de forma ambulatoria: el paciente vuelve a su casa el mismo día.</p></article>
      <article class="proc reveal"><i class="ti ti-arrows-minimize" aria-hidden="true"></i><h3>Mini-invasiva y artroscópica</h3><p>Procedimientos con incisiones pequeñas o por artroscopía, cuando el caso lo permite.</p></article>
      <article class="proc reveal"><i class="ti ti-microscope" aria-hidden="true"></i><h3>Microcirugía</h3><p>Reparación de vasos y nervios de pequeño calibre con técnica microquirúrgica.</p></article>
    </div>
  </div>
</section>

<section class="sec sec-alt" id="rehabilitacion">
  <div class="wrap split">
    <figure class="split-foto reveal"><img src="./img/clinica_mano_1.jpg" alt="Profesional de la clínica atendiendo a un paciente" width="620" height="280" loading="lazy"></figure>
    <div class="reveal">
      <p class="eyebrow">Dolor y rehabilitación</p>
      <h2 class="h2">El seguimiento, en la misma clínica</h2>
      <p class="lead">La atención se completa con el departamento de tratamiento del dolor y rehabilitación especializada.</p>
      <p>Así, la recuperación después de una lesión o de una cirugía la acompaña el mismo equipo que hizo el diagnóstico.</p>
      <a class="link-arrow" href="./procedimientos.html#dolor">Ver dolor y rehabilitación <i class="ti ti-arrow-right" aria-hidden="true"></i></a>
    </div>
  </div>
</section>

''' + cta("Pedí tu turno", "Atendemos de lunes a viernes, de 9 a 13 y de 15 a 18 h, en Garibaldi 394.")

# ---------------- PROCEDIMIENTOS ----------------
GRUPOS = [
 ("fracturas", "ti-bone", "Fracturas y secuelas", "Lesiones de los huesos de la mano, la muñeca y el resto del miembro superior.", [
   ("Fracturas de muñeca", "Las más frecuentes del miembro superior, en general por caídas sobre la mano."),
   ("Fracturas de metacarpianos y falanges", "Los huesos de la palma y de los dedos."),
   ("Reconstrucción ósea por secuelas de accidentes", "Cuando una fractura consolidó en mala posición o dejó pérdida de hueso."),
   ("Lesiones deportivas", "Golpes, torceduras y lesiones por esfuerzo de la mano, la muñeca, el codo y el hombro.")]),
 ("tendones", "ti-route", "Tendones y nervios", "Lesiones que afectan el movimiento o la sensibilidad de la mano.", [
   ("Lesiones de tendones", "Cortes o roturas que impiden doblar o estirar un dedo o la muñeca."),
   ("Microcirugía vascular y nerviosa", "Reparación de arterias y nervios de pequeño calibre."),
   ("Síndrome del túnel carpiano", "Compresión del nervio mediano en la muñeca, que suele dar hormigueo y adormecimiento en los dedos."),
   ("Otros atrapamientos nerviosos", "Compresiones de nervios en el codo y el antebrazo.")]),
 ("artrosis", "ti-hand-finger", "Artrosis e inflamación", "Enfermedades reumáticas, degenerativas e inflamatorias de la mano.", [
   ("Artrosis del pulgar", "Desgaste de la articulación de la base del pulgar, que da dolor al hacer pinza o girar."),
   ("Deformidades por artritis y reemplazos articulares", "Corrección de deformidades y reemplazo de articulaciones dañadas."),
   ("Tenosinovitis", "Inflamación de la vaina de los tendones, como el dedo en gatillo.")]),
 ("reconstructiva", "ti-scissors", "Cirugía reconstructiva", "Cirugía plástica y reconstructiva del miembro superior.", [
   ("Malformaciones congénitas de la mano", "Diferencias en la formación de la mano presentes desde el nacimiento."),
   ("Quistes y lesiones tumorales", "Quistes, como el ganglión de la muñeca, y tumores del miembro superior."),
   ("Lesiones de la piel y defectos cutáneos", "Cirugía plástica para reparar y cubrir la piel.")]),
 ("dolor", "ti-activity-heartbeat", "Dolor y rehabilitación", "El seguimiento antes y después de la cirugía, en la misma clínica.", [
   ("Tratamiento del dolor agudo y crónico", "Dolor del miembro superior, con o sin cirugía previa."),
   ("Rehabilitación especializada", "Ejercicios y terapias para recuperar movilidad y fuerza."),
   ("Férulas", "Férulas a medida para inmovilizar o corregir la posición de la mano.")]),
]
chips = "".join(f'<a href="#{k}">{t}</a>' for k, _, t, _, _ in GRUPOS)
bloques = ""
for n, (k, ic, t, intro, items) in enumerate(GRUPOS):
    alt = " sec-alt" if n % 2 else ""
    bloques += f'''
<section class="sec grupo{alt}" id="{k}">
  <div class="wrap grupo-grid">
    <div class="grupo-head reveal">
      <span class="tile" aria-hidden="true"><i class="ti {ic}"></i></span>
      <h2 class="h2">{t}</h2>
      <p class="lead">{intro}</p>
      <a class="link-arrow js-wa" href="#" data-msg="Hola, quisiera consultar por {t.lower()}.">Consultar por WhatsApp <i class="ti ti-arrow-right" aria-hidden="true"></i></a>
    </div>
    <ul class="proc-rows reveal">
{rows(items)}
    </ul>
  </div>
</section>
'''
procedimientos = ph("Procedimientos", "Qué tratamos en la mano, la muñeca, el codo y el hombro.", "cirugia_mano_3.jpg", "Procedimientos") + f'''

<nav class="chips" aria-label="Grupos de procedimientos"><div class="wrap chips-in">{chips}</div></nav>
{bloques}
<p class="wrap nota">La indicación de cada tratamiento la define el médico después de la consulta y los estudios.</p>

''' + cta("¿Tenés una consulta?", "Contanos qué te pasa y te damos un turno con el médico que corresponda.", "Hola, quisiera consultar por un tratamiento.")

# ---------------- STAFF ----------------
STAFF = [("AM", "Dr. Adolfo Martedi"), ("CM", "Dr. Carlos Martedi"), ("AR", "Dr. Ángel Rivero"), ("ML", "Dr. Mauricio Luna"),
         ("DZ", "Dr. Danilo Zapata"), ("CB", "Dr. Carlos Bueno"), ("DY", "Dr. Danilo Yapur Musale")]
cards = "\n".join(f'      <li class="reveal"><span class="tile">{i}</span><h3>{n}</h3></li>' for i, n in STAFF)
staff = ph("Staff médico", "Traumatólogos dedicados a la mano y el miembro superior.", "cirugia_1.jpg", "Staff médico") + f'''

<section class="sec" id="equipo">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">El equipo</p>
      <h2 class="h2">Nuestros médicos</h2>
      <p class="lead">Médicos de ortopedia y traumatología, miembros titulares de la Asociación Argentina de Cirugía de la Mano y Reconstructiva del Miembro Superior.</p>
    </div>
    <!-- Matrículas (MN/MP) y fotos: no figuran en su web actual. Pedirlas al cliente y sumarlas a cada ficha. -->
    <ul class="staff-cards">
{cards}
    </ul>
  </div>
</section>

<section class="sec sec-dark" id="asociacion">
  <div class="wrap split split-rev">
    <div class="reveal">
      <p class="eyebrow">Formación</p>
      <h2 class="h2">Miembros de la sociedad de la especialidad</h2>
      <p class="lead">La Asociación Argentina de Cirugía de la Mano y Reconstructiva del Miembro Superior reúne a los cirujanos de mano del país. Nuestros médicos son miembros titulares.</p>
      <p>En la clínica trabajamos con cirugía ambulatoria, técnicas mini-invasivas, artroscopía y microcirugía.</p>
    </div>
    <figure class="split-foto reveal"><img src="./img/cirugia_mano_3.jpg" alt="Médicos del staff revisando una radiografía" width="620" height="280" loading="lazy"></figure>
  </div>
</section>

''' + cta("Turnos con el staff", "Escribinos y coordinamos tu consulta con el médico que corresponda.")

PAGES = {
 "clinica.html": ("La clínica | Clínica de Mano · Mendoza", "Clínica de Mano, Mendoza: desde 1986 dedicada a la mano y el miembro superior. Cirugía ambulatoria, microcirugía, tratamiento del dolor y rehabilitación.", clinica),
 "procedimientos.html": ("Procedimientos | Clínica de Mano · Mendoza", "Fracturas, tendones, túnel carpiano, artrosis del pulgar, cirugía reconstructiva, dolor y rehabilitación de la mano, la muñeca, el codo y el hombro en Mendoza.", procedimientos),
 "staff.html": ("Staff médico | Clínica de Mano · Mendoza", "El staff de Clínica de Mano: médicos traumatólogos dedicados a la mano y el miembro superior, miembros titulares de la Asociación Argentina de Cirugía de la Mano.", staff),
}
for f, (title, desc, body) in PAGES.items():
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, flags=re.S)
    h = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', h, flags=re.S)
    h = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', h)
    h = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', h)
    hh = hdr.replace(f'href="./{f}"', f'href="./{f}" aria-current="page"')
    html = f'''{h}</head>
<body class="pg">

{hh}<main>

{body}

</main>

{ftr}<script src="./main.js"></script>
</body>
</html>
'''
    (D / f).write_text(html, encoding="utf8")
    print("ok", f)
