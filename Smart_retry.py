#continue in while loop
testcase=["Simran_testcase","Rahul_testcase","Rohit_testcase","failed_testcase","Ankit_testcase","Amit_testcase"]
i = 0
retry = 0
max_retries = 3
while i < len(testcase):
   if testcase[i] == "failed_testcase":
      
      retry += 1
      if retry > max_retries:
         print (f"Max retries reached for testcase: {testcase[i]}")
         i += 1  # Move to the next testcase after max retries
         continue  # Skip to the next iteration after max retries
      print (f"Testcase failed: {testcase[i]}, retrying... (Attempt {retry})") 
      continue
   print (f"Testcase name passed: {testcase[i]}")
   i += 1
   retry = 0  # Reset retry count for successful testcases