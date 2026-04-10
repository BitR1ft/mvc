![[WhatsApp Image 2026-04-10 at 11.53.22 AM.jpeg]]

# Chapter 11: Three-Dimensional Space & Vectors — Complete Tutor Notes

This is a comprehensive guide. I'll teach each section with theory, examples, and then solve every assigned question with the best/shortest exam approach.

---

# SECTION 11.1: Rectangular Coordinates in 3-Space; Spheres; Cylindrical Surfaces

## Key Concepts

**3D Coordinate System:** Three mutually perpendicular axes (x, y, z) create 8 octants. A point is P(a, b, c).

**Distance Formula:** Between P₁(x₁,y₁,z₁) and P₂(x₂,y₂,z₂): $$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$$

**Sphere Equation:** Center (x₀,y₀,z₀), radius r: $$(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2 = r^2$$

**General form:** x² + y² + z² + Gx + Hy + Iz + J = 0 → complete the square to identify center/radius.

- k > 0: sphere; k = 0: single point; k < 0: no graph

**Cylindrical Surfaces:** An equation missing one variable creates a surface by extruding that curve parallel to the missing variable's axis. Example: y = x² in 3-space is a parabolic cylinder extending along z-axis.

---

## Solutions — Section 11.1

**Q9.** _Find the center and radius of the sphere with diameter endpoints (1,−2,4) and (3,4,−12)._

**Approach:** Center = midpoint, radius = half the distance.

$$\text{Center} = \left(\frac{1+3}{2}, \frac{-2+4}{2}, \frac{4-12}{2}\right) = (2, 1, -4)$$

$$d = \sqrt{(3-1)^2+(4+2)^2+(-12-4)^2} = \sqrt{4+36+256} = \sqrt{296}$$

$$r = \frac{\sqrt{296}}{2} = \frac{2\sqrt{74}}{2} = \sqrt{74}$$

$$\boxed{(x-2)^2 + (y-1)^2 + (z+4)^2 = 74}$$

---

**Q11.** _(a) Show (2,1,6), (4,7,9), (8,5,−6) are vertices of a right triangle. (b) Which vertex has the 90° angle? (c) Find area._

**Approach:** Compute all three side lengths. If a²+b²=c², it's a right triangle.

Let A=(2,1,6), B=(4,7,9), C=(8,5,−6).

$$AB = \sqrt{4+36+9} = 7$$ $$AC = \sqrt{36+16+144} = 14$$ $$BC = \sqrt{16+4+225} = \sqrt{245} = 7\sqrt{5}$$

Check: AB² + AC² = 49 + 196 = 245 = BC² ✓ → **Right angle at A**

$$\text{Area} = \frac{1}{2}(AB)(AC) = \frac{1}{2}(7)(14) = \boxed{49}$$

---

**Q13.** _Find standard equation of each sphere._

**(a)** Center (7,1,1), r = 4: $$(x-7)^2 + (y-1)^2 + (z-1)^2 = 16$$

**(b)** Center (1,0,−1), diameter = 8 → r = 4: $$(x-1)^2 + y^2 + (z+1)^2 = 16$$

**(c)** Center (−1,3,2), passing through origin. First find r: $$r = \sqrt{(-1)^2+3^2+2^2} = \sqrt{14}$$ $$(x+1)^2 + (y-3)^2 + (z-2)^2 = 14$$

**(d)** Diameter endpoints (−1,2,1) and (0,2,3): $$\text{Center} = \left(-\frac{1}{2}, 2, 2\right), \quad r = \frac{1}{2}\sqrt{1+0+4} = \frac{\sqrt{5}}{2}$$ $$\left(x+\frac{1}{2}\right)^2 + (y-2)^2 + (z-2)^2 = \frac{5}{4}$$

---

**Q14.** _Find equations of two spheres centered at origin, tangent to sphere of radius 1 centered at (3,−2,4)._

**Approach:** Distance from origin to center (3,−2,4) = √(9+4+16) = √29.

A sphere of radius R centered at origin is tangent to the given sphere when:

- **External tangency:** R + 1 = √29 → R = √29 − 1
- **Internal tangency:** |R − 1| = √29 → R = √29 + 1

$$\boxed{x^2+y^2+z^2 = (\sqrt{29}-1)^2} \quad \text{and} \quad \boxed{x^2+y^2+z^2 = (\sqrt{29}+1)^2}$$

---

**Q15.** _Find equation of sphere with center (2,−1,−3) satisfying:_

**(a)** Tangent to xy-plane: r = |z-coordinate| = 3 $$(x-2)^2+(y+1)^2+(z+3)^2=9$$

**(b)** Tangent to xz-plane: r = |y-coordinate| = 1 $$(x-2)^2+(y+1)^2+(z+3)^2=1$$

**(c)** Tangent to yz-plane: r = |x-coordinate| = 2 $$(x-2)^2+(y+1)^2+(z+3)^2=4$$

---

**Q18.** _Sphere with center in first octant, tangent to all three coordinate planes. Distance from origin = 3−√3. Find equation._

**Key insight:** If tangent to all three coordinate planes and center in first octant, center = (r,r,r).

Distance from origin to sphere surface = distance to center − radius: $$\sqrt{r^2+r^2+r^2} - r = 3-\sqrt{3}$$ $$r\sqrt{3} - r = 3-\sqrt{3}$$ $$r(\sqrt{3}-1) = \sqrt{3}(\sqrt{3}-1)$$ $$r = \sqrt{3}$$

$$\boxed{(x-\sqrt{3})^2+(y-\sqrt{3})^2+(z-\sqrt{3})^2=3}$$

---

**Q27–Q28:** _Describe surfaces (by completing the square)._

**Q27.** x² + y² + z² − 3x + 4y − 8z + 25 = 0

$$\left(x-\frac{3}{2}\right)^2 + (y+2)^2 + (z-4)^2 = \frac{9}{4}+4+16-25 = \frac{9}{4}-5 = -\frac{11}{4}$$

Since k < 0: **No graph.**

**Q28.** x² + y² + z² − 2x − 6y − 8z + 1 = 0

$$(x-1)^2+(y-3)^2+(z-4)^2 = 1+9+16-1 = 25$$

**Sphere**, center (1,3,4), radius 5.

**Q29.** Sketch portions of surfaces in first octant:

**(a)** y = x: plane containing z-axis, at 45° to xz and yz planes. **(b)** y = z: plane containing x-axis, at 45° to xy and xz planes. **(c)** x = z: plane containing y-axis, at 45° to xy and yz planes.

**Q30.** Graphs in 3-space:

**(a)** x = 1: plane parallel to yz-plane **(b)** y = 1: plane parallel to xz-plane **(c)** z = 1: plane parallel to xy-plane

**Q31.** Graphs in 3-space (missing variable = cylinder along that axis):

**(a)** x² + y² = 25: **circular cylinder** of radius 5, axis along z-axis **(b)** y² + z² = 25: **circular cylinder** of radius 5, axis along x-axis **(c)** x² + z² = 25: **circular cylinder** of radius 5, axis along y-axis

**Q32.**

**(a)** x = y²: parabolic cylinder, extends along z-axis, opens in +x direction **(b)** z = x²: parabolic cylinder, extends along y-axis, opens in +z direction **(c)** y = z²: parabolic cylinder, extends along x-axis, opens in +y direction

**Q33.** Write equations for surfaces:

**(a)** Contains x-axis and point (0,1,2): Normal = cross product of direction along x-axis (1,0,0) and vector to point (0,1,2): **n = (1,0,0)×(0,1,2) = (0·2−0·1, 0·0−1·2, 1·1−0·0) = (0,−2,1)**. Plane: −2y + z = 0, i.e., **z = 2y**

**(b)** Contains y-axis and (1,0,2): Similarly **z = 2x**

**(c)** Cylinder radius 1, centered on z-line through (1,1,0): $$(x-1)^2+(y-1)^2=1$$

**(d)** Cylinder radius 1, centered on y-line through (1,0,1): $$(x-1)^2+(z-1)^2=1$$

---

**Q47.** _Bug walks on sphere x² + y² + z² + 2x − 2y − 4z − 3 = 0. How close/far from origin?_

Complete the square: $$(x+1)^2+(y-1)^2+(z-2)^2 = 3+1+1+4 = 9$$

Center (−1,1,2), radius 3. Distance from origin to center: $$d = \sqrt{1+1+4} = \sqrt{6}$$

- **Closest:** √6 − 3
- **Farthest:** √6 + 3

---

# SECTION 11.2: Vectors

## Key Concepts

**Component form:** v = ⟨v₁,v₂,v₃⟩

**Operations:**

- v + w = ⟨v₁+w₁, v₂+w₂, v₃+w₃⟩
- kv = ⟨kv₁, kv₂, kv₃⟩

**Vector from P₁ to P₂:** ⟨x₂−x₁, y₂−y₁, z₂−z₁⟩

**Norm (length):** ‖v‖ = √(v₁²+v₂²+v₃²)

**Unit vector:** u = v/‖v‖

**Trigonometric form:** v = ‖v‖⟨cos θ, sin θ⟩ in 2D

**Scalar multiple rule:** ‖kv‖ = |k|‖v‖

---

## Solutions — Section 11.2

**Q7.** _Find components of vector P₁P₂._

**(a)** P₁(3,5), P₂(2,8): ⟨2−3, 8−5⟩ = **⟨−1, 3⟩**

**(b)** P₁(7,−2), P₂(0,0): ⟨0−7, 0+2⟩ = **⟨−7, 2⟩**

**(c)** P₁(5,−2,1), P₂(2,4,2): **⟨−3, 6, 1⟩**

---

**Q9.**

**(a)** Terminal point of v = 3i−2j with initial point (1,−2): $$(1+3, -2-2) = \boxed{(4,-4)}$$

**(b)** Initial point of v = ⟨−3,1,2⟩ if terminal = (5,0,−1): $$\text{Initial} = (5-(-3), 0-1, -1-2) = \boxed{(8,-1,-3)}$$

---

**Q15.** u = i−3j+2k, v = i+j, w = 2i+2j−4k.

**(a)** u + v = ⟨2,−2,2⟩

**(b)** ‖u+v‖ = √(4+4+4) = **2√3**

**(c)** −2u + 2v = ⟨−2+2, 6+2, −4+0⟩ = **⟨0, 8, −4⟩**

**(d)** 3u − 5v + w = ⟨3−5+2, −9−5+2, 6+0−4⟩ = **⟨0, −12, 2⟩**

**(e)** (1/‖w‖)w: ‖w‖ = √(4+4+16) = √24 = 2√6. Unit vector = **⟨1/√6, 1/√6, −2/√6⟩**

**(f)** ‖(1/‖w‖)w‖ = 1 (it's a unit vector)

---

**Q23.** _Find vectors satisfying conditions._

**(a)** Oppositely directed to v = ⟨3,−4⟩, half the length: ‖v‖ = 5, half = 5/2, opposite direction: $$\text{Unit opposite} = \frac{1}{5}\langle-3,4\rangle, \quad \text{result} = \frac{5}{2}\cdot\frac{1}{5}\langle-3,4\rangle = \boxed{\left\langle-\frac{3}{2}, 2\right\rangle}$$

**(b)** Length √17, same direction as v = ⟨7,0,−6⟩: ‖v‖ = √(49+36) = √85

$$\text{Unit} = \frac{1}{\sqrt{85}}\langle7,0,-6\rangle, \quad \text{result} = \sqrt{17}\cdot\frac{1}{\sqrt{85}}\langle7,0,-6\rangle = \frac{1}{\sqrt{5}}\langle7,0,-6\rangle = \boxed{\left\langle\frac{7}{\sqrt{5}},0,\frac{-6}{\sqrt{5}}\right\rangle}$$

---

**Q24.**

**(a)** Same direction as v = −2i+3j, three times the length: **3v = ⟨−6, 9⟩**

**(b)** Length 2, opposite to v = −3i+4j+k: ‖v‖ = √(9+16+1) = √26

$$\text{result} = \frac{2}{\sqrt{26}}\langle3,-4,-1\rangle = \boxed{\left\langle\frac{6}{\sqrt{26}},\frac{-8}{\sqrt{26}},\frac{-2}{\sqrt{26}}\right\rangle}$$

---

**Q25.** _Component form of v with given length and angle θ with positive x-axis. Use v = ‖v‖⟨cos θ, sin θ⟩._

**(a)** ‖v‖=3, θ=π/4: **⟨3cos(π/4), 3sin(π/4)⟩ = ⟨3/√2, 3/√2⟩**

**(b)** ‖v‖=2, θ=90°: **⟨0, 2⟩**

**(c)** ‖v‖=5, θ=120°: **⟨5cos120°, 5sin120°⟩ = ⟨−5/2, 5√3/2⟩**

**(d)** ‖v‖=1, θ=π: **⟨−1, 0⟩**

---

**Q26.** _v+w and v−w where ‖v‖=‖w‖=1, v makes π/6 with x-axis, w makes 3π/4._

$$\mathbf{v} = \langle\cos(\pi/6),\sin(\pi/6)\rangle = \langle\tfrac{\sqrt3}{2},\tfrac{1}{2}\rangle$$ $$\mathbf{w} = \langle\cos(3\pi/4),\sin(3\pi/4)\rangle = \langle-\tfrac{\sqrt2}{2},\tfrac{\sqrt2}{2}\rangle$$

$$\mathbf{v+w} = \left\langle\frac{\sqrt3-\sqrt2}{2},\ \frac{1+\sqrt2}{2}\right\rangle, \quad \mathbf{v-w} = \left\langle\frac{\sqrt3+\sqrt2}{2},\ \frac{1-\sqrt2}{2}\right\rangle$$

---

**Q34.** _Find u and v if u+v = ⟨2,−3⟩ and 3u+2v = ⟨−1,2⟩._

From first equation: u = ⟨2,−3⟩ − v. Substitute: $$3(\langle2,-3\rangle - \mathbf{v}) + 2\mathbf{v} = \langle-1,2\rangle$$ $$\langle6,-9\rangle - \mathbf{v} = \langle-1,2\rangle$$ $$\mathbf{v} = \langle7,-11\rangle, \quad \mathbf{u} = \langle2,-3\rangle-\langle7,-11\rangle = \boxed{\langle-5,8\rangle}$$

---

**Q35.** _Find lengths of diagonals of parallelogram with adjacent sides i+j and i−2j._

The diagonals are **(i+j)+(i−2j) = 2i−j** and **(i+j)−(i−2j) = 3j**

$$\text{Diagonal 1: }|2\mathbf{i}-\mathbf{j}| = \sqrt{5}, \quad \text{Diagonal 2: }|3\mathbf{j}| = 3$$

---

**Q36.** _Fourth vertex of parallelogram with three vertices (0,0), (1,3), (2,4)._

**Approach:** In a parallelogram ABCD, D = A + C − B (using vector addition).

With A=(0,0), B=(1,3), C=(2,4):

- D = A + AC = (0,0)+(2,4) = **(2,4)** — wait, this is C itself. Try different assignments:

If sides are AB and AC, then D = B + C − A = (1+2−0, 3+4−0) = **(3,7)** If sides are AB and BC, then D = A + C − B... actually there are 3 possible parallelograms:

Using (0,0)=A, (1,3)=B, (2,4)=C:

- 4th vertex = B + C − A = **(3,7)**
- Or: A + C − B = **(1,1)**
- Or: A + B − C = **(−1,−1)**

---

**Q40.** _Find two unit vectors in 3-space perpendicular to each coordinate plane._

**(a)** Perpendicular to xy-plane: **±k = ⟨0,0,±1⟩**

**(b)** Perpendicular to xz-plane: **±j = ⟨0,±1,0⟩**

**(c)** Perpendicular to yz-plane: **±i = ⟨±1,0,0⟩**

---

# SECTION 11.3: Dot Product; Projections

## Key Concepts

**Dot Product:** u·v = u₁v₁ + u₂v₂ + u₃v₃ (scalar result)

**Angle formula:** cos θ = (u·v)/(‖u‖‖v‖), so **u·v = ‖u‖‖v‖cos θ**

**Sign interpretation:**

- u·v > 0 → acute angle
- u·v = 0 → perpendicular (orthogonal)
- u·v < 0 → obtuse angle

**Direction cosines:** cos α = v₁/‖v‖, cos β = v₂/‖v‖, cos γ = v₃/‖v‖; and cos²α+cos²β+cos²γ = 1

**Orthogonal Projection of v onto b:** $$\text{proj}_{\mathbf{b}}\mathbf{v} = \frac{\mathbf{v}\cdot\mathbf{b}}{|\mathbf{b}|^2}\mathbf{b}$$

**Vector component of v orthogonal to b:** v − projᵦv

**Work:** W = F·d (dot product of force and displacement vectors)

---

## Solutions — Section 11.3

**Q13.** _Find r so that vector from A(1,−1,3) to B(3,0,5) is orthogonal to vector from A to P(r,r,r)._

$$\overrightarrow{AB} = \langle2,1,2\rangle, \quad \overrightarrow{AP} = \langle r-1, r+1, r-3\rangle$$

For orthogonality, AB·AP = 0: $$2(r-1)+1(r+1)+2(r-3) = 0$$ $$2r-2+r+1+2r-6 = 0$$ $$5r-7=0 \implies \boxed{r = \frac{7}{5}}$$

---

**Q14.** _Find two unit vectors in 2-space making 45° angle with 4i+3j._

‖4i+3j‖ = 5, so unit vector along it: u = ⟨4/5, 3/5⟩

A unit vector making 45° with u satisfies cos 45° = a·(4/5) + b·(3/5) = 1/√2 with a²+b²=1.

Let the unit vector be ⟨cos θ, sin θ⟩. Then the angle between it and ⟨4/5,3/5⟩ is 45°. The direction of ⟨4/5,3/5⟩ is α = arctan(3/4). So the two vectors make angles α+45° and α−45° with x-axis:

$$\alpha = \arctan(3/4) \approx 36.87°$$

**Vector 1** (θ = α+45° ≈ 81.87°): ⟨cos81.87°, sin81.87°⟩ = **⟨1/5√2, 7/5√2⟩**

More precisely: ⟨cos(α+45°), sin(α+45°)⟩ = ⟨cosα·cos45°−sinα·sin45°, sinα·cos45°+cosα·sin45°⟩ = 1/√2⟨4/5−3/5, 3/5+4/5⟩ = **⟨1/(5√2), 7/(5√2)⟩**

**Vector 2** (θ = α−45°): = 1/√2⟨4/5+3/5, 3/5−4/5⟩ = **⟨7/(5√2), −1/(5√2)⟩**

---

**Q25.** _Find vector component of v along b and orthogonal to b._

**(a)** v = 2i−j+3k, b = i+2j+2k; ‖b‖² = 9

$$\mathbf{v}\cdot\mathbf{b} = 2-2+6 = 6$$ $$\text{proj}_\mathbf{b}\mathbf{v} = \frac{6}{9}(i+2j+2k) = \frac{2}{3}i+\frac{4}{3}j+\frac{4}{3}k$$ $$\mathbf{v}-\text{proj}_\mathbf{b}\mathbf{v} = \left(2-\frac{2}{3}\right)i+\left(-1-\frac{4}{3}\right)j+\left(3-\frac{4}{3}\right)k = \frac{4}{3}i-\frac{7}{3}j+\frac{5}{3}k$$

**(b)** v = ⟨4,−1,7⟩, b = ⟨2,3,−6⟩; ‖b‖² = 4+9+36 = 49

$$\mathbf{v}\cdot\mathbf{b} = 8-3-42 = -37$$ $$\text{proj}_\mathbf{b}\mathbf{v} = \frac{-37}{49}\langle2,3,-6\rangle = \left\langle\frac{-74}{49},\frac{-111}{49},\frac{222}{49}\right\rangle$$ $$\mathbf{v}-\text{proj}_\mathbf{b}\mathbf{v} = \left\langle\frac{270}{49},\frac{46}{49},\frac{121}{49}\right\rangle$$

---

**Q27.** _Express v as sum of vector parallel and orthogonal to b._

**(a)** v = ⟨−3,5⟩, b = ⟨1,1⟩; ‖b‖²=2, v·b=2

$$\text{proj}_\mathbf{b}\mathbf{v} = \frac{2}{2}\langle1,1\rangle = \langle1,1\rangle$$ $$\mathbf{v} = \underbrace{\langle1,1\rangle}_{\parallel\mathbf{b}} + \underbrace{\langle-4,4\rangle}_{\perp\mathbf{b}}$$

**(b)** v = ⟨−2,1,6⟩, b = ⟨0,−2,1⟩; ‖b‖²=5, v·b=−2+6=4

$$\text{proj}_\mathbf{b}\mathbf{v} = \frac{4}{5}\langle0,-2,1\rangle = \langle0,-8/5,4/5\rangle$$ $$\mathbf{v} = \langle0,-8/5,4/5\rangle + \langle-2,13/5,26/5\rangle$$

**(c)** v = ⟨1,4,1⟩, b = ⟨3,−2,5⟩; ‖b‖²=38, v·b=3−8+5=0

Since v·b = 0, v is already **orthogonal to b**, so: $$\mathbf{v} = \underbrace{\langle0,0,0\rangle}_{\parallel\mathbf{b}} + \underbrace{\langle1,4,1\rangle}_{\perp\mathbf{b}}$$

---

**Q35.** _Work done by F = −3j lb from (1,3) to (4,7). Distance in feet._

$$\overrightarrow{PQ} = \langle3,4\rangle, \quad W = \mathbf{F}\cdot\overrightarrow{PQ} = (0)(3)+(-3)(4) = \boxed{-12 \text{ ft·lb}}$$

(Negative work: force opposes motion component.)

---

**Q36.** _Slide 4m long, child slides top to bottom, gravity does how much work? (From Q34 setup: 34kg, 27° incline)_

Weight = mg = 34 × 9.8 = 333.2 N downward = ⟨0, −333.2⟩

Displacement vector along ramp (4m at 27° below horizontal): d = ⟨4cos27°, −4sin27°⟩

$$W = \mathbf{F}\cdot\mathbf{d} = (0)(4\cos27°)+(-333.2)(-4\sin27°) = 333.2\times4\sin27° \approx 333.2\times1.814 \approx \boxed{604.7 \text{ J}}$$

---

# SECTION 11.4: Cross Product

## Key Concepts

**Cross Product (3×3 determinant mnemonic):** $$\mathbf{u}\times\mathbf{v} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\u_1&u_2&u_3\v_1&v_2&v_3\end{vmatrix} = (u_2v_3-u_3v_2)\mathbf{i}-(u_1v_3-u_3v_1)\mathbf{j}+(u_1v_2-u_2v_1)\mathbf{k}$$

**Key properties:**

- u×v = −(v×u) (anti-commutative)
- u×v is orthogonal to BOTH u and v
- ‖u×v‖ = ‖u‖‖v‖sin θ
- u×v = 0 iff u and v are parallel
- **Area of parallelogram** = ‖u×v‖
- **Area of triangle** = ½‖u×v‖

**Scalar Triple Product:** $$\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w}) = \begin{vmatrix}u_1&u_2&u_3\v_1&v_2&v_3\w_1&w_2&w_3\end{vmatrix}$$ **Volume of parallelepiped** = |u·(v×w)|

---

## Solutions — Section 11.4

**Q5.** u = ⟨0,1,−2⟩, v = ⟨3,0,−4⟩

$$\mathbf{u}\times\mathbf{v} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\0&1&-2\3&0&-4\end{vmatrix}$$ $$= [(1)(-4)-(-2)(0)]\mathbf{i} - [(0)(-4)-(-2)(3)]\mathbf{j} + [(0)(0)-(1)(3)]\mathbf{k}$$ $$= -4\mathbf{i} - 6\mathbf{j} - 3\mathbf{k}$$

**Verify orthogonality:** u·(u×v) = (0)(−4)+(1)(−6)+(−2)(−3) = 0−6+6 = 0 ✓

---

**Q9.** _Find direction cosines of u×v for vectors from figure (u and v both from origin to (1,1,1), appearing to be unit vectors along edges)._

From the figure: u = i+j (along face), v = i+k (along another edge) — using u = ⟨1,1,0⟩, v = ⟨1,0,1⟩

$$\mathbf{u}\times\mathbf{v} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\1&1&0\1&0&1\end{vmatrix} = (1)\mathbf{i}-(1)\mathbf{j}+(-1)\mathbf{k} = \langle1,-1,-1\rangle$$

$$|\mathbf{u}\times\mathbf{v}| = \sqrt{3}$$

Direction cosines: **cos α = 1/√3, cos β = −1/√3, cos γ = −1/√3**

---

**Q10.** _Find two unit vectors orthogonal to both u = −7i+3j+k and v = 2i+4k._

$$\mathbf{u}\times\mathbf{v} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\-7&3&1\2&0&4\end{vmatrix} = (12-0)\mathbf{i}-(−28-2)\mathbf{j}+(0-6)\mathbf{k} = \langle12,30,-6\rangle$$

$$|\langle12,30,-6\rangle| = \sqrt{144+900+36} = \sqrt{1080} = 6\sqrt{30}$$

Two unit vectors: $\pm\frac{1}{6\sqrt{30}}\langle12,30,-6\rangle = \pm\frac{1}{\sqrt{30}}\langle2,5,-1\rangle$

---

**Q11.** _Find two unit vectors normal to plane through A(0,−2,1), B(1,−1,−2), C(−1,1,0)._

$$\overrightarrow{AB} = \langle1,1,-3\rangle, \quad \overrightarrow{AC} = \langle-1,3,-1\rangle$$

$$\overrightarrow{AB}\times\overrightarrow{AC} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\1&1&-3\-1&3&-1\end{vmatrix} = (−1+9)\mathbf{i}−(−1−3)\mathbf{j}+(3+1)\mathbf{k} = \langle8,4,4\rangle = 4\langle2,1,1\rangle$$

$$|\langle2,1,1\rangle| = \sqrt{6}$$

Unit normals: $\boxed{\pm\frac{1}{\sqrt{6}}\langle2,1,1\rangle}$

---

**Q12.** _Find two unit vectors parallel to yz-plane and orthogonal to 3i−j+2k._

Parallel to yz-plane means **x-component = 0**, so vector has form ⟨0, b, c⟩. Orthogonal to 3i−j+2k: 0(3) + b(−1) + c(2) = 0 → −b + 2c = 0 → b = 2c

With b²+c²=1: 4c²+c²=1 → c=±1/√5, b=±2/√5

$$\boxed{\pm\left\langle0, \frac{2}{\sqrt{5}}, \frac{1}{\sqrt{5}}\right\rangle}$$

---

**Q19.** _Area of triangle P(1,5,−2), Q(0,0,0), R(3,5,1)._

$$\overrightarrow{QP} = \langle1,5,-2\rangle, \quad \overrightarrow{QR} = \langle3,5,1\rangle$$

$$\overrightarrow{QP}\times\overrightarrow{QR} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\1&5&-2\3&5&1\end{vmatrix} = (5+10)\mathbf{i}-(1+6)\mathbf{j}+(5-15)\mathbf{k} = \langle15,-7,-10\rangle$$

$$\text{Area} = \frac{1}{2}|\langle15,-7,-10\rangle| = \frac{1}{2}\sqrt{225+49+100} = \frac{1}{2}\sqrt{374} = \boxed{\frac{\sqrt{374}}{2}}$$

---

**Q23.** _Find u·(v×w):_ u = ⟨2,1,0⟩, v = ⟨1,−3,1⟩, w = ⟨4,0,1⟩

$$\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w}) = \begin{vmatrix}2&1&0\1&-3&1\4&0&1\end{vmatrix}$$ $$= 2\begin{vmatrix}-3&1\0&1\end{vmatrix}-1\begin{vmatrix}1&1\4&1\end{vmatrix}+0 = 2(-3)-1(1-4) = -6+3 = \boxed{-3}$$

---

**Q28.** _Given u·(v×w) = 3, find:_

Using the property that scalar triple product is invariant under cyclic permutations and changes sign when two vectors swap:

**(a)** u·(w×v) = −u·(v×w) = **−3**

**(b)** (v×w)·u = u·(v×w) = **3**

**(c)** w·(u×v) = u·(v×w) = **3** (cyclic permutation)

**(d)** v·(u×w) = −v·(w×u) = −u·(v×w) = **−3**

**(e)** (u×w)·v = v·(u×w) = **−3**

**(f)** v·(w×w) = v·**0** = **0** (cross product of vector with itself is zero)

---

**Q29.** u = 3i+2j+k, v = i+j+2k, w = i+3j+3k

**(a) Volume:** $$\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w}) = \begin{vmatrix}3&2&1\1&1&2\1&3&3\end{vmatrix} = 3(3-6)-2(3-2)+1(3-1) = -9-2+2 = \boxed{-9}$$

Volume = |−9| = **9**

**(b) Area of face determined by u and w:** $$\mathbf{u}\times\mathbf{w} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\3&2&1\1&3&3\end{vmatrix} = (6-3)\mathbf{i}-(9-1)\mathbf{j}+(9-2)\mathbf{k} = \langle3,-8,7\rangle$$ $$\text{Area} = |\langle3,-8,7\rangle| = \sqrt{9+64+49} = \sqrt{122}$$

**(c) Angle between u and face determined by v and w:**

First find normal to face: n = v×w = ⟨3-6, 2-3, 3-1⟩ = ⟨−3,−1,2⟩

The angle φ between u and the **plane** is the complement of the angle between u and n: $$\sin\phi = \frac{|\mathbf{u}\cdot\mathbf{n}|}{|\mathbf{u}||\mathbf{n}|} = \frac{|-9+(-2)+2|}{\sqrt{14}\cdot\sqrt{14}} = \frac{9}{14}$$ $$\phi = \sin^{-1}(9/14) \approx 40°$$

---

# SECTION 11.5: Parametric Equations of Lines

## Key Concepts

**Parametric form:** Line through P₀(x₀,y₀,z₀) parallel to v = ⟨a,b,c⟩: $$x = x_0+at,\quad y = y_0+bt,\quad z = z_0+ct$$

**Vector form:** **r** = **r₀** + t**v**

**Line segment from P₁ to P₂:** Use P₁ as base, direction = P₁P₂, restrict **0 ≤ t ≤ 1**

**Symmetric equations** (when a,b,c all nonzero): $$\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}$$

**Skew lines:** Not parallel, do not intersect.

**Parallel lines:** Direction vectors are scalar multiples.

---

## Solutions — Section 11.5

**Q4.** _Find parametric equations for line through P₁, P₂, and for the segment._

**(a)** P₁(0,1), P₂(−3,−4): Direction = ⟨−3,−5⟩

Line: x = −3t, y = 1−5t

Segment: x = −3t, y = 1−5t, **0 ≤ t ≤ 1**

**(b)** P₁(−1,3,5), P₂(−1,3,2): Direction = ⟨0,0,−3⟩

Line: x = −1, y = 3, z = 5−3t

Segment: x = −1, y = 3, z = 5−3t, **0 ≤ t ≤ 1**

---

**Q7.** _Find point P on line and vector v parallel to line._

**(a)** x,y = (2i−j) + t(4i−j): **P(2,−1)**, **v = 4i−j = ⟨4,−1⟩**

**(b)** ⟨x,y,z⟩ = ⟨−1,2,4⟩ + t⟨5,7,−8⟩: **P(−1,2,4)**, **v = ⟨5,7,−8⟩**

---

**Q17.** _Line tangent to circle x²+y²=25 at (3,−4)._

The radius to (3,−4) is in direction ⟨3,−4⟩. The tangent is **perpendicular** to this, so direction v = ⟨4,3⟩ (rotate 90°).

$$x = 3+4t, \quad y = -4+3t$$

---

**Q18.** _Tangent to y = x² at (−2,4)._

dy/dx = 2x = −4 at x=−2. Slope = −4, direction v = ⟨1,−4⟩.

$$x = -2+t, \quad y = 4-4t$$

---

**Q19.** Line through (−1,2,4), parallel to 3i−4j+k: $$x = -1+3t,\quad y = 2-4t,\quad z = 4+t$$

**Q20.** Line through (2,−1,5), parallel to ⟨−1,2,7⟩: $$x = 2-t,\quad y = -1+2t,\quad z = 5+7t$$

**Q21.** Line through (−2,0,5), parallel to x=1+2t,y=4−t,z=6+2t (direction ⟨2,−1,2⟩): $$x = -2+2t,\quad y = -t,\quad z = 5+2t$$

**Q22.** Line through origin, parallel to x=t, y=−1+t, z=2 (direction ⟨1,1,0⟩): $$x = t,\quad y = t,\quad z = 0$$

---

**Q25.** _Find intersections of x=−2, y=4+2t, z=−3+t with coordinate planes._

- **xy-plane** (z=0): −3+t=0 → t=3: point **(−2, 10, 0)**
- **xz-plane** (y=0): 4+2t=0 → t=−2: point **(−2, 0, −5)**
- **yz-plane** (x=0): x=−2 always, so **no intersection** (line is parallel to yz-plane)

---

**Q31.** _Show L₁ and L₂ are skew._

L₁: x=1+7t, y=3+t, z=5−3t (direction ⟨7,1,−3⟩) L₂: x=4−t, y=6, z=7+2t (direction ⟨−1,0,2⟩)

**Step 1:** Check parallel: ⟨7,1,−3⟩ ≠ k⟨−1,0,2⟩ — not parallel (1≠0).

**Step 2:** Check intersection: Set equal with parameters t₁, t₂:

- 1+7t₁ = 4−t₂
- 3+t₁ = 6 → **t₁ = 3**
- 5−3t₁ = 7+2t₂ → 5−9 = 7+2t₂ → t₂ = −11/2

Check equation 1: 1+21 = 22, 4−(−11/2) = 4+5.5 = 9.5. **22 ≠ 9.5** — no intersection.

Lines are **skew**. ✓

---

**Q32.** _Show L₁ and L₂ are skew._

L₁: x=2+8t, y=6−8t, z=10t (direction ⟨8,−8,10⟩) L₂: x=3+8t, y=5−3t, z=6+t (direction ⟨8,−3,1⟩)

**Not parallel:** ⟨8,−8,10⟩ ≠ k⟨8,−3,1⟩ (ratio not consistent).

**No intersection:** Equations 2+8t₁=3+8t₂ → 8(t₁−t₂)=1; 6−8t₁=5−3t₂ → 3t₂−8t₁=−1. From first: t₁−t₂=1/8. Substitute into second gives contradiction. **Skew.** ✓

---

**Q33.** _Are L₁ and L₂ parallel?_

L₁ direction: ⟨−2,1,−1⟩; L₂ direction: ⟨−4,2,−2⟩ = 2⟨−2,1,−1⟩. **Yes, parallel.**

---

**Q35.** _Do P₁(6,9,7), P₂(9,2,0), P₃(0,−5,−3) lie on same line?_

Direction P₁P₂ = ⟨3,−7,−7⟩. Direction P₁P₃ = ⟨−6,−14,−10⟩.

For collinearity, P₁P₃ must be scalar multiple of P₁P₂: ⟨−6,−14,−10⟩ = k⟨3,−7,−7⟩ → k=−2, −14=14? No. **Not collinear.**

---

**Q38.** _Show L₁ and L₂ are the same line._

L₁: x=1+3t, y=−2+t, z=2t (direction ⟨3,1,2⟩, point (1,−2,0)) L₂: x=4−6t, y=−1−2t, z=2−4t (direction ⟨−6,−2,−4⟩ = −2⟨3,1,2⟩ ✓ parallel)

Check if (4,−1,2) on L₁: 1+3t=4→t=1; y=−2+1=−1 ✓; z=2 ✓. **Same line.**

---

**Q46.** _Point 2/3 of way from P₁(1,4,−3) to P₂(1,5,−1)._

$$\mathbf{r} = \mathbf{P_1} + \frac{2}{3}\overrightarrow{P_1P_2} = (1,4,-3) + \frac{2}{3}(0,1,2) = \left(1, \frac{14}{3}, -\frac{5}{3}\right)$$

---

**Q55.** _L₁: x=1+2t, y=2−t, z=4−2t; L₂: x=9+t, y=5+3t, z=−4−t_

**(a)** Check (7,−1,−2): L₁: t=3 → (7,−1,−2) ✓; L₂: t=−2 → (7,−1,−2) ✓

**(b)** Direction vectors: v₁=⟨2,−1,−2⟩, v₂=⟨1,3,−1⟩

$$\cos\theta = \frac{|\mathbf{v_1}\cdot\mathbf{v_2}|}{|\mathbf{v_1}||\mathbf{v_2}|} = \frac{|2-3+2|}{3\cdot\sqrt{11}} = \frac{1}{3\sqrt{11}} \approx 6°$$

**(c)** Direction of perpendicular line: v₁×v₂

$$\mathbf{v_1}\times\mathbf{v_2} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\2&-1&-2\1&3&-1\end{vmatrix} = (1+6)\mathbf{i}-(-2+2)\mathbf{j}+(6+1)\mathbf{k} = \langle7,0,7\rangle = 7\langle1,0,1\rangle$$

Through (7,−1,−2): **x = 7+t, y = −1, z = −2+t**

---

**Q56.** _L₁: x=4t, y=1−2t, z=2+2t; L₂: x=1+t, y=1−t, z=−1+4t_

**(a)** (2,0,3): L₁: t=1/2 → (2,0,3) ✓; L₂: t=1 → (2,0,3) ✓

**(b)** v₁=⟨4,−2,2⟩, v₂=⟨1,−1,4⟩

$$\cos\theta = \frac{|4+2+8|}{\sqrt{24}\cdot\sqrt{18}} = \frac{14}{\sqrt{432}} = \frac{14}{12\sqrt{3}} = \frac{7}{6\sqrt{3}} \approx 47.9° \approx 48°$$

**(c)** v₁×v₂: $$\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\4&-2&2\1&-1&4\end{vmatrix} = (-8+2)\mathbf{i}-(16-2)\mathbf{j}+(-4+2)\mathbf{k} = \langle-6,-14,-2\rangle$$

Through (2,0,3): **x = 2−6t, y = −14t, z = 3−2t**

---

# SECTION 11.6: Planes in 3-Space

## Key Concepts

**Point-normal form:** a(x−x₀)+b(y−y₀)+c(z−z₀) = 0, where n = ⟨a,b,c⟩ is normal.

**General form:** ax+by+cz+d = 0

**Finding normal when given 3 points:** n = P₁P₂ × P₁P₃

**Parallel planes:** Same normal direction (normals are scalar multiples).

**Angle between planes:** $$\cos\theta = \frac{|\mathbf{n_1}\cdot\mathbf{n_2}|}{|\mathbf{n_1}||\mathbf{n_2}|}$$

**Distance: point P₀(x₀,y₀,z₀) to plane ax+by+cz+d=0:** $$D = \frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}$$

**Line of intersection of two planes:** Direction = n₁×n₂; find a point by setting one variable = 0.

---

## Solutions — Section 11.6

**Q11.** _Plane through (−2,1,1), (0,2,3), (1,0,−1)._

$$\overrightarrow{P_1P_2} = \langle2,1,2\rangle, \quad \overrightarrow{P_1P_3} = \langle3,-1,-2\rangle$$

$$\mathbf{n} = \overrightarrow{P_1P_2}\times\overrightarrow{P_1P_3} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\2&1&2\3&-1&-2\end{vmatrix} = (−2+2)\mathbf{i}−(−4-6)\mathbf{j}+(−2-3)\mathbf{k} = \langle0,10,-5\rangle$$

Simplify: n = ⟨0,2,−1⟩. Using point (−2,1,1): $$0(x+2)+2(y-1)-1(z-1) = 0 \implies \boxed{2y-z-1=0}$$

---

**Q17.** _Determine intersection of line and plane._

**(a)** x=t, y=t, z=t; plane 3x−2y+z=5: $$3t-2t+t=5 \implies 2t=5 \implies t=5/2$$ Point: **(5/2, 5/2, 5/2)**

**(b)** x=2−t, y=3+t, z=t; plane 2x+y+z=1: $$2(2-t)+(3+t)+t=1 \implies 7=1$$

No solution — **line is parallel to plane** (or check: direction ⟨−1,1,1⟩, normal ⟨2,1,1⟩; dot product = −2+1+1 = 0 ✓ parallel).

---

**Q26.** _Plane containing x=−2+3t, y=4+2t, z=3−t and perpendicular to plane x−2y+z=5._

Direction of line: v = ⟨3,2,−1⟩. Normal to given plane: n = ⟨1,−2,1⟩.

Normal to desired plane must be perpendicular to both v and n: $$\mathbf{N} = \mathbf{v}\times\mathbf{n} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\3&2&-1\1&-2&1\end{vmatrix} = (2-2)\mathbf{i}-(3+1)\mathbf{j}+(-6-2)\mathbf{k} = \langle0,-4,-8\rangle$$

Simplify: N = ⟨0,1,2⟩. Point on line (t=0): (−2,4,3). $$0(x+2)+1(y-4)+2(z-3)=0 \implies \boxed{y+2z-10=0}$$

---

**Q29.** _Plane through (1,2,−1) perpendicular to line of intersection of planes 2x+y+z=2 and x+2y+z=3._

Direction of line of intersection = n₁×n₂ where n₁=⟨2,1,1⟩, n₂=⟨1,2,1⟩: $$\mathbf{n_1}\times\mathbf{n_2} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\2&1&1\1&2&1\end{vmatrix} = (1-2)\mathbf{i}-(2-1)\mathbf{j}+(4-1)\mathbf{k} = \langle-1,-1,3\rangle$$

This direction is the **normal** to the desired plane. Using point (1,2,−1): $$-(x-1)-(y-2)+3(z+1)=0 \implies -x-y+3z+6=0 \implies \boxed{x+y-3z=6}$$

---

**Q30.** _Plane through P₁(−2,1,4), P₂(1,0,3) perpendicular to plane 4x−y+3z=2._

n of given plane = ⟨4,−1,3⟩. Direction P₁P₂ = ⟨3,−1,−1⟩.

Normal to desired plane ⊥ to both: $$\mathbf{N} = \langle3,-1,-1\rangle\times\langle4,-1,3\rangle = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\3&-1&-1\4&-1&3\end{vmatrix} = (-3-1)\mathbf{i}-(9+4)\mathbf{j}+(-3+4)\mathbf{k} = \langle-4,-13,1\rangle$$

Using P₁(−2,1,4): $$-4(x+2)-13(y-1)+(z-4)=0 \implies \boxed{-4x-13y+z+9=0}$$

---

**Q33.** _Plane whose points are equidistant from (2,−1,1) and (3,1,5)._

This is the **perpendicular bisector plane**.

Midpoint: (5/2, 0, 3). Normal = direction between points = ⟨1,2,4⟩.

$$1(x-5/2)+2(y-0)+4(z-3)=0 \implies x+2y+4z = 5/2+12 = 29/2$$ $$\boxed{2x+4y+8z=29}$$

---

**Q35.** _Line through (5,0,−2) parallel to both planes x−4y+2z=0 and 2x+3y−z+1=0._

Direction = n₁×n₂ where n₁=⟨1,−4,2⟩, n₂=⟨2,3,−1⟩: $$\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\1&-4&2\2&3&-1\end{vmatrix} = (4-6)\mathbf{i}-(−1-4)\mathbf{j}+(3+8)\mathbf{k} = \langle-2,5,11\rangle$$

$$\boxed{x = 5-2t,\quad y = 5t,\quad z = -2+11t}$$

---

**Q37.** _Show lines are parallel and find their plane._

L₁: x=−2+t, y=3+2t, z=4−t (direction v=⟨1,2,−1⟩) L₂: x=3−t, y=4−2t, z=t (direction ⟨−1,−2,1⟩ = −v ✓ parallel)

Normal to their plane: n = v × P₁P₂, where P₁=(−2,3,4) on L₁, P₂=(3,4,0) on L₂. P₁P₂ = ⟨5,1,−4⟩

$$\mathbf{n} = \langle1,2,-1\rangle\times\langle5,1,-4\rangle = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\1&2&-1\5&1&-4\end{vmatrix} = (-8+1)\mathbf{i}-(-4+5)\mathbf{j}+(1-10)\mathbf{k} = \langle-7,-1,-9\rangle$$

Using P₁(−2,3,4): −7(x+2)−(y−3)−9(z−4)=0 $$\boxed{-7x-y-9z+25=0} \text{ or } 7x+y+9z=25$$

---

**Q41.** _Parametric equations for line of intersection of:_ −2x+3y+7z+2=0 and x+2y−3z+5=0

Direction = n₁×n₂, n₁=⟨−2,3,7⟩, n₂=⟨1,2,−3⟩: $$\mathbf{n_1}\times\mathbf{n_2} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\-2&3&7\1&2&-3\end{vmatrix} = (-9-14)\mathbf{i}-( 6-7)\mathbf{j}+(-4-3)\mathbf{k} = \langle-23,1,-7\rangle$$

Find point: set z=0. Then −2x+3y=−2 and x+2y=−5. Multiply 2nd by 2: 2x+4y=−10. Add: 7y=−12, y=−12/7. x=−5−2(−12/7)=−5+24/7=−11/7.

$$\boxed{x = -\frac{11}{7}-23t, \quad y = -\frac{12}{7}+t, \quad z = -7t}$$

---

**Q51.** _Show line x=−1+t, y=3+2t, z=−t is parallel to 2x−2y−2z+3=0, find distance._

Direction v=⟨1,2,−1⟩, normal n=⟨2,−2,−2⟩. v·n = 2−4+2 = 0 ✓ **parallel.**

Point on line (t=0): (−1,3,0). Distance: $$D = \frac{|2(-1)-2(3)-2(0)+3|}{\sqrt{4+4+4}} = \frac{|-2-6+3|}{2\sqrt{3}} = \frac{5}{2\sqrt{3}} = \boxed{\frac{5\sqrt{3}}{6}}$$

---

# SECTION 11.7: Quadric Surfaces

## Key Concepts

**The six quadric surfaces** (memorize the table):

|Name|Equation|Key feature|
|---|---|---|
|Ellipsoid|x²/a²+y²/b²+z²/c²=1|All + , =1|
|Hyperboloid 1 sheet|x²/a²+y²/b²−z²/c²=1|One minus, =1|
|Hyperboloid 2 sheets|z²/c²−x²/a²−y²/b²=1|Two minus, =1|
|Elliptic Cone|z²=x²/a²+y²/b²|No linear, =0|
|Elliptic Paraboloid|z=x²/a²+y²/b²|One linear, two same-sign quadratic|
|Hyperbolic Paraboloid|z=y²/b²−x²/a²|One linear, two opposite-sign quadratic|

**Quick ID rule:** Move everything to left with 1 or 0 on right:

- No minus → Ellipsoid
- One minus, =1 → Hyperboloid 1 sheet
- Two minus, =1 → Hyperboloid 2 sheets
- All quadratic, =0 → Elliptic Cone
- One linear term, two same-sign → Elliptic Paraboloid
- One linear, opposite signs → Hyperbolic Paraboloid

---

## Solutions — Section 11.7

**Q7.** _Find traces in coordinate planes and sketch._

**(a)** x²/9+y²/25+z²/4=1 (Ellipsoid)

- xy-plane (z=0): x²/9+y²/25=1 — **ellipse**
- xz-plane (y=0): x²/9+z²/4=1 — **ellipse**
- yz-plane (x=0): y²/25+z²/4=1 — **ellipse**

**(b)** z=x²+4y² (Elliptic Paraboloid)

- xy-plane (z=0): x²+4y²=0 → just the **point** (0,0)
- xz-plane (y=0): z=x² — **parabola**
- yz-plane (x=0): z=4y² — **parabola**

**(c)** x²/9+y²/16−z²/4=1 (Hyperboloid 1 sheet)

- xy-plane (z=0): x²/9+y²/16=1 — **ellipse**
- xz-plane (y=0): x²/9−z²/4=1 — **hyperbola**
- yz-plane (x=0): y²/16−z²/4=1 — **hyperbola**

---

**Q9.** _Find equations of traces, classify._

**(a)** 4x²+y²+z²=4; **y=1**: 4x²+1+z²=4 → 4x²+z²=3 → **ellipse**

**(b)** 4x²+y²+z²=4; **x=1/2**: 4(1/4)+y²+z²=4 → y²+z²=3 → **circle (special ellipse)**

**(c)** 9x²−y²−z²=16; **x=2**: 36−y²−z²=16 → y²+z²=20 → **circle (ellipse)**

---

**Q15.** x²+y²/4+z²/9=1 — **Ellipsoid**, semi-axes a=1, b=2, c=3. Sketch: traces all ellipses, intersects x-axis at ±1, y-axis at ±2, z-axis at ±3.

**Q17.** x²/4+y²/9−z²/16=1 — **Hyperboloid of one sheet**, axis along z. Trace in xy-plane: ellipse x²/4+y²/9=1.

**Q19.** 4z²=x²+4y² → z²=x²/4+y² — **Elliptic Cone**, axis along z.

**Q21.** 9z²−4y²−9x²=36 → z²/4−y²/9−x²/4=1 — **Hyperboloid of two sheets**, axis along z. Intercepts z=±2.

**Q25.** 4z=x²+2y² — **Elliptic Paraboloid**, opens in +z direction, vertex at origin.

**Q32.** 4x²−y²+4z²=16 → x²/4−y²/16+z²/4=1

Rewrite: x²/4+z²/4−y²/16=1 — **Hyperboloid of one sheet**, axis along y.

---

**Q35.** z=x²+y² — **Circular Paraboloid** opening upward, vertex at origin. Traces: circles z=k (k>0); parabolas in xz and yz planes.

---

**Q39.** 9x²+y²+4z²−18x+2y+16z=10. Complete the square:

$$9(x-1)^2-9+( y+1)^2-1+4(z+2)^2-16=10$$ $$9(x-1)^2+(y+1)^2+4(z+2)^2=36$$ $$\frac{(x-1)^2}{4}+\frac{(y+1)^2}{36}+\frac{(z+2)^2}{9}=1$$

**Ellipsoid** centered at (1,−1,−2), semi-axes a=2, b=6, c=3.

---

# SECTION 11.8: Cylindrical and Spherical Coordinates

## Key Concepts

**Cylindrical (r,θ,z):** Like polar + z

- x = r cosθ, y = r sinθ, z = z
- r = √(x²+y²), tan θ = y/x

**Spherical (ρ,θ,φ):** ρ=distance from origin, θ=azimuthal, φ=polar (from z-axis)

- x = ρ sinφ cosθ
- y = ρ sinφ sinθ
- z = ρ cosφ
- ρ = √(x²+y²+z²), tan θ = y/x, cos φ = z/ρ

**Spherical → Cylindrical:** r = ρ sinφ, θ = θ, z = ρ cosφ

**Exam tip for θ:** Always check which quadrant (x,y) is in to pick correct θ from tan θ = y/x.

---

## Solutions — Section 11.8

**Q3.** _Cylindrical to rectangular._

**(a)** (4, π/6, 3): x=4cos(π/6)=2√3, y=4sin(π/6)=2, z=3 → **(2√3, 2, 3)**

**(b)** (8, 3π/4, −2): x=8cos(3π/4)=−4√2, y=8sin(3π/4)=4√2, z=−2 → **(−4√2, 4√2, −2)**

**(c)** (5, 0, 4): x=5, y=0, z=4 → **(5, 0, 4)**

**(d)** (7, π, −9): x=−7, y=0, z=−9 → **(−7, 0, −9)**

---

**Q5.** _Rectangular to spherical._

**(a)** (1, √3, −2): ρ=√(1+3+4)=√8=2√2; tan θ=√3/1 → θ=π/3 (x,y both positive, Q1); cos φ=−2/(2√2)=−1/√2 → φ=3π/4 → **(2√2, π/3, 3π/4)**

**(b)** (1, −1, √2): ρ=√(1+1+2)=2; tan θ=−1/1, x>0,y<0 → θ=7π/4; cos φ=√2/2 → φ=π/4 → **(2, 7π/4, π/4)**

**(c)** (0, 3√3, 3): ρ=√(0+27+9)=6; tan θ undefined (x=0), y>0 → θ=π/2; cos φ=3/6=1/2 → φ=π/3 → **(6, π/2, π/3)**

**(d)** (−5√3, 5, 0): ρ=√(75+25+0)=10; x<0,y>0 → θ=5π/6 (tan θ=5/(−5√3)=−1/√3); cos φ=0 → φ=π/2 → **(10, 5π/6, π/2)**

---

**Q7.** _Spherical to rectangular._

**(a)** (5, π/6, π/4): x=5sin(π/4)cos(π/6)=5·(√2/2)·(√3/2)=5√6/4; y=5·(√2/2)·(1/2)=5√2/4; z=5cos(π/4)=5√2/2 → **(5√6/4, 5√2/4, 5√2/2)**

**(b)** (7, 0, π/2): x=7sin(π/2)cos0=7, y=7sin(π/2)sin0=0, z=7cos(π/2)=0 → **(7, 0, 0)**

**(c)** (1, π, 0): x=1·sin0·cosπ=0, y=0, z=1·cos0=1 → **(0, 0, 1)**

**(d)** (2, 3π/2, π/2): x=2sin(π/2)cos(3π/2)=0, y=2sin(π/2)sin(3π/2)=−2, z=2cos(π/2)=0 → **(0, −2, 0)**

---

**Q9.** _Cylindrical to spherical._

**(a)** (√3, π/6, 3): ρ=√(r²+z²)=√(3+9)=2√3; θ=π/6; tan φ=r/z=√3/3=1/√3 → φ=π/6 → **(2√3, π/6, π/6)**

**(b)** (1, π/4, −1): ρ=√(1+1)=√2; θ=π/4; z<0 → φ = π−arctan(1/1) = π−π/4 = 3π/4 → **(√2, π/4, 3π/4)**

**(c)** (2, 3π/4, 0): ρ=√(4+0)=2; θ=3π/4; φ=π/2 (since z=0) → **(2, 3π/4, π/2)**

**(d)** (6, 1, −2√3): ρ=√(36+12)=4√3; θ=1 radian; tan φ=6/(−2√3)<0 → φ=π−arctan(√3)=π−π/3=5π/6 → **(4√3, 1, 5π/6)**

---

**Q11.** _Spherical to cylindrical._

**(a)** (5, π/4, 2π/3): r=5sin(2π/3)=5·(√3/2)=5√3/2; θ=π/4; z=5cos(2π/3)=5·(−1/2)=−5/2 → **(5√3/2, π/4, −5/2)**

**(b)** (1, 7π/6, π): r=1·sin(π)=0; θ=7π/6; z=1·cos(π)=−1 → **(0, 7π/6, −1)** (the origin shifted, i.e., the point (0,0,−1))

**(c)** (3, 0, 0): r=3sin0=0; z=3cos0=3 → **(0, 0, 3)**

**(d)** (4, π/6, π/2): r=4sin(π/2)=4; z=4cos(π/2)=0 → **(4, π/6, 0)**

---

**Q24.** _Describe the intersection of r=5 and z=1 in cylindrical coordinates._

r=5 is a cylinder of radius 5 about z-axis; z=1 is a horizontal plane. Their intersection is a **circle of radius 5 in the plane z=1, centered on the z-axis**.

---

**Q33.** _Express ρ sinφ = 2cosθ in rectangular coordinates._

Note: ρ sinφ = r (the cylindrical r), and r cosθ = x. Also ρ sinφ cosθ = x.

$$\rho\sin\phi = 2\cos\theta$$ Multiply both sides by ρ sinφ: $$(\rho\sin\phi)^2 = 2\rho\sin\phi\cos\theta = 2x$$ $$r^2 = 2x \implies x^2+y^2 = 2x \implies \boxed{(x-1)^2+y^2=1}$$

This is a **circular cylinder** of radius 1, centered on the line x=1, y=0 (parallel to z-axis).

---

**Q43.** _Express 2x+3y+4z=1 in (a) cylindrical and (b) spherical._

**(a) Cylindrical:** Substitute x=r cosθ, y=r sinθ, z=z: $$\boxed{2r\cos\theta + 3r\sin\theta + 4z = 1}$$

**(b) Spherical:** Substitute x=ρ sinφ cosθ, y=ρ sinφ sinθ, z=ρ cosφ: $$\boxed{2\rho\sin\phi\cos\theta + 3\rho\sin\phi\sin\theta + 4\rho\cos\phi = 1}$$ $$\rho(2\sin\phi\cos\theta + 3\sin\phi\sin\theta + 4\cos\phi) = 1$$

---

## Quick Exam Reference Summary

|Topic|Key Formula|
|---|---|
|Distance 3D|√[(Δx)²+(Δy)²+(Δz)²]|
|Sphere|(x−x₀)²+(y−y₀)²+(z−z₀)²=r²|
|Dot product|u·v=‖u‖‖v‖cosθ|
|Cross product|Use 3×3 det; result ⊥ both vectors|
|Area △|½‖u×v‖|
|Volume ∥-piped||
|Line|r=r₀+tv|
|Plane (pt-normal)|n·(r−r₀)=0|
|Point-plane dist||
|Projection|projᵦv = (v·b/‖b‖²)b|

---

# SECTION 10.4 — CONIC SECTIONS

---

## 📚 WHAT ARE CONIC SECTIONS?

Conic sections are curves formed when a plane intersects a double-napped cone. The 4 types:

- **Circle** — plane cuts perpendicular to axis
- **Ellipse** — plane cuts at a tilt
- **Parabola** — plane cuts parallel to one slant edge
- **Hyperbola** — plane cuts through both nappes

**Degenerate conics** (when plane passes through vertex): a point, a pair of lines, or a single line.

---

## 📐 THE PARABOLA

**Definition:** Set of all points equidistant from a fixed point (focus) and a fixed line (directrix).

**Key terms:**

- **p** = distance from vertex to focus = distance from vertex to directrix
- **Vertex** = midpoint between focus and directrix (the tip)

### Standard Forms (Vertex at Origin)

|Equation|Opens|Focus|Directrix|
|---|---|---|---|
|y² = 4px, p > 0|Right|(p, 0)|x = −p|
|y² = 4px, p < 0|Left|(p, 0)|x = −p|
|x² = 4py, p > 0|Up|(0, p)|y = −p|
|x² = 4py, p < 0|Down|(0, p)|y = −p|

**⚡ EXAM TIP:** `x²` form → opens up/down. `y²` form → opens left/right. Sign of p tells direction.

### Shifted Form (Vertex at (h, k))

```
(x − h)² = 4p(y − k)   → opens up/down,   focus = (h, k+p),  directrix: y = k−p
(y − k)² = 4p(x − h)   → opens left/right, focus = (h+p, k),  directrix: x = h−p
```

**To convert a general equation → complete the square.**

---

## 📐 THE ELLIPSE

**Definition:** Set of all points where **sum of distances to two foci = 2a** (constant).

**Key terms:** a = semi-major axis, b = semi-minor axis, c = center-to-focus distance **Golden rule: c² = a² − b²** (minus, because c < a always)

### Standard Forms (Center at Origin)

|Equation|Major Axis|Vertices|Foci|
|---|---|---|---|
|x²/a² + y²/b² = 1, a > b|Horizontal|(±a, 0)|(±c, 0)|
|x²/b² + y²/a² = 1, a > b|Vertical|(0, ±a)|(0, ±c)|

**⚡ EXAM TIP:** Bigger denominator = that axis is the major axis. Always identify a² (bigger) and b² (smaller) FIRST.

### Shifted Form: Center at (h, k)

```
(x−h)²/a² + (y−k)²/b² = 1   (horizontal major axis)
(x−h)²/b² + (y−k)²/a² = 1   (vertical major axis)
```

---

## 📐 THE HYPERBOLA

**Definition:** Set of all points where **difference of distances to two foci = 2a**.

**Key terms:** a = semi-transverse axis, b = semi-conjugate axis **Golden rule: c² = a² + b²** (PLUS — opposite of ellipse! c > a always)

### Standard Forms (Center at Origin)

|Equation|Opens|Vertices|Asymptotes|
|---|---|---|---|
|x²/a² − y²/b² = 1|Left/Right|(±a, 0)|y = ±(b/a)x|
|y²/a² − x²/b² = 1|Up/Down|(0, ±a)|y = ±(a/b)x|

**⚡ EXAM TIP:** Positive term tells you direction. `x²` positive → L/R. `y²` positive → U/D. Asymptote slope = b/a for L/R form, a/b for U/D form.

### Quick ID Table

|Conic|Clue|c-formula|
|---|---|---|
|Parabola|Only ONE of x² or y²|No c, use p|
|Ellipse|Both x² and y², SAME sign|c² = a² − b²|
|Hyperbola|Both x² and y², OPPOSITE signs|c² = a² + b²|
|Circle|Both x² and y², same sign, same coeff|c = 0|

---

---

# 10.4 — SOLVED QUESTIONS

---

## PARABOLAS

### Q3. x² = 8y — find vertex, focus, directrix

Match to **x² = 4py**:

- 4p = 8 → **p = 2**
- Vertex = **(0, 0)**
- Focus = (0, p) = **(0, 2)**
- Directrix: **y = −2**
- Opens **upward** ✓

---

### Q4. y² = −6x — find vertex, focus, directrix

Match to **y² = 4px**:

- 4p = −6 → **p = −3/2**
- Vertex = **(0, 0)**
- Focus = (p, 0) = **(−3/2, 0)**
- Directrix: **x = 3/2**
- Opens **left** (p < 0) ✓

---

### Q5. (x−1)² = −8(y+2) — find vertex, focus, directrix

Match to **(x−h)² = 4p(y−k)**:

- h = 1, k = −2, 4p = −8 → **p = −2**
- Vertex = **(1, −2)**
- Focus = (h, k+p) = (1, −2+(−2)) = **(1, −4)**
- Directrix: y = k − p = −2 − (−2) = **y = 0**
- Opens **downward** ✓

**⚡ EXAM TIP:** Focus = (h, k+p). Directrix = y = k−p. These two formulas cover all up/down parabolas.

---

### Q7. Vertex (0,0), Focus (0, −3) — find equation

Focus is on y-axis → form is **x² = 4py**

- p = −3
- **x² = −12y** ✓

---

### Q8. Vertex (0,0), Focus (2, 0) — find equation

Focus is on x-axis → form is **y² = 4px**

- p = 2
- **y² = 8x** ✓

---

### Q9. Vertex (3,2), Focus (3,4) — find equation

Same x-coordinate → vertical axis → **(x−h)² = 4p(y−k)**

- h = 3, k = 2
- p = (focus y) − (vertex y) = 4 − 2 = **2**
- **(x−3)² = 8(y−2)** ✓

**⚡ EXAM TIP:** p = distance from vertex to focus (with sign). Same x → vertical parabola. Same y → horizontal.

---

## ELLIPSES

### Q11. x²/9 + y²/4 = 1

- a² = 9, b² = 4 → **a = 3, b = 2** (horizontal major, bigger denom under x²)
- c² = 9 − 4 = 5 → **c = √5**
- Vertices: **(±3, 0)**
- Foci: **(±√5, 0)**
- Major axis length = 2a = **6**, Minor = 2b = **4**

---

### Q12. x²/4 + y²/25 = 1

- a² = 25 (under y², bigger!) → **a = 5, b = 2**, vertical major axis
- c² = 25 − 4 = 21 → **c = √21**
- Vertices: **(0, ±5)**
- Foci: **(0, ±√21)**

**⚡ EXAM TIP:** Bigger denominator → that variable's axis is the major axis. Check this FIRST every time.

---

### Q13. 4x² + 9y² = 36

- Divide by 36 first: **x²/9 + y²/4 = 1**
- Now same as Q11 → a = 3, b = 2, c = √5
- Vertices: **(±3, 0)**, Foci: **(±√5, 0)**

📝 Always divide to get standard form first. Never read off values from non-standard form.

---

### Q15. Foci (±2, 0), vertices (±3, 0) — find equation

- Foci on x-axis → horizontal → **x²/a² + y²/b² = 1**
- a = 3 → a² = 9
- c = 2 → b² = a² − c² = 9 − 4 = **5**
- **x²/9 + y²/5 = 1** ✓

---

### Q16. Foci (0, ±3), vertices (0, ±5) — find equation

- Foci on y-axis → vertical → **x²/b² + y²/a² = 1**
- a = 5, c = 3 → b² = 25 − 9 = **16**
- **x²/16 + y²/25 = 1** ✓

---

### Q17. Foci (±1, 0), minor axis length = 6 — find equation

- Foci on x-axis → horizontal → **x²/a² + y²/b² = 1**
- Minor axis length = 2b = 6 → b = 3 → b² = 9
- c = 1 → a² = b² + c² = 9 + 1 = **10**
- **x²/10 + y²/9 = 1** ✓

**⚡ EXAM TIP:** Given minor axis → b = length/2. Then a² = b² + c² (rearranged from c² = a²−b²).

---

## HYPERBOLAS

### Q19. x²/4 − y²/9 = 1

- x² positive → opens **Left/Right**. a² = 4, b² = 9 → a = 2, b = 3
- c² = 4 + 9 = 13 → **c = √13**
- Vertices: **(±2, 0)**
- Foci: **(±√13, 0)**
- Asymptotes: **y = ±(3/2)x**

**⚡ EXAM TIP:** Hyperbola c² = a²+b² (ADD). Asymptote = ±(b/a)x for L/R type.

---

### Q21. 9y² − x² = 9

- Divide by 9: **y²/1 − x²/9 = 1**
- y² positive → opens **Up/Down**. a² = 1, b² = 9 → a = 1, b = 3
- c² = 1 + 9 = 10 → **c = √10**
- Vertices: **(0, ±1)**
- Foci: **(0, ±√10)**
- Asymptotes: **y = ±(1/3)x** (slope = a/b for U/D type)

---

### Q23. Vertices (±2, 0), foci (±3, 0) — find equation

- Vertices on x-axis → **x²/a² − y²/b² = 1**
- a = 2, c = 3 → b² = c² − a² = 9 − 4 = **5**
- **x²/4 − y²/5 = 1** ✓

📝 For hyperbola: b² = c² − a². Never mix this up with ellipse (b² = a² − c²).

---

### Q24. Vertices (0, ±3), foci (0, ±5) — find equation

- Vertices on y-axis → **y²/a² − x²/b² = 1**
- a = 3, c = 5 → b² = 25 − 9 = **16**
- **y²/9 − x²/16 = 1** ✓

---

### Q25. Vertices (±3, 0), asymptotes y = ±2x — find equation

- Vertices on x-axis → **x²/a² − y²/b² = 1**, a = 3
- Asymptote slope = b/a = 2 → b = 2a = **6**
- **x²/9 − y²/36 = 1** ✓

**⚡ EXAM TIP:** When given asymptotes, use slope = b/a (L/R) or a/b (U/D) to find the missing value. No foci needed.

---

---

# SECTION 13.1 — FUNCTIONS OF TWO OR MORE VARIABLES

---

## 📚 CORE CONCEPT

In Calc 1: z = f(x) → curve in 2D. Now: **z = f(x, y)** → **surface in 3D** (two inputs, one output).

**Evaluating:** Just plug in. f(2, 3) means substitute x = 2, y = 3.

---

## 📐 DOMAIN OF f(x, y)

The domain is all input points (x, y) where the formula is **defined**.

|Expression|Restriction|
|---|---|
|√(expression)|expression ≥ 0|
|1/expression|expression ≠ 0|
|ln(expression)|expression > 0 (strict!)|
|trig functions|usually no restriction unless there's division inside|

The domain is usually described as a **region** in the xy-plane (half-plane, disk, exterior of circle, etc.)

---

## 📐 3D SURFACE TYPES — RECOGNIZE THESE

|Formula|Surface|
|---|---|
|z = ax + by + c|Plane (flat)|
|z = x² + y²|Circular paraboloid (bowl, opens up)|
|z = ax² + by², a≠b|Elliptic paraboloid|
|z = y² − x²|Hyperbolic paraboloid (saddle shape)|
|x² + y² + z² = r²|Sphere|
|z = √(r² − x² − y²)|Upper hemisphere|
|z = −√(r² − x² − y²)|Lower hemisphere|
|z² = x² + y²|Cone|
|z = √(x² + y²)|Upper nappe of cone|

---

## 📐 LEVEL CURVES — THE KEY IDEA

A **level curve** of height k is: **f(x, y) = k** (a curve in the xy-plane)

**How to find them:**

1. Set f(x, y) = k
2. Simplify → identify the curve type (line, circle, ellipse, hyperbola...)
3. Repeat for different k values → you get a **contour plot**

**Intuition:** Like elevation lines on a topographic map. Each curve = constant height on the surface.

**Level curve shapes to recognize:**

|f(x, y)|Level curves f = k|
|---|---|
|x² + y²|Circles (if k > 0)|
|ax² + by²|Ellipses|
|y² − x²|Hyperbolas (k≠0); lines y=±x (k=0)|
|ax + by|Parallel lines|
|xy|Hyperbolas (y = k/x)|

---

## 📐 LEVEL SURFACES (f of 3 variables)

For **w = f(x, y, z)**, set f = k → get a **surface** in 3D.

Example: f = x² + y² + z²

- k > 0 → spheres of radius √k
- k = 0 → single point
- k < 0 → empty

---

---

# 13.1 — SOLVED QUESTIONS

---

## DOMAIN QUESTIONS

### Q1. f(x, y) = √(x − y) — find domain

Need: x − y ≥ 0 → **x ≥ y**

**Domain:** All points on or above the line y = x → the half-plane {(x,y) : x ≥ y}

---

### Q3. f(x, y) = ln(x² + y² − 1) — find domain

Need: x² + y² − 1 > 0 → **x² + y² > 1**

**Domain:** All points strictly **outside** the unit circle. (Note: strict inequality for ln — boundary excluded.)

---

### Q6. f(x, y) = (x − y)/(x + y) — find domain

Denominator ≠ 0: x + y ≠ 0 → **y ≠ −x**

**Domain:** Entire plane **minus** the line y = −x

---

### Q7. f(x, y) = e^(x+y) / (x − y) — find domain

e^(x+y) is defined everywhere. Denominator: x − y ≠ 0 → **x ≠ y**

**Domain:** Entire plane minus the line y = x

---

### Q8. f(x, y) = sin(x/y) — find domain

sin is always defined. But x/y requires **y ≠ 0**.

**Domain:** Entire plane minus the x-axis → {(x, y) : y ≠ 0}

---

## GRAPH / SURFACE QUESTIONS

### Q18. f(x, y) = √(1 − x² − y²) — describe the graph

- Write as: z = √(1 − x² − y²) → square both sides: z² = 1 − x² − y²
- Rearrange: **x² + y² + z² = 1** (sphere of radius 1)
- Since z = √(...) ≥ 0 → only the **upper hemisphere**
- Domain: x² + y² ≤ 1 (unit disk)

**Answer:** Upper hemisphere of sphere x² + y² + z² = 1 (z ≥ 0) ✓

**⚡ EXAM TIP:** z = √(r²−x²−y²) → upper hemisphere. z = −√(r²−x²−y²) → lower hemisphere. Always square to identify the surface, then use the sign of z to pick which half.

---

### Q19. f(x, y) = −√(x² + y²) — describe the graph

- z = −√(x² + y²) → z ≤ 0 → square: z² = x² + y² (cone)
- Since z ≤ 0 → **lower nappe of cone** opening downward

**Answer:** Lower nappe of cone z² = x² + y² (z ≤ 0) ✓

---

### Q20. f(x, y) = √(x² + y²) — describe the graph

- z = √(x² + y²) → z ≥ 0 → z² = x² + y² (cone)
- Since z ≥ 0 → **upper nappe of cone** opening upward

**Answer:** Upper nappe of cone z² = x² + y² (z ≥ 0) ✓

---

## LEVEL CURVE QUESTIONS

### Q28. f(x, y) = x − 2y — sketch level curves k = 0, 1, 2, 3, 4

Set f = k: x − 2y = k → rearrange: **y = (1/2)x − k/2**

- k = 0: y = (1/2)x
- k = 1: y = (1/2)x − 1/2
- k = 2: y = (1/2)x − 1
- k = 3, 4: same pattern, keep shifting down

**Pattern:** Family of **parallel lines** with slope 1/2. Each increase in k shifts the line downward/right by equal spacing.

**⚡ EXAM TIP:** f = ax + by always gives parallel lines as level curves. Slope of lines = −a/b.

---

### Q67. f(x, y) = x² + y² — describe level curves and behavior

Set f = k: **x² + y² = k**

- k > 0 → circle of radius √k (centered at origin) ✓
- k = 0 → single point (0, 0)
- k < 0 → empty set (impossible)

**Behavior moving away from origin:** As (x,y) moves away, f = x²+y² increases — the surface is a paraboloid rising from origin. The level circles get **closer together** in the contour plot as k increases (same Δk = smaller Δr since r = √k slows down).

**Answer:** Concentric circles centered at origin, radius √k. Surface is a circular paraboloid opening upward. ✓

---
