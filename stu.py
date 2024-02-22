marks={'ravi':[97,85,85,67],
       'rahul':[92,91,94,85]}
tot=0
tot_marks=marks.copy()
for key, vals in marks.items():
    tot=sum(vals)
    tot_marks[key]=tot
print(tot_marks)
