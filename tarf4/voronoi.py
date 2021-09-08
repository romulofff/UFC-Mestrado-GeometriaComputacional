import numpy
from PIL import Image

def voronoi(points,shape=(600,600)):
    depthmap = numpy.ones(shape,numpy.float)*1e308
    colormap = numpy.zeros(shape,numpy.int)

    def hypot(X,Y):
        return (X-x)**2 + (Y-y)**2

    for i,(x,y) in enumerate(points):
        paraboloid = numpy.fromfunction(hypot,shape)
        colormap = numpy.where(paraboloid < depthmap,i+1,colormap)
        depthmap = numpy.where(paraboloid <
depthmap,paraboloid,depthmap)

    for (x,y) in points:
        colormap[x-1:x+2,y-1:y+2] = 0

    return colormap

def draw_map(colormap):
    shape = colormap.shape

    palette = numpy.array([
            0x000000FF,
            0xFF0000FF,
            0x00FF00FF,
            0xFFFF00FF,
            0x0000FFFF,
            0xFF00FFFF,
            0x00FFFFFF,
            0xFFFFFFFF,
            0xFFDDDCCA,
            0x123D432A
            ])

    colormap = numpy.transpose(colormap)
    pixels = numpy.empty(colormap.shape+(4,),numpy.int8)

    pixels[:,:,3] = palette[colormap] & 0xFF
    pixels[:,:,2] = (palette[colormap]>>8) & 0xFF
    pixels[:,:,1] = (palette[colormap]>>16) & 0xFF
    pixels[:,:,0] = (palette[colormap]>>24) & 0xFF

    image = Image.frombytes("RGBA",shape,pixels)
    image.save('voronoi2.png')

if __name__ == '__main__':
    # draw_map(voronoi(([100,300], [200,500], [300,200], [400,500], [500,300], [200,300])))
    draw_map(voronoi(([100,300], [200,500], [300,200], [400,500], [500,300], [245, 431], [105, 381], [444, 333], [200,300])))
#     draw_map(voronoi(([100,100],[356,301],[400,65],[324,145],
# [200,399])))