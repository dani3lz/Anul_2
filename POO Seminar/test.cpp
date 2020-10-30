#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

class persoana{
public:
    string name;
    int anul;
    persoana(){
        name = "";
        anul = 0;
    }
};

class Sofer : public persoana{
protected:
    double distanta_parcursa;
    double plata_pentru_km;
public:
    Sofer(){
        distanta_parcursa = 0;
        plata_pentru_km = 0;
    }
    void citire(){
        cout << "Numele: "; cin >> name;
        cout << "Anul nasterii: "; cin >> anul;
        cout << "Distanta parcursa: "; cin >> distanta_parcursa;
        cout << "Plata pentru 1 km: "; cin >> plata_pentru_km;
    }
    double salariu(){
        double salariul;
        salariul = distanta_parcursa * plata_pentru_km;
        return salariul;
    }
    void afisare(){
        cout << "Numele: " << name << endl;
        cout << "Anul nasterii: " << anul << endl;
        cout << "Salariul: " << salariu() << endl;
    }
};

int main(){
    int n;
    cout << "Dati numarul de soferi: "; 
    cin >> n;
    Sofer *tir = new Sofer[n];
    for(int i = 0; i < n; i++){
        tir[i].citire();
    }
    int tanar, j=0;
    tanar = tir[0].anul;
    for(int i = 0; i < n; i++){
        if(tir[i].anul > tanar ){
            tanar = tir[i].anul;
            j = i;
        }
    }
    cout << "\n\nCel mai tanar sofer:" << endl;
    tir[j].afisare();
   double maxim;
    int h=0;
    maxim = tir[0].salariu();
    for(int i = 1; i < n; i++){
        if(tir[i].salariu() > maxim ){
            maxim = tir[i].salariu();
            h = i;
        }
    }
    cout << "\n\nSoferul cu plata maxima:" << endl;
    tir[h].afisare();
    return 0;
}