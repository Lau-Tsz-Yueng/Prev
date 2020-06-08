#include <stdio.h>
#ifndef MENU_H
#define MENU_H

void menu_main(void){
	int choice = 0;
	printf("***************************************\n"
		   "***** My Book Management System *******\n"
		   "***************************************\n"
		   "\n"
		   "\t1. Add a book\n"
		   "\t2. Delete books\n"
		   "\t3. Search books\n"
		   "\t4. Reload database\n"
		   "\t0. Exit\n"
		   "\nPlease select your choice(0~4):"
	      );
	choice = menu_choice(4);

	switch (choice){
		case 1:
			menu_add();
			break;
		case 2;
			menu_delete();
			break;
		case 3;
			menu_search();
			break;
		case 4;
			menu_reload();
			break;
		case 0;
			menu_exit();
			break;
		default:
			menu_error();
			break;


	}

}
#endif
