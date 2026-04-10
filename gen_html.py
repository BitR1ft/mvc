#!/usr/bin/env python3
import json
import numpy as np

PATH = '/home/runner/work/mvc/mvc/index.html'

# ── 3-D graph helpers ──────────────────────────────────────────────────────
_graph_id_counter = [0]

def _next_id():
    _graph_id_counter[0] += 1
    return f'gplt{_graph_id_counter[0]}'

GOLD_CS  = [[0, '#e8d9b0'], [0.5, '#c8a84c'], [1, '#8b6914']]
BLUE_CS  = [[0, '#b0cce8'], [0.5, '#4c8ac8'], [1, '#14568b']]
GREEN_CS = [[0, '#b0e8c0'], [0.5, '#4cc870'], [1, '#1a8b3a']]

def _surf(x2d, y2d, z2d, colorscale=None, opacity=0.85):
    return {'type': 'surface',
            'x': x2d, 'y': y2d, 'z': z2d,
            'colorscale': colorscale or GOLD_CS,
            'showscale': False,
            'opacity': opacity,
            'contours': {'x': {'highlight': False},
                         'y': {'highlight': False},
                         'z': {'highlight': False}}}

def _layout(h):
    return {'height': h,
            'margin': {'l': 0, 'r': 0, 't': 28, 'b': 0},
            'scene': {'aspectmode': 'data',
                      'xaxis': {'showgrid': True, 'zeroline': True},
                      'yaxis': {'showgrid': True, 'zeroline': True},
                      'zaxis': {'showgrid': True, 'zeroline': True}},
            'showlegend': False,
            'paper_bgcolor': 'rgba(0,0,0,0)'}

def plot3d(title, traces, height=340):
    pid = _next_id()
    cfg = json.dumps({'traces': traces, 'layout': _layout(height)},
                     separators=(',', ':'))
    return (f'<div class="graph-wrap">'
            f'<div class="graph-title">{title}</div>'
            f'<div id="{pid}" style="height:{height}px"></div>'
            f'<script type="application/json" data-for="{pid}">{cfg}</script>'
            f'</div>')

def sphere_traces(cx, cy, cz, r, colorscale=None, n=30):
    u = np.linspace(0, 2*np.pi, n)
    v = np.linspace(0, np.pi, n)
    U, V = np.meshgrid(u, v)
    x = (cx + r*np.cos(U)*np.sin(V)).tolist()
    y = (cy + r*np.sin(U)*np.sin(V)).tolist()
    z = (cz + r*np.cos(V)).tolist()
    return [_surf(x, y, z, colorscale)]

def ellipsoid_traces(cx, cy, cz, a, b, c, colorscale=None, n=30):
    u = np.linspace(0, 2*np.pi, n)
    v = np.linspace(0, np.pi, n)
    U, V = np.meshgrid(u, v)
    x = (cx + a*np.cos(U)*np.sin(V)).tolist()
    y = (cy + b*np.sin(U)*np.sin(V)).tolist()
    z = (cz + c*np.cos(V)).tolist()
    return [_surf(x, y, z, colorscale)]

def paraboloid_traces(cx, cy, a_sq, b_sq, zdir=1, zoff=0, xlim=None, ylim=None, n=38):
    """Generate surface traces for an elliptic paraboloid z = zoff + zdir*(x²/a_sq + y²/b_sq)."""
    ra, rb = np.sqrt(a_sq), np.sqrt(b_sq)
    xs = np.linspace(cx - 2*ra, cx + 2*ra, n) if xlim is None else np.linspace(*xlim, n)
    ys = np.linspace(cy - 2*rb, cy + 2*rb, n) if ylim is None else np.linspace(*ylim, n)
    X, Y = np.meshgrid(xs, ys)
    Z = zoff + zdir*((X - cx)**2/a_sq + (Y - cy)**2/b_sq)
    return [_surf(xs.tolist(), ys.tolist(), Z.tolist())]

def hyperboloid1_traces(a, b, c, t_range=2.5, n=38):
    u = np.linspace(0, 2*np.pi, n)
    t = np.linspace(-t_range, t_range, n)
    U, T = np.meshgrid(u, t)
    x = (a*np.cosh(T)*np.cos(U)).tolist()
    y = (b*np.cosh(T)*np.sin(U)).tolist()
    z = (c*np.sinh(T)).tolist()
    return [_surf(x, y, z)]

def hyperboloid2_traces(a, b, c, t_range=2.0, n=30):
    u = np.linspace(0, 2*np.pi, n)
    t = np.linspace(0, t_range, n)
    U, T = np.meshgrid(u, t)
    x = (a*np.sinh(T)*np.cos(U)).tolist()
    y = (b*np.sinh(T)*np.sin(U)).tolist()
    zu = (c*np.cosh(T)).tolist()
    zl = (-c*np.cosh(T)).tolist()
    return [_surf(x, y, zu), _surf(x, y, zl, BLUE_CS)]

def cone_traces(a, b, c, lim=2.0, n=38):
    xs = np.linspace(-a*lim, a*lim, n)
    ys = np.linspace(-b*lim, b*lim, n)
    X, Y = np.meshgrid(xs, ys)
    inner = np.sqrt((X/a)**2 + (Y/b)**2)
    return [_surf(xs.tolist(), ys.tolist(), (c*inner).tolist()),
            _surf(xs.tolist(), ys.tolist(), (-c*inner).tolist(), BLUE_CS)]

def zfunc_traces(f, xlim, ylim, n=38):
    xs = np.linspace(*xlim, n)
    ys = np.linspace(*ylim, n)
    X, Y = np.meshgrid(xs, ys)
    Z = f(X, Y)
    return [_surf(xs.tolist(), ys.tolist(), Z.tolist())]

def _upper_hemisphere_surface(n=38):
    """Return surface traces for the upper unit hemisphere z = √(1−x²−y²)."""
    xs = np.linspace(-1, 1, n)
    ys = np.linspace(-1, 1, n)
    X, Y = np.meshgrid(xs, ys)
    Z = np.where(X**2 + Y**2 <= 1,
                 np.sqrt(np.maximum(0, 1 - X**2 - Y**2)),
                 np.nan)
    return [_surf(xs.tolist(), ys.tolist(), Z.tolist())]

# ── helpers ────────────────────────────────────────────────────────────────
def card(num, question, tags, overview, formula, steps, answer, graph=''):
    tag_html = ''.join(f'<span class="tag">{t}</span>' for t in tags)
    formula_html = f'<div class="key-formula"><strong>Formula:</strong> {formula}</div>' if formula else ''
    steps_html = ''.join(
        f'<div class="step"><div class="step-n">{i+1}</div><div class="step-body">{s}</div></div>'
        for i, s in enumerate(steps)
    )
    return f'''
<div class="problem-card">
  <div class="problem-header">
    <div class="problem-num">{num}</div>
    <div class="problem-q">{question}</div>
    <div class="problem-tags">{tag_html}</div>
  </div>
  <div class="solution">
    <div class="sol-overview">{overview}</div>
    {formula_html}
    <div class="sol-steps">{steps_html}</div>
    <div class="sol-answer"><strong>Answer:</strong> {answer}</div>
    {graph}
  </div>
</div>'''

def concepts(title, items):
    items_html = ''.join(
        f'<div class="concept-item"><span class="concept-label">{lbl}</span><span class="concept-desc">{desc}</span></div>'
        for lbl, desc in items
    )
    return f'''
<div class="concepts-box">
  <button class="concepts-toggle">{title}</button>
  <div class="concepts-body">
    <div class="concept-grid">{items_html}</div>
  </div>
</div>'''

def section(sid, label, content):
    active = ' active' if sid == 's10_4' else ''
    return f'<div class="section{active}" id="{sid}"><h2 class="problems-header">{label}</h2>{content}</div>'

# ── Section 10.4 ────────────────────────────────────────────────────────────
s10_4_concepts = concepts('Key Concepts — Section 10.4 Conic Sections', [
    ('Parabola x²=4py', 'Opens up/down; vertex (0,0); focus (0,p); directrix y=−p'),
    ('Parabola y²=4px', 'Opens right/left; focus (p,0); directrix x=−p'),
    ('Ellipse', r'\(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\); \(c^2=a^2-b^2\); foci at (±c,0) when a>b'),
    ('Hyperbola', r'\(\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\); \(c^2=a^2+b^2\); asymptotes \(y=\pm\frac{b}{a}x\)'),
])

s10_4_cards = (
    card('Q3', r'Find vertex, focus, directrix of \(x^2=8y\)', ['parabola'],
         'Match standard form x²=4py and read off the parameter p.',
         r'\(x^2=4py\)',
         [r'Match: \(4p=8 \Rightarrow p=2\)',
          r'Vertex \((0,0)\), Focus \((0,2)\), Directrix \(y=-2\); opens upward.'],
         r'Vertex \((0,0)\), Focus \((0,2)\), Directrix \(y=-2\)')

  + card('Q4', r'Find vertex, focus, directrix of \(y^2=-6x\)', ['parabola'],
         'Match standard form y²=4px — negative p means opens left.',
         r'\(y^2=4px\)',
         [r'Match: \(4p=-6 \Rightarrow p=-\tfrac{3}{2}\)',
          r'Vertex \((0,0)\), Focus \(\bigl(-\tfrac{3}{2},0\bigr)\), Directrix \(x=\tfrac{3}{2}\); opens left.'],
         r'Vertex \((0,0)\), Focus \(\bigl(-\tfrac{3}{2},0\bigr)\), Directrix \(x=\tfrac{3}{2}\)')

  + card('Q5', r'Find vertex, focus, directrix of \((x-1)^2=-8(y+2)\)', ['parabola','shifted'],
         'Identify vertex (h,k) from shifted form, then find p.',
         r'\((x-h)^2=4p(y-k)\)',
         [r'Read off: \(h=1\), \(k=-2\), \(4p=-8 \Rightarrow p=-2\).',
          r'Vertex \((1,-2)\), Focus \((1,-4)\), Directrix \(y=0\); opens downward.'],
         r'Vertex \((1,-2)\), Focus \((1,-4)\), Directrix \(y=0\)')

  + card('Q7', r'Find equation of parabola: Vertex \((0,0)\), Focus \((0,-3)\)', ['parabola'],
         'Focus on the y-axis → use x²=4py form.',
         r'\(x^2=4py\)',
         [r'Focus is at \((0,-3)\) so \(p=-3\).',
          r'Equation: \(x^2=4(-3)y=-12y\).'],
         r'\(x^2=-12y\)')

  + card('Q8', r'Find equation of parabola: Vertex \((0,0)\), Focus \((2,0)\)', ['parabola'],
         'Focus on the x-axis → use y²=4px form.',
         r'\(y^2=4px\)',
         [r'Focus is at \((2,0)\) so \(p=2\).',
          r'Equation: \(y^2=4(2)x=8x\).'],
         r'\(y^2=8x\)')

  + card('Q9', r'Find equation: Vertex \((3,2)\), Focus \((3,4)\)', ['parabola','shifted'],
         'Same x-coordinate for vertex and focus → vertical parabola.',
         r'\((x-h)^2=4p(y-k)\)',
         [r'Vertex \((h,k)=(3,2)\). Focus is 2 units above vertex, so \(p=2\).',
          r'Equation: \((x-3)^2=8(y-2)\).'],
         r'\((x-3)^2=8(y-2)\)')

  + card('Q11', r'Find vertices and foci of \(\dfrac{x^2}{9}+\dfrac{y^2}{4}=1\)', ['ellipse'],
         'Identify a² and b², compute c²=a²−b².',
         r'\(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,\quad c^2=a^2-b^2\)',
         [r'\(a^2=9,\ b^2=4 \Rightarrow a=3,\ b=2\)',
          r'\(c^2=9-4=5 \Rightarrow c=\sqrt{5}\). Major axis along x-axis.',
          r'Vertices \((\pm3,0)\), Foci \((\pm\sqrt{5},0)\).'],
         r'Vertices \((\pm3,0)\), Foci \((\pm\sqrt{5},0)\)')

  + card('Q12', r'Find vertices and foci of \(\dfrac{x^2}{4}+\dfrac{y^2}{25}=1\)', ['ellipse'],
         'Larger denominator is a²; here major axis is along the y-axis.',
         r'\(c^2=a^2-b^2\)',
         [r'\(a^2=25,\ b^2=4 \Rightarrow a=5,\ b=2\)',
          r'\(c^2=25-4=21 \Rightarrow c=\sqrt{21}\). Major axis along y-axis.',
          r'Vertices \((0,\pm5)\), Foci \((0,\pm\sqrt{21})\).'],
         r'Vertices \((0,\pm5)\), Foci \((0,\pm\sqrt{21})\)')

  + card('Q13', r'Find vertices and foci of \(4x^2+9y^2=36\)', ['ellipse'],
         'Divide through by 36 to get standard form.',
         r'\(\frac{x^2}{9}+\frac{y^2}{4}=1\)',
         [r'Divide by 36: \(\dfrac{x^2}{9}+\dfrac{y^2}{4}=1\).',
          r'\(a^2=9, b^2=4, c^2=5, c=\sqrt{5}\). Vertices \((\pm3,0)\), Foci \((\pm\sqrt{5},0)\).'],
         r'Vertices \((\pm3,0)\), Foci \((\pm\sqrt{5},0)\)')

  + card('Q15', r'Find ellipse equation: Foci \((\pm2,0)\), Vertices \((\pm3,0)\)', ['ellipse'],
         'Use a=3, c=2 and the relation b²=a²−c² to find b².',
         r'\(\frac{x^2}{a^2}+\frac{y^2}{b^2}=1\)',
         [r'\(a=3,\ c=2 \Rightarrow b^2=9-4=5\)',
          r'Equation: \(\dfrac{x^2}{9}+\dfrac{y^2}{5}=1\).'],
         r'\(\dfrac{x^2}{9}+\dfrac{y^2}{5}=1\)')

  + card('Q16', r'Find ellipse equation: Foci \((0,\pm3)\), Vertices \((0,\pm5)\)', ['ellipse'],
         'Foci and vertices on y-axis → a² under y².',
         r'\(\frac{x^2}{b^2}+\frac{y^2}{a^2}=1\)',
         [r'\(a=5,\ c=3 \Rightarrow b^2=25-9=16\)',
          r'Equation: \(\dfrac{x^2}{16}+\dfrac{y^2}{25}=1\).'],
         r'\(\dfrac{x^2}{16}+\dfrac{y^2}{25}=1\)')

  + card('Q17', r'Find ellipse equation: Foci \((\pm1,0)\), minor axis length \(=6\)', ['ellipse'],
         'Minor axis length = 2b = 6, so b = 3. Then a² = b² + c².',
         r'\(a^2=b^2+c^2\)',
         [r'\(b=3,\ b^2=9,\ c=1\)',
          r'\(a^2=9+1=10\). Equation: \(\dfrac{x^2}{10}+\dfrac{y^2}{9}=1\).'],
         r'\(\dfrac{x^2}{10}+\dfrac{y^2}{9}=1\)')

  + card('Q19', r'Find vertices, foci, asymptotes of \(\dfrac{x^2}{4}-\dfrac{y^2}{9}=1\)', ['hyperbola'],
         'Standard hyperbola opening left/right. c²=a²+b², asymptotes y=±(b/a)x.',
         r'\(\frac{x^2}{a^2}-\frac{y^2}{b^2}=1,\quad c^2=a^2+b^2\)',
         [r'\(a^2=4,\ b^2=9 \Rightarrow a=2,\ b=3\)',
          r'\(c^2=4+9=13 \Rightarrow c=\sqrt{13}\)',
          r'Vertices \((\pm2,0)\), Foci \((\pm\sqrt{13},0)\), Asymptotes \(y=\pm\tfrac{3}{2}x\).'],
         r'Vertices \((\pm2,0)\), Foci \((\pm\sqrt{13},0)\), Asymptotes \(y=\pm\tfrac{3}{2}x\)')

  + card('Q21', r'Find vertices, foci, asymptotes of \(9y^2-x^2=9\)', ['hyperbola'],
         'Divide by 9 to get standard form with y² leading.',
         r'\(\frac{y^2}{a^2}-\frac{x^2}{b^2}=1\)',
         [r'Divide by 9: \(y^2-\dfrac{x^2}{9}=1\). So \(a=1,\ b=3\).',
          r'\(c^2=1+9=10 \Rightarrow c=\sqrt{10}\). Axis along y.',
          r'Vertices \((0,\pm1)\), Foci \((0,\pm\sqrt{10})\), Asymptotes \(y=\pm\tfrac{1}{3}x\).'],
         r'Vertices \((0,\pm1)\), Foci \((0,\pm\sqrt{10})\), Asymptotes \(y=\pm\tfrac{1}{3}x\)')

  + card('Q23', r'Find hyperbola equation: Vertices \((\pm2,0)\), Foci \((\pm3,0)\)', ['hyperbola'],
         'Horizontal hyperbola; use b²=c²−a².',
         r'\(\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\)',
         [r'\(a=2,\ c=3 \Rightarrow b^2=9-4=5\)',
          r'Equation: \(\dfrac{x^2}{4}-\dfrac{y^2}{5}=1\).'],
         r'\(\dfrac{x^2}{4}-\dfrac{y^2}{5}=1\)')

  + card('Q24', r'Find hyperbola equation: Vertices \((0,\pm3)\), Foci \((0,\pm5)\)', ['hyperbola'],
         'Vertical hyperbola (y² leads); b²=c²−a².',
         r'\(\frac{y^2}{a^2}-\frac{x^2}{b^2}=1\)',
         [r'\(a=3,\ c=5 \Rightarrow b^2=25-9=16\)',
          r'Equation: \(\dfrac{y^2}{9}-\dfrac{x^2}{16}=1\).'],
         r'\(\dfrac{y^2}{9}-\dfrac{x^2}{16}=1\)')

  + card('Q25', r'Find hyperbola equation: Vertices \((\pm3,0)\), Asymptotes \(y=\pm2x\)', ['hyperbola'],
         'Horizontal hyperbola; asymptote slope = b/a.',
         r'\(y=\pm\frac{b}{a}x\)',
         [r'\(a=3\), slope \(\tfrac{b}{a}=2 \Rightarrow b=6\)',
          r'Equation: \(\dfrac{x^2}{9}-\dfrac{y^2}{36}=1\).'],
         r'\(\dfrac{x^2}{9}-\dfrac{y^2}{36}=1\)')
)

s10_4 = section('s10_4', '10.4 — Conic Sections', s10_4_concepts + s10_4_cards)

# ── Section 11.1 ────────────────────────────────────────────────────────────
s11_1_concepts = concepts('Key Concepts — Section 11.1 3D Coordinates & Spheres', [
    ('Distance 3D', r'\(d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}\)'),
    ('Sphere', r'\((x-h)^2+(y-k)^2+(z-l)^2=r^2\), center \((h,k,l)\), radius \(r\)'),
    ('Complete Square', 'Group each variable, add (b/2)² to both sides to convert general form'),
    ('Midpoint 3D', r'\(\bigl(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2},\frac{z_1+z_2}{2}\bigr)\)'),
])

s11_1_cards = (
    card('Q9', r'Sphere with diameter endpoints \((1,-2,4)\) and \((3,4,-12)\)', ['sphere','midpoint'],
         'Center = midpoint of diameter; radius = half the diameter length.',
         r'\((x-h)^2+(y-k)^2+(z-l)^2=r^2\)',
         [r'Center = midpoint \(=\bigl(\frac{1+3}{2},\frac{-2+4}{2},\frac{4-12}{2}\bigr)=(2,1,-4)\).',
          r'Diameter: \(d=\sqrt{(3-1)^2+(4-(-2))^2+(-12-4)^2}=\sqrt{4+36+256}=\sqrt{296}=2\sqrt{74}\)',
          r'\(r=\sqrt{74}\). Equation: \((x-2)^2+(y-1)^2+(z+4)^2=74\).'],
         r'\((x-2)^2+(y-1)^2+(z+4)^2=74\)',
         plot3d('Sphere: center (2, 1, −4), radius √74',
                sphere_traces(2, 1, -4, 74**0.5)))

  + card('Q11a', r'Show \((2,1,6)\), \((4,7,9)\), \((8,5,-6)\) are vertices of a right triangle, find area', ['distance','right triangle'],
         'Compute all three side lengths and check the Pythagorean theorem.',
         r'\(d=\sqrt{\Delta x^2+\Delta y^2+\Delta z^2}\)',
         [r'\(|AB|=\sqrt{4+36+9}=7\)',
          r'\(|AC|=\sqrt{36+16+144}=\sqrt{196}=14\)',
          r'\(|BC|=\sqrt{16+4+225}=\sqrt{245}=7\sqrt{5}\)',
          r'Check: \(|AB|^2+|AC|^2=49+196=245=|BC|^2\) ✓ Right angle at \(A\).',
          r'Area \(=\frac{1}{2}|AB|\cdot|AC|=\frac{1}{2}(7)(14)=49\).'],
         r'Right triangle (right angle at \(A\)), Area \(=49\)')

  + card('Q13', r'Write sphere equations for four cases', ['sphere'],
         'Use standard sphere form; find r from given information in each case.',
         r'\((x-h)^2+(y-k)^2+(z-l)^2=r^2\)',
         [r'(a) Center \((7,1,1)\), \(r=4\): \((x-7)^2+(y-1)^2+(z-1)^2=16\)',
          r'(b) Center \((1,0,-1)\), diameter \(8 \Rightarrow r=4\): \((x-1)^2+y^2+(z+1)^2=16\)',
          r'(c) Center \((-1,3,2)\), through origin: \(r=\sqrt{1+9+4}=\sqrt{14}\); \((x+1)^2+(y-3)^2+(z-2)^2=14\)',
          r'(d) Diameter ends \((-1,2,1),(0,2,3)\): Center \(=(-\tfrac{1}{2},2,2)\), \(r^2=\tfrac{1}{4}+0+1=\tfrac{5}{4}\); \(\bigl(x+\tfrac{1}{2}\bigr)^2+(y-2)^2+(z-2)^2=\tfrac{5}{4}\)'],
         r'See steps for each equation')

  + card('Q14', r'Two spheres centered at origin tangent to sphere of radius 1 centered at \((3,-2,4)\)', ['sphere','tangency'],
         'Tangency conditions: center-to-center distance = sum or difference of radii.',
         '',
         [r'Distance from origin to center \((3,-2,4)\): \(d=\sqrt{9+4+16}=\sqrt{29}\)',
          r'<strong>External tangency</strong> (spheres outside each other): \(R+1=\sqrt{29} \Rightarrow R=\sqrt{29}-1\)',
          r'<strong>Internal tangency</strong> (one inside other): \(R-1=\sqrt{29} \Rightarrow R=\sqrt{29}+1\)',
          r'Equations: \(x^2+y^2+z^2=(\sqrt{29}-1)^2\) and \(x^2+y^2+z^2=(\sqrt{29}+1)^2\)'],
         r'\(x^2+y^2+z^2=(\sqrt{29}\pm1)^2\)')

  + card('Q15', r'Sphere center \((2,-1,-3)\) tangent to each coordinate plane', ['sphere','tangency'],
         'Tangent to a coordinate plane means r = perpendicular distance from center to that plane.',
         '',
         [r'(a) Tangent to \(xy\)-plane (\(z=0\)): \(r=|-3|=3\); \((x-2)^2+(y+1)^2+(z+3)^2=9\)',
          r'(b) Tangent to \(xz\)-plane (\(y=0\)): \(r=|-1|=1\); \((x-2)^2+(y+1)^2+(z+3)^2=1\)',
          r'(c) Tangent to \(yz\)-plane (\(x=0\)): \(r=|2|=2\); \((x-2)^2+(y+1)^2+(z+3)^2=4\)'],
         r'Three spheres with \(r=3, 1, 2\) respectively')

  + card('Q18', r'Sphere in first octant, tangent to all 3 coordinate planes, point on sphere nearest origin at distance \(3-\sqrt{3}\) from origin', ['sphere'],
         'Center (r,r,r) by symmetry; set distance from origin to surface equal to given value.',
         '',
         [r'Center must be \((r,r,r)\) for some \(r>0\) (equidistant from all coordinate planes).',
          r'Distance from origin to center: \(r\sqrt{3}\). Distance from origin to nearest surface point: \(r\sqrt{3}-r=r(\sqrt{3}-1)\)',
          r'Set equal: \(r(\sqrt{3}-1)=3-\sqrt{3}=\sqrt{3}(\sqrt{3}-1) \Rightarrow r=\sqrt{3}\)',
          r'Equation: \((x-\sqrt{3})^2+(y-\sqrt{3})^2+(z-\sqrt{3})^2=3\)'],
         r'\((x-\sqrt{3})^2+(y-\sqrt{3})^2+(z-\sqrt{3})^2=3\)')

  + card('Q27', r'Classify \(x^2+y^2+z^2-3x+4y-8z+25=0\)', ['sphere','complete square'],
         'Complete the square in each variable to identify center and radius.',
         '',
         [r'Group: \((x^2-3x)+(y^2+4y)+(z^2-8z)=-25\)',
          r'Complete: \(\bigl(x-\tfrac{3}{2}\bigr)^2-\tfrac{9}{4}+(y+2)^2-4+(z-4)^2-16=-25\)',
          r'\(\bigl(x-\tfrac{3}{2}\bigr)^2+(y+2)^2+(z-4)^2=-25+\tfrac{9}{4}+4+16=-\tfrac{3}{4}\)',
          r'Right side is negative — <strong>no real graph</strong>.'],
         r'No real graph (degenerate)')

  + card('Q28', r'Classify \(x^2+y^2+z^2-2x-6y-8z+1=0\)', ['sphere','complete square'],
         'Complete the square in each variable.',
         '',
         [r'Group: \((x^2-2x)+(y^2-6y)+(z^2-8z)=-1\)',
          r'Complete: \((x-1)^2-1+(y-3)^2-9+(z-4)^2-16=-1\)',
          r'\((x-1)^2+(y-3)^2+(z-4)^2=1+9+16-1=25\)',
          r'Sphere, center \((1,3,4)\), radius \(5\).'],
         r'Sphere; center \((1,3,4)\), radius \(5\)',
         plot3d('Sphere: center (1, 3, 4), radius 5',
                sphere_traces(1, 3, 4, 5)))

  + card('Q47', r'Bug on sphere \(x^2+y^2+z^2+2x-2y-4z-3=0\). How close and far from origin?', ['sphere','distance'],
         'Complete the square to find center and radius; use triangle inequality.',
         '',
         [r'Complete: \((x+1)^2+(y-1)^2+(z-2)^2=1+1+4+3=9\), center \((-1,1,2)\), \(r=3\)',
          r'Distance origin to center: \(D=\sqrt{1+1+4}=\sqrt{6}\)',
          r'Closest point on sphere: \(D-r=\sqrt{6}-3\approx-0.55\)... since \(\sqrt{6}<3\), origin is <em>inside</em> the sphere.',
          r'Closest distance: \(3-\sqrt{6}\), Farthest distance: \(3+\sqrt{6}\)'],
         r'Closest: \(3-\sqrt{6}\), Farthest: \(3+\sqrt{6}\)',
         plot3d('Sphere: center (−1, 1, 2), radius 3',
                sphere_traces(-1, 1, 2, 3)))
)

s11_1 = section('s11_1', '11.1 — 3D Coordinates &amp; Spheres', s11_1_concepts + s11_1_cards)

# ── Section 11.2 ────────────────────────────────────────────────────────────
s11_2_concepts = concepts('Key Concepts — Section 11.2 Vectors', [
    ('Components', r'\(\vec{P_1P_2}=\langle x_2-x_1,y_2-y_1,z_2-z_1\rangle\)'),
    ('Magnitude', r'\(\|\mathbf{v}\|=\sqrt{v_1^2+v_2^2+v_3^2}\)'),
    ('Unit vector', r'\(\hat{u}=\frac{\mathbf{v}}{\|\mathbf{v}\|}\)'),
    ('Angle form', r'\(\mathbf{v}=\|\mathbf{v}\|\langle\cos\theta,\sin\theta\rangle\)'),
])

s11_2_cards = (
    card('Q7', r'Find component form of vector \(\overrightarrow{P_1P_2}\) for given points', ['components'],
         'Subtract initial point from terminal point.',
         r'\(\overrightarrow{P_1P_2}=\langle x_2-x_1,\,y_2-y_1\rangle\)',
         [r'(a) \(P_1(3,5)\), \(P_2(2,8)\): \(\langle 2-3,\,8-5\rangle=\langle -1,3\rangle\)',
          r'(b) \(P_1(7,-2)\), \(P_2(0,0)\): \(\langle -7,2\rangle\)',
          r'(c) \(P_1(5,-2,1)\), \(P_2(2,4,2)\): \(\langle -3,6,1\rangle\)'],
         r'\(\langle-1,3\rangle\), \(\langle-7,2\rangle\), \(\langle-3,6,1\rangle\)')

  + card('Q9', r'Terminal/initial point problems', ['components'],
         'To find terminal point: add vector to initial. To find initial: subtract vector from terminal.',
         '',
         [r'(a) \(\mathbf{v}=3\mathbf{i}-2\mathbf{j}\), initial \((1,-2)\): terminal \(=(1+3,-2-2)=(4,-4)\)',
          r'(b) \(\mathbf{v}=\langle-3,1,2\rangle\), terminal \((5,0,-1)\): initial \(=(5-(-3),0-1,-1-2)=(8,-1,-3)\)'],
         r'(a) \((4,-4)\); (b) \((8,-1,-3)\)')

  + card('Q15', r'\(\mathbf{u}=\mathbf{i}-3\mathbf{j}+2\mathbf{k},\ \mathbf{v}=\mathbf{i}+\mathbf{j},\ \mathbf{w}=2\mathbf{i}+2\mathbf{j}-4\mathbf{k}\)', ['vector arithmetic'],
         'Apply standard vector operations component-wise.',
         '',
         [r'(a) \(\mathbf{u}+\mathbf{v}=\langle 2,-2,2\rangle\)',
          r'(b) \(\|\mathbf{u}+\mathbf{v}\|=\sqrt{4+4+4}=2\sqrt{3}\)',
          r'(c) \(-2\mathbf{u}+2\mathbf{v}=\langle-2+2,6+2,-4\rangle=\langle 0,8,-4\rangle\)',
          r'(d) \(3\mathbf{u}-5\mathbf{v}+\mathbf{w}=\langle 3-5+2,-9-5+2,6-4\rangle=\langle 0,-12,2\rangle\)',
          r'(e) \(\|\mathbf{w}\|=\sqrt{4+4+16}=2\sqrt{6}\); unit \(\mathbf{w}=\langle\tfrac{1}{\sqrt{6}},\tfrac{1}{\sqrt{6}},\tfrac{-2}{\sqrt{6}}\rangle\)',
          r'(f) \(\left\|\tfrac{1}{\|\mathbf{w}\|}\mathbf{w}\right\|=1\)'],
         r'See each sub-part above')

  + card('Q23', r'Vector operations with direction and length', ['unit vector'],
         'Scale the unit vector of the given vector.',
         '',
         [r'(a) Oppositely directed to \(\mathbf{v}=\langle 3,-4\rangle\), half the length: unit \(\mathbf{v}=\langle\tfrac{3}{5},-\tfrac{4}{5}\rangle\); result \(=-\tfrac{1}{2}\mathbf{v}_\text{unit}\cdot 5\cdot\tfrac{1}{2}\). Actually: \(-\tfrac{1}{2}\langle 3,-4\rangle=\langle-\tfrac{3}{2},2\rangle\)',
          r'(b) Length \(\sqrt{17}\), same direction as \(\mathbf{v}=\langle 7,0,-6\rangle\): \(\|\mathbf{v}\|=\sqrt{85}\); result \(=\sqrt{17}\cdot\frac{\mathbf{v}}{\sqrt{85}}=\langle\tfrac{7\sqrt{17}}{\sqrt{85}},0,\tfrac{-6\sqrt{17}}{\sqrt{85}}\rangle=\langle\tfrac{7}{\sqrt{5}},0,\tfrac{-6}{\sqrt{5}}\rangle\)'],
         r'(a) \(\langle-\tfrac{3}{2},2\rangle\); (b) \(\langle\tfrac{7}{\sqrt{5}},0,-\tfrac{6}{\sqrt{5}}\rangle\)')

  + card('Q24', r'More direction/length problems', ['unit vector'],
         'Multiply the unit vector by the desired length.',
         '',
         [r'(a) Same direction as \(-2\mathbf{i}+3\mathbf{j}\), three times its length: \(3(-2\mathbf{i}+3\mathbf{j})=\langle-6,9\rangle\)',
          r'(b) Length 2, opposite to \(\mathbf{v}=-3\mathbf{i}+4\mathbf{j}+\mathbf{k}\): \(\|\mathbf{v}\|=\sqrt{9+16+1}=\sqrt{26}\); result \(=-\tfrac{2}{\sqrt{26}}\langle-3,4,1\rangle=\langle\tfrac{6}{\sqrt{26}},-\tfrac{8}{\sqrt{26}},-\tfrac{2}{\sqrt{26}}\rangle\)'],
         r'(a) \(\langle-6,9\rangle\); (b) \(\langle\tfrac{6}{\sqrt{26}},-\tfrac{8}{\sqrt{26}},-\tfrac{2}{\sqrt{26}}\rangle\)')

  + card('Q25', r'Component form from magnitude and angle', ['angle form'],
         r'Use \(\mathbf{v}=\|\mathbf{v}\|\langle\cos\theta,\sin\theta\rangle\).',
         r'\(\mathbf{v}=\|\mathbf{v}\|\langle\cos\theta,\sin\theta\rangle\)',
         [r'(a) \(\|\mathbf{v}\|=3, \theta=\pi/4\): \(\langle\tfrac{3\sqrt{2}}{2},\tfrac{3\sqrt{2}}{2}\rangle\)',
          r'(b) \(\|\mathbf{v}\|=2, \theta=90°\): \(\langle 0,2\rangle\)',
          r'(c) \(\|\mathbf{v}\|=5, \theta=120°\): \(\langle-\tfrac{5}{2},\tfrac{5\sqrt{3}}{2}\rangle\)',
          r'(d) \(\|\mathbf{v}\|=1, \theta=\pi\): \(\langle-1,0\rangle\)'],
         r'(a) \(\langle\tfrac{3\sqrt{2}}{2},\tfrac{3\sqrt{2}}{2}\rangle\), (b) \(\langle0,2\rangle\), (c) \(\langle-\tfrac{5}{2},\tfrac{5\sqrt{3}}{2}\rangle\), (d) \(\langle-1,0\rangle\)')

  + card('Q26', r'Find \(\mathbf{v}+\mathbf{w}\) and \(\mathbf{v}-\mathbf{w}\) where \(\|\mathbf{v}\|=\|\mathbf{w}\|=1\), \(\mathbf{v}\) at \(\pi/6\), \(\mathbf{w}\) at \(3\pi/4\)', ['angle form'],
         'Convert each to component form then add/subtract.',
         '',
         [r'\(\mathbf{v}=\langle\cos(\pi/6),\sin(\pi/6)\rangle=\langle\tfrac{\sqrt{3}}{2},\tfrac{1}{2}\rangle\)',
          r'\(\mathbf{w}=\langle\cos(3\pi/4),\sin(3\pi/4)\rangle=\langle-\tfrac{\sqrt{2}}{2},\tfrac{\sqrt{2}}{2}\rangle\)',
          r'\(\mathbf{v}+\mathbf{w}=\langle\tfrac{\sqrt{3}-\sqrt{2}}{2},\tfrac{1+\sqrt{2}}{2}\rangle\)',
          r'\(\mathbf{v}-\mathbf{w}=\langle\tfrac{\sqrt{3}+\sqrt{2}}{2},\tfrac{1-\sqrt{2}}{2}\rangle\)'],
         r'\(\mathbf{v}+\mathbf{w}=\langle\tfrac{\sqrt{3}-\sqrt{2}}{2},\tfrac{1+\sqrt{2}}{2}\rangle\)')

  + card('Q34', r'Find \(\mathbf{u}\) and \(\mathbf{v}\) if \(\mathbf{u}+\mathbf{v}=\langle 2,-3\rangle\) and \(3\mathbf{u}+2\mathbf{v}=\langle-1,2\rangle\)', ['system'],
         'Solve the linear system by elimination.',
         '',
         [r'From \(\mathbf{u}+\mathbf{v}=\langle 2,-3\rangle\): \(\mathbf{u}=\langle 2,-3\rangle-\mathbf{v}\)',
          r'Sub into second: \(3(\langle 2,-3\rangle-\mathbf{v})+2\mathbf{v}=\langle-1,2\rangle\)',
          r'\(\langle 6,-9\rangle-\mathbf{v}=\langle-1,2\rangle \Rightarrow \mathbf{v}=\langle 7,-11\rangle\)',
          r'\(\mathbf{u}=\langle 2,-3\rangle-\langle 7,-11\rangle=\langle-5,8\rangle\)'],
         r'\(\mathbf{u}=\langle-5,8\rangle\), \(\mathbf{v}=\langle 7,-11\rangle\)')

  + card('Q35', r'Lengths of diagonals of parallelogram with sides \(\mathbf{i}+\mathbf{j}\) and \(\mathbf{i}-2\mathbf{j}\)', ['parallelogram'],
         'Diagonals of parallelogram are the sum and difference of side vectors.',
         '',
         [r'Diagonal 1: \((\mathbf{i}+\mathbf{j})+(\mathbf{i}-2\mathbf{j})=2\mathbf{i}-\mathbf{j}\); length \(=\sqrt{4+1}=\sqrt{5}\)',
          r'Diagonal 2: \((\mathbf{i}+\mathbf{j})-(\mathbf{i}-2\mathbf{j})=3\mathbf{j}\); length \(=3\)'],
         r'\(\sqrt{5}\) and \(3\)')
)

s11_2 = section('s11_2', '11.2 — Vectors', s11_2_concepts + s11_2_cards)

# ── Section 11.3 ────────────────────────────────────────────────────────────
s11_3_concepts = concepts('Key Concepts — Section 11.3 Dot Product &amp; Projections', [
    ('Dot product', r'\(\mathbf{u}\cdot\mathbf{v}=u_1v_1+u_2v_2+u_3v_3=\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta\)'),
    ('Perpendicularity', r'\(\mathbf{u}\perp\mathbf{v}\iff\mathbf{u}\cdot\mathbf{v}=0\)'),
    ('Projection', r'\(\text{proj}_{\mathbf{b}}\mathbf{v}=\dfrac{\mathbf{v}\cdot\mathbf{b}}{\|\mathbf{b}\|^2}\mathbf{b}\)'),
    ('Orthogonal part', r'\(\text{orth}_{\mathbf{b}}\mathbf{v}=\mathbf{v}-\text{proj}_{\mathbf{b}}\mathbf{v}\)'),
    ('Work', r'\(W=\mathbf{F}\cdot\mathbf{d}\)'),
])

s11_3_cards = (
    card('Q13', r'Find \(r\) so \(\overrightarrow{AB}\perp\overrightarrow{AP}\) where \(A(1,-1,3)\), \(B(3,0,5)\), \(P(r,r,r)\)', ['dot product','perpendicular'],
         'Set the dot product of AB and AP equal to zero and solve for r.',
         r'\(\overrightarrow{AB}\cdot\overrightarrow{AP}=0\)',
         [r'\(\overrightarrow{AB}=\langle 2,1,2\rangle\), \(\overrightarrow{AP}=\langle r-1,r+1,r-3\rangle\)',
          r'\(\overrightarrow{AB}\cdot\overrightarrow{AP}=2(r-1)+(r+1)+2(r-3)=5r-7=0\)',
          r'\(r=\tfrac{7}{5}\)'],
         r'\(r=\tfrac{7}{5}\)')

  + card('Q14', r'Find two unit vectors making 45° with \(4\mathbf{i}+3\mathbf{j}\)', ['angle','unit vector'],
         'Find the angle of the given vector, then add/subtract π/4.',
         '',
         [r'Let \(\alpha=\arctan(3/4)\) (angle of \(4\mathbf{i}+3\mathbf{j}\) with \(\cos\alpha=\tfrac{4}{5}, \sin\alpha=\tfrac{3}{5}\))',
          r'\(\mathbf{v}_1\) at angle \(\alpha+\tfrac{\pi}{4}\): \(\cos(\alpha+\tfrac{\pi}{4})=\cos\alpha\cos\tfrac{\pi}{4}-\sin\alpha\sin\tfrac{\pi}{4}=\tfrac{4-3}{5\sqrt{2}}=\tfrac{1}{5\sqrt{2}}\); \(\sin(\alpha+\tfrac{\pi}{4})=\tfrac{7}{5\sqrt{2}}\)',
          r'\(\mathbf{v}_2\) at angle \(\alpha-\tfrac{\pi}{4}\): \(\cos(\alpha-\tfrac{\pi}{4})=\tfrac{7}{5\sqrt{2}}\); \(\sin(\alpha-\tfrac{\pi}{4})=\tfrac{-1}{5\sqrt{2}}\)',
          r'\(\mathbf{v}_1=\langle\tfrac{1}{5\sqrt{2}},\tfrac{7}{5\sqrt{2}}\rangle\), \(\mathbf{v}_2=\langle\tfrac{7}{5\sqrt{2}},-\tfrac{1}{5\sqrt{2}}\rangle\)'],
         r'\(\langle\tfrac{1}{5\sqrt{2}},\tfrac{7}{5\sqrt{2}}\rangle\) and \(\langle\tfrac{7}{5\sqrt{2}},-\tfrac{1}{5\sqrt{2}}\rangle\)')

  + card('Q25', r'Find projection of \(\mathbf{v}\) onto \(\mathbf{b}\) and the orthogonal component', ['projection'],
         r'Use \(\text{proj}_{\mathbf{b}}\mathbf{v}=\frac{\mathbf{v}\cdot\mathbf{b}}{\|\mathbf{b}\|^2}\mathbf{b}\).',
         r'\(\text{proj}_{\mathbf{b}}\mathbf{v}=\dfrac{\mathbf{v}\cdot\mathbf{b}}{\|\mathbf{b}\|^2}\mathbf{b}\)',
         [r'(a) \(\mathbf{v}=2\mathbf{i}-\mathbf{j}+3\mathbf{k}\), \(\mathbf{b}=\mathbf{i}+2\mathbf{j}+2\mathbf{k}\): \(\mathbf{v}\cdot\mathbf{b}=2-2+6=6\), \(\|\mathbf{b}\|^2=9\); \(\text{proj}=\tfrac{6}{9}\langle 1,2,2\rangle=\langle\tfrac{2}{3},\tfrac{4}{3},\tfrac{4}{3}\rangle\); orth \(=\langle\tfrac{4}{3},-\tfrac{7}{3},\tfrac{5}{3}\rangle\)',
          r'(b) \(\mathbf{v}=\langle 4,-1,7\rangle\), \(\mathbf{b}=\langle 2,3,-6\rangle\): \(\mathbf{v}\cdot\mathbf{b}=8-3-42=-37\), \(\|\mathbf{b}\|^2=49\); \(\text{proj}=-\tfrac{37}{49}\langle 2,3,-6\rangle\); orth \(=\mathbf{v}-\text{proj}\)'],
         r'See each sub-part')

  + card('Q27', r'Express \(\mathbf{v}\) as sum of vector parallel to \(\mathbf{b}\) and vector orthogonal to \(\mathbf{b}\)', ['projection','decomposition'],
         r'\(\mathbf{v}=\text{proj}_{\mathbf{b}}\mathbf{v}+\text{orth}_{\mathbf{b}}\mathbf{v}\)',
         r'\(\mathbf{v}=\text{proj}_{\mathbf{b}}\mathbf{v}+(\mathbf{v}-\text{proj}_{\mathbf{b}}\mathbf{v})\)',
         [r'(a) \(\mathbf{v}=\langle-3,5\rangle\), \(\mathbf{b}=\langle 1,1\rangle\): \(\mathbf{v}\cdot\mathbf{b}=2\), \(\|\mathbf{b}\|^2=2\); proj \(=\langle 1,1\rangle\); orth \(=\langle-4,4\rangle\)',
          r'(b) \(\mathbf{v}=\langle-2,1,6\rangle\), \(\mathbf{b}=\langle 0,-2,1\rangle\): \(\mathbf{v}\cdot\mathbf{b}=0-2+6=4\), \(\|\mathbf{b}\|^2=5\); proj \(=\tfrac{4}{5}\langle 0,-2,1\rangle=\langle 0,-\tfrac{8}{5},\tfrac{4}{5}\rangle\); orth \(=\langle-2,\tfrac{13}{5},\tfrac{26}{5}\rangle\)',
          r'(c) \(\mathbf{v}=\langle 1,4,1\rangle\), \(\mathbf{b}=\langle 3,-2,5\rangle\): \(\mathbf{v}\cdot\mathbf{b}=3-8+5=0\); proj \(=\mathbf{0}\); \(\mathbf{v}=\mathbf{0}+\mathbf{v}\)'],
         r'(c) Entire \(\mathbf{v}\) is already orthogonal to \(\mathbf{b}\)')

  + card('Q35', r'Work done by \(\mathbf{F}=-3\mathbf{j}\) lb moving object from \((1,3)\) to \((4,7)\)', ['work'],
         r'Work = F · displacement.',
         r'\(W=\mathbf{F}\cdot\mathbf{d}\)',
         [r'Displacement \(\mathbf{d}=\langle 4-1,7-3\rangle=\langle 3,4\rangle\)',
          r'\(\mathbf{F}=\langle 0,-3\rangle\)',
          r'\(W=\langle 0,-3\rangle\cdot\langle 3,4\rangle=0-12=-12\) ft·lb'],
         r'\(W=-12\) ft·lb')

  + card('Q36', r'Child (34 kg) slides 4 m ramp at 27°; work done by gravity', ['work','physics'],
         'Component of gravity along the ramp times distance.',
         r'\(W=mgd\sin\theta\)',
         [r'\(m=34\text{ kg},\ g=9.8\text{ m/s}^2,\ d=4\text{ m},\ \theta=27°\)',
          r'\(W=34\times 9.8\times 4\times\sin 27°\approx 1332.8\times 0.454\approx 604.7\text{ J}\)'],
         r'\(W\approx 604.7\) J')
)

s11_3 = section('s11_3', '11.3 — Dot Product &amp; Projections', s11_3_concepts + s11_3_cards)

# ── Section 11.4 ────────────────────────────────────────────────────────────
s11_4_concepts = concepts('Key Concepts — Section 11.4 Cross Product', [
    ('Cross product', r'\(\mathbf{u}\times\mathbf{v}=\det\begin{pmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\u_1&u_2&u_3\\v_1&v_2&v_3\end{pmatrix}\)'),
    ('Orthogonality', r'\((\mathbf{u}\times\mathbf{v})\perp\mathbf{u}\) and \((\mathbf{u}\times\mathbf{v})\perp\mathbf{v}\)'),
    ('Area', r'Area of parallelogram \(=\|\mathbf{u}\times\mathbf{v}\|\); triangle \(=\tfrac{1}{2}\|\mathbf{u}\times\mathbf{v}\|\)'),
    ('Scalar triple', r'\(\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})=\det[\mathbf{u}\ \mathbf{v}\ \mathbf{w}]\); volume of parallelepiped'),
])

s11_4_cards = (
    card('Q5', r'\(\mathbf{u}=\langle 0,1,-2\rangle\), \(\mathbf{v}=\langle 3,0,-4\rangle\). Find \(\mathbf{u}\times\mathbf{v}\) and verify.', ['cross product'],
         'Expand the 3×3 determinant and verify orthogonality.',
         r'\(\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\0&1&-2\\3&0&-4\end{vmatrix}\)',
         [r'\(\mathbf{u}\times\mathbf{v}=\mathbf{i}(1\cdot(-4)-(-2)\cdot 0)-\mathbf{j}(0\cdot(-4)-(-2)\cdot 3)+\mathbf{k}(0\cdot 0-1\cdot 3)=\langle-4,-6,-3\rangle\)',
          r'Verify \(\mathbf{u}\cdot(\mathbf{u}\times\mathbf{v})=0(-4)+1(-6)+(-2)(-3)=-6+6=0\) ✓',
          r'Verify \(\mathbf{v}\cdot(\mathbf{u}\times\mathbf{v})=3(-4)+0(-6)+(-4)(-3)=-12+12=0\) ✓'],
         r'\(\mathbf{u}\times\mathbf{v}=\langle-4,-6,-3\rangle\)')

  + card('Q9', r'Direction cosines of \(\mathbf{u}\times\mathbf{v}\) for \(\mathbf{u}=\langle 1,1,0\rangle\), \(\mathbf{v}=\langle 1,0,1\rangle\)', ['cross product','direction cosines'],
         'Find the cross product then compute direction cosines.',
         '',
         [r'\(\mathbf{u}\times\mathbf{v}=\langle 1\cdot1-0\cdot0,\,0\cdot1-1\cdot1,\,1\cdot0-1\cdot1\rangle=\langle 1,-1,-1\rangle\)',
          r'\(|\mathbf{u}\times\mathbf{v}|=\sqrt{3}\)',
          r'\(\cos\alpha=\tfrac{1}{\sqrt{3}},\ \cos\beta=-\tfrac{1}{\sqrt{3}},\ \cos\gamma=-\tfrac{1}{\sqrt{3}}\)'],
         r'\(\cos\alpha=\tfrac{1}{\sqrt{3}},\ \cos\beta=\cos\gamma=-\tfrac{1}{\sqrt{3}}\)')

  + card('Q10', r'Two unit vectors orthogonal to both \(\mathbf{u}=-7\mathbf{i}+3\mathbf{j}+\mathbf{k}\) and \(\mathbf{v}=2\mathbf{i}+4\mathbf{k}\)', ['cross product','unit vector'],
         'The cross product gives a vector orthogonal to both; normalize.',
         '',
         [r'\(\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\-7&3&1\\2&0&4\end{vmatrix}=\langle 12-0,\,2-(-28),\,0-6\rangle=\langle 12,30,-6\rangle=6\langle 2,5,-1\rangle\)',
          r'\(|\langle 2,5,-1\rangle|=\sqrt{4+25+1}=\sqrt{30}\)',
          r'Unit vectors: \(\pm\tfrac{1}{\sqrt{30}}\langle 2,5,-1\rangle\)'],
         r'\(\pm\dfrac{1}{\sqrt{30}}\langle 2,5,-1\rangle\)')

  + card('Q11', r'Two unit vectors normal to plane through \(A(0,-2,1)\), \(B(1,-1,-2)\), \(C(-1,1,0)\)', ['cross product','normal'],
         'Find two edge vectors in the plane, compute their cross product.',
         '',
         [r'\(\overrightarrow{AB}=\langle 1,1,-3\rangle\), \(\overrightarrow{AC}=\langle-1,3,-1\rangle\)',
          r'\(\overrightarrow{AB}\times\overrightarrow{AC}=\langle 1(-1)-(-3)(3),\,(-3)(-1)-1(-1),\,1(3)-1(-1)\rangle=\langle 8,4,4\rangle=4\langle 2,1,1\rangle\)',
          r'\(|\langle 2,1,1\rangle|=\sqrt{6}\); unit normals: \(\pm\tfrac{1}{\sqrt{6}}\langle 2,1,1\rangle\)'],
         r'\(\pm\dfrac{1}{\sqrt{6}}\langle 2,1,1\rangle\)')

  + card('Q12', r'Two unit vectors parallel to \(yz\)-plane and orthogonal to \(3\mathbf{i}-\mathbf{j}+2\mathbf{k}\)', ['cross product','constraint'],
         'Parallel to yz-plane means x-component = 0; then apply orthogonality.',
         '',
         [r'Form \(\mathbf{w}=\langle 0,b,c\rangle\). Orthogonality: \(\langle 0,b,c\rangle\cdot\langle 3,-1,2\rangle=-b+2c=0 \Rightarrow b=2c\)',
          r'Choose \(c=1\): \(\mathbf{w}=\langle 0,2,1\rangle\), \(|\mathbf{w}|=\sqrt{5}\)',
          r'Unit vectors: \(\pm\tfrac{1}{\sqrt{5}}\langle 0,2,1\rangle\)'],
         r'\(\pm\dfrac{1}{\sqrt{5}}\langle 0,2,1\rangle\)')

  + card('Q19', r'Area of triangle \(P(1,5,-2)\), \(Q(0,0,0)\), \(R(3,5,1)\)', ['cross product','area'],
         'Area = ½|QP × QR|.',
         r'\(\text{Area}=\tfrac{1}{2}\|\mathbf{QP}\times\mathbf{QR}\|\)',
         [r'\(\overrightarrow{QP}=\langle 1,5,-2\rangle\), \(\overrightarrow{QR}=\langle 3,5,1\rangle\)',
          r'\(\overrightarrow{QP}\times\overrightarrow{QR}=\langle 5(1)-(-2)(5),\,(-2)(3)-1(1),\,1(5)-5(3)\rangle=\langle 15,-7,-10\rangle\)',
          r'\(\text{Area}=\tfrac{1}{2}\sqrt{225+49+100}=\tfrac{1}{2}\sqrt{374}=\dfrac{\sqrt{374}}{2}\)'],
         r'\(\dfrac{\sqrt{374}}{2}\)')

  + card('Q23', r'Scalar triple product \(\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})\) for \(\mathbf{u}=\langle 2,1,0\rangle\), \(\mathbf{v}=\langle 1,-3,1\rangle\), \(\mathbf{w}=\langle 4,0,1\rangle\)', ['scalar triple product'],
         'Evaluate as a 3×3 determinant.',
         r'\(\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})=\det\begin{pmatrix}2&1&0\\1&-3&1\\4&0&1\end{pmatrix}\)',
         [r'Expand along first row: \(2(-3-0)-1(1-4)+0=2(-3)-1(-3)=-6+3=-3\)'],
         r'\(-3\)')

  + card('Q29', r'\(\mathbf{u}=3\mathbf{i}+2\mathbf{j}+\mathbf{k}\), \(\mathbf{v}=\mathbf{i}+\mathbf{j}+2\mathbf{k}\), \(\mathbf{w}=\mathbf{i}+3\mathbf{j}+3\mathbf{k}\)', ['parallelepiped','area'],
         'Use scalar triple product for volume; cross product for area; angle via sine formula.',
         '',
         [r'(a) Volume \(=|\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})|\): det \(=3(3-6)-2(3-2)+1(3-1)=-9-2+2=-9\); Volume \(=9\)',
          r'(b) Area of face (u,w): \(\mathbf{u}\times\mathbf{w}=\langle 2(3)-1(3),\,1(1)-3(3),\,3(3)-2(1)\rangle=\langle 3,-8,7\rangle\); Area \(=\sqrt{9+64+49}=\sqrt{122}\)',
          r'(c) Angle \(\varphi\) between \(\mathbf{u}\) and face (v,w): \(\mathbf{v}\times\mathbf{w}=\langle 1(3)-2(3),\,2(1)-1(3),\,1(3)-1(1)\rangle=\langle-3,-1,2\rangle\), \(|\mathbf{v}\times\mathbf{w}|=\sqrt{14}\); \(\sin\varphi=\tfrac{9}{\sqrt{14}\cdot\sqrt{14}}=\tfrac{9}{14}\); \(\varphi\approx 40°\)'],
         r'(a) Volume \(=9\); (b) Area \(=\sqrt{122}\); (c) \(\varphi\approx40°\)')
)

s11_4 = section('s11_4', '11.4 — Cross Product', s11_4_concepts + s11_4_cards)

# ── Section 11.5 ────────────────────────────────────────────────────────────
s11_5_concepts = concepts('Key Concepts — Section 11.5 Lines in 3-Space', [
    ('Parametric', r'\(x=x_0+at,\ y=y_0+bt,\ z=z_0+ct\)'),
    ('Vector form', r'\(\mathbf{r}=\mathbf{r}_0+t\mathbf{v}\)'),
    ('Skew lines', 'Neither parallel nor intersecting; no common point'),
    ('Symmetric', r'\(\dfrac{x-x_0}{a}=\dfrac{y-y_0}{b}=\dfrac{z-z_0}{c}\)'),
])

s11_5_cards = (
    card('Q4', r'Write parametric equations for lines through two points', ['parametric'],
         'Direction vector = P₂ − P₁; substitute into parametric form.',
         r'\(\mathbf{r}=P_1+t(P_2-P_1)\)',
         [r'(a) \(P_1(0,1)\), \(P_2(-3,-4)\): direction \(\langle-3,-5\rangle\); \(x=-3t,\ y=1-5t\); segment: \(0\le t\le 1\)',
          r'(b) \(P_1(-1,3,5)\), \(P_2(-1,3,2)\): direction \(\langle 0,0,-3\rangle\); \(x=-1,\ y=3,\ z=5-3t\); segment: \(0\le t\le 1\)'],
         r'(a) \(x=-3t,\,y=1-5t\); (b) \(x=-1,\,y=3,\,z=5-3t\)')

  + card('Q17', r'Line tangent to \(x^2+y^2=25\) at \((3,-4)\)', ['tangent line','parametric'],
         'Radius at tangent point is perpendicular to tangent; rotate radius direction 90°.',
         '',
         [r'Radius direction to \((3,-4)\): \(\langle 3,-4\rangle\). Tangent is perpendicular: direction \(\langle 4,3\rangle\).',
          r'Parametric: \(x=3+4t,\ y=-4+3t\)'],
         r'\(x=3+4t,\ y=-4+3t\)')

  + card('Q18', r'Line tangent to \(y=x^2\) at \((-2,4)\)', ['tangent line','parametric'],
         r"Slope = dy/dx = 2x evaluated at the point.",
         '',
         [r'\(\dfrac{dy}{dx}=2x\Big|_{x=-2}=-4\). Direction vector: \(\langle 1,-4\rangle\).',
          r'Parametric: \(x=-2+t,\ y=4-4t\)'],
         r'\(x=-2+t,\ y=4-4t\)')

  + card('Q25', r'Line \(x=-2,\ y=4+2t,\ z=-3+t\): intersections with coordinate planes', ['line','intercepts'],
         'Set the appropriate variable to zero and solve for t.',
         '',
         [r'\(xy\)-plane (\(z=0\)): \(-3+t=0 \Rightarrow t=3\); point \((-2,10,0)\)',
          r'\(xz\)-plane (\(y=0\)): \(4+2t=0 \Rightarrow t=-2\); point \((-2,0,-5)\)',
          r'\(yz\)-plane (\(x=0\)): \(x=-2\) always, so the line never reaches \(x=0\) — <strong>no intersection</strong>.'],
         r'\((-2,10,0)\), \((-2,0,-5)\), no yz-intersection')

  + card('Q31', r'Show \(L_1\) and \(L_2\) are skew', ['skew lines'],
         'Verify not parallel; then show no common point.',
         '',
         [r'\(L_1: x=1+7t,y=3+t,z=5-3t\); direction \(\mathbf{v}_1=\langle 7,1,-3\rangle\)',
          r'\(L_2: x=4-t,y=6,z=7+2t\); direction \(\mathbf{v}_2=\langle-1,0,2\rangle\)',
          r'Not parallel: \(\mathbf{v}_1\ne k\mathbf{v}_2\).',
          r'Check intersection: from \(y\)-equations: \(3+t=6\Rightarrow t=3\); \(z_1=5-9=-4\); from \(L_2\): \(z_2=7+2s\); \(x_1=22,\ x_2=4-s\) → no consistent solution. <strong>Skew.</strong>'],
         r'Lines are skew (not parallel, no intersection)')

  + card('Q33', r'Determine if \(L_1\) and \(L_2\) are parallel, skew, or intersecting', ['parallel lines'],
         'Compare direction vectors.',
         '',
         [r'\(L_1\) direction: \(\langle-2,1,-1\rangle\)',
          r'\(L_2\) direction: \(\langle-4,2,-2\rangle=2\langle-2,1,-1\rangle\)',
          r'Directions are scalar multiples → <strong>Parallel</strong>.'],
         r'The lines are parallel')

  + card('Q46', r'Point \(\tfrac{2}{3}\) of the way from \(P_1(1,4,-3)\) to \(P_2(1,5,-1)\)', ['parametric','point'],
         r'Use \(\mathbf{r}=P_1+\frac{2}{3}(P_2-P_1)\).',
         r'\(\mathbf{r}=P_1+t(P_2-P_1)\)',
         [r'\(P_2-P_1=\langle 0,1,2\rangle\)',
          r'\(\mathbf{r}=(1,4,-3)+\tfrac{2}{3}\langle 0,1,2\rangle=(1,\,4+\tfrac{2}{3},\,-3+\tfrac{4}{3})=\bigl(1,\tfrac{14}{3},-\tfrac{5}{3}\bigr)\)'],
         r'\(\bigl(1,\tfrac{14}{3},-\tfrac{5}{3}\bigr)\)')

  + card('Q55', r'\(L_1: x=1+2t,y=2-t,z=4-2t\) and \(L_2: x=9+t,y=5+3t,z=-4-t\)', ['line intersection','angle'],
         'Verify common point, compute intersection angle, find line through that point perpendicular to both.',
         '',
         [r'(a) \((7,-1,-2)\) on \(L_1\) at \(t=3\): \((1+6,2-3,4-6)=(7,-1,-2)\) ✓; on \(L_2\) at \(t=-2\): \((9-2,5-6,-4+2)=(7,-1,-2)\) ✓',
          r'(b) \(\mathbf{v}_1=\langle 2,-1,-2\rangle\), \(\mathbf{v}_2=\langle 1,3,-1\rangle\); \(\cos\theta=\dfrac{|\mathbf{v}_1\cdot\mathbf{v}_2|}{\|\mathbf{v}_1\|\|\mathbf{v}_2\|}=\dfrac{|2-3+2|}{3\sqrt{11}}=\dfrac{1}{3\sqrt{11}}\); \(\theta\approx 84°\)',
          r'(c) \(\mathbf{v}_1\times\mathbf{v}_2=\langle(-1)(-1)-(-2)(3),\,(-2)(1)-(2)(-1),\,(2)(3)-(-1)(1)\rangle=\langle 7,0,7\rangle\); line: \(x=7+7t,\,y=-1,\,z=-2+7t\)'],
         r'(a) Yes ✓; (b) \(\theta\approx84°\); (c) \(x=7+7t,\,y=-1,\,z=-2+7t\)')
)

s11_5 = section('s11_5', '11.5 — Lines', s11_5_concepts + s11_5_cards)

# ── Section 11.6 ────────────────────────────────────────────────────────────
s11_6_concepts = concepts('Key Concepts — Section 11.6 Planes', [
    ('Plane equation', r'\(a(x-x_0)+b(y-y_0)+c(z-z_0)=0\) with normal \(\mathbf{n}=\langle a,b,c\rangle\)'),
    ('Distance point-plane', r'\(D=\dfrac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}\)'),
    ('Parallel planes', 'Same normal direction (normals are scalar multiples)'),
    ('⊥ planes', 'Normal vectors are perpendicular: n₁·n₂ = 0'),
])

s11_6_cards = (
    card('Q11', r'Plane through \((-2,1,1)\), \((0,2,3)\), \((1,0,-1)\)', ['plane','three points'],
         'Find two edge vectors, cross them to get the normal, then use point-normal form.',
         '',
         [r'\(\overrightarrow{P_1P_2}=\langle 2,1,2\rangle\), \(\overrightarrow{P_1P_3}=\langle 3,-1,-2\rangle\)',
          r'\(\mathbf{n}=\overrightarrow{P_1P_2}\times\overrightarrow{P_1P_3}=\langle(1)(-2)-(2)(-1),\,(2)(3)-(2)(-2),\,(2)(-1)-(1)(3)\rangle=\langle 0,10,-5\rangle\propto\langle 0,2,-1\rangle\)',
          r'Through \((-2,1,1)\): \(0+2(1)-(1)=1\); Equation: \(\boxed{2y-z=1}\)'],
         r'\(2y-z=1\)')

  + card('Q17', r'Intersection of line and plane', ['line-plane intersection'],
         'Substitute parametric equations into plane equation and solve for t.',
         '',
         [r'(a) \(x=y=z=t\) and \(3x-2y+z=5\): \(3t-2t+t=2t=5\Rightarrow t=\tfrac{5}{2}\); point \(\bigl(\tfrac{5}{2},\tfrac{5}{2},\tfrac{5}{2}\bigr)\)',
          r'(b) \(x=2-t,\,y=3+t,\,z=t\) and \(2x+y+z=1\): \(2(2-t)+(3+t)+t=7\ne 1\) — contradiction; <strong>parallel, no intersection</strong>.'],
         r'(a) \(\bigl(\tfrac{5}{2},\tfrac{5}{2},\tfrac{5}{2}\bigr)\); (b) parallel, no intersection')

  + card('Q26', r'Plane containing line \(x=-2+3t,y=4+2t,z=3-t\) and ⊥ to \(x-2y+z=5\)', ['plane','perpendicular planes'],
         'New normal = line direction × given plane normal.',
         '',
         [r'Line direction \(\mathbf{v}=\langle 3,2,-1\rangle\); given normal \(\mathbf{n}=\langle 1,-2,1\rangle\)',
          r'\(\mathbf{N}=\mathbf{v}\times\mathbf{n}=\langle(2)(1)-(-1)(-2),\,(-1)(1)-(3)(1),\,(3)(-2)-(2)(1)\rangle=\langle 0,-4,-8\rangle\propto\langle 0,1,2\rangle\)',
          r'Through \((-2,4,3)\): \(0+4+6=10\); Equation: \(y+2z=10\)'],
         r'\(y+2z=10\)')

  + card('Q29', r'Plane through \((1,2,-1)\) ⊥ to intersection line of \(2x+y+z=2\) and \(x+2y+z=3\)', ['plane','perpendicular'],
         'Direction of intersection = n₁ × n₂, which becomes the new plane normal.',
         '',
         [r'\(\mathbf{n}_1=\langle 2,1,1\rangle\), \(\mathbf{n}_2=\langle 1,2,1\rangle\)',
          r'\(\mathbf{n}_1\times\mathbf{n}_2=\langle(1)(1)-(1)(2),\,(1)(1)-(2)(1),\,(2)(2)-(1)(1)\rangle=\langle-1,-1,3\rangle\)',
          r'Through \((1,2,-1)\): \(-1-2-3=-6\); Equation: \(-x-y+3z=-6\) or \(x+y-3z=6\)'],
         r'\(x+y-3z=6\)')

  + card('Q33', r'Plane equidistant from \((2,-1,1)\) and \((3,1,5)\)', ['plane','midpoint'],
         'The desired plane is the perpendicular bisector plane of the segment.',
         '',
         [r'Midpoint: \(M=\bigl(\tfrac{5}{2},0,3\bigr)\); normal direction: \(\langle 3-2,1-(-1),5-1\rangle=\langle 1,2,4\rangle\)',
          r'Through \(M\): \(\tfrac{5}{2}+0+12=\tfrac{29}{2}\); Equation: \(x+2y+4z=\tfrac{29}{2}\) or \(2x+4y+8z=29\)'],
         r'\(2x+4y+8z=29\)')

  + card('Q37', r'Show \(L_1,L_2\) are parallel; find plane containing both', ['parallel lines','plane'],
         'Check direction vectors; then use a point on each line to form a third vector for the normal.',
         '',
         [r'\(L_1: x=-2+t,y=3+2t,z=4-t\); dir \(\mathbf{d}=\langle 1,2,-1\rangle\)',
          r'\(L_2: x=3-t,y=4-2t,z=t\); dir \(=\langle-1,-2,1\rangle=-\mathbf{d}\) → <strong>Parallel ✓</strong>',
          r'Points: \(P_1=(-2,3,4)\) on \(L_1\), \(P_2=(3,4,0)\) on \(L_2\); \(\overrightarrow{P_1P_2}=\langle 5,1,-4\rangle\)',
          r'\(\mathbf{n}=\langle 1,2,-1\rangle\times\langle 5,1,-4\rangle=\langle(2)(-4)-(-1)(1),\,(-1)(5)-(1)(-4),\,(1)(1)-(2)(5)\rangle=\langle-7,-1,-9\rangle\)',
          r'Through \((-2,3,4)\): \(14-3-36=-25\); \(-7x-y-9z=-25\) → \(7x+y+9z=25\)'],
         r'\(7x+y+9z=25\)')

  + card('Q51', r'Show \(x=-1+t,y=3+2t,z=-t\) is parallel to \(2x-2y-2z+3=0\); find distance', ['parallel','distance'],
         'Check v·n = 0 for parallel; then use distance formula with any point on the line.',
         r'\(D=\dfrac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}\)',
         [r'Direction \(\mathbf{v}=\langle 1,2,-1\rangle\); normal \(\mathbf{n}=\langle 2,-2,-2\rangle\)',
          r'\(\mathbf{v}\cdot\mathbf{n}=2-4+2=0\) ✓ parallel',
          r'Point on line: \((-1,3,0)\); \(D=\dfrac{|2(-1)-2(3)-2(0)+3|}{\sqrt{4+4+4}}=\dfrac{|-2-6+3|}{2\sqrt{3}}=\dfrac{5}{2\sqrt{3}}=\dfrac{5\sqrt{3}}{6}\)'],
         r'\(D=\dfrac{5\sqrt{3}}{6}\)')
)

s11_6 = section('s11_6', '11.6 — Planes', s11_6_concepts + s11_6_cards)

# ── Section 11.7 ────────────────────────────────────────────────────────────
s11_7_concepts = concepts('Key Concepts — Section 11.7 Quadric Surfaces', [
    ('Ellipsoid', r'\(\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1\); all traces are ellipses'),
    ('Paraboloid', r'Elliptic: \(z=\frac{x^2}{a^2}+\frac{y^2}{b^2}\); Hyperbolic: \(z=\frac{x^2}{a^2}-\frac{y^2}{b^2}\)'),
    ('Hyperboloid 1-sheet', r'\(\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1\); connected surface'),
    ('Hyperboloid 2-sheets', r'\(\frac{z^2}{c^2}-\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\); two separate pieces'),
    ('Cone', r'\(\frac{z^2}{c^2}=\frac{x^2}{a^2}+\frac{y^2}{b^2}\)'),
])

s11_7_cards = (
    card('Q7', r'Classify each quadric surface by traces', ['classification'],
         'Examine cross-sectional traces in coordinate planes.',
         '',
         [r'(a) \(\dfrac{x^2}{9}+\dfrac{y^2}{25}+\dfrac{z^2}{4}=1\): all traces ellipses → <strong>Ellipsoid</strong>',
          r'(b) \(z=x^2+4y^2\): horizontal traces ellipses, vertical traces parabolas → <strong>Elliptic Paraboloid</strong>',
          r'(c) \(\dfrac{x^2}{9}+\dfrac{y^2}{16}-\dfrac{z^2}{4}=1\): horizontal traces ellipses, one sign different → <strong>Hyperboloid of One Sheet</strong>'],
         r'(a) Ellipsoid; (b) Elliptic Paraboloid; (c) Hyperboloid of One Sheet',
         plot3d('(a) Ellipsoid x²/9+y²/25+z²/4=1',
                ellipsoid_traces(0, 0, 0, 3, 5, 2))
         + plot3d('(b) Elliptic Paraboloid z=x²+4y²',
                  paraboloid_traces(0, 0, 1, 0.25, xlim=(-2, 2), ylim=(-1, 1)))
         + plot3d('(c) Hyperboloid of One Sheet x²/9+y²/16−z²/4=1',
                  hyperboloid1_traces(3, 4, 2)))

  + card('Q15', r'Describe \(x^2+\dfrac{y^2}{4}+\dfrac{z^2}{9}=1\)', ['ellipsoid'],
         'Identify the quadric type and semi-axes.',
         '',
         [r'All three terms positive, equals 1 → <strong>Ellipsoid</strong>',
          r'Semi-axes: \(a=1\) along \(x\), \(b=2\) along \(y\), \(c=3\) along \(z\)'],
         r'Ellipsoid; semi-axes 1, 2, 3 along x, y, z respectively',
         plot3d('Ellipsoid x²+y²/4+z²/9=1  (semi-axes 1, 2, 3)',
                ellipsoid_traces(0, 0, 0, 1, 2, 3)))

  + card('Q17', r'Describe \(\dfrac{x^2}{4}+\dfrac{y^2}{9}-\dfrac{z^2}{16}=1\)', ['hyperboloid'],
         'One term negative on left → hyperboloid of one sheet.',
         '',
         [r'Two positive terms, one negative → <strong>Hyperboloid of One Sheet</strong>',
          r'Axis of symmetry along \(z\)-axis (the subtracted variable).'],
         r'Hyperboloid of One Sheet (axis along z)',
         plot3d('Hyperboloid of One Sheet x²/4+y²/9−z²/16=1',
                hyperboloid1_traces(2, 3, 4)))

  + card('Q19', r'Describe \(4z^2=x^2+4y^2\)', ['cone'],
         'Rewrite with zero on one side to reveal the cone structure.',
         '',
         [r'Rewrite: \(\dfrac{x^2}{4}+y^2-z^2=0\) or \(z^2=\dfrac{x^2}{4}+y^2\)',
          r'Right-hand side has two variables, left has one squared → <strong>Elliptic Cone</strong> with axis along \(z\)'],
         r'Elliptic Cone (axis along z)',
         plot3d('Elliptic Cone 4z²=x²+4y²  (z²=x²/4+y²)',
                cone_traces(2, 1, 1)))

  + card('Q21', r'Describe \(9z^2-4y^2-9x^2=36\)', ['hyperboloid'],
         'Divide by 36 to get standard form; count signs.',
         '',
         [r'Divide by 36: \(\dfrac{z^2}{4}-\dfrac{y^2}{9}-\dfrac{x^2}{4}=1\)',
          r'One positive, two negative → <strong>Hyperboloid of Two Sheets</strong> (axis along \(z\))'],
         r'Hyperboloid of Two Sheets (axis along z)',
         plot3d('Hyperboloid of Two Sheets z²/4−y²/9−x²/4=1',
                hyperboloid2_traces(2, 3, 2)))

  + card('Q25', r'Describe \(4z=x^2+2y^2\)', ['paraboloid'],
         'Rewrite as z = ... to identify orientation.',
         '',
         [r'Solve for \(z\): \(z=\dfrac{x^2}{4}+\dfrac{y^2}{2}\)',
          r'Horizontal traces: ellipses; vertical traces: parabolas → <strong>Elliptic Paraboloid</strong> opening in +z direction'],
         r'Elliptic Paraboloid opening upward (+z)',
         plot3d('Elliptic Paraboloid 4z=x²+2y²  (z=x²/4+y²/2)',
                paraboloid_traces(0, 0, 4, 2, xlim=(-4, 4), ylim=(-3, 3))))

  + card('Q39', r'Classify \(9x^2+y^2+4z^2-18x+2y+16z=10\)', ['completing square','ellipsoid'],
         'Complete the square in each variable to get standard form.',
         '',
         [r'Group: \(9(x^2-2x)+(y^2+2y)+4(z^2+4z)=10\)',
          r'Complete: \(9(x-1)^2-9+(y+1)^2-1+4(z+2)^2-16=10\)',
          r'\(9(x-1)^2+(y+1)^2+4(z+2)^2=36\) → \(\dfrac{(x-1)^2}{4}+\dfrac{(y+1)^2}{36}+\dfrac{(z+2)^2}{9}=1\)',
          r'<strong>Ellipsoid</strong> centered at \((1,-1,-2)\), semi-axes 2, 6, 3'],
         r'Ellipsoid centered at \((1,-1,-2)\)',
         plot3d('Ellipsoid centered at (1, −1, −2), semi-axes 2, 6, 3',
                ellipsoid_traces(1, -1, -2, 2, 6, 3)))
)

s11_7 = section('s11_7', '11.7 — Quadric Surfaces', s11_7_concepts + s11_7_cards)

# ── Section 11.8 ────────────────────────────────────────────────────────────
s11_8_concepts = concepts('Key Concepts — Section 11.8 Cylindrical &amp; Spherical Coordinates', [
    ('Cylindrical', r'\(x=r\cos\theta,\;y=r\sin\theta,\;z=z\)'),
    ('Spherical → rect', r'\(x=\rho\sin\phi\cos\theta,\;y=\rho\sin\phi\sin\theta,\;z=\rho\cos\phi\)'),
    ('Rect → spherical', r'\(\rho=\sqrt{x^2+y^2+z^2},\;\theta=\arctan(y/x),\;\phi=\arccos(z/\rho)\)'),
    ('Spherical → cyl', r'\(r=\rho\sin\phi,\;z=\rho\cos\phi\)'),
])

s11_8_cards = (
    card('Q3', r'Convert cylindrical to rectangular', ['cylindrical','conversion'],
         r'Use \(x=r\cos\theta,\,y=r\sin\theta,\,z=z\).',
         r'\(x=r\cos\theta,\;y=r\sin\theta,\;z=z\)',
         [r'(a) \((4,\pi/6,3)\): \(x=4\cos(\pi/6)=2\sqrt{3},\,y=4\sin(\pi/6)=2,\,z=3\) → \((2\sqrt{3},2,3)\)',
          r'(b) \((8,3\pi/4,-2)\): \(x=8\cos(3\pi/4)=-4\sqrt{2},\,y=8\sin(3\pi/4)=4\sqrt{2}\) → \((-4\sqrt{2},4\sqrt{2},-2)\)',
          r'(c) \((5,0,4)\) → \((5,0,4)\)',
          r'(d) \((7,\pi,-9)\): \(x=7\cos\pi=-7,\,y=0\) → \((-7,0,-9)\)'],
         r'(a) \((2\sqrt{3},2,3)\); (b) \((-4\sqrt{2},4\sqrt{2},-2)\); (c) \((5,0,4)\); (d) \((-7,0,-9)\)')

  + card('Q5', r'Convert rectangular to spherical', ['spherical','conversion'],
         r'Use \(\rho=\sqrt{x^2+y^2+z^2}\), \(\theta=\arctan(y/x)\), \(\phi=\arccos(z/\rho)\).',
         r'\(\rho=\sqrt{x^2+y^2+z^2}\)',
         [r'(a) \((1,\sqrt{3},-2)\): \(\rho=\sqrt{1+3+4}=2\sqrt{2}\), \(\theta=\arctan(\sqrt{3}/1)=\pi/3\), \(\phi=\arccos(-2/(2\sqrt{2}))=\arccos(-1/\sqrt{2})=3\pi/4\) → \((2\sqrt{2},\pi/3,3\pi/4)\)',
          r'(b) \((1,-1,\sqrt{2})\): \(\rho=2\), \(\theta=\arctan(-1/1)=7\pi/4\) (Q4), \(\phi=\arccos(\sqrt{2}/2)=\pi/4\) → \((2,7\pi/4,\pi/4)\)',
          r'(c) \((0,3\sqrt{3},3)\): \(\rho=\sqrt{0+27+9}=6\), \(\theta=\pi/2\), \(\phi=\arccos(3/6)=\pi/3\) → \((6,\pi/2,\pi/3)\)',
          r'(d) \((-5\sqrt{3},5,0)\): \(\rho=\sqrt{75+25}=10\), \(\theta=5\pi/6\), \(\phi=\arccos(0)=\pi/2\) → \((10,5\pi/6,\pi/2)\)'],
         r'(a) \((2\sqrt{2},\pi/3,3\pi/4)\); (b) \((2,7\pi/4,\pi/4)\); (c) \((6,\pi/2,\pi/3)\); (d) \((10,5\pi/6,\pi/2)\)')

  + card('Q7', r'Convert spherical \((\rho,\theta,\phi)\) to rectangular', ['spherical','conversion'],
         r'Use \(x=\rho\sin\phi\cos\theta,\,y=\rho\sin\phi\sin\theta,\,z=\rho\cos\phi\).',
         r'\(x=\rho\sin\phi\cos\theta,\;y=\rho\sin\phi\sin\theta,\;z=\rho\cos\phi\)',
         [r'(a) \((5,\pi/6,\pi/4)\): \(x=5\sin(\pi/4)\cos(\pi/6)=\tfrac{5\sqrt{2}}{2}\cdot\tfrac{\sqrt{3}}{2}=\tfrac{5\sqrt{6}}{4}\); \(y=\tfrac{5\sqrt{2}}{2}\cdot\tfrac{1}{2}=\tfrac{5\sqrt{2}}{4}\); \(z=5\cos(\pi/4)=\tfrac{5\sqrt{2}}{2}\)',
          r'(b) \((7,0,\pi/2)\): \(x=7\sin(\pi/2)\cos(0)=7,\,y=0,\,z=0\) → \((7,0,0)\)',
          r'(c) \((1,\pi,0)\): \(x=\sin(0)\cos(\pi)=0,\,y=0,\,z=\cos(0)=1\) → \((0,0,1)\)',
          r'(d) \((2,3\pi/2,\pi/2)\): \(x=2\sin(\pi/2)\cos(3\pi/2)=0,\,y=2\sin(\pi/2)\sin(3\pi/2)=-2,\,z=0\) → \((0,-2,0)\)'],
         r'(a) \(\bigl(\tfrac{5\sqrt{6}}{4},\tfrac{5\sqrt{2}}{4},\tfrac{5\sqrt{2}}{2}\bigr)\); (b) \((7,0,0)\); (c) \((0,0,1)\); (d) \((0,-2,0)\)')

  + card('Q9', r'Convert cylindrical to spherical', ['cylindrical','spherical','conversion'],
         r'Use \(\rho=\sqrt{r^2+z^2}\), keep \(\theta\), \(\phi=\arccos(z/\rho)\).',
         r'\(\rho=\sqrt{r^2+z^2},\;\phi=\arccos(z/\rho)\)',
         [r'(a) \((\sqrt{3},\pi/6,3)\): \(\rho=\sqrt{3+9}=2\sqrt{3}\), \(\phi=\arccos(3/(2\sqrt{3}))=\arccos(\sqrt{3}/2)=\pi/6\) → \((2\sqrt{3},\pi/6,\pi/6)\)',
          r'(b) \((1,\pi/4,-1)\): \(\rho=\sqrt{1+1}=\sqrt{2}\), \(\phi=\arccos(-1/\sqrt{2})=3\pi/4\) → \((\sqrt{2},\pi/4,3\pi/4)\)',
          r'(c) \((2,3\pi/4,0)\): \(\rho=2\), \(\phi=\arccos(0)=\pi/2\) → \((2,3\pi/4,\pi/2)\)',
          r'(d) \((6,1,-2\sqrt{3})\): \(\rho=\sqrt{36+12}=4\sqrt{3}\), \(\phi=\arccos(-2\sqrt{3}/(4\sqrt{3}))=\arccos(-1/2)=2\pi/3\) → \((4\sqrt{3},1,2\pi/3)\)'],
         r'(a) \((2\sqrt{3},\pi/6,\pi/6)\); (b) \((\sqrt{2},\pi/4,3\pi/4)\); (c) \((2,3\pi/4,\pi/2)\); (d) \((4\sqrt{3},1,2\pi/3)\)')

  + card('Q11', r'Convert spherical \((\rho,\theta,\phi)\) to cylindrical', ['spherical','cylindrical','conversion'],
         r'Use \(r=\rho\sin\phi\), keep \(\theta\), \(z=\rho\cos\phi\).',
         r'\(r=\rho\sin\phi,\;\theta=\theta,\;z=\rho\cos\phi\)',
         [r'(a) \((5,\pi/4,2\pi/3)\): \(r=5\sin(2\pi/3)=\tfrac{5\sqrt{3}}{2}\), \(z=5\cos(2\pi/3)=-\tfrac{5}{2}\) → \((\tfrac{5\sqrt{3}}{2},\pi/4,-\tfrac{5}{2})\)',
          r'(b) \((1,7\pi/6,\pi)\): \(r=\sin\pi=0\), \(z=\cos\pi=-1\) → \((0,7\pi/6,-1)\)',
          r'(c) \((3,0,0)\): \(r=3\sin 0=0\), \(z=3\cos 0=3\) → \((0,0,3)\)',
          r'(d) \((4,\pi/6,\pi/2)\): \(r=4\sin(\pi/2)=4\), \(z=4\cos(\pi/2)=0\) → \((4,\pi/6,0)\)'],
         r'(a) \((\tfrac{5\sqrt{3}}{2},\pi/4,-\tfrac{5}{2})\); (b) \((0,7\pi/6,-1)\); (c) \((0,0,3)\); (d) \((4,\pi/6,0)\)')

  + card('Q33', r'Convert \(\rho\sin\phi=2\cos\theta\) to rectangular', ['spherical','conversion'],
         r'Use \(\rho\sin\phi=r\) and \(\cos\theta=x/r\).',
         '',
         [r'\(\rho\sin\phi=r\) (cylindrical radius), so the equation becomes \(r=2\cos\theta\)',
          r'Multiply both sides by \(r\): \(r^2=2r\cos\theta\)',
          r'\(x^2+y^2=2x\) → \((x-1)^2+y^2=1\)',
          r'This is a <strong>cylinder</strong> of radius 1 with axis through \((1,0,z)\)'],
         r'\((x-1)^2+y^2=1\) — cylinder, radius 1, axis through \((1,0)\)')

  + card('Q43', r'Convert \(2x+3y+4z=1\) to cylindrical and spherical', ['conversion','plane'],
         'Substitute coordinate transformation formulas directly.',
         '',
         [r'<strong>Cylindrical:</strong> substitute \(x=r\cos\theta,\,y=r\sin\theta\): \(2r\cos\theta+3r\sin\theta+4z=1\)',
          r'<strong>Spherical:</strong> substitute \(x=\rho\sin\phi\cos\theta,\,y=\rho\sin\phi\sin\theta,\,z=\rho\cos\phi\):<br>\(\rho(2\sin\phi\cos\theta+3\sin\phi\sin\theta+4\cos\phi)=1\)'],
         r'Cylindrical: \(r(2\cos\theta+3\sin\theta)+4z=1\); Spherical: \(\rho(2\sin\phi\cos\theta+3\sin\phi\sin\theta+4\cos\phi)=1\)')
)

s11_8 = section('s11_8', '11.8 — Cylindrical &amp; Spherical Coordinates', s11_8_concepts + s11_8_cards)

# ── Section 13.1 ────────────────────────────────────────────────────────────
s13_1_concepts = concepts('Key Concepts — Section 13.1 Functions of Two Variables', [
    ('Domain', 'Set of all (x,y) for which f(x,y) is defined (real, finite)'),
    ('Level curves', r'Curves \(f(x,y)=k\) (constant) — cross-sections at height k'),
    ('Graph', r'Surface \(z=f(x,y)\) in 3-space'),
    ('Restrictions', 'Log requires argument > 0; square root requires argument ≥ 0; denominator ≠ 0'),
])

s13_1_cards = (
    card('Q1', r'Domain of \(f(x,y)=\sqrt{x-y}\)', ['domain'],
         'Square root requires non-negative argument.',
         '',
         [r'Need \(x-y\ge 0\), i.e., \(x\ge y\)',
          r'Domain: all points \((x,y)\) on or below the line \(y=x\) in the \(xy\)-plane.'],
         r'\(\{(x,y):x\ge y\}\)')

  + card('Q3', r'Domain of \(f(x,y)=\ln(x^2+y^2-1)\)', ['domain'],
         'Logarithm requires positive argument.',
         '',
         [r'Need \(x^2+y^2-1>0\), i.e., \(x^2+y^2>1\)',
          r'Domain: all points <strong>exterior</strong> to the unit circle.'],
         r'\(\{(x,y):x^2+y^2>1\}\)')

  + card('Q6', r'Domain of \(f(x,y)=\dfrac{x-y}{x+y}\)', ['domain'],
         'Rational function — denominator cannot be zero.',
         '',
         [r'Need \(x+y\ne 0\), i.e., \(y\ne-x\)',
          r'Domain: all \((x,y)\) except the line \(y=-x\).'],
         r'All \((x,y)\) with \(y\ne-x\)')

  + card('Q7', r'Domain of \(f(x,y)=\dfrac{e^{x+y}}{x-y}\)', ['domain'],
         'Exponential is always defined; denominator must be non-zero.',
         '',
         [r'Need \(x-y\ne 0\), i.e., \(x\ne y\)',
          r'Domain: all \((x,y)\) except the line \(y=x\).'],
         r'All \((x,y)\) with \(x\ne y\)')

  + card('Q8', r'Domain of \(f(x,y)=\sin(x/y)\)', ['domain'],
         'Sine is always defined; argument must be valid (denominator ≠ 0).',
         '',
         [r'Need \(y\ne 0\) (division by zero)',
          r'Domain: all \((x,y)\) with \(y\ne 0\) (entire plane except the \(x\)-axis).'],
         r'All \((x,y)\) with \(y\ne 0\)')

  + card('Q18', r'Domain and graph of \(f(x,y)=\sqrt{1-x^2-y^2}\)', ['domain','graph'],
         'Square root ≥ 0; the graph is part of a sphere.',
         '',
         [r'Need \(1-x^2-y^2\ge 0\), i.e., \(x^2+y^2\le 1\): closed unit disk.',
          r'Graph: \(z=\sqrt{1-x^2-y^2}\ge 0\); rearranging: \(x^2+y^2+z^2=1,\ z\ge 0\)',
          r'This is the <strong>upper hemisphere</strong> of the unit sphere.'],
         r'Domain: unit disk \(x^2+y^2\le 1\); graph: upper hemisphere of unit sphere',
         plot3d('Upper hemisphere  z = √(1−x²−y²)',
                _upper_hemisphere_surface()))

  + card('Q19', r'Domain and graph of \(f(x,y)=-\sqrt{x^2+y^2}\)', ['domain','graph'],
         'Square root of a sum of squares — always defined. Negative sign gives lower nappe.',
         '',
         [r'Domain: all \((x,y)\) (no restriction needed, \(x^2+y^2\ge 0\) always).',
          r'Graph: \(z=-\sqrt{x^2+y^2}\le 0\); rewrite: \(z^2=x^2+y^2,\ z\le 0\)',
          r'<strong>Lower nappe of a cone</strong> with vertex at origin, opening downward.'],
         r'Domain: all \((x,y)\); graph: lower nappe of cone \(z^2=x^2+y^2,\,z\le0\)',
         plot3d('Lower cone nappe  z = −√(x²+y²)',
                zfunc_traces(lambda X, Y: -np.sqrt(X**2+Y**2),
                             (-2, 2), (-2, 2))))

  + card('Q20', r'Domain and graph of \(f(x,y)=\sqrt{x^2+y^2}\)', ['domain','graph'],
         'Square root of a sum of squares — always defined.',
         '',
         [r'Domain: all \((x,y)\).',
          r'Graph: \(z=\sqrt{x^2+y^2}\ge 0\); i.e., \(z^2=x^2+y^2,\ z\ge 0\)',
          r'<strong>Upper nappe of a cone</strong> with vertex at origin, opening upward.'],
         r'Domain: all \((x,y)\); graph: upper nappe of cone \(z^2=x^2+y^2,\,z\ge0\)',
         plot3d('Upper cone nappe  z = √(x²+y²)',
                zfunc_traces(lambda X, Y: np.sqrt(X**2+Y**2),
                             (-2, 2), (-2, 2))))

  + card('Q28', r'Level curves of \(f(x,y)=x-2y\) for \(f=k\)', ['level curves'],
         'Set f = k and describe the resulting curves.',
         '',
         [r'\(x-2y=k\) → \(y=\dfrac{x-k}{2}=\dfrac{1}{2}x-\dfrac{k}{2}\)',
          r'Parallel lines with slope \(\tfrac{1}{2}\), y-intercept \(-\tfrac{k}{2}\).',
          r'As \(k\) increases, lines shift downward.'],
         r'Family of parallel lines \(y=\tfrac{1}{2}x-\tfrac{k}{2}\) (slope \(\tfrac{1}{2}\))')

  + card('Q67', r'Describe \(f(x,y)=x^2+y^2\): graph and level curves', ['graph','level curves'],
         'Identify the surface type and the shape of level curves.',
         '',
         [r'Graph: \(z=x^2+y^2\) — <strong>circular paraboloid</strong> opening upward, vertex at origin.',
          r'Level curves: \(x^2+y^2=k\) for \(k\ge 0\) — <strong>circles</strong> centered at origin with radius \(\sqrt{k}\).',
          r'For \(k<0\): no level curve (graph lies above \(xy\)-plane).'],
         r'Graph: circular paraboloid; level curves: concentric circles \(x^2+y^2=k\)',
         plot3d('Circular Paraboloid  z = x²+y²',
                zfunc_traces(lambda X, Y: X**2+Y**2,
                             (-2, 2), (-2, 2))))
)

s13_1 = section('s13_1', '13.1 — Functions of Two Variables', s13_1_concepts + s13_1_cards)

# ── Nav ────────────────────────────────────────────────────────────────────
nav_items = [
    ('10.4 Conics', 's10_4'),
    ('11.1 3D &amp; Spheres', 's11_1'),
    ('11.2 Vectors', 's11_2'),
    ('11.3 Dot Product', 's11_3'),
    ('11.4 Cross Product', 's11_4'),
    ('11.5 Lines', 's11_5'),
    ('11.6 Planes', 's11_6'),
    ('11.7 Quadric Surfaces', 's11_7'),
    ('11.8 Cyl &amp; Sph', 's11_8'),
    ('13.1 Multivariable', 's13_1'),
]

nav_btns = ''.join(
    f'<button class="nav-btn{" active" if i==0 else ""}" data-sec="{sec}">{lbl}</button>'
    for i, (lbl, sec) in enumerate(nav_items)
)

# ── Full HTML ──────────────────────────────────────────────────────────────
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MVC Study Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<script>
window.MathJax = {
  tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']], tags: 'ams' },
  svg: { fontCache: 'global' }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
<script src="https://cdn.plot.ly/plotly-2.26.0.min.js"></script>
<style>
:root {
  --bg: #f8f7f2; --surface: #ffffff; --card: #f0efe8; --border: #d4d0c4;
  --gold: #8b6914; --gold2: #6b4f0f; --text: #1a1a1a; --muted: #6b6b6b;
  --accent: #5a4fb0; --green: #2d7a52; --red: #c0392b; --blue: #2a6fa8;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;font-size:16px;line-height:1.65;min-height:100vh}
a{color:var(--gold);text-decoration:none}
code{font-family:'Space Mono',monospace;font-size:.85em;background:var(--card);padding:.1em .3em;border-radius:3px;color:var(--gold2)}
header{background:var(--surface);border-bottom:2px solid var(--gold);padding:1.5rem 2rem;display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap}
header h1{font-family:'DM Serif Display',serif;font-size:1.9rem;color:var(--gold);letter-spacing:-.01em}
header span{color:var(--muted);font-size:.95rem}
nav{background:var(--surface);border-bottom:1px solid var(--border);padding:.5rem 1rem;display:flex;flex-wrap:wrap;gap:.4rem;position:sticky;top:0;z-index:100}
.nav-btn{background:transparent;border:1px solid var(--border);color:var(--muted);border-radius:6px;padding:.35rem .75rem;cursor:pointer;font-size:.82rem;font-family:'Space Mono',monospace;transition:all .2s}
.nav-btn:hover{border-color:var(--gold);color:var(--gold)}
.nav-btn.active{background:var(--gold);border-color:var(--gold);color:#fff;font-weight:700}
main{max-width:1100px;margin:0 auto;padding:2rem 1.5rem}
.section{display:none}
.section.active{display:block}
.concepts-box{background:var(--card);border:1px solid var(--border);border-left:4px solid var(--gold);border-radius:10px;margin-bottom:2rem;overflow:hidden}
.concepts-toggle{width:100%;background:none;border:none;color:var(--gold2);font-family:'DM Serif Display',serif;font-size:1.15rem;padding:1rem 1.25rem;display:flex;align-items:center;justify-content:space-between;cursor:pointer;text-align:left}
.concepts-toggle::after{content:'▾';font-size:1.2rem;transition:transform .25s}
.concepts-toggle.collapsed::after{transform:rotate(-90deg)}
.concepts-body{padding:1rem 1.5rem 1.25rem;display:grid;gap:.6rem}
.concepts-body.hidden{display:none}
.concept-item{display:flex;gap:.75rem;align-items:flex-start;padding:.5rem .75rem;background:var(--surface);border-radius:6px;border:1px solid var(--border)}
.concept-label{color:var(--gold);font-weight:600;min-width:110px;font-size:.88rem;font-family:'Space Mono',monospace}
.concept-desc{color:var(--text);font-size:.9rem;line-height:1.6}
.concept-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:.5rem}
.problems-header{font-family:'DM Serif Display',serif;font-size:1.4rem;color:var(--gold);margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)}
.problem-card{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:1.5rem;overflow:hidden}
.problem-header{background:var(--surface);padding:.75rem 1.25rem;display:flex;align-items:center;gap:.75rem;border-bottom:1px solid var(--border)}
.problem-num{background:var(--gold);color:#fff;border-radius:50%;width:32px;height:32px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.85rem;font-family:'Space Mono',monospace;flex-shrink:0}
.problem-q{color:var(--text);font-size:.95rem;line-height:1.5}
.problem-tags{margin-left:auto;display:flex;gap:.3rem}
.tag{background:var(--border);color:var(--muted);border-radius:4px;padding:.15rem .5rem;font-size:.75rem;font-family:'Space Mono',monospace}
.solution{padding:1.25rem 1.5rem}
.sol-overview{color:var(--muted);font-size:.9rem;margin-bottom:1rem;padding:.6rem 1rem;background:#f5f4ee;border-left:3px solid var(--accent);border-radius:0 6px 6px 0}
.key-formula{color:var(--gold2);font-size:.95rem;margin-bottom:1rem;padding:.5rem 1rem;background:#fdf9ee;border:1px solid #c8a84c;border-radius:6px}
.key-formula strong{color:var(--gold);margin-right:.5rem}
.sol-steps{display:flex;flex-direction:column;gap:.75rem;margin-bottom:1rem}
.step{display:flex;gap:.75rem;align-items:flex-start}
.step-n{background:var(--accent);color:#fff;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;flex-shrink:0;margin-top:.1rem;font-family:'Space Mono',monospace}
.step-body{color:var(--text);font-size:.93rem;line-height:1.65;flex:1}
.step-body .sub{padding:.4rem .75rem;background:var(--surface);border-radius:5px;margin:.4rem 0;display:block}
.sol-answer{background:#fffdf0;border:1px solid var(--gold);border-radius:8px;padding:.75rem 1.25rem;color:var(--gold2);font-size:.95rem}
.sol-answer strong{color:var(--gold);margin-right:.5rem}
.part-label{font-family:'Space Mono',monospace;color:var(--gold);font-weight:700;margin:.75rem 0 .25rem;font-size:.88rem}
.divider{border:none;border-top:1px solid var(--border);margin:.75rem 0}
.graph-wrap{background:var(--card);border-radius:8px;margin:1rem 0;overflow:hidden}
.graph-title{background:var(--surface);color:var(--muted);font-size:.8rem;padding:.4rem .75rem;font-family:'Space Mono',monospace;border-bottom:1px solid var(--border)}
</style>
</head>
<body>
<header>
  <h1>MVC Study Guide</h1>
  <span>Multivariable Calculus — Sections 10.4 · 11.1–11.8 · 13.1</span>
</header>
<nav>
""" + nav_btns + r"""
</nav>
<main>
""" + s10_4 + s11_1 + s11_2 + s11_3 + s11_4 + s11_5 + s11_6 + s11_7 + s11_8 + s13_1 + r"""
</main>
<script>
function initPlots(sec) {
  sec.querySelectorAll('script[data-for]').forEach(s => {
    const id = s.dataset.for;
    const el = document.getElementById(id);
    if (el && !el.dataset.plotted) {
      const d = JSON.parse(s.textContent);
      Plotly.newPlot(el, d.traces, d.layout, {responsive: true, displayModeBar: false});
      el.dataset.plotted = '1';
    }
  });
}
document.querySelectorAll('.nav-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    btn.classList.add('active');
    const sec = document.getElementById(btn.dataset.sec);
    sec.classList.add('active');
    initPlots(sec);
    if (window.MathJax) MathJax.typesetPromise();
  });
});
document.querySelectorAll('.concepts-toggle').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.classList.toggle('collapsed');
    btn.nextElementSibling.classList.toggle('hidden');
  });
});
initPlots(document.querySelector('.section.active'));
if (window.MathJax) MathJax.typesetPromise();
</script>
</body>
</html>"""

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written {len(html):,} chars ({len(html.encode('utf-8')):,} bytes) to {PATH}")
