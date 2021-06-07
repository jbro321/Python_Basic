# Enthusiastic_Python_Basic #P_13_1_1

class Friend:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def show_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone)

def main():
    f = Friend('박재형', '010-1111-2222')
    print(f.get_name())
    print(f.get_phone())
    f.set_phone('010-3333-5555')
    f.show_info()

main()