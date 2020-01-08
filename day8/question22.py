

string = input().split(" ")

print({i: string.count(i) for i in sorted(string)})
  

