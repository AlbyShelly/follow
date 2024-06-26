SELECT "eid", "ename", "name" AS "cname", "age" AS "cage", "address", "last_contacted", "cid"

FROM "contacts" JOIN 
	(SELECT "evangelists"."id" AS "eid", "evangelists"."name" AS "ename", "contact_id" AS "cid"
	FROM "evangelists" JOIN "follow"
	ON "evangelists"."id" = "follow"."evangelist_id") AS "t1"
ON "contacts"."id" = "t1"."cid"
