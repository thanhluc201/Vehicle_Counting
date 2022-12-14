%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This example tests C++ MEX-file backgroundSubtractorOCV. The MEX function
% uses BackgroundSubtractorMOG2 class in OpenCV. This example shows how to
% use background/foreground segmentation algorithm to find the moving cars
% in a video stream.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    

% Create video reader object
hsrc = vision.VideoFileReader('Sample1.avi', ...
                                  'ImageColorSpace', 'RGB', ...
                                  'VideoOutputDataType', 'uint8');
                              
% Create background/foreground segmentation object
hfg = backgroundSubtractor(5, 16, true); 

% Create blob analysis object
hblob = vision.BlobAnalysis(...
    'CentroidOutputPort', false, 'AreaOutputPort', false, ...
    'BoundingBoxOutputPort', true, 'MinimumBlobArea', 1000);

% Create video player object
hsnk = vision.VideoPlayer('Position',[100 100 660 400]);
frameCnt = 1;

while ~isDone(hsrc)
  % Read frame
  frame  = step(hsrc);
  
  % Compute foreground mask
  fgMask = getForegroundMask(hfg, frame);

  bbox   = step(hblob, fgMask);
  
  % Reset background model
  % This step just demonstrates how to use reset method
  if (frameCnt==10)
      reset(hfg);
  end
  
  % draw bounding boxes around cars
  n = size(bbox);
  N = n(1);

  if N == 0
      continue;
  end

  for i = 1:N
      index = i;
      if(bbox(i,3) <= 200 || bbox(i,4) <= 200)
          bbox(i,:) = [0 0 0 0];
      end
  end

  out = insertShape(frame, 'Rectangle', bbox, 'Color', 'White','LineWidth', 5);

  % view results in the video player
  step(hsnk, out);
  frameCnt = frameCnt + 1;
end

release(hfg);
release(hsnk);
release(hsrc);