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
void decrementServiceTime(tuple<string, int, int>& a){
    get<2>(a) = get<2>(a)-1;
}

void firstComeFirstServe(){
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
}

void roundRobin(){

}

void shortestProcessNext(){
    priority_queue<pair<int,tuple<string,int,int>>>pq;
    unordered_map<int,bool>done;
    for(int i=0;i<last_instant;i++){
        for(int j=0;j<process_count;j++){
            if(getArrivalTime(processes[j])<=i && !done[j]){
                pq.push(make_pair(-getServiceTime(processes[j]),processes[j]));
                done[j] = true;
            }
        }
        if(!pq.empty()){
            tuple<string,int,int>process= pq.top().second;
            string processName = getProcessName(process);
            int arrivalTime = getArrivalTime(process);
            int serviceTime = getServiceTime(process);
            int processIndex = processToIndex[processName];
            pq.pop();

            int temp = arrivalTime;
            for(;temp<i;temp++)
                timeline[temp][processIndex]='.';

            temp = i;
            for(;temp<i+serviceTime;temp++)
                timeline[temp][processIndex]='*';

            finishTime[processIndex]= (i+serviceTime);
            turnAroundTime[processIndex]= (finishTime[processIndex]-arrivalTime);
            normTurn[processIndex]= (turnAroundTime[processIndex]*1.0/serviceTime);
            i =temp-1;
        }
    }
}

void shortestRemainingTime(){
    priority_queue<pair<int,string>,vector<pair<int,string>>,greater<pair<int,string>>>pq;
    int j=0;
    for(int i=0;i<last_instant;i++){
        for(;j<process_count;){
            if(getArrivalTime(processes[j])==i){
                pq.push(make_pair(getServiceTime(processes[j]),getProcessName(processes[j])));
                j++;
            }else
                break;
        }
        if(!pq.empty()){
            string processName= pq.top().second;
            int remainingTime = pq.top().first;
            pq.pop();
            int processIndex = processToIndex[processName];
            int serviceTime = getServiceTime(processes[processIndex]);
            int arrivalTime= getArrivalTime(processes[processIndex]);
            timeline[i][processIndex]= '*';
            if(remainingTime==1){// process finished
                finishTime[processIndex]= i+1;
                turnAroundTime[processIndex]= (finishTime[processIndex]-arrivalTime);
                normTurn[processIndex]= (turnAroundTime[processIndex]*1.0/serviceTime);
            }else{
                pq.push(make_pair(remainingTime-1,processName));
            }
        }
    }

    for(int i=0;i<process_count;i++){
        int arrivalTime = getArrivalTime(processes[i]);
        for(int k=arrivalTime;k<finishTime[i];k++){
            if(timeline[k][i]!='*')
                timeline[k][i]='.';
        }
    }
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
    for(int i=0;i<process_count;i++)
        cout<<"| "<<getProcessName(processes[i])<<" ";
    cout<<"|"<<endl;
}
void printArrivalTime(){
    cout<<"Arrival\t\t";
    for(int i=0;i<process_count;i++)
        cout<<"| "<<getArrivalTime(processes[i])<<" ";

    cout<<"|"<<endl;
}
void printServiceTime(){
    cout<<"Service\t\t";
    for(int i=0;i<process_count;i++)
        cout<<"| "<<getServiceTime(processes[i])<<" ";
    cout<<"| Mean|"<<endl;
}
void printFinishTime(){
    cout<<"Finish\t\t";
    for(int i=0;i<process_count;i++)
        cout<<"| "<<finishTime[i]<<" ";
    cout<<"|-----|"<<endl;
}
void printTurnAroundTime(){
    cout<<"Turnaround\t";
    int sum =0;
    for(int i=0;i<process_count;i++){
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
    for(int i=0;i<process_count;i++){
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
    cout<<ALGORITHMS[stoi(algorithms[0])]<<" ";
    for(int i=0;i<=last_instant;i++)
        cout<<" "<<i%10<<" ";
    cout<<endl;
    cout<<"------------------------------------------------"<<endl;
    for(int i=0;i<process_count;i++){
        cout<<getProcessName(processes[i])<<"\t";
        for(int j=0;j<last_instant;j++){
            cout<<"|"<<timeline[j][i];
        }
        cout<<"|"<<endl;
    }

    cout<<"------------------------------------------------"<<endl;
}

int main()
{
    freopen("input.txt","r",stdin);
    parse();
    shortestRemainingTime();
    printStats();
    return 0;
}


