
marks = int(input("marks:"))

if marks > 100:
  print("error")

elif marks >80 <100:
    grade ="A plain"

elif marks >75 <79:
    grade = "A-"

elif marks>70 <74:
    grade ="B+"

elif marks >65 < 69:
    grade ="B plain"

elif marks >60 <64:
    grade ="B-"

elif marks >55 <59:
    grade ="C+"

elif marks >50 <54:
    grade ="C plain"

elif marks > 45 < 49:
    grade = "C-"

elif marks > 40 < 44:
    grade = "D+"

elif marks > 35 < 39:
    grade = "D plain"

elif marks > 30 < 34:
    grade = "D-"

elif marks  > 0 < 29:
    grade = "E"

else:grade = "error"

print( grade)
