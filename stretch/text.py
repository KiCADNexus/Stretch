from .colour import Colour

#https://github.com/KiCad/kicad-source-mirror/blob/93466fa1653191104c5e13231dfdc1640b272777/pcbnew/plugins/kicad/pcb_parser.cpp#L2353

# 0 gr_text
# 1 text
# 2
#   0 at
#   1 66.66
#   2 99.99
# 3
#   0 layer
#   1 F.SilkS
# 4
#   0 hide
# 5
#   0 tstamp
#   1 5E451B20
# 6
#   0 effects
#   1 
#       0 font
#           1
#               0 size
#               1 1.5
#               2 1.5
#           2
#               0 thickness
#               1 0.3
#           3
#               0 bold
#           4
#               0 italic
#   2
#       0 justify
#       1 mirror
#
# ---
# 0 fp_text
# 1 reference / value / user
# 2 text
# 3
#   0 at

pxToMM = 96 / 25.4

class Text(object):

    def __init__(self):
        self.type = 'gr_text'
        self.reference = ''
        self.text = ''
        self.at = []
        self.layer = ''
        self.hide = False
        self.tstamp = ''

        #Effects params
        self.size = [1.27, 1.27]
        self.thickness = 0
        self.bold = False
        self.italic = False
        # Left, right, top, bottom, or mirror
        self.justify = ''



    def From_PCB(self, input):

        #gr_text is user-created label, fp_text is module ref/value
        if input[0] == 'gr_text':
            self.reference = 'gr_text'
            self.text = input[1]
            self.type = 'gr_text'

        elif input[0] == 'fp_text':
            self.reference = input[1]
            self.text = input[2]
            self.type = 'fp_text'

        for item in input:
            if type(item) == str:
                if item == 'hide':
                    self.hide = True

            if item[0] == 'at':
                self.at = item[1:]
                
            if item[0] == 'layer':
                self.layer = item[1]
                
            if item[0] == 'tstamp':
                self.tstamp = item[1]

            if item[0] == 'effects':
                for effect in item[1:]:
                    if effect[0] == 'font':
                        for param in effect[1:]:
                            if param[0] == 'size':
                                self.size = [param[1], param[2]]
                            if param[0] == 'thickness':
                                self.thickness = param[1]
                    elif effect[0] == 'justify':
                        self.justify = effect[1] 


    def To_PCB(self):
        pcb = [self.type]

        if self.reference != "":
            pcb.append(self.reference)

        pcb.append(self.text)

        at = ['at'] + self.at

        pcb.append(at)

        pcb.append(self.layer)

        if self.hide == True:
            pcb.append("hide")

        if self.tstamp:
            pcb.append(['tstamp', self.tstamp])

        font = ['font', ['size'] + self.size, ['thickness', self.thickness]]

        effects = ['effects', font]

        if self.justify:
            justify = ['justify', self.justify]
            effects.append(justify)
            
        pcb.append(effects)



        return pcb


    def From_SVG(self, tag):
        text = []
        
        if tag.has_attr('type'):
            if tag['type'] == 'gr_text':
                self.type = 'gr_text'
            else:
                self.type = 'fp_text'
                self.reference = tag['reference']
            
        self.text = tag.contents[0]

        x = str(float(tag['x']) / pxToMM)
        y = str(float(tag['y']) / pxToMM)
                
        if tag.has_attr('mirrored'):
            if tag['mirrored'] == 'true':
                self.justify = ['mirror']
                x = str(float(x) * -1.0)
            
            
        self.at = [x, y]
        
        if tag.has_attr('layer'):
            layer = ['layer', tag['layer']]
        elif tag.parent.has_attr('inkscape:label'):
            #XML metadata trashed, try to recover from parent tag
            layer = ['layer', tag.parent['inkscape:label']]
        else:
            assert False, "Text not in layer"
            
        self.layer = layer
        
        if tag.has_attr('hide'):
            if tag['hide'] == 'True':
                self.hide = True
        
        if tag.has_attr('tstamp'):
            self.tstamp = tag['tstamp']
        
        style = tag['style']

        styletag = style[style.find('font-size:') + 10:]
        
        size = styletag[0:styletag.find('px')]
        size = str(float(size) / pxToMM)

        self.size = [size, size]
        self.thickness = tag['thickness']
        self.justify = tag['justify']
        if tag.has_attr('bold'):
            self.bold = True
        if tag.has_attr('italic'):
            self.italic = True
        
                

    def To_SVG(self):
        #    transform += 'rotate(' + str(float(item[3]) + r_offset)+ ')'
        #    self.tstamp = 'tstamp="' + item[1] + '" '
        # if item[0] == 'effects':
        #     for effect in item[1:]:
        #         if effect[0] == 'font':
        #             for param in effect[1:]:
        #                 if param[0] == 'size':
        #                     size = [param[1], param[2]]
        #                 if param[0] == 'thickness':
        #                     thickness = param[1]
        #         elif effect[0] == 'justify':
        #             if len(effect) > 1:
        #                 if effect[1] == 'mirror':
        #                     transform += ' scale(-1,1)'
        #                     mirror = -1
        #                     mirror_text = 'mirrored="true" '
                    
        #         else:
        #             effect_text = 'effects="' + ';'.join(effect) + '" '
                        
        # if len(transform) > 0:
        #     print(transform)
        #     transform = 'transform="' + transform + '" '
            
        hidelayer = ''
        mirror = 1
        # if self.layer in self.hiddenLayers:
        #     hidelayer = ';display:none'

        hide = ''
        if self.hide == True:
            hide = 'hide="True" '
            hidelayer = ';display:none'
            
        parameters = '<text '
        parameters += 'xml:space="preserve" '
        parameters += 'style="font-style:normal;font-weight:normal;font-family:sans-serif'
        parameters += ';fill-opacity:1;stroke:none'
        parameters += hidelayer
        parameters += ';font-size:' + str(float(self.size[0]) * pxToMM) + 'px'
        parameters += ';fill:#' + Colour.Assign(self.layer)
        parameters += '" '
        parameters += 'x="' + str(float(self.at[0]) * pxToMM * mirror) + '" '
        parameters += 'y="' + str(float(self.at[1]) * pxToMM) + '" '
        # parameters += 'id="text' + str(id) + '" '
        # parameters += self.effect_text
        # parameters += self.mirror_text
        parameters += 'layer="' + self.layer + '" '
        parameters += 'text-anchor="middle" '
        parameters += 'thickness="' + self.thickness + '" '
        parameters += 'type="' + self.type + '" '
        parameters += 'tstamp="' + self.tstamp + '" '
        parameters += 'justify="' + self.justify + '" '
        parameters += 'reference="' + self.reference + '" '
        parameters += hide
        # parameters += transform
        parameters += '>' + self.text
        parameters += '</text>'

        # print(parameters)

        return parameters
