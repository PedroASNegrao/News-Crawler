#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

using namespace std;

int main()
{
	setlocale(LC_ALL, "Portuguese");
	ifstream inFile;
	ofstream newlist;
	string line, filein, fileout;
	string *lista;
	int i, j;
	
	i = 0;
	inFile.open("list.txt");
	newlist.open("newlist.txt");
	if (inFile.is_open()){
		newlist << "[";
		while(getline(inFile,line)){
			newlist << "\"" + line + "\", ";
		}
		newlist << "]";
	inFile.close();
	}
	newlist.close();

	
}
