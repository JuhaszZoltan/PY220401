from module import IdozitettFelirat, get_lista, leghosszabb_felirat

idozitett_feliratok = get_lista('feliratok.txt')

print(f'5. feladat - feliratok száma: {len(idozitett_feliratok)}')
print('7. feladat - legtöbb szóból álló felirat:')
print(leghosszabb_felirat(idozitett_feliratok))