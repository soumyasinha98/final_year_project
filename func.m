function func()
tim=[0,100]
IC=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[T,Y]=ode45(@(t,x) slidemode11(t,x),tim,IC)
plot(T,Y(:,1),T,Y(:,15))
end