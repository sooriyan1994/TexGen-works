import numpy

nwarp = input('Number of warp yarns : ')
nweft = input('Number of weft yarns : ')
yarn_spacing = input('Enter the minimum spacing between yarns')
tex_thick = input('Enter the textile thickness')

#Create a 2D weave textile
weave = CTextileWeave2D(nwarp, nweft, yarn_spacing, tex_thick, True)

#Set the weave pattern
weave.SwapPosition(0,0)
weave.SwapPosition(1,1)

#Add the textile
AddTextile(weave)

