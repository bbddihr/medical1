class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average = sum(scores) / len(scores)

    def __str__(self):
        return f"이름: {self.name}, 평균 성적: {self.average:.2f}"

def input_student():
    name = input("학생 이름을 입력하세요: ")
    scores = list(map(float, input("성적을 공백으로 구분하여 입력하세요 (예: 90 80 70): ").split()))
    return Student(name, scores)

def print_students(students):
    print("\n학생 목록:")
    for student in students:
        print(student)

def sort_students(students):
    return sorted(students, key=lambda student: student.average, reverse=True)

def main():
    students = []

    while True:
        print("\n[학생 성적 관리 프로그램]")
        print("1. 학생 정보 입력")
        print("2. 성적 목록 보기")
        print("3. 성적 순으로 보기")
        print("4. 프로그램 종료")
        choice = input("선택: ")

        if choice == '1':
            student = input_student()
            students.append(student)
        elif choice == '2':
            print_students(students)
        elif choice == '3':
            sorted_students = sort_students(students)
            print_students(sorted_students)
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
