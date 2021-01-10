from bs4 import BeautifulSoup

from .layers import Layers
from .segment import Segment

#https://github.com/KiCad/kicad-source-mirror/blob/93466fa1653191104c5e13231dfdc1640b272777/pcbnew/plugins/kicad/pcb_parser.cpp#L533

# kicad_pcb
# version
# host
# general
# page
# title_block
# layers
# setup
# net
# net_class
# module
# dimension
# gr_line
# gr_arc
# gr_text
# segment
# via
# zone

#Prettifies SVG output, but messes up text field spacing
debug = False

class Board(object):

    def __init__(self):
        self.general = ''
        self.paper = ''
        self.title_block = ''
        self.layers = ''
        self.setup = ''
        self.property = ''
        self.net = ''
        self.net_class = ''
        self.gr_arc = ''
        self.gr_curve = ''
        self.gr_line = ''
        self.gr_poly = ''
        self.gr_circle = ''
        self.gr_rect = ''
        self.gr_text = ''
        self.gr_dimension = ''
        self.module = ''
        self.footprint = ''
        self.segment = []
        self.arc = ''
        self.group = ''
        self.via = ''
        self.zone = ''
        self.target = ''
        
        
    def From_PCB(self, pcb):
        # svg = ''
        dic = []
        segments = []

        i = 0
        for item in pcb:
            if type(item) is str:
                print(item)
            else:
            
                if item[0] == 'layers':
                    print(item[0])
                    self.layers = Layers()
                    self.layers.From_PCB(item)
                    
                elif item[0] == 'module':
                    print(item[0])

                elif item[0] == 'segment':
                    print(item[0])
                    segment = Segment()
                    segment.From_PCB(item)
                    self.segment.append(segment)
                    # tag = BeautifulSoup(self.Convert_Segment_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                elif item[0] == 'gr_line':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Gr_Line_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)
                    
                elif item[0] == 'gr_poly':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Gr_Poly_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                elif item[0] == 'gr_arc':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Gr_Arc_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                elif item[0] == 'gr_curve':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Gr_Curve_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                elif item[0] == 'gr_text':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Gr_Text_To_SVG(item, i), 'html.parser')
                    # layer = tag.find('text')['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                elif item[0] == 'zone':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Zone_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # if layer:
                        # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                elif item[0] == 'via':
                    print(item[0])
                    # tag = BeautifulSoup(self.Convert_Via_To_SVG(item, i), 'html.parser')
                    # base.svg.find('g', {'inkscape:label': 'Vias'}, recursive=False).append(tag)
                    
                else:
                    print(item[0])
                    # svg = self.Convert_Metadata_To_SVG(item)
                    # base.svg.kicad.append(BeautifulSoup(svg, 'html.parser'))
                    
                    
    def To_SVG(self):
        # svg = ''
        dic = []
        segments = []

        base.svg.append(BeautifulSoup('<kicad />', 'html.parser'))

        layers = self.layers.To_SVG()
       
        for layer in layers:
            tag = BeautifulSoup(layer, 'html.parser')
            base.svg.append(tag)
                             
        # for item in items:
            # if type(item) is str:
                # print(item)
            # else:
                # if item[0] == 'module':
                    # base.svg.append(self.Convert_Module_To_SVG(item, i))
            # i = i + 1
            
        base.svg.append(BeautifulSoup('<g inkscape:label="Vias" inkscape:groupmode="layer" id="layervia" user="True" />', 'html.parser'))


        for item in self.segment:
            tag = BeautifulSoup(item.To_SVG(), 'html.parser')
            layer = item.layer
            base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)
        
        
        # for item in items:
            # if type(item) is str:
                # print(item)
            # else:
                # # print(item[0])

                # elif item[0] == 'gr_line':
                    # tag = BeautifulSoup(self.Convert_Gr_Line_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)
                    
                # elif item[0] == 'gr_poly':
                    # tag = BeautifulSoup(self.Convert_Gr_Poly_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                # elif item[0] == 'gr_arc':
                    # tag = BeautifulSoup(self.Convert_Gr_Arc_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                # elif item[0] == 'gr_curve':
                    # tag = BeautifulSoup(self.Convert_Gr_Curve_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                # elif item[0] == 'gr_text':
                    # tag = BeautifulSoup(self.Convert_Gr_Text_To_SVG(item, i), 'html.parser')
                    # layer = tag.find('text')['layer']
                    # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                # elif item[0] == 'zone':
                    # tag = BeautifulSoup(self.Convert_Zone_To_SVG(item, i), 'html.parser')
                    # layer = tag.path['layer']
                    # if layer:
                        # base.svg.find('g', {'inkscape:label': layer}, recursive=False).append(tag)

                # elif item[0] == 'via':
                    # tag = BeautifulSoup(self.Convert_Via_To_SVG(item, i), 'html.parser')
                    # base.svg.find('g', {'inkscape:label': 'Vias'}, recursive=False).append(tag)
                    
                # elif item[0] != 'layers' and item[0] != 'module':
                    # # Already handled above
                    # svg = self.Convert_Metadata_To_SVG(item)
                    # base.svg.kicad.append(BeautifulSoup(svg, 'html.parser'))
                    
            # i = i + 1
        dic.append({'segment': segments})

        if debug == True:
            svg = base.prettify("utf-8")
        else:
            svg = base.encode()
        
        return svg
        
        
base = BeautifulSoup('''
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   viewBox="0 0 210 297"
   version="1.1"
   id="svg8290"
   inkscape:version="0.92.4 (5da689c313, 2019-01-14)"
   sodipodi:docname="base.svg">
  <defs
     id="defs8284" />
  <sodipodi:namedview
     id="base"
     pagecolor="#000000"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.7"
     inkscape:cx="-8.4507329"
     inkscape:cy="782.79942"
     inkscape:document-units="mm"
     inkscape:current-layer="svg8290"
     showgrid="false"
     inkscape:window-width="1920"
     inkscape:window-height="1137"
     inkscape:window-x="-8"
     inkscape:window-y="32"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata1">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
</svg>
''', 'html.parser')