
from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print("Zip evaluate : {}".format(Evaluator.zip_evaluate(coefs, words)))
print("Enumerate evaluate : {}".format(Evaluator.zip_evaluate(coefs, words)))

words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print("Zip evaluate : {}".format(Evaluator.zip_evaluate(coefs, words)))
print("Enumerate evaluate : {}".format(Evaluator.zip_evaluate(coefs, words)))