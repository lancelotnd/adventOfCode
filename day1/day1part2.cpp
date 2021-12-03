using namespace std;
#include <iostream>
#include <fstream>
#include <vector>
int getNumber(int index, vector<int>& input) {
    if(index > input.size() -1){
        return 0;
    } else {
        return input.at(index);
    }
}
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
    vector<int> input;
    int lastNumber;
    int number;
    *entree >> number;
    int bigger = 0;
    while(*entree) {
        lastNumber = number;
        *entree >> number;
        input.push_back(number);
        if (lastNumber < number)
            bigger++;
        if(!(*entree)){
            int totalNumber =  input.size();
            int lastIndex;
            for(int i = 0; i < totalNumber-1; i++){
                int n = getNumber(i, input) + getNumber(i+1, input) +getNumber(i+2, input);
              cout << n << endl;
                lastIndex = i;
            }
            int lastSum =0;
            break;
        }
    }
}


