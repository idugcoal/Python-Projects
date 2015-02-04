//Doug Cole
//CSIT 832
//Final Exam
//Question #3

#include <iostream>
using namespace std;

struct Employee {
	int ID;
	Employee() { ID = -1; }
};

int showMenu();

void display(Employee[], int);
// prototype the assignID function and (optional) any helper functions 

void assignID(Employee[], int);
int gethash(int);


int main()
{
	Employee emps[100];
	int choice;
	int input;
	do
	{
		choice=showMenu();
		switch(choice)
		{
		case 1:
			cout<<"Enter the ID:";
			cin>>input;
			assignID(emps, input);
			//
			break;
		case 2:
			display(emps, 100);
			break;
		case 3:
			cout<<"Terminating......\n";
			break;
		}
	}while(choice!=3);
	return 0;
}

int showMenu()
{
	int choice;
	cout<<"1. Insert\n";
	cout<<"2. Display\n";
	cout<<"3. Exit\n";
	cout<<"Enter your choice:";
	cin>>choice;
	return choice;
}

void display(Employee e[], int size)
{
	for(int x=0;x<size;x++)
		if(e[x].ID != -1)
			cout<<"Slot " << x << ": " << e[x].ID << endl;
}

// write the assignID function

void assignID(Employee e[], int input)
{
	int location = gethash(input);

	while(e[location].ID != -1)
		location = (location + 1) % 100;

	e[location].ID = input;	

}

int gethash(int input)
{
	int temp = input;
	temp %= 100;
	return (temp % 100);

}

