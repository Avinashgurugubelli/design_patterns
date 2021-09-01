"""
    Single responsibility principal.

    BMI calculator.

    This also implements the facade pattern - if you see class 'BMI' it encapsulates all the logic like calculation, and evaluation and giving the single result, basically it is masking more complex underlying or structural code.

    we used static method here, because we are not sharing the resources and data b/w classes - we just relying on the end result.

    Facade Pattern Defnition:
    -------------------------
    Facade pattern hides the complexities of the system and provides an interface to the client using which the client can access the system. 
    This type of design pattern comes under structural pattern as this pattern adds an interface to existing system to hide its complexities.
    This pattern involves a single class which provides simplified methods required by client and delegates calls to methods of existing system classes. 

"""
class BMIParams:

    def __init__(self, height, weight) -> None:
        self.height = height
        self.weight = weight

class BMICalculator:

    @staticmethod
    def get_bmi_index(params: BMIParams):
        bmi = params.weight/(params.height*params.height)
        return bmi
    
class BMIResultEvaluator:
    @staticmethod
    def evaluate(bmi):
        if bmi <= 18.5:
            return f'Your BMI is {round(bmi, 0)} - underweight'
        elif 18.5 < bmi < 25:
            return f'Your BMI is {round(bmi, 0)} -  normal'

        elif 25 < bmi < 30:
            return f'your BMI is {round(bmi, 0)} - overweight'

        elif bmi > 30:
          return f'Your BMI is  {round(bmi, 0)} - obese'

class BMI:
    @staticmethod
    def calculate_bmi(params: BMIParams):
        bmi = BMICalculator.get_bmi_index(params)
        result = BMIResultEvaluator.evaluate(bmi)
        return result


if __name__=="__main__":
    bmi_params = BMIParams(161, 60)
    print(BMI.calculate_bmi(bmi_params))

