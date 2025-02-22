class CreateAccount:
    username="Loki"
    def createAccount(self):
        print("Acc Created")
class DeleteAccount(CreateAccount):
    def deleteId(self):
        print("Acc deleted successfully")
a=DeleteAccount()
print(a.createAccount())
