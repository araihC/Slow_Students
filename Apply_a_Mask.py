
def Apply_a_mask(img_float, Contours_Limit):
    #This function finds and drows contures of an image given.
    #It returns the cropped image as a numpy array of float
    import numpy as np
    from PIL import Image
    import skimage
    from skimage import data, io, filters, measure, img_as_float, img_as_uint
    from matplotlib import pyplot as plt

#-------------------------------FUNCTION DEFINITION-----------------------------
        #This function drows all contours founded on the mask
    def drawShape(img, coordinates, color):
            # In order to draw our line in red
        img = skimage.color.gray2rgb(img)

            # Make sure the coordinates are expressed as integers
        coordinates = coordinates.astype(int)

        img[coordinates[:, 0], coordinates[:, 1]] = color

        return img
#-------------------------------------------------------------------------------

        #Transform the array to a 2D matrix 100x100
    img_float = img_float.reshape(100,100)
    #plt.matshow(img_float)
    #plt.show()

        # Find contours at a constant value of Contours_Limit (diciamo 0.45)
    contours = measure.find_contours(img_float, Contours_Limit)

        # Display the image and plot all contours found
    fig, ax = plt.subplots()
    ax.imshow(img_float, interpolation='nearest', cmap=plt.cm.gray)

    for n, contour in enumerate(contours):
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    #plt.show()

        #Create a Black mask of the same dimentions of the image
    mask = np.zeros_like(img_float) # Create mask where white is what we want, black otherwise

    #Drow contours on 'mask'
    for contour in contours:
        mask = drawShape(mask, contour, [255, 0, 0])

#------------------------------Rectangoular cut---------------------------------

    #Now crop
    contour_position_x=[]
    contour_position_y=[]

    #print mask [30][2]
    for i in range(len(mask)):
        for j in range(len(mask)):
                #print mask [i][:][:]
                if (np.array_equal(mask[i][j], [255., 0., 0.])):
                    contour_position_x.append([i])
                    contour_position_y.append(j)

    (topx, topy) = (np.min(contour_position_x), np.min(contour_position_y))
    (bottomx, bottomy) = (np.max(contour_position_x), np.max(contour_position_y))
    #print topx, topy
    #print bottomx, bottomy
    cropped  = img_float[topx:bottomx, topy:bottomy]
    plt.matshow(cropped)
    plt.show()
    return(cropped)

#-------------------------------------------------------------------------------
