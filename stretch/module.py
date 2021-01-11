from bs4 import BeautifulSoup

from .arc import Arc
from .circle import Circle
from .curve import Curve
from .layers import Layers
from .line import Line
from .metadata import Metadata
from .pad import Pad
from .poly import Poly
from .segment import Segment
from .text import Text
from .via import Via
from .zone import Zone


# https://github.com/KiCad/kicad-source-mirror/blob/93466fa1653191104c5e13231dfdc1640b272777/pcbnew/plugins/kicad/pcb_parser.cpp#L2839

# 0 module
# 1 Diode_SMD:D_SMD_SOD123
# 2
#   0 layer
#   1 B.Cu
# 3
#   0 tstamp
#   1 0DF
# 4
#   0 at
#   1 66.66
#   2 99.99
# 3
#   0 descr
#   1 0.25
# 4
#   0 tags
#   1 B.Cu
# 5
#   0 path
#   1 1
# 5
#   0 attr
#   1 1
# 5
#   0 fp_text / fp_line / fp_text / pad
#   1 1
#....
#....
# 5
#   0 model
#   1 ${KISYS3DMOD}/Package_TO_SOT_SMD.3dshapes/SOT-23-6.wrl
#   2 offset
#     0 xyz
#     1 0
#     2 0
#     3 0
#   3 scale
#     0 xyz
#     1 1
#     2 1
#     3 1
#   4 rotate
#     0 xyz
#     1 0
#     2 0
#     3 0


pxToMM = 96 / 25.4

class Module(object):

    def __init__(self):
        self.symbol = ''
        self.version = ''
        self.generator = ''
        self.locked = False
        self.placed = False
        self.layer = ''
        self.tedit = ''
        self.tstamp = ''
        self.at = []
        self.descr = ''
        self.tags = ''
        self.property = ''
        self.path = ''
        self.autoplace_cost90 = ''
        self.autoplace_cost180 = ''
        self.solder_mask_margin = ''
        self.solder_paste_margin = ''
        self.solder_paste_ratio = ''
        self.clearance = ''
        self.zone_connect = ''
        self.thermal_width = ''
        self.thermal_gap = ''
        self.attr = []
        self.fp_text = []
        self.fp_arc = []
        self.fp_circle = []
        self.fp_curve = []
        self.fp_rect = []
        self.fp_line = []
        self.fp_poly = []
        self.pad = []
        self.model = ''
        self.zone = []
        self.group = ''
        
        
    def From_PCB(self, pcblist):

        if type(pcblist[1]) != str:
            assert False,"Module: Expected symbol"
            return None

        self.symbol = pcblist[1]
        
        a = 0

        for item in pcblist[2:]:


            if item[0] == 'version':
                self.version = item[1]
                
            if item[0] == 'generator':
                self.generator = item[1]
                
            if item[0] == 'locked':
                self.locked = True
                
            if item[0] == 'placed':
                self.placed = True
                
            if item[0] == 'layer':
                self.layer = item[1]
                
            if item[0] == 'tedit':
                self.tedit = item[1]
                
            if item[0] == 'tstamp':
                self.tstamp = item[1]
            
            if item[0] == 'at':
                self.at += item[1:]
                
            if item[0] == 'descr':
                self.descr = item[1]
                
            if item[0] == 'tags':
                self.tags = item[1]
                
            if item[0] == 'property':
                self.property = item[1]
                
            if item[0] == 'path':
                self.path = item[1]
                
            if item[0] == 'autoplace_cost90':
                self.autoplace_cost90 = item[1]
                
            if item[0] == 'autoplace_cost180':
                self.autoplace_cost180 = item[1]
                
            if item[0] == 'solder_mask_margin':
                self.solder_mask_margin = item[1]
                
            if item[0] == 'solder_paste_margin':
                self.solder_paste_margin = item[1]
                
            if item[0] == 'solder_paste_ratio':
                self.solder_paste_ratio = item[1]
                
            if item[0] == 'clearance':
                self.clearance = item[1]
                
            if item[0] == 'zone_connect':
                self.zone_connect = item[1]
                
            if item[0] == 'thermal_width':
                self.thermal_width = item[1]
                
            if item[0] == 'thermal_gap':
                self.thermal_gap = item[1]
                
            if item[0] == 'attr':
                self.attr += item[1:]
                
            if item[0] == 'fp_text':
                # for fp_text in item:
                text = Text()
                # text.From_PCB(item)
                # self.fp_text.append(text)
                
            if item[0] == 'fp_line':
                line = Line()
                line.From_PCB(item)
                self.fp_line.append(line)



            # if item[0] == 'model':
                # svg.g['model'] = item[1] + ';'
                # #offset
                # svg.g['model'] += item[2][1][1] + ',' + item[2][1][2] + ',' + item[2][1][3] + ';'
                # #scale
                # svg.g['model'] += item[3][1][1] + ',' + item[3][1][2] + ',' + item[3][1][3] + ';'
                # #rotate
                # svg.g['model'] += item[4][1][1] + ',' + item[4][1][2] + ',' + item[4][1][3] + ';'

            # if item[0] == 'fp_line':
                # tag = BeautifulSoup(self.Convert_Gr_Line_To_SVG(item, str(id) + '-' + str(a)), 'html.parser')
                # svg.g.append(tag)

            # if item[0] == 'fp_curve':
                # tag = BeautifulSoup(self.Convert_Gr_Curve_To_SVG(item, str(id) + '-' + str(a)), 'html.parser')
                # svg.g.append(tag)

            # if item[0] == 'fp_text':
                # tag = BeautifulSoup(self.Convert_Gr_Text_To_SVG(item, str(id) + '-' + str(a), rotate), 'html.parser')
                # svg.g.append(tag)

            # elif item[0] == 'pad':
                # tag = BeautifulSoup(self.Convert_Pad_To_SVG(item, str(id) + '-' + str(a), rotate), 'html.parser')
                # svg.g.append(tag)

            # a += 1



    def To_SVG(self):
        svg = BeautifulSoup('<g type="module" name="' + self.symbol + '">', 'html.parser')
        

        if self.version != '':
            svg.g['version'] = self.version
            
        if self.generator != '':
            svg.g['generator'] = self.generator
            
        if self.locked == True:
            svg.g['locked'] = 'true'
            
        if self.placed == True:
            svg.g['placed'] = 'true'
            
        if self.layer != '':
            svg.g['layer'] = self.layer
        else:
            svg.g['layer'] = 'F.Cu'
            
        if self.tedit != '':
            svg.g['tedit'] = self.tedit
            
        if self.tstamp != '':
            svg.g['tstamp'] = self.tstamp

        #at
        x = float(self.at[0]) * pxToMM
        y = float(self.at[1]) * pxToMM
        rotate = 0

        transform = 'translate(' + str(x) + ',' + str(y) + ')'

        if len(self.at) > 2:
            rotate = float(self.at[2])
            transform += ' rotate(' + str(-1 * rotate) + ')'

        svg.g['transform'] = transform
            
        for item in self.fp_line:
            tag = BeautifulSoup(item.To_SVG(), 'html.parser')
            layer = item.layer
            svg.g.append(tag)
            


            # if item[0] == 'model':
                # svg.g['model'] = item[1] + ';'
                # #offset
                # svg.g['model'] += item[2][1][1] + ',' + item[2][1][2] + ',' + item[2][1][3] + ';'
                # #scale
                # svg.g['model'] += item[3][1][1] + ',' + item[3][1][2] + ',' + item[3][1][3] + ';'
                # #rotate
                # svg.g['model'] += item[4][1][1] + ',' + item[4][1][2] + ',' + item[4][1][3] + ';'

            # if item[0] == 'fp_line':
                # tag = BeautifulSoup(self.Convert_Gr_Line_To_SVG(item, str(id) + '-' + str(a)), 'html.parser')
                # svg.g.append(tag)

            # if item[0] == 'fp_curve':
                # tag = BeautifulSoup(self.Convert_Gr_Curve_To_SVG(item, str(id) + '-' + str(a)), 'html.parser')
                # svg.g.append(tag)

            # if item[0] == 'fp_text':
                # tag = BeautifulSoup(self.Convert_Gr_Text_To_SVG(item, str(id) + '-' + str(a), rotate), 'html.parser')
                # svg.g.append(tag)

            # elif item[0] == 'pad':
                # tag = BeautifulSoup(self.Convert_Pad_To_SVG(item, str(id) + '-' + str(a), rotate), 'html.parser')
                # svg.g.append(tag)

            # a += 1

        return svg


        
    def Parse_Module(self, tag):
        # print(tag['id'])
        module = ['module', tag['name'], ['layer', tag['layer']]]
        segments = []
        gr_lines = []
        gr_arcs = []
        gr_curves = []
        gr_polys = []
        pads = []
        zones = []
        transform = tag['transform']
        
        translate = transform[transform.find('translate(') + 10:]
        translate = translate[0:translate.find(')')]
        x = translate[0:translate.find(',')]
        y = translate[len(x) + 1:]
        x = float(x) / pxToMM
        y = float(y) / pxToMM

        rotate = 0
        if 'rotate(' in transform:
            rotate = transform[transform.find('rotate(') + 7:]
            rotate = float(rotate[0:-1]) * -1

        
        if tag.has_attr('tedit'):
            module.append(['tedit', tag['tedit']])

        if tag.has_attr('tstamp'):
            module.append(['tstamp', tag['tstamp']])

        at = ['at', str(x), str(y), str(rotate)]
        module.append(at)
        
        if tag.has_attr('descr'):
            module.append(['descr', tag['descr']])

        if tag.has_attr('tags'):
            module.append(['tags', tag['tags']])

        if tag.has_attr('path'):
            module.append(['path', tag['path']])

        if tag.has_attr('attr'):
            module.append(['attr', tag['attr']])
            
        for text in tag.find_all('text'):
            module.append(self.Parse_Text(text))

        if tag.has_attr('model'):
            modeltag = tag['model']
            model = ['model']
            model.append(modeltag[0:modeltag.find(';')])
            modeltag = modeltag[modeltag.find(';') + 1:]
            offset = ['xyz'] + modeltag[0:modeltag.find(';')].split(',')
            modeltag = modeltag[modeltag.find(';') + 1:]
            scale = ['xyz'] + modeltag[0:modeltag.find(';')].split(',')
            modeltag = modeltag[modeltag.find(';') + 1:]
            rotate = ['xyz'] + modeltag[0:modeltag.find(';')].split(',')
            model.append(['offset', offset])
            model.append(['scale', scale])
            model.append(['rotate', rotate])
            
            module.append(model)

        for path in tag.find_all('path'):
            if path.has_attr('type') == True and path['type'] == 'zone':
                zones.append(self.Parse_Zone(path))
            else:
                segment, gr_line, gr_arc, gr_curve = self.Parse_Segment(path)
                segments = segments + segment
                gr_line[0][0] = 'fp_line'
                gr_lines += gr_line
                gr_arcs += gr_arc
                gr_curves += gr_curve

        for rect in tag.find_all('rect'):
            pad = self.Parse_Pad(rect, 'rect')
            if pad != None:
                pads.append(pad)
        for circle in tag.find_all('circle'):
            pad = self.Parse_Pad(circle, 'circle')
            if pad != None:
                pads.append(pad)

        if len(segments) > 0:
            module.append(segments)
        if len(pads) > 0:
            module = module + pads
            
        gr_lines.reverse()
        gr_arcs.reverse()
        gr_curves.reverse()
        gr_polys.reverse()
        zones.reverse()
            
        module = module + gr_lines + gr_arcs + gr_curves + gr_polys + zones
        return module

