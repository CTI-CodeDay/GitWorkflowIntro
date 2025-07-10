import csv


with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    with open('output.html', 'w') as outfile:
        for row in reader:
            name = row[0]
            outfile.write(f"""
<div class="student-container">  
    <div>
        <img src="">
    </div>
    <div class="student-name">{name}</div>
    <div> School:  </div>
    <p> What I'm most looking forward to about the CodeDay Labs internship is ... </p>
    <a href="">Team page (leave blank until Module 5 when you will be assigned to your teams</a>
</div>
            """)