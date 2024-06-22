CREATE TRIGGER "last_contacted_store"
AFTER INSERT ON "contacts"
FOR EACH ROW
BEGIN
	UPDATE "contacts" SET "last_contacted" = DATE('now')	
	WHERE "id" = NEW."id";
END;

