from wavebender import *
import random

number_of_files = 1848 # equivalent to number of training calls
target_directory = "/Users/bogdan/Documents/Studium/Chick-Calls/whitenoise_files"

print("Creating white noise...")
for i in range(number_of_files):
  # random amplitude between 0.0 and 1.0
  current_amplitude = random.random()
  # random length between 200 ms and 5s
  current_length = random.uniform(0.002, 5.0)
  print(current_length)

  channels = ((white_noise(amplitude=current_amplitude),),)
  samples = compute_samples(channels, int(44100 * current_length))

  filename = "{}/whitenoise_{}.wav".format(target_directory, i + 1)
  write_wavefile(filename, samples, int(44100 * current_length), nchannels=1)


