from bayes import bayes

b = bayes()
bayes.readTrainingData(b)
bayes.getDifferentAttributes(b)
bayes.readTestData(b)
bayes.test(b)
bayes.userInputVector(b)