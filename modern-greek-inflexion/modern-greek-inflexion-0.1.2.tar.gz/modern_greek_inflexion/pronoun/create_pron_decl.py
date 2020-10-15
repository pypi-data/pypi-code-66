from modern_greek_inflexion.adjective.create_adj_decl import create_all_adj_forms

m = 'masc'
f = 'fem'
n = 'neut'
sg = 'sg'
pl = 'pl'
acc = 'acc'
nom = 'nom'
gen = 'gen'
voc = 'voc'


def create_all_pron_forms(bas_forms, strong=True):
    # inflected: boolean
    # forms: dic 'fem', 'masc', neut', if not inflected forms is a string

    masc, fem, neut = bas_forms.split('/')
    forms = None

    if masc != neut:

        if masc[-2:] in ['ός', 'ος'] or masc[-3:] == 'πας':

            forms, _ = create_all_adj_forms(bas_forms)

            # acc masc
            acc_masc_sg = forms[sg][m][acc]
            acc_fem_sg = forms[sg][f][acc]
            if acc_masc_sg[-1] in ['ο', 'ό']:
                forms[sg][m][acc] = acc_masc_sg + ',' + acc_masc_sg + 'ν'
            forms[sg][f][acc] = acc_fem_sg + ',' + acc_fem_sg + 'ν'

            if masc == 'αυτός':
                if strong:
                    from .resources import AUTOS_STRONG
                    forms = AUTOS_STRONG
                else:
                    from .resources import AUTOS_WEAK
                    forms = AUTOS_WEAK

            if masc == 'ποιος':

                gen_fem_sg = 'ποιας,ποιανάς,τίνος'
                gen_neut_sg = gen_masc_sg = 'ποιου,ποιανού,τίνος'
                gen_pl = 'ποιων,ποιανών,τίνων'
                forms[sg][m][gen] = gen_masc_sg
                forms[sg][f][gen] = gen_fem_sg
                forms[sg][n][gen] = gen_neut_sg
                forms[pl][m][gen] = gen_pl
                forms[pl][f][gen] = gen_pl
                forms[pl][n][gen] = gen_pl

        elif masc[-6:] == 'δήποτε':
            suffix = 'δήποτε'
            bas_forms = bas_forms.replace('σδήποτε', 'ς')
            bas_forms = bas_forms.replace('δήποτε', '')

            forms = create_all_pron_forms(bas_forms)
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:
                        form = forms[number][gender][case]

                        forms_for_case = []
                        for s_f in form.split(','):
                            if s_f:
                                if s_f[-1] == 'ς':
                                    s_f = s_f[:-1] + 'σ'
                                r = s_f + suffix
                                forms_for_case.append(r)

                        forms[number][gender][case] = ','.join(forms_for_case)
        # ενας, μια, ενα

        elif masc[-4:] == 'ένας' or masc[-3:] == 'είς':
            forms = {'sg': {'masc': {},
                            'fem': {},
                            'neut': {}}
                     }
            if masc[-4:] == 'ένας':
                prefix_mn = masc[:-4]
            else:
                prefix_mn = masc[:-3]

            forms['sg']['masc']['nom'] = prefix_mn + 'ένας' + ',' + prefix_mn + 'είς'
            if masc in ['κανείς', 'κανένας']:
                forms['sg']['masc']['nom'] = 'κανείς,κανένας,' + 'κάνας'
            forms['sg']['masc']['acc'] = prefix_mn + 'ένα' + ',' + prefix_mn + 'έναν'
            forms['sg']['masc']['gen'] = prefix_mn + 'ενός'

            forms['sg']['fem']['nom'] = fem
            forms['sg']['fem']['acc'] = ','.join([sf + ',' + sf + 'ν' for sf in fem.split(',')])
            forms['sg']['fem']['gen'] = ','.join([sf + 'ς' for sf in fem.split(',')])

            forms['sg']['neut']['nom'] = prefix_mn + 'ένα'
            forms['sg']['neut']['acc'] = prefix_mn + 'ένα'
            forms['sg']['neut']['gen'] = prefix_mn + 'ενός'

        elif masc == 'τις':
            from .resources import TIS
            forms = TIS


    else:
        if masc in ['καθετί', 'τι', 'κατιτί', 'τίποτα', 'τίποτε', 'οτιδήποτε']:
            forms, _ = create_all_adj_forms(bas_forms)
            for number in forms:
                for gender in forms[number]:
                    for case in forms[number][gender]:

                        if gender != n or case not in [nom, acc]:

                            forms[number][gender][case] = ''
        elif masc == 'εγώ':
            if strong:
                from .resources import EGO_STRONG
                forms = EGO_STRONG
            else:
                from .resources import EGO_WEAK
                forms = EGO_WEAK
        elif masc == 'εσύ':
            if strong:
                from .resources import ESU_STRONG
                forms = ESU_STRONG
            else:
                from .resources import ESU_WEAK
                forms = ESU_WEAK

        elif masc == 'αλλήλων':
            forms = {'pl': {
                        'masc': {
                            'gen': 'αλλήλων',
                            'acc': 'αλλήλους'
                        },
                        'fem': {
                            'gen': 'αλλήλων',
                            'acc': 'αλλήλες'
                        },
                    }}

        elif masc == 'όπερ':

                forms = {'sg':{
                        'neut':{
                            'nom': masc,
                            'acc': masc
                        }}}
                return forms

        elif masc == 'ταύτα':
            forms = {'pl':{
                        'neut':{
                                'nom': masc,
                                'acc': masc
                        }}}

        else:
            raise ValueError

    # remove vocatives
    for number in forms:
        for gender in forms[number]:
            for case in forms[number][gender]:

                if case == voc:
                    forms[number][gender][case] = ''

    return forms



