

class Menu:
    def __init__(self):
        pass

    def generate_image(self,model,prompt):

        response_json = {
            "model": model,
            "prompt": prompt
        }

        print(response_json)
        print ("Generate Image")


    def create_transcription(self,model,prompt,lang):

        response_json = {
            "model": model,
            "prompt": prompt,
            "language": lang
        }

        print(response_json)
        print ("Create Transcription")

    def operation(self,num1,num2):

        function_sum(1,2)


    def saudation(self,name,last_name):
        
        self.name = name

        self.last_name = last_name

        greeting(self.name,self.last_name)

RUN = Menu()

# RUN.generate_image("dall-e-3","lamborghini aventador running in city cyberpunk 3033 in tokyo night,3d art, references digital arts, hight definition, quality 8k")

def function_sum(num1,num2):

    part1 = num1 + num2

    part2 = part1 / 2

    print(f"result: {part2}")

def greeting(name,last_name):

    print(f"Hello {name.upper()} {last_name.upper()}")


RUN.operation(866,123)

RUN.saudation("wictor","santos")