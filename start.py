import boto3


class Cloudformation:
    def __init__(self):
        pass

    def usrinput(self):
        self.state = input("Enter state: ")
        self.province = input("Enter province: ")
        print(self.state)
        print(self.province)

    def create_lambda_Stack(self):
        pass

    def deploy_lambda_Stack(self):
        client = boto3.client('cloudformation')


if __name__ == "__main__":
    cfmn = Cloudformation()
    cfmn.usrinput()
