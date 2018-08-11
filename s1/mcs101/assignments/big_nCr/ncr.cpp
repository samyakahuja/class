#include <iostream>
#include <cmath>
#include <vector>

bool isPrime(int x){
    if(x == 2 || x == 3) return true;
    for(int i = 2; i * i <= x; i++){
        if(x % i == 0) return false;
        else if((i + 1) > sqrt(x)) return true;
    }
}

//occurence of f in n!
int fact(int n, int f){
    int sum = 0;
    while(n >= f){
        sum += (int) n / f;
        n = (int) n / f;
    }    
    return sum;
}

int main(){ 
    int n,r,nr;
    std::cout<<"Enter n in nCr\t";
    std::cin>>n;
    std::cout<<"Enter r in nCr\t";
    std::cin>>r;
    nr = n - r;

    if(n < 0 || r < 0){
        std::cout<<"Enter +ve integers\n";
        return 0;
    }
    if(r > n){
        std::cout<<"0\n";
        return 0;
    }
    if(r == 0 || n == r){
        std::cout<<"1\n";
        return 0;
    }

    //vectors for prime factors of n,r,and n-r
    std::vector<int> nVec;
    std::vector<int> rVec;
    std::vector<int> nrVec;

    std::vector<int> nFac(n);
    std::vector<int> rFac(n);
    std::vector<int> nrFac(n);

    for(int i = 2; i <= n; i++){
        //check if i is prime
        if(!isPrime(i)) continue;
        nVec.push_back(i);
    }

    for(int i = 2; i <= r; i++){
        //check if i is prime
        if(!isPrime(i)) continue;
        rVec.push_back(i);
    }

    for(int i = 2; i <= nr; i++){
        //check if i is prime
        if(!isPrime(i)) continue;
        nrVec.push_back(i);
    }

    for(int i = 0; i < nVec.size(); i++){
        nFac[nVec[i] - 2] = fact(n, nVec[i]);
    }
    
    for(int i = 0; i < rVec.size(); i++){
        rFac[rVec[i] - 2] = fact(r, rVec[i]);
    }
    
    for(int i = 0; i < nrVec.size(); i++){
        nrFac[nrVec[i] - 2] = fact(nr, nrVec[i]);
    }

    bool show = false;

    for(int i = 0; i < nFac.size(); i++){
        nFac[i] = nFac[i] - rFac[i] - nrFac[i];
        if(nFac[i] != 0){
            if(show) std::cout<<" * ";
            std::cout<<i + 2<<"^"<<nFac[i];
            show = true;
        }
    }
    std::cout<<"\n";
    return 0;
}

