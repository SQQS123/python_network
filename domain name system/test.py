import pydns
d = pydns.dns()
q = d.coding('www','google','com')
sr = d.send(q)
d.info(q)
d.info(sr)
