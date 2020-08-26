img=imread('gg.jpg');
img=rgb2gray(img);
img=imresize(img,[256,256],'nearest');
 
h=hadamard(256);
h_t=h.';
F=h*double(img)*h_t/256;
f=h_t*F*h/256;
F(1,1)=0;
disp(isequal(F,zeros([256,256])));
 
res=fft2(img);
res_inv=ifft2(res);
 
c=zeros(256,1);
for i=1:256
    sign_change=0;
    for j=1:255
        if(h(i,j)*h(i,j+1)==-1)
            sign_change=sign_change+1;
        end
    end
    c(i)=sign_change;
end
 
w=zeros(256,256);
for i=1:256
    w(i,:)=h(find(c==i-1),:);
end
 
w_t=w.';
G=w*double(img)*w_t/256;
g=w_t*G*w/256;
 
subplot(3,5,1),imshow(uint8(real(res))),title('FFT-Real');
subplot(3,5,2),imshow(uint8(imag(res))),title('FFT-Imag');
subplot(3,5,3),imshow(uint8(atand(imag(res)/real(res)))),title('FFT-Angle');
subplot(3,5,4),imshow(uint8(abs(res))),title('FFT-Magnitude');
subplot(3,5,5),imshow(uint8(res_inv)),title('Inverse');
 
subplot(3,5,6),imshow(img),title('INPUT');
subplot(3,5,7),imshow(uint8(h)),title('h Matrix');
subplot(3,5,8),imshow(uint8(F)),title('h Transform');
subplot(3,5,9),imshow(uint8(f)),title('Inv h Transform');
 
subplot(3,5,11),imshow(img),title('INPUT');
subplot(3,5,12),imshow(uint8(w)),title('w Matrix');
subplot(3,5,13),imshow(uint8(G)),title('w Transform');
subplot(3,5,14),imshow(uint8(g)),title('Inv w Transform');
