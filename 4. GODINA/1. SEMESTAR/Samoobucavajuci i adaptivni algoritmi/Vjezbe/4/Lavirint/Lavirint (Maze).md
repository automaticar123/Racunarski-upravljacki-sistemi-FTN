# Lavirint (Maze)

- **Lavirint** - $n \times n$ matrica.
- Agent $x$ ima definisane akcije $\mathcal{A} = (\text{up}, \text{down}, \text{left}, \text{right})$. 
- Tipovi polja u lavirintu
	- **Regularno polje** - Nagrada je $r = -1$
	- **Kazneno polje** - Nagrada je $r = -100$
	- **Zidovi**
	- **Terminalno polje** - kraj, "igra" je gotova, cilj, pobjeda - Nagrada je $r = 0$
	- **Teleport polje** - *opciono*, smanjiće broj stanja za onoliko koliko ima teleport polja, iz razloga što je polje na koje se teleportujemo suštinski isto sa teleport poljem. 
	- **Smrt polje** - *opciono*, označava smrt agenta.
- **Cilj** - naći **optimalnu** strateriju i provjeriti algoritam iteriranjem kroz politike.
- **Stanje** - polje u kojem se nalazimo.
- Vrijednost stanja $$v(s) = r + \gamma v(s^{+})$$
- Optimalna putanja $$v(s) = \max_{a \in \mathcal{A}}\{h(s, a) + \gamma v(f(s, a))\}$$