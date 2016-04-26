# hallucinate
news aggregator site whose only goal is to create a fair algorithm for sorting content that encourages a variety of viewpoints.

mysql> show tables;
+-----------------------+
| Tables_in_hallucinate |
+-----------------------+
| cite                  |
| posts                 |
| reply                 |
| session               |
| sources               |
| users                 |
| votes                 |
+-----------------------+
7 rows in set (0.00 sec)

mysql> describe cite;
+-----------+---------------------+------+-----+---------+-------+
| Field     | Type                | Null | Key | Default | Extra |
+-----------+---------------------+------+-----+---------+-------+
| post_id   | bigint(20) unsigned | YES  |     | NULL    |       |
| source_id | bigint(20) unsigned | YES  |     | NULL    |       |
+-----------+---------------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> describe posts;
+---------+---------------------+------+-----+---------+----------------+
| Field   | Type                | Null | Key | Default | Extra          |
+---------+---------------------+------+-----+---------+----------------+
| post_id | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| user_id | bigint(20) unsigned | YES  |     | NULL    |                |
| content | text                | YES  |     | NULL    |                |
+---------+---------------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> describe reply;
+-------------+---------------------+------+-----+---------+-------+
| Field       | Type                | Null | Key | Default | Extra |
+-------------+---------------------+------+-----+---------+-------+
| post_id     | bigint(20) unsigned | YES  |     | NULL    |       |
| response_id | bigint(20) unsigned | YES  |     | NULL    |       |
+-------------+---------------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> describe session;
+------------+---------------------+------+-----+-------------------+-----------------------------+
| Field      | Type                | Null | Key | Default           | Extra                       |
+------------+---------------------+------+-----+-------------------+-----------------------------+
| session_id | varchar(256)        | NO   | PRI | NULL              |                             |
| user_id    | bigint(20) unsigned | YES  |     | NULL              |                             |
| timestamp  | timestamp           | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+------------+---------------------+------+-----+-------------------+-----------------------------+
3 rows in set (0.00 sec)

mysql> describe sources;
+-----------+---------------------+------+-----+---------+----------------+
| Field     | Type                | Null | Key | Default | Extra          |
+-----------+---------------------+------+-----+---------+----------------+
| source_id | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| source    | text                | YES  |     | NULL    |                |
+-----------+---------------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> describe users;
+-----------+---------------------+------+-----+---------+----------------+
| Field     | Type                | Null | Key | Default | Extra          |
+-----------+---------------------+------+-----+---------+----------------+
| user_id   | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| user_name | varchar(256)        | YES  |     | NULL    |                |
| hash      | varchar(256)        | YES  |     | NULL    |                |
+-----------+---------------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> describe votes;
+---------+---------------------+------+-----+-------------------+-----------------------------+
| Field   | Type                | Null | Key | Default           | Extra                       |
+---------+---------------------+------+-----+-------------------+-----------------------------+
| time    | timestamp           | NO   | PRI | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| user_id | varchar(256)        | YES  |     | NULL              |                             |
| post_id | bigint(20) unsigned | YES  |     | NULL              |                             |
| score   | tinyint(4)          | YES  |     | NULL              |                             |
+---------+---------------------+------+-----+-------------------+-----------------------------+
4 rows in set (0.00 sec)
