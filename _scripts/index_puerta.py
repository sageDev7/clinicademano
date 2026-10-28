"""Pasa el index a «puerta»: resúmenes con link a las internas (el contenido completo vive en cada página)."""
from pathlib import Path
D = Path(__file__).resolve().parent.parent
p = D / "index.html"; s = p.read_text(encoding="utf8")

A, B = "<!-- ============ LA CLÍNICA ============ -->", "<!-- ============ CONTACTO / CÓMO LLEGAR ============ -->"
i, j = s.index(A), s.index(B)
nuevo = '''<!-- ============ LA CLÍNICA ============ -->
<section class="sec" id="clinica">
  <div class="wrap clinica-grid">
    <div class="clinica-fotos reveal">
      <figure class="f-a"><img src="./img/clinica_mano_1.jpg" alt="Atención en el consultorio de Clínica de Mano" width="620" height="280" loading="lazy"></figure>
      <figure class="f-b"><img src="./img/cirugia_mano_3.jpg" alt="Equipo quirúrgico revisando una radiografía" width="620" height="280" loading="lazy"></figure>
    </div>
    <div class="clinica-txt reveal">
      <p class="eyebrow">La clínica</p>
      <h2 class="h2">Un centro dedicado a la mano desde 1986</h2>
      <p class="lead">Somos uno de los primeros centros del país dedicados a la mano y el miembro superior, y hoy una referencia en la región de Cuyo.</p>
      <p>Operamos de forma ambulatoria, con técnicas mini-invasivas, artroscópicas y microquirúrgicas, y tenemos un departamento propio de dolor y rehabilitación.</p>
      <a class="link-arrow" href="./clinica.html">Conocer la clínica <i class="ti ti-arrow-right" aria-hidden="true"></i></a>
    </div>
  </div>
</section>

<!-- ============ PROCEDIMIENTOS ============ -->
<section class="sec sec-dark" id="procedimientos">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Procedimientos</p>
      <h2 class="h2">Qué tratamos</h2>
      <p class="lead">Desde una fractura de muñeca hasta la rehabilitación posterior, con el mismo equipo.</p>
    </div>
    <div class="proc-grid">
      <a class="proc reveal" href="./procedimientos.html#fracturas">
        <i class="ti ti-bone" aria-hidden="true"></i>
        <h3>Fracturas y secuelas</h3>
        <p>Muñeca, metacarpianos y falanges, secuelas de accidentes y lesiones deportivas.</p>
        <span class="proc-more">Ver más <i class="ti ti-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="proc reveal" href="./procedimientos.html#tendones">
        <i class="ti ti-route" aria-hidden="true"></i>
        <h3>Tendones y nervios</h3>
        <p>Lesiones de tendones, microcirugía y túnel carpiano.</p>
        <span class="proc-more">Ver más <i class="ti ti-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="proc reveal" href="./procedimientos.html#artrosis">
        <i class="ti ti-hand-finger" aria-hidden="true"></i>
        <h3>Artrosis e inflamación</h3>
        <p>Artrosis del pulgar, artritis, reemplazos articulares y tenosinovitis.</p>
        <span class="proc-more">Ver más <i class="ti ti-arrow-right" aria-hidden="true"></i></span>
      </a>
      <a class="proc reveal" href="./procedimientos.html#reconstructiva">
        <i class="ti ti-scissors" aria-hidden="true"></i>
        <h3>Cirugía reconstructiva</h3>
        <p>Malformaciones congénitas, quistes, tumores y defectos de la piel.</p>
        <span class="proc-more">Ver más <i class="ti ti-arrow-right" aria-hidden="true"></i></span>
      </a>
    </div>
    <div class="proc-band reveal">
      <div><h3>Dolor y rehabilitación</h3><p>Tratamiento del dolor agudo y crónico, rehabilitación y férulas a medida, en la misma clínica.</p></div>
      <a class="btn btn-gold" href="./procedimientos.html#dolor">Ver dolor y rehabilitación</a>
    </div>
  </div>
</section>

<!-- ============ STAFF ============ -->
<section class="sec sec-alt" id="staff">
  <div class="wrap staff-prev">
    <figure class="split-foto reveal"><img src="./img/cirugia_mano_2.jpg" alt="Médicos del staff de Clínica de Mano durante una cirugía" width="620" height="280" loading="lazy"></figure>
    <div class="staff-txt reveal">
      <p class="eyebrow">Staff médico</p>
      <h2 class="h2">Siete médicos, un mismo criterio</h2>
      <p class="lead">Traumatólogos dedicados a la mano y el miembro superior, miembros titulares de la Asociación Argentina de Cirugía de la Mano.</p>
      <a class="link-arrow" href="./staff.html">Ver el staff <i class="ti ti-arrow-right" aria-hidden="true"></i></a>
    </div>
  </div>
</section>

'''
s = s[:i] + nuevo + s[j:]

# navegación: secciones con página propia apuntan a la página
for a, b in [('href="#clinica"', 'href="./clinica.html"'), ('href="#staff"', 'href="./staff.html"')]:
    s = s.replace(a, b)
# procedimientos: en header, menú y footer va a la página (el botón del hero sigue bajando a la sección)
s = s.replace('<a href="#procedimientos">Procedimientos</a>', '<a href="./procedimientos.html">Procedimientos</a>')
for k, a in [("fracturas", "Fracturas y secuelas"), ("tendones", "Tendones y nervios"), ("artrosis", "Artrosis e inflamación"), ("reconstructiva", "Cirugía reconstructiva")]:
    s = s.replace(f'<li><a href="#procedimientos">{a}</a></li>', f'<li><a href="./procedimientos.html#{k}">{a}</a></li>')
s = s.replace('<li><a href="./procedimientos.html#reconstructiva">Cirugía reconstructiva</a></li>',
              '<li><a href="./procedimientos.html#reconstructiva">Cirugía reconstructiva</a></li><li><a href="./procedimientos.html#dolor">Dolor y rehabilitación</a></li>')
s = s.replace('<li><a href="./clinica.html">La clínica</a></li>', '<li><a href="./clinica.html">La clínica</a></li><li><a href="./procedimientos.html">Procedimientos</a></li>')
p.write_text(s, encoding="utf8")
print("ok", s.count("procedimientos.html"))
