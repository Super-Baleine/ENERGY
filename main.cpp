#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;
int main(){
	int E, m,L;
	cin >> m >> L;
	E = m*L;cout << E;
	string choice;
	cin >> choice;cout << "\n\n";
	if (choice == "again") {
		return main();
	}else{
		return 0;
	}
return 0;}
