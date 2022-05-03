class Evaluator:

    def zip_evaluate(coefs, words):
        if (len(coefs) == len(words)):
            zip_list = list(zip(coefs, words))
            result = sum(zip_list[i][0] * len(zip_list[i][1]) for i in range(len(zip_list)))
            return result
        else:
            return -1

    def enumerate_evaluate(self, coefs, words):
        print("enumerate evaluate")