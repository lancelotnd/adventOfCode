using namespace std;
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
string producetarget(vector<string> &candidates, bool isO2)
{
    string o2t;
    string co2t;
    int size = candidates.at(0).length();
    int diagnostics[size];
    for (int i = 0; i < size; i++)
    {
        diagnostics[i] = 0;
    }
    for (string &s : candidates)
    {
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
    for (int &i : diagnostics)
    {
        if (i >= 0)
        {
            o2t += "1";
            co2t += "0";
        }
        else
        {
            o2t += "0";
            co2t += "1";
        }
    }
    string toReturn;
    if (isO2)
    {
        toReturn = o2t;
    }
    else
    {
        toReturn = co2t;
    }

    return toReturn;
}
string isolate(vector<string> &allData, string target, bool isO2)
{
    string trueTarget = "";
    char targetUnit = target[0];
    trueTarget += targetUnit;
    vector<string> toReturn;
    toReturn = allData;
    target = producetarget(allData, isO2);
    int numberMatches = 100000000;
    int i = 0;
    while (numberMatches != 1)
    {
        vector<string> tmp;
        for (string &s : toReturn)
        {
            if (trueTarget == s.substr(0, i + 1))
            {
                tmp.push_back(s);
            }
        }
        toReturn = tmp;
        numberMatches = toReturn.size();
        i++;
        target = producetarget(toReturn, isO2);
        targetUnit = target[i];
        trueTarget += targetUnit;
    }
    return toReturn.at(0);
}
int stringToBinary(string s)
{
    int result = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[s.length() - 1 - i] == '1')
        {
            result += pow(2, i);
        }
    }
    return result;
}
int main(int argc, const char **argv)
{
    vector<string> all_data;

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
        if (s.length() != 0)
        {
            all_data.push_back(s);
        }
    }
    string oxygenTarget = producetarget(all_data, true);
    string oxygen = isolate(all_data, oxygenTarget, true);
    string co2Target = producetarget(all_data, false);
    string co2 = isolate(all_data, co2Target, false);
    cout << "Answer: " << stringToBinary(oxygen) * stringToBinary(co2) << endl;
}
