import os
import os.path


file_query = "auto_query.sql"

host_ = "localhost"
user_ = "root"
pass_ = "root"
db_   = "db_name"
conn_ = "mysql --host="+host_+" --user="+user_+" --password="+pass_+" -f --database="+db_



with open(file_query, 'w')as f:
    f.write("""#Write Query
""")

os.system(conn_+" < "+file_query)