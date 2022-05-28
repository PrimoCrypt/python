class student:
    # [assignment] Skeleton class. Add your code here
    def init(self,name,age,tracks,score):
        self.name=name
        self.score=score
        self.tracks=tracks
        self.age=age


    def change_name(self,name):
        self.name=name
    def change_score(self,score):
        self.score=score
    def add_track(self,tracks):
        self.tracks=tracks
    def change_age(self,age):
        self.age=age
    def get_score(self):
        return self.score



Bob = student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())