import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

d += (vcc := elm.Dot().label("$V_{CC}$", loc="left"))
d += elm.Resistor().down().label("$R$")
d += (node := elm.Dot())
d += elm.Capacitor().down().label("$C$")
d += elm.Ground()

d += elm.Line().at(node.start).right().length(1.5)
d += (mcu := elm.Ic(
    pins=[elm.IcPin(name=r"$\overline{\mathrm{RESET}}$" + "\n(active low)",
                     side="left")],
    size=(3, 2.2),
).anchor("inL1").label("MCU", loc="top"))

d.save("figures/drawn/por_circuit.pdf")