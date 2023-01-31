def printit(cur, sql):
  print(f"\nThe SQL...\n{sql}\nThe result...")
  cur.execute(sql)
  for i, row in enumerate(cur):
    print(i, row)
