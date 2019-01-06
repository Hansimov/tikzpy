# import png
# png.from_array([[255, 0, 0, 255],
                # [255, 0, 255, 0]], 'L').save("z_test_png.png")

import png
import numpy
rows = numpy.zeros((256, 256, 4), dtype = 'int') # eassier format to deal with each individual pixel
rows[:, :] = [255, 0, 0, 255] # Setting the color red for each pixel
rows[10:40, 10:40] = [0, 255, 255, 255] #  filled squared starting at (10,10) to (40,40)
locs = numpy.indices(rows.shape[0:2])
rows[(locs[0] - 80)**2 + (locs[1] - 80)**2 <= 20**2] = [255, 255, 0, 255] # yellow filled circle, with center at (80, 80) and radius 20
png_writer = png.Writer(width = 256, height = 256, alpha = 'RGBA') # create writer
png_writer.write(open('z_test_png.png', 'wb'), rows.reshape(rows.shape[0], rows.shape[1]*rows.shape[2])) 