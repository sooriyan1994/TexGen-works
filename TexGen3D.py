# Create a textile
Textile = CTextile()

# Define some parameters
# Spacing between weft yarns
sx = 2
# Spacing between warp yarns
sy = 0.8
# Vertical distance between yarns at cross overs
sz = 0.16

# Width of the weft yarns is less than the weft spacing
weftyarnwidth = 1.2
# Width of the warp yarns set equal to the warp spacing
warpyarnwidth = sy
# Yarn height equal to the vertical distance between yarns at cross overs
yarnheight = sz

# Create warp stuffer yarns
for i in range(3):
    yarn = CYarn()
    yarn.AddNode(CNode(XYZ(0, 0, 2*i*sz)))
    yarn.AddNode(CNode(XYZ(2*sx, 0, 2*i*sz)))

    yarn.AssignInterpolation(CInterpolationCubic())
    yarn.AssignSection(CYarnSectionConstant(CSectionEllipse(warpyarnwidth, yarnheight)))
    yarn.SetResolution(20)
    yarn.AddRepeat(XYZ(2*sx, 0, 0))
    yarn.AddRepeat(XYZ(0, 2*sy, 0))

    Textile.AddYarn(yarn)

# Create weft stuffer yarns
for i in range(4):
    yarn = CYarn()
    yarn.AddNode(CNode(XYZ(0, 0, (2*i-1)*sz)))
    yarn.AddNode(CNode(XYZ(0, 2*sy, (2*i-1)*sz)))

    yarn.AssignInterpolation(CInterpolationCubic())
    yarn.AssignSection(CYarnSectionConstant(CSectionEllipse(weftyarnwidth, yarnheight)))
    yarn.SetResolution(20)
    yarn.AddRepeat(XYZ(sx, 0, 0))
    yarn.AddRepeat(XYZ(0, 2*sy, 0))

    Textile.AddYarn(yarn)

# Create warp binder yarns
top = 6*sz
bottom = -2*sz

oh = 0.5*weftyarnwidth+0.12
ov = 0.8*sz

yarn = CYarn()
yarn.AddNode(CNode(XYZ(0, sy, top)))
yarn.AddNode(CNode(XYZ(oh, sy, top-ov)))
yarn.AddNode(CNode(XYZ(sx-oh, sy, bottom+ov)))
yarn.AddNode(CNode(XYZ(sx, sy, bottom)))
yarn.AddNode(CNode(XYZ(sx+oh, sy, bottom+ov)))
yarn.AddNode(CNode(XYZ(2*sx-oh, sy, top-ov)))
yarn.AddNode(CNode(XYZ(2*sx, sy, top)))

yarn.AssignInterpolation(CInterpolationBezier())
yarn.AssignSection(CYarnSectionConstant(CSectionEllipse(warpyarnwidth, yarnheight)))
yarn.SetResolution(20)
yarn.AddRepeat(XYZ(2*sx, 0, 0))
yarn.AddRepeat(XYZ(sx, 2*sy, 0))

Textile.AddYarn(yarn)

Textile.AssignDomain(CDomainPlanes(XYZ(-0.5*sx,-0.5*sy,bottom-sz), XYZ(1.5*sx,3.5*sy,top+sz)))

# Add the textile to our TexGen singleton
AddTextile(Textile)