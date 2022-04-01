class IdozitettFelirat:
    def __init__(self, idoz:str, feli:str):
        self.idozites:str = idoz
        self.felirat:str = feli
        self.szavak_szama = len(self.felirat.split(' '))
        e_v = self.idozites.split(' - ')
        ep = e_v[0].split(':')[0]
        vp = e_v[1].split(':')[0]
        eo = f'0{0 if int(ep) < 60 else 1}'
        vo = f'0{0 if int(vp) < 60 else 1}'
        ep = ep if eo != '01' else f'{"0" if int(ep)-60 <= 10 else ""}{int(ep)-60}'
        vp = vp if vo != '01' else f'{"0" if int(vp)-60 <= 10 else ""}{int(vp)-60}'
        self.srt_idozites = f'{eo}:{ep}:{e_v[0].split(":")[1]} --> {vo}:{vp}:{e_v[1].split(":")[1]}'
        # eleje_vege[0] = f'00:{eleje_vege[0]}' if int(eleje_vege[0].split(':')[0]) < 60 else f'01:0{int(eleje_vege[0].split(":")[0]) - 60}:{eleje_vege[0].split(":")[1]}'
        # eleje_vege[1] = f'00:{eleje_vege[1]}' if int(eleje_vege[1].split(':')[0]) < 60 else f'01:0{int(eleje_vege[1].split(":")[0]) - 60}:{eleje_vege[1].split(":")[1]}'
        # self.srt_idozites = f'{eleje_vege[0]} --> {eleje_vege[1]}'


def get_lista(f:str) -> list[IdozitettFelirat]:
    ifs = []
    file = open(f)
    while True:
        idozites:str = file.readline().strip()
        if not idozites: break
        felirat:str = file.readline().strip()
        ifs.append(IdozitettFelirat(idozites, felirat))
    return ifs


def leghosszabb_felirat(ifs:list[IdozitettFelirat]) -> str:
    maxi:int = 0
    for i in range(1, len(ifs)):
        if ifs[i].szavak_szama > ifs[maxi].szavak_szama:
            maxi = i
    return ifs[maxi].felirat