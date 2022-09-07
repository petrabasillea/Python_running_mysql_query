import os


file_query = "auto_query.sql"
load_file  = "D:\\Folder\\file.csv"

host_ = "localhost"
user_ = "root"
pass_ = "root"
db_   = "db_name"
conn_ = "mysql --host="+host_+" --user="+user_+" --password="+pass_+" -f --database="+db_



with open(file_query, 'w')as f:
    f.write("""LOAD DATA LOCAL INFILE '"""+str(load_file).replace('\\','\\\\')+"""' 
IGNORE
INTO TABLE top4
CHARACTER SET UTF8 
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '\\"' 
LINES TERMINATED BY '\\n'
IGNORE 1 LINES;
""")

os.system(conn_+" < "+file_query)