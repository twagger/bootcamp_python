from unittest import result


class Evaluator:

    def zip_evaluate(coefs, words):
        """zip_evaluate creates a tuple with two lists and \
        compute the sum of the lengths of every words of a \
        given list weighted by a list of coefficinents coefs"""
        if (len(coefs) == len(words)):
            zip_list = list(zip(coefs, words))
            result = sum(zip_list[i][0] * len(zip_list[i][1]) for i in range(len(zip_list)))
            return result
        else:
            return -1

    def enumerate_evaluate(self, coefs, words):
        """enumerate_evaluate creates a counter that can be used \ 
        as an index to access list entries"""
        if (len(coefs) == len(words)):
            for index, value in enumerate(words):
                result += sum(coefs[index] * len(value))
            return result
        else:
            return -1