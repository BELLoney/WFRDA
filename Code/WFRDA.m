%%% A weighted fuzzy rough density-based anomaly (WFRDA) algorithm
%%% Please refer to the following papers: 
%%% Anomaly detection based on weighted fuzzy-rough density, Information Sciences, 2023
%%% Uploaded by Yuan Zhong on July 24, 2021. E-mail:yuanzhong2799@foxmail.com.
function AS=WFRDA(data,sigma)
%%%input:
% data is data matrix without decisions, where rows for samples and columns for attributes. 
% Numeric attribute data is normalized to [0,1].
% Sigma is an adjustable parameter.
%%%output
% Weighted fuzzy rough density-based anomaly score (AS).
[n,m]=size(data); %

delta=zeros(1,m);%Initialize the radius  
for k=1:m
    if all(data(:,k)<=1)
     delta(k)=sigma; %Find the radius of the numeric feature
    end
end

E=zeros(1,m);%complement entropy
%%
FADens=zeros(n,m);
for k=1:m
    x=data(:,k); 
    for i=1:n      
        for j=1:i
              rm(i,j)=wfrda_kersim(x(i),x(j),delta(k)); %Compute relation matrice
              rm(j,i)=rm(i,j);
        end
    end    
rm_temp=rm;
E(k)=-sum((1/n)*log2(sum(rm,2)./n));%Compute fuzzy entropy
FADens(1:n,k)=sum(rm_temp,2)./n;
end
%%
W=E./sum(E);
AS=zeros(n,1);
for i=1:n
    AS(i)=sum((1-FADens(i,:)).*W);
end
end
