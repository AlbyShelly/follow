CREATE TABLE "contacts"(
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"name" TEXT NOT NULL,
	"age" INTEGER NOT NULL,
	"gender" TEXT NOT NULL,
	"address" TEXT NOT NULL,
	"last_contacted" DATETIME
);

