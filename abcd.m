final_point=3;
time=1:0.01:final_point;
omega=2*pi*4;
y1=2.5*sin(omega*time);
% %FFT
acc_inpt=y1;
n_fft=length(acc_inpt);
 
ff=fft(acc_inpt,n_fft);
num_points=n_fft; 
ff=ff/(num_points/2);
figure;
plot(abs(ff))