# Define the Person class
class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_objs = [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            wife_name = person_dict["wife"]
            wife_obj = Person.people.get(wife_name)
            if wife_obj:
                person_obj.wife = wife_obj
                wife_obj.husband = person_obj

        if "husband" in person_dict and person_dict["husband"]:
            husband_name = person_dict["husband"]
            husband_obj = Person.people.get(husband_name)
            if husband_obj:
                person_obj.husband = husband_obj
                husband_obj.wife = person_obj

    return person_objs
