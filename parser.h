#ifndef PARSER_H_INCLUDED
#define PARSER_H_INCLUDED

#include <bits/stdc++.h>

using namespace std;

/** This file handles parsing the data we are going to work with **/
/** It also holds all the global variables we parse into         **/


string operation;
int last_instant, process_count;
vector<string> algorithms;
vector<tuple<string,int,int>> processes;
unordered_map<string,int>processToIndex;


//Results

vector<int>finishTime;
vector<int>turnAroundTime;
vector<float>normTurn;


void parse_algorithms(string algorithmChunk)
{
    stringstream stream(algorithmChunk);
    while (stream.good())
    {
        string substr;
        getline(stream, substr, ',');
        algorithms.push_back(substr);
    }
}

void parse()
{
    string algorithmChunk;
    cin >> operation >> algorithmChunk >> last_instant >> process_count;
    for(int i=0; i<process_count; i++)
    {
        string p;
        int arrival,service;
        cin >> p >> arrival >> service;
        processes.push_back(make_tuple(p,arrival,service));
        processToIndex[p]=i;
    }
    parse_algorithms(algorithmChunk);
    finishTime.resize(process_count);
    turnAroundTime.resize(process_count);
    normTurn.resize(process_count);
}


#endif // PARSER_H_INCLUDED
