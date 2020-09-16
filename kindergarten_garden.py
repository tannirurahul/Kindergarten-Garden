veggies = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
}

students_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
            "Larry"]

class Garden:
    def __init__(self, diagram, students=students_list):
        self.students = sorted(students)
        self.pattern= diagram.split()

    def plants(self,student):
        student_index=self.students.index(student)
        veggie_person = []
        for x in self.pattern:
            for y in (student_index*2, (student_index*2)+1):
                final_result= veggies[x[y]]
                veggie_person.append(final_result)
        return veggie_person
