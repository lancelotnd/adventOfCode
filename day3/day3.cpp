using namespace std;
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

int stringToBinary(string s)
{
    int result = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[s.length()-1-i] == '1')
        {
            result += pow(2, i);
        }
    }
    return result;
}

int main(int argc, const char **argv)
{

    static int diagnostics[] = {0, 0, 0, 0, 0};

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
    while (*entree)
    {

        if (!(*entree))
        {

            break;
        }
        string s;
        *entree >> s;
        int i = 0;
        for (char &c : s)
        {
            if (c == '1')
                diagnostics[i] += 1;
            else
                diagnostics[i] -= 1;
            i++;
        }
    }
    string gamma;
    string epsilon;
    for (int &i : diagnostics)
    {

        if (i > 0)
        {
            gamma += "1";
            epsilon += "0";        }
        else
        {
            gamma += "0";
            epsilon += "1";
            /*  */
        }
    }
    cout << "Answer: " << stringToBinary(gamma) * stringToBinary(epsilon) <<endl;

}
