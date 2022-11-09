#include <bits/stdc++.h>
#include "parser.h"

using namespace std;

/** Global Constants **/
const string TRACE = "trace";
const string SHOW_STATISTICS = "stats";
const string ALGORITHMS[8] = {"","FCFS","RR","SPN","SRT","HRRN","FB-1","FB-2i"};
void firstComeFirstServe(){
    int time=get<1>(processes[0]);
    for(int i=0;i<processes.size();i++){
        finishTime.push_back(time+get<2>(processes[i]));
        turnAroundTime.push_back(finishTime[i]-get<1>(processes[i]));
        normTurn.push_back(turnAroundTime[i]*1.0/get<2>(processes[i]));
        time+=get<2>(processes[i]);
    }
}

void roundRobin(){

}

void shortestProcessNext(){

}

void shortestRemainingTime(){

}

void highestResponseRatioNext(){

}

void feedbackQ1(){

}

void feedbackQ2i(){

}

void printAlgorithm(){
    cout<<ALGORITHMS[stoi(algorithms[0])]<<endl;
}

void printProcesses(){
    cout<<"Process\t\t";
    for(int i=0;i<processes.size();i++)
        cout<<"| "<<get<0>(processes[i])<<" ";
    cout<<"|"<<endl;
}
void printArrivalTime(){
    cout<<"Arrival\t\t";
    for(int i=0;i<processes.size();i++)
        cout<<"| "<<get<1>(processes[i])<<" ";

    cout<<"|"<<endl;
}
void printServiceTime(){
    cout<<"Service\t\t";
    for(int i=0;i<processes.size();i++)
        cout<<"| "<<get<2>(processes[i])<<" ";
    cout<<"| Mean|"<<endl;
}
void printFinishTime(){
    cout<<"Finish\t\t";
    for(int i=0;i<finishTime.size();i++)
        cout<<"| "<<finishTime[i]<<" ";
    cout<<"|-----|"<<endl;
}
void printTurnAroundTime(){
    cout<<"Turnaround\t";
    int sum =0;
    for(int i=0;i<turnAroundTime.size();i++){
        cout<<"| "<<turnAroundTime[i]<<" ";
        sum+=turnAroundTime[i];
    }
    cout<<fixed<<setprecision(2);
    cout<<"| "<<(1.0*sum/turnAroundTime.size())<<"|"<<endl;
}

void printNormTurn(){
    cout<<"NormTurn\t";
    cout<<fixed<<setprecision(2);
    float sum =0;
    for(int i=0;i<normTurn.size();i++){
        cout<<"| "<<normTurn[i]<<" ";
        sum+=normTurn[i];
    }

    cout<<"| "<<(1.0*sum/normTurn.size())<<"|"<<endl;
}
void printStats(){
    printAlgorithm();
    printProcesses();
    printArrivalTime();
    printServiceTime();
    printFinishTime();
    printTurnAroundTime();
    printNormTurn();
}

int main()
{
    parse();
    firstComeFirstServe();
    printStats();
    return 0;
}


