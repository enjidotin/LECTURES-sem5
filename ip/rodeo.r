clc;

a = imread("me.jpg");
b = imread("img2.png");
ag = rgb2gray(a);
img1 = imresize(ag, [256, 256]);
img2 = imresize(b, [256, 256]);

n = input("Choose a Distance Measure: ");


fprintf("--Without For Loop--\n\n");

p = 3;
tic
md = nthroot(sum(abs((double(img1) - double(img2))).^p, "all"), p);
toc
fprintf("Minkowaski Distance: %f\n\n", md);

tic
ed = nthroot(sum(abs((double(img1) - double(img2))).^2, "all"), 2);
toc
fprintf("Euclidian Distance: %f\n\n", ed);

tic
cd = sum(abs(double(img1) - double(img2)), "all");
toc
fprintf("City Block Distance: %f\n\n", cd);

tic
cbd = max(abs( double(img1) - double(img2) ), [], "all");
toc
fprintf("Chess Board Distance: %f\n\n", cbd);


fprintf("--With For Loop--\n\n");

MD = 0;
p = 3;
tic
for i = 1:256
    for j = 1:256
        MD = MD + abs(double(img1(i,j)) - double(img2(i,j)) ).^p;
    end
end
toc
MD = double(MD).^(double(1/p));
fprintf("Minkowaski Distance: %f\n\n", MD);


ED = 0;
ED = double(ED);
tic
for i = 1:256
    for j = 1:256
        ED = ED + abs( double(img1(i,j)) - double(img2(i,j)) ).^2;
    end
end
toc
ED = ED.^(double(0.5));
fprintf("Euclidian  Distance: %f\n\n", ED);


CD = 0;
tic
for i = 1:256
    for j = 1:256
        CD = CD + abs( double(img1(i,j)) - double(img2(i,j)) );
    end
end
toc
fprintf("City Block Distance: %f\n\n", CD);

CBD = 0;
tic
for i = 1:256
    for j = 1:256
        x = abs( double(img1(i,j)) - double(img2(i,j)) );
        if x > CBD
            CBD = x;
        end
    end
end
toc
fprintf("Chess Board Distance: %f\n\n", CBD);