% Chenghung Yeh
% 7/20/2017
% % sample code
% I = imread('sample files\circle0.tif');
% figure;imagesc(I);
% [x, y] = getpts
% BW = roipoly(I,x,y);
% figure;imagesc(BW)

close all;
filesname = 'P06_L01_020_C';
I = imread(['training data\' filesname '.tiff']);
BW = false(size(I,1),size(I,2));
start = 1;
figure1 = figure;
% axes1 = axes('Parent',figure1);hold(axes1,'all');
imagesc(I);
hold on;
while(start)
    [x, y] = getpts;
    
    BW_tmp = roipoly(I,x,y);
    plot([x' x(1)],[y' y(1)])
    prompt2 = 'Save result? 1:yes, 0:no ';
    saveID = input(prompt2)
    if(saveID)
        BW = BW + BW_tmp;
    end
    
    prompt = 'Continue? 1:yes, 0:no ';
    start = input(prompt)
end
% I = imread('sample files\circle0.tif');
% figure;imagesc(I);
% [x, y] = getpts
% BW = roipoly(I,x,y);
saveas(figure1,['training data\' filesname '_overlay.jpg'])
imwrite(I,['training data\' filesname '.tif'])
imwrite(BW,['training data\' filesname '_mask.tif'])
figure;imagesc(BW)
