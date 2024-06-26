--This is a rewritten qeury for all_work.sql using cte(common table expression)

WITH "t1" AS(
	SELECT "evangelists"."id" AS "eid", "evangelists"."name" AS "ename", "contact_id" AS "cid"
	FROM "evangelists" JOIN "follow"
	ON "evangelists"."id" = "follow"."evangelist_id"
)
SELECT "ename", "name" AS "cname", "age" AS "cage", "address", "last_contacted", "cid"
FROM "contacts" JOIN "t1"
ON "contacts"."id" = "t1"."cid"
