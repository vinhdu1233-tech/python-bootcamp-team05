#member 4_dmdung2520 - C++ Starting point
# #include <iostream>
# #include <vector>
# using namespace std;
# vector<int> sieveOfEratosthenes(int n) {
#     vector<bool> is_prime(n + 1, true);
#     if (n >= 0) is_prime[0] = false;
#     if (n >= 1) is_prime[1] = false;
#     for (int p = 2; p * p <= n; p++) {
#         if (is_prime[p]) {
#             for (int i = p * p; i <= n; i += p) {
#                 is_prime[i] = false;
#             }
#         }
#     }
#     vector<int> primes;
#     for (int p = 2; p <= n; p++) {
#         if (is_prime[p]) {
#             primes.push_back(p);
#         }
#     }
#     return primes;
# }
# int main() {
#     int n = 30;
#     vector<int> primes = sieveOfEratosthenes(n);
#     cout << "Cac so nguyen to <= " << n << " la:\n";
#     for (int prime : primes) {
#         cout << prime << " ";
#     }
#     return 0;
# }



#member 4_dmdung2520 - Python Starting Point
def sieve(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False 
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
