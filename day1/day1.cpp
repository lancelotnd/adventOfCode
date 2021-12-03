using namespace std;
#include <iostream>
#include <fstream>
#include <vector>


int main(int argc, const char **argv)
{
    std::istream *entree;
    std::ifstream *entree_fichier = NULL;

    if (argc > 1)
    {
        entree = entree_fichier = new std::ifstream(argv[1]);
        if (entree->fail())
            std::cerr << "Erreur d'ouverture du fichier '" << argv[1] << "'" << std::endl;
    }
    else
    {
        entree = &std::cin;
    }
    int lastNumber;
    int number;
    *entree >> number;
    int bigger =0;
    while(*entree) {
        lastNumber = number;
        *entree >> number;
        if (lastNumber < number)
            bigger++;
        if(!(*entree)){
            cout<< "total bigger : " << bigger<< endl;
            break;
        }
            
    }

}
