trainingImages = fopen(train-images-idx3-ubyte);
numImg = 60000;
imgWidth = 28;
imgHeight
rawImageDataTrain = uint8 (fread(trainingImages, ...
    numImg * numRows * numCols, 'unit8'));
