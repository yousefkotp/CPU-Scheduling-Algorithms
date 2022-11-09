#include <bits/stdc++.h>
#include "parser.h"

using namespace std;

/** Global Constants **/
const string TRACE = "trace";
const string SHOW_STATISTICS = "stats";
const string ALGORITHMS[8] = {"","FCFS","RR","SPN","SRT","HRRN","FB-1","FB-2i"};

bool sortByServiceTime(const tuple<string, int, int>& a,const tuple<string, int, int>& b){
    return (get<2>(a) < get<2>(b));
}
bool sortByArrivalTime(const tuple<string, int, int>& a,const tuple<string, int, int>& b){
    return (get<1>(a) < get<1>(b));
}

string getProcessName(tuple<string, int, int>& a){
    return get<0>(a);
}

int getArrivalTime(tuple<string, int, int>& a){
    return get<1>(a);
}

int getServiceTime(tuple<string, int, int>& a){
    return get<2>(a);
}

void firstComeFirstServe(){
    sort(processes.begin(),processes.end(),sortByArrivalTime);
    int time=getArrivalTime(processes[0]);

    for(int i=0;i<processes.size();i++){
        string processName = getProcessName(processes[i]);
        int processIndex = processToIndex[processName];
        int arrivalTime = getArrivalTime(processes[i]);
        int serviceTime = getServiceTime(processes[i]);

        finishTime[processIndex]= (time+serviceTime);
        turnAroundTime[processIndex]= (finishTime[processIndex]-arrivalTime);
        normTurn[processIndex]= (turnAroundTime[processIndex]*1.0/serviceTime);

        for(int j = time;j<finishTime[processIndex];j++)
            timeline[j][processIndex]='*';
        for(int j=arrivalTime;j<time;j++)
            timeline[j][processIndex]='.';
        time+=serviceTime;
    }
    processes= defaultProcesses;
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

void printTimeline(){


    cout<<"------------------------------------------------"<<endl;


    cout<<"------------------------------------------------"<<endl;
}

int main()
{
    parse();
    shortestProcessNext();
    printStats();
    return 0;
}


