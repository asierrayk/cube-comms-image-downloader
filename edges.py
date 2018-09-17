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
BL_template_fc = u_face + r_face + f_face + d_face + 'nnnylnnnn' + 'nnnnbxnnn'
BR_template_fc = u_face + 'nnnnrynnn' + f_face + d_face + l_face + 'nnnxbnnnn'
BU_template_fc = 'nynnunnnn' + r_face + f_face + d_face + l_face + 'nxnnbnnnn'
DB_template_fc = u_face + r_face + f_face + 'nnnndnnxn' + l_face + 'nnnnbnnyn'
DL_template_fc = u_face + r_face + f_face + 'nnnxdnnnn' + 'nnnnlnnyn' + b_face
DR_template_fc = u_face + 'nnnnrnnyn' + f_face + 'nnnndxnnn' + l_face + b_face
FL_template_fc = u_face + r_face + 'nnnxfnnnn' + d_face + 'nnnnlynnn' + b_face
FR_template_fc = u_face + 'nnnyrnnnn' + 'nnnnfxnnn' + d_face + l_face + b_face
FU_template_fc = 'nnnnunnxn' + r_face + 'nynnfnnnn' + d_face + l_face + b_face
LB_template_fc = u_face + r_face + f_face + d_face + 'nnnxlnnnn' + 'nnnnbynnn'
LD_template_fc = u_face + r_face + f_face + 'nnnydnnnn' + 'nnnnlnnxn' + b_face
LF_template_fc = u_face + r_face + 'nnnyfnnnn' + d_face + 'nnnnlxnnn' + b_face
LU_template_fc = 'nnnxunnnn' + r_face + f_face + d_face + 'nynnlnnnn' + b_face
RB_template_fc = u_face + 'nnnnrxnnn' + f_face + d_face + l_face + 'nnnybnnnn'
RD_template_fc = u_face + 'nnnnrnnxn' + f_face + 'nnnndynnn' + l_face + b_face
RF_template_fc = u_face + 'nnnxrnnnn' + 'nnnnfynnn' + d_face + l_face + b_face
RU_template_fc = 'nnnnuxnnn'  + 'nynnrnnnn' + f_face + d_face + l_face + b_face
UB_template_fc = 'nxnnunnnn'  + r_face + f_face + d_face + l_face + 'nynnbnnnn'
UF_template_fc = 'nnnnunnxn' + r_face + 'nynnfnnnn' + d_face + l_face + b_face
UL_template_fc = 'nnnxunnnn' + r_face + f_face + d_face + 'nynnlnnnn' + b_face
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
    'BD': 'x-22y30',
    'DB': 'x-22y30',
    'BL': 'x-22y30',
    'LB': 'x-22y30',
    'BR': 'x-90y30x30',
    'RB': 'x-90y30x30',
    'BU': 'x-140',
    'UB': 'x-130',
    'DL': 'y-30x45',
    'LD': 'y-30x45',
    'DR': 'x45y30',
    'RD': 'x45y30',
    'FL': 'x22y30',
    'LF': 'x22y30',
    'FR': 'x-22y30',
    'RF': 'x-22y30',
    'FU': 'x-50',
    'UF': 'x-50',
    'LU': 'x-22y-30',
    'UL': 'x-22y-30',
    'RU': 'x-22y30',
    'UR': 'x-22y-30'
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
    'UR': 'ur'
}

for first, template in edges_templates.items():
    for second, piece in pieces.items():
        fd = template.replace('x', piece[0]).replace('y', piece[1])

        params = default_params.copy()
        params.update({'fd': fd})

        r = edges_rotation[first]
        params.update({'r': r})

        path = 'images/{}_{}_comm.'.format(first, second) + fmt
        download_image(path, params)





