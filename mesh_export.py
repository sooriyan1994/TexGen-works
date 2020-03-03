from TexGen.Core import *

# Read in the textile
ReadFromXML('textile.tg3')

# Get a hold of the textile we just loaded in
textile = GetTextile()

# Create a mesh instance
mesh = CMesh()
# Add the volume of the textile to the mesh
textile.AddVolumeToMesh(mesh, True)

file = open("mesh.vtk", "w")

# Write the header
file.write("# vtk DataFile Version 2.0\n")
file.write("Textile mesh data\n")
file.write("ASCII\n")
file.write("DATASET UNSTRUCTURED_GRID\n")

# Write the points
file.write("POINTS %d float\n" % mesh.GetNumNodes())
for node in mesh.GetNodes():
	file.write("%g %g %g\n" % (node.x, node.y, node.z))

# Get element information from the mesh
wedgeIndices = list(mesh.GetIndices(CMesh.WEDGE))
hexIndices = list(mesh.GetIndices(CMesh.HEX))
numWedges = len(wedgeIndices)/6
numHexes = len(hexIndices)/8

# Write the element information
file.write("CELLS %d %d\n" % (numWedges+numHexes, numWedges*7+numHexes*9))
for i in range(numWedges):
	file.write("6 %d %d %d %d %d %d\n" % tuple(wedgeIndices[i*6:(i+1)*6]))
for i in range(numHexes):
	file.write("8 %d %d %d %d %d %d %d %d\n" % tuple(hexIndices[i*8:(i+1)*8]))

file.write("CELL_TYPES %d\n" % (numWedges+numHexes))
for i in range(numWedges):
	file.write("13\n")
for i in range(numHexes):
	file.write("12\n")
