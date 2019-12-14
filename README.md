# Classification of Chick Calls with LSTM
## Aim
Build a classifier using LSTM that does the following:
  - Take as input an audio stream containing chick calls
  - Cut the audio stream in chunks of 100ms
  - Convert each chunk into a feature vector using Google's audio embeddings
  - Pass the feature vectors subsequently to an LSTM model
  - Return *SOFT* or *DISTRESS* if audio chunk was the end of either a soft or distress chick call

## To-Dos
  - [x] Restructure data
  - [x] Split data in train and test set
  - [x] Create white noise files
  - [ ] Create audio files containing sequences of soft and distress calls interjected by white noise, keeping information about where a call is
  - [ ] Split audio files in chunks of 100ms, keeping information about in which chunk a call ends
  - [ ] Extract features for each chunk
  - [ ] Build the architecture of the LSTM model
  - [ ] Train the LSTM model
  - [ ] Evaluate on test set 