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
	string items[11] = {"id", "category", "excerpt", "title", "date", "image", "credit", "url", "category_father", "content", "date_single"};
	//string id = "", category = "", excerpt = "", title = "", date = "", image = "", credit = "", url = "", category_father = "", content = "", date_single = "";
	initialEdit.open("news_metropoles_parsed.txt", fstream::app);
	
	/*
	if (initialEdit.is_open()){
		//for (j=0; j<11; j++ ){
		j=2;
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
			
			//stringAdd += ",";
			//initialEdit << stringAdd;
				
		//}
	initialEdit << "\n";
	initialEdit << "teste";
	initialEdit.close();
	}
	*/
	
	if (initialEdit.is_open()){
		for (j=0; j<11; j++ ){
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
	initialEdit << "teste";
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
	int tamanho, i, row;
	bool record;
	int *v;
	
	inFile.open("news_metropoles.txt");
	
	if (!inFile) {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }
	
	//pegar o numero de linhas;
	//getline(inFile,line);
	//cout << line[line.size()-1] << endl;
	
	for(i=0; i<30; i++){
		getline(inFile,line);
		
		if(line[0] == '\"'){
			//cout << "OK"<< endl;
			record = true;	
		}
		
		if(line[line.size()-1] == '\"'){
			record = false;
		}
		
		if(record == false){
			whriteSection(section);
			section += line;
		}
		else{
			section += line;
			//cout << "secao AGREGADA: " + section << endl;
		}
	}
	
	record = true;
	row = 0;
	/*	
	while(getline(inFile,line)){
		
		if(line[0] == "\""){
			record = true;	
		}
		
		if(line[line.size()-1] == "\""){
			record = false;
		}
		
		if(record == false){
			whriteSection();
			section = "";
		}
		else{
			section += line
		}
		
		
		row++;
	} 
	*/
	
	inFile.close();
	
}

int main()
{
	setlocale(LC_ALL, "Portuguese");
	ofstream initialEdit;
	initialEdit.open("news_metropoles_parsed.txt");
	if (initialEdit.is_open()){
		initialEdit << "id, category, excerpt, title, date, image, credit, url, category_father, content, date_single \n";
		initialEdit.close();
	}
	metropoles_parse();
    //cout << "Hello World" << endl;
}

