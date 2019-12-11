import os

test_distress = '/Users/bogdan/Documents/Studium/Chick-Calls/Chick_calls_classification/testing/distress_test'
test_soft = '/Users/bogdan/Documents/Studium/Chick-Calls/Chick_calls_classification/testing/soft_test'

training_distress = '/Users/bogdan/Documents/Studium/Chick-Calls/Chick_calls_classification/training/Calls/Distress'
training_soft = '/Users/bogdan/Documents/Studium/Chick-Calls/Chick_calls_classification/training/Calls/soft'

new_directory = '/Users/bogdan/Documents/Studium/Chick-Calls/raw_chick_calls'

all_labels = open('chick_calls_labels.tsv', 'w')
os.mkdir(new_directory)
counter = 1


for distress_test_file in os.listdir(test_distress):
  src = test_distress + '/' + distress_test_file
  dst = new_directory + '/' + str(counter) + '.wav'
  os.rename(src, dst)
  all_labels.write('{}.wav\tDISTRESS\n'.format(counter))
  counter += 1

for distress_training_file in os.listdir(training_distress):
  src = training_distress + '/' + distress_training_file
  dst = new_directory + '/' + str(counter) + '.wav'
  os.rename(src, dst)
  all_labels.write('{}.wav\tDISTRESS\n'.format(counter))
  counter += 1

for soft_test_file in os.listdir(test_soft):
  src = test_soft + '/' + soft_test_file
  dst = new_directory + '/' + str(counter) + '.wav'
  os.rename(src, dst)
  all_labels.write('{}.wav\tSOFT\n'.format(counter))
  counter += 1

for soft_training_file in os.listdir(training_soft):
  src = training_soft + '/' + soft_training_file
  dst = new_directory + '/' + str(counter) + '.wav'
  os.rename(src, dst)
  all_labels.write('{}.wav\tSOFT\n'.format(counter))
  counter += 1