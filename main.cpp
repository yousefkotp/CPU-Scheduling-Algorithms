#include <bits/stdc++.h>
#include "parser.h"

using namespace std;

/** Global Constants **/
const string TRACE = "trace";
const string SHOW_STATISTICS = "stats";
const string ALGORITHMS[8] = {"","FCFS","RR","SPN","SRT","HRRN","FB-1","FB-2i"};
void firstComeFirstServe(){
    int time=arrivalTime[0];
    for(int i=0;i<processes.size();i++){
        finishTime.push_back(time+serviceTime[i]);
        turnAroundTime.push_back(finishTime[i]-arrivalTime[i]);
        normTurn.push_back(turnAroundTime[i]*1.0/serviceTime[i]);
        time+=serviceTime[i];
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
        cout<<"| "<<processes[i]<<" ";
    cout<<"|"<<endl;
}
void printArrivalTime(){
    cout<<"Arrival\t\t";
    for(int i=0;i<arrivalTime.size();i++)
        cout<<"| "<<arrivalTime[i]<<" ";

    cout<<"|"<<endl;
}
void printServiceTime(){
    cout<<"Service\t\t";
    for(int i=0;i<serviceTime.size();i++)
        cout<<"| "<<serviceTime[i]<<" ";
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


