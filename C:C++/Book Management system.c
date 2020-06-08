typedef struct {
	char name[LEN_BOOK_NAME];
	char author[LEN_AUTHOR_NAME];
	char publisher[LEB_PUBLISHER_NAME];
	int serial;
	int page;
	TimeInfor time_pub;
	TimeInfor time_in;
}BookInfor;

typedef struct{
	unsigned year : 16;
	unsigned month : 8;
	unsigned day : 8;
}TimeInfor;

