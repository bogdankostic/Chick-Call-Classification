import wave
import csv
import random
from pydub import AudioSegment

def get_audiolength(file):
  with wave.open(file, 'rb') as audiofile:
    number_of_frames = audiofile.getnframes()
    framerate = audiofile.getframerate()

    return number_of_frames / float(framerate)

training_files = [row for row in csv.reader(open('train_labels.tsv', 'r'), delimiter='\t')]
whitenoise_files = [row[0] for row in csv.reader(open('whitenoise_filenames.tsv', 'r'), delimiter='\t')]


for file_number in range(1):
  # For each chick call, start time, end time and label are saved
  labels_with_time = open('labels_with_time_{}.tsv'.format(file_number + 1),'w')

  # shuffle training files
  current_training_files = training_files
  random.shuffle(current_training_files)
  current_whitenoise_files = whitenoise_files
  random.shuffle(current_whitenoise_files)
  
  # initialize audio file
  first_whitenoise = current_whitenoise_files.pop()
  current_length = get_audiolength('whitenoise_files/{}'.format(first_whitenoise))
  final_audio = AudioSegment.from_wav('whitenoise_files/{}'.format(first_whitenoise))

  # iterate over training files as long as list not empty
  while current_training_files:
    current_training_file = current_training_files.pop()
    if current_whitenoise_files:
      current_whitenoise_file = current_whitenoise_files.pop()

    current_trainig_audio = AudioSegment.from_wav('raw_chick_calls/{}'.format(current_training_file[0]))
    current_whitenoise_audio = AudioSegment.from_wav('whitenoise_files/{}'.format(current_whitenoise_file))

    # start time of chick call
    labels_with_time.write('{}\t'.format(current_length))

    # end time of chick call + label
    current_length += get_audiolength('raw_chick_calls/{}'.format(current_training_file[0]))
    current_label = current_training_file[1]
    labels_with_time.write('{}\t{}\n'.format(current_length, current_label))

    # concatenate existing audio with chick call and whitenoise and update length of file
    final_audio += current_trainig_audio
    final_audio += current_whitenoise_audio
    current_length += get_audiolength('whitenoise_files/{}'.format(current_whitenoise_file))

  # export final audio file
  final_audio.export('training_files/training_file_{}.wav'.format(file_number + 1), format='wav')

