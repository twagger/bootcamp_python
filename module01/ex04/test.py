
from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print("Zip evaluate : {}".format(Evaluator.zip_evaluate(coefs, words)))
print("Enumerate evaluate : {}".format(Evaluator.zip_evaluate(coefs, words)))