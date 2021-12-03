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
    string command;
    int aim = 0;
    int amount = 0;
    int horizontal_pos = 0;
    int depth = 0;
    while (*entree)
    {
        *entree >> command;
        *entree >> amount;
        if (!(*entree))
        {
            cout << "horizontal pos " << horizontal_pos << endl;
            cout << "depth pos " << depth << endl;
            cout << "ANSWER: " << depth * horizontal_pos << endl;
            break;
        }
        if (command == "forward")
        {
            horizontal_pos += amount;
            depth += aim * amount;
        }

        else if (command == "down")
            aim += amount;
        else if (command == "up")
            aim -= amount;
    }
}
