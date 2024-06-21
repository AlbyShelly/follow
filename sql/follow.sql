CREATE TABLE "follow"(
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"evangelist_id" INTEGER REFERENCES "evangelists"("id"),
	"contact_id" INTEGER REFERENCES "contacts"("id")
);
