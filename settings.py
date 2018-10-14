default = {
    "embedding_size": 500,
    "hidden_size": 1000,
    "max_length": 20,
    "num_batches": 7500,
    "num_epochs": 1000,
    "vocab_size": 15000,
}

en_path = "data/training/europarl-v7.fr-en.en"
fr_path = "data/training/europarl-v7.fr-en.fr"

gru_encoder_model = "models/gru_encoder.pkl"
gru_decoder_model = "models/gru_decoder.pkl"