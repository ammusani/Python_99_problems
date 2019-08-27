#include<bits/stdc++.h>
using namespace std;

set<int> genClosure(set<int> clos, char c, vector<vector<vector<int>>> table, int states[], char arg[], int numOfStates, int numOfArg, set<int> done) {
	set<int> v;
	
	for(auto i = clos.begin(); i != clos.end(); i++) { 	//this loop checks if the loop is already generating the epsilon transition then it will store them back in return set and another set which we will use to remove those states to enter next recursion
		if(c == '$'){
			v.insert(*i);
			done.insert(*i);
		}
	}
	
	int argL;					//finding the index of the current string character
	for(int i = 0; i <= numOfArg; i++) if(c == arg[i]) {
		argL = i;
		break;
	}

	
	for(auto i = clos.begin(); i != clos.end(); i++) {	//generating v for the transition for the character c

		for(int k = 0; k < table[*i][argL].size(); k++) {
			
			int value = table[*i][argL][k];
			if(value == -1) break;
			for(int ll = 0; ll < numOfStates; ll++) {
				if(value == states[ll]) {
					v.insert(ll);
					break;
				}
			}
		}
	}
	
	
	for(auto i = v.begin(); i != v.end(); i++) {		//generating all epsilon transitions for the new vector
		set<int> v2;
		if(done.find(*i) == done.end()) v2 = genClosure(v, '$', table, states, arg, numOfStates, numOfArg, done); //it won't perform transition on those v's on which an epsilon transition has already been performed
		for(auto j = v2.begin(); j != v2.end(); j++) v.insert(*j);
	}

	
	return v;
	
}


vector<int> genValue(string s) {
	vector<int> v;

	if(s[0] == '^') {			//denoting ^ by -1
		v.push_back(-1);
		return v;
	}


	vector<int> comma;			//locating positions of comma
	for(int i = 0; i < s.size(); i++) if(s[i] == ',') comma.push_back(i);
	int back = 0;
	int val;
	int k;
	
	

	for(auto i = comma.begin(); i != comma.end(); i++) {		//generating numbers
		val = 0;	
		for(int j = back; j < *i; j++) {
			val *= 10;			
			k = (s[j] - '0');
			val += k;
		}
		v.push_back(val);
				
		back = (*i) + 1;
	}
	val = 0;
	for(int j = back; j < s.size(); j++) {	
			val *= 10;			
			k = (s[j] - '0');
			val += k;
	}
	v.push_back(val);
	
	return v;		//it contains all the numbers
}


int main(int argc, char *argv[]) {

	int numOfStates = stoi(argv[1]);		//1st input argument - number of states

	int numOfFinStates = stoi(argv[2]);		//2nd input argument - number of finite states


	int numOfArg = stoi(argv[3]);			//3rd input argument - number of input symbols

	ifstream cinn;		//opening the file tables.txt using file pointer
	cinn.open("table.txt");
	
	
	int states[numOfStates];				//setting up states
	for(int i = 0; i < numOfStates; i++) {
		cinn >> states[i];
	}


	set<int> s;									//setting up final states
	int k;
	for(int i = 0; i < numOfFinStates; i++) {
		cinn >> k;
		s.insert(k);
	}

	

	char arg[numOfArg + 1];					//setting up input symbols
	char r;
	for(int i = 0; i < numOfArg; i++) {	
		cinn >> r;
		arg[i] = r;
	}

	arg[numOfArg] = '$';

	vector<vector<vector<int>>> transtable;				//setting up the transition table
	string sss;
	vector<vector<int>> v1;
	vector<int> v2;

	for(int i = 0; i <= numOfArg; i++) v1.push_back(v2);
	for(int i = 0; i < numOfStates; i++) transtable.push_back(v1);

	for(int i = 0; i < numOfStates; i++) for(int j = 0; j  <= numOfArg; j++) {
		cinn >> sss;
		
		transtable[i][j] = genValue(sss);
	}

	
	
	
	cinn.close();							//closing the file table.txt
	
	set<int> epsilonClosure;
	epsilonClosure.insert(0);
	set<int> empty;
	epsilonClosure = genClosure(epsilonClosure, '$', transtable, states, arg, numOfStates, numOfArg, empty);	//generating closure for the first state.
	
	for(auto i = epsilonClosure.begin(); i != epsilonClosure.end(); i++) cout << *i << endl;

	return 0;
}

