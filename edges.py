#http://cube.crider.co.uk/visualcube.php?fmt=svg&size=200&fo=100&co=15&r=y45x34&fd=ttttuttttttttlttttttttbttttttttdttttttttrttttttttftttttt
import requests
import configparser

config = configparser.ConfigParser()
config.read('scheme.cfg')

fmt = config.get('image', 'fmt')
default_params = {
    'fmt': fmt,
    'size': config.get('image', 'size'),
    'sch': config.get('style', 'sch'),
    'bg': config.get('style', 'bg'),
    'cc': config.get('style', 'cc'),
    'co': config.get('style', 'co'),
    'fo': config.get('style', 'fo'),
    'dist': config.get('style', 'dist')
}

def rotation(x, y, z):
    return 'x{}y{}z{}'.format(x, y, z)

def download_image(path, params):
    base_url = "http://cube.crider.co.uk/visualcube.php"
    response = requests.get(base_url, params)

    if response.status_code == 200:
        open(path, 'wb').write(response.content)


u_face = 'nnnnunnnn'
r_face = 'nnnnrnnnn'
f_face = 'nnnnfnnnn'
d_face = 'nnnndnnnn'
l_face = 'nnnnlnnnn'
b_face = 'nnnnbnnnn'
clear_template = u_face + r_face + f_face + d_face + l_face + b_face

BD_template_fc = u_face + r_face + f_face + 'nnnndnnyn' + l_face + 'nnnnbnnxn'
DB_template_fc = u_face + r_face + f_face + 'nnnndnnxn' + l_face + 'nnnnbnnyn'
BL_template_fc = u_face + r_face + f_face + d_face + 'nnnylnnnn' + 'nnnnbxnnn'
LB_template_fc = u_face + r_face + f_face + d_face + 'nnnxlnnnn' + 'nnnnbynnn'
BR_template_fc = u_face + 'nnnnrynnn' + f_face + d_face + l_face + 'nnnxbnnnn'
RB_template_fc = u_face + 'nnnnrxnnn' + f_face + d_face + l_face + 'nnnybnnnn'
BU_template_fc = 'nynnunnnn' + r_face + f_face + d_face + l_face + 'nxnnbnnnn'
UB_template_fc = 'nxnnunnnn' + r_face + f_face + d_face + l_face + 'nynnbnnnn'
DL_template_fc = u_face + r_face + f_face + 'nnnxdnnnn' + 'nnnnlnnyn' + b_face
LD_template_fc = u_face + r_face + f_face + 'nnnydnnnn' + 'nnnnlnnxn' + b_face
DR_template_fc = u_face + 'nnnnrnnyn' + f_face + 'nnnndxnnn' + l_face + b_face
RD_template_fc = u_face + 'nnnnrnnxn' + f_face + 'nnnndynnn' + l_face + b_face
FL_template_fc = u_face + r_face + 'nnnxfnnnn' + d_face + 'nnnnlynnn' + b_face
LF_template_fc = u_face + r_face + 'nnnyfnnnn' + d_face + 'nnnnlxnnn' + b_face
FR_template_fc = u_face + 'nnnyrnnnn' + 'nnnnfxnnn' + d_face + l_face + b_face
RF_template_fc = u_face + 'nnnxrnnnn' + 'nnnnfynnn' + d_face + l_face + b_face
FU_template_fc = 'nnnnunnyn' + r_face + 'nxnnfnnnn' + d_face + l_face + b_face
UF_template_fc = 'nnnnunnxn' + r_face + 'nynnfnnnn' + d_face + l_face + b_face
LU_template_fc = 'nnnyunnnn' + r_face + f_face + d_face + 'nxnnlnnnn' + b_face
UL_template_fc = 'nnnxunnnn' + r_face + f_face + d_face + 'nynnlnnnn' + b_face
RU_template_fc = 'nnnnuynnn' + 'nxnnrnnnn' + f_face + d_face + l_face + b_face
UR_template_fc = 'nnnnuxnnn' + 'nynnrnnnn' + f_face + d_face + l_face + b_face

edges_templates = {
    'BD': BD_template_fc,
    'BL': BL_template_fc,
    'BR': BR_template_fc,
    'BU': BU_template_fc,
    'DB': DB_template_fc,
    'DL': DL_template_fc,
    'DR': DR_template_fc,
    'FL': FL_template_fc,
    'FR': FR_template_fc,
    'FU': FU_template_fc,
    'LB': LB_template_fc,
    'LD': LD_template_fc,
    'LF': LF_template_fc,
    'LU': LU_template_fc,
    'RB': RB_template_fc,
    'RD': RD_template_fc,
    'RF': RF_template_fc,
    'RU': RU_template_fc,
    'UB': UB_template_fc,
    'UF': UF_template_fc,
    'UL': UL_template_fc,
    'UR': UR_template_fc
}


edges_rotation = {
    'BD': 'x-45y-120',
    'DB': 'x-45y-120',
    'BL': 'z30x-120',
    'LB': 'z30x-120',
    'BR': 'z-30x-120',
    'RB': 'z-30x-120',
    'BU': 'x-125',
    'UB': 'x-120',
    'DL': 'y-30x30',
    'LD': 'y-45x30',
    'DR': 'y30x30',
    'RD': 'y45x30',
    'FL': 'y-30x-30',
    'LF': 'y-60x-30',
    'FR': 'y30x-30',
    'RF': 'y60x-30',
    'FU': 'x-30',
    'UF': 'x-45',
    'LU': 'y-60x-30',
    'UL': 'y-30x-30',
    'RU': 'y60x-30',
    'UR': 'y30x-30'
}

edges_arrows = {
    'BD': 'B4B7',
    'DB': 'D4D7',
    'BL': 'B4B5',
    'LB': 'L4L3',
    'BR': 'B4B3',
    'RB': 'R4R5',
    'BU': 'B4B1',
    'UB': 'U4U1',
    'DL': 'D4D3',
    'LD': 'L4L7',
    'DR': 'D4D5',
    'RD': 'R4R7',
    'FL': 'F4F3',
    'LF': 'L4L5',
    'FR': 'F4F5',
    'RF': 'R4R3',
    'FU': 'F4F1',
    'UF': 'U4U7',
    'LU': 'L4L1',
    'UL': 'U4U3',
    'RU': 'R4R1',
    'UR': 'U4U5'
}

pieces = {
    'BD': 'bd',
    'BL': 'bl',
    'BR': 'br',
    'BU': 'bu',
    'DB': 'db',
    'DL': 'dl',
    'DR': 'dr',
    'FL': 'fl',
    'FR': 'fr',
    'FU': 'fu',
    'LB': 'lb',
    'LD': 'ld',
    'LF': 'lf',
    'LU': 'lu',
    'RB': 'rb',
    'RD': 'rd',
    'RF': 'rf',
    'RU': 'ru',
    'UB': 'ub',
    'UF': 'uf',
    'UL': 'ul',
    'UR': 'ur',
    'DF': 'df'
}

for first, template in edges_templates.items():
    for second, piece in pieces.items():
        fd = template.replace('x', piece[0]).replace('y', piece[1])

        params = default_params.copy()
        params.update({'fd': fd})

        r = edges_rotation[first]
        params.update({'r': r})

        arw = edges_arrows[first]
        params.update({'arw': arw + '-s7'})

        params.update({'ac': 'purple'})

        path = 'images/{}_{}_comm.'.format(first, second) + fmt
        download_image(path, params)





