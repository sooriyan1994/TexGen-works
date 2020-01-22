# Create a 2D weave textile
weave = CTextileWeave2D(2, 2, 1, 0.2, True)

# Set the weave pattern
weave.SwapPosition(0, 0)
weave.SwapPosition(1, 1)

# Add the textile
AddTextile(weave)
