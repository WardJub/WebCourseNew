import mysql.connector


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10_schema')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    if query_type == 'commit':
        # Use for INSERT,UPDATE,DELETE statements
        # return the number of rows affected by the query
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT Statement.
        # Returns false if the query failed, or the result of the query.
        query_results = cursor.fetchall()
        return_value = query_results

    connection.close()
    cursor.close()
    return return_value
