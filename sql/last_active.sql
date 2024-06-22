CREATE TRIGGER "last_active"
AFTER INSERT ON "follow"
FOR EACH ROW
BEGIN
	UPDATE "evangelists" SET "last_active" = DATE('now')	
	WHERE "id" = NEW."evangelist_id";
END;

