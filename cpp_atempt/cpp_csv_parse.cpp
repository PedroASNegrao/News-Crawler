#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

using namespace std;


void whriteSection(string section){
	
	ofstream initialEdit;
	int j, k, t, index, increment;
	string stringAdd = "";
	string items[9] = {"id", "category", "excerpt", "title", "date", "credit", "url", "category_father", "\'content"};
	//string id = "", category = "", excerpt = "", title = "", date = "", image = "", credit = "", url = "", category_father = "", content = "", date_single = "";
	initialEdit.open("news_metropoles_parsed.txt", fstream::app);
	
	/*
	if (initialEdit.is_open()){
		//for (j=0; j<11; j++ ){
		j=8;
			//cout << items[j] << endl;
			size_t found = section.find(items[j]);
			index = section[found + items[j].size()];
			k=0;
			stringAdd = "";
			while(section[found + items[j].size()+ k] == '\'' || section[found + items[j].size()+k] == ' ' ){
				k++;
			}
			
			while(section[found + items[j].size() + k] != '\''){
				if(section[found + items[j].size() + k] != ','){
					stringAdd += section[found + items[j].size() + k];
				}
				else{
					stringAdd += ' ';
				}
				k++;
			}
			
			cout << stringAdd;
			
			stringAdd += ",";
			initialEdit << stringAdd;
				
		//}
	initialEdit << "\n";
	initialEdit << "teste";
	initialEdit.close();
	}
	
	*/
	
	
	if (initialEdit.is_open()){
		for (j=0; j<9; j++ ){
			//cout << items[j] << endl;
			size_t found = section.find(items[j]);
			index = section[found + items[j].size() + 3];
			k=0;
			stringAdd = "";
			while(section[found + items[j].size()+ k] == '\'' || section[found + items[j].size()+k] == ' ' ){
				k++;
			}
			
			while(section[found + items[j].size() + k] != '\''){
				if(section[found + items[j].size() + k] != ','){
					stringAdd += section[found + items[j].size() + k];
				}
				else{
					stringAdd += ' ';
				}
				k++;
			}
			
			stringAdd += ",";
			initialEdit << stringAdd;
				
		}
	
	initialEdit << "\n";
	//initialEdit << "teste";
	initialEdit.close();
	}
	
	
	
	/*
	size_t found = section.find(string1); 
	
	index = section[found + string1.size() + 3];
	
	j = 0;
	
	while(section[found + string1.size() + 3 + j] != '\''){
		id += section[found + string1.size() + 3 + j];
		j++;
	}
	
	
	initialEdit.open("news_metropoles_parsed.txt", fstream::app);
	if (initialEdit.is_open()){
		initialEdit << id;
		initialEdit.close();
	}
	*/
}

void metropoles_parse(){
	ifstream inFile;
	string line, section;
	long int tamanho, i, row;
	bool record;
	int *v;
	
	ofstream initialEdit;
	int j, k, t, index, increment;
	string stringAdd = "";
	string items[9] = {"id", "category", "excerpt", "title", "date", "credit", "url", "category_father", "\'content"};
	
	inFile.open("news_metropoles.txt");
	initialEdit.open("news_metropoles_parsed.txt", fstream::app);
	
	if (!inFile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }
	
	//pegar o numero de linhas;
	//getline(inFile,line);
	//cout << line[line.size()-1] << endl;
	row = 0;
	record = true;
	
	//for(i=0; i<70; i++){
	while(getline(inFile,line)){
		
		if(line[0] == '\"'){
			//cout << "OK"<< endl;
			record = true;	
		}
		
		if(line[line.size()-1] == '\"'){
			record = false;
		}
		
		if(record == false){
			section += line;
			row++;
			cout << "Loading: " + row << endl;
			
				if (initialEdit.is_open()){
					for (j=0; j<9; j++ ){
						//cout << items[j] << endl;
						size_t found = section.find(items[j]);
						index = section[found + items[j].size() + 3];
						k=0;
						stringAdd = "";
						while(section[found + items[j].size()+ k] == '\'' || section[found + items[j].size()+k] == ' ' ){
							k++;
						}
						
						while(section[found + items[j].size() + k] != '\''){
							if(section[found + items[j].size() + k] != ','){
								stringAdd += section[found + items[j].size() + k];
							}
							else{
								stringAdd += ' ';
							}
							k++;
						}
						
						stringAdd += ",";
						initialEdit << stringAdd;
							
					}
				
				initialEdit << "\n";
				//initialEdit << "teste";
				
				}
			section = "";
		}
		else{
			section += line;
			//cout << "secao AGREGADA: " + section << endl;
		}
	}
	
	
	
	initialEdit.close();
	inFile.close();
	
}

void correio_parse(){
	
}

int main()
{
	setlocale(LC_ALL, "Portuguese");
	ofstream initialEdit;
	
	initialEdit.open("news_metropoles_parsed.txt");
	if (initialEdit.is_open()){
		initialEdit << "id, category, excerpt, title, date, credit, url, category_father, content \n";
		initialEdit.close();
	}
	metropoles_parse();
	
	
    //cout << "Hello World" << endl;
}

