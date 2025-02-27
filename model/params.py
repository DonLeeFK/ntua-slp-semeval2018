"""

Model Configurations

"""

TASK1_EIOC = {
    "name": "TASK1_EI-oc",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
   "epochs": 50,
    "embeddings_file": "word2vec_500_6_concatened",
    "embed_dim": 510,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.3,
    "encoder_dropout": 0.4,
    "encoder_size": 300,
    "encoder_layers": 1,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.0,
    "base": 0.58,
    "patience": 20,
    "weight_decay": 0.0,
    "clip_norm": 1,
}
TASK1_EIREG = {
    "name": "TASK1_EI-reg",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_concatened",
    "embed_dim": 310,
    "embed_finetune": False,
    "embed_noise": 0.0,
    "embed_dropout": 0.0,
    "encoder_dropout": 0.0,
    "encoder_size": 10,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.0,
    "base": 0.71,
    "patience": 20,
    "weight_decay": 0.0,
    "clip_norm": 1,
}
TASK1_VREG = {
    "name": "TASK1_V-reg",
    "token_type": "word",
    "batch_train": 30,
    "batch_eval": 30,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_concatened",
    "embed_dim": 310,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.3,
    "encoder_size": 150,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 2,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.3,
    "base": 0.83,
    "patience": 20,
    "weight_decay": 0.0,
    "clip_norm": 1,
}
TASK1_VOC = {
    "name": "TASK1_V-oc",
    "token_type": "word",
    "batch_train": 30,
    "batch_eval": 30,
   "epochs": 50,
    "embeddings_file": "word2vec_500_6_concatened",
    "embed_dim": 500,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.3,
    "encoder_size": 250,
    "encoder_layers": 1,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.3,
    "base": 0.76,
    "patience": 20,
    "weight_decay": 0.0,
    "clip_norm": 1,
}
TASK1_EC = {
    "name": "TASK1_E-c",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_concatened",
    "embed_dim": 310,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.3,
    "encoder_size": 250,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 2,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.3,
    "base": 0.56,
    "patience": 20,
    "weight_decay": 0.0,
    "clip_norm": 1,
}

TASK2_A = {
    "name": "TASK2_A",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_20_neg",
    "embed_dim": 300,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.3,
    "encoder_size": 300,
    "encoder_layers": 1,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.,
    "base": 0.3,
    "patience": 5,
    "weight_decay": 0.0,
    "clip_norm": 1,
}

TASK3_A = {
    "name": "TASK3_A",
    "token_type": "word",
    "batch_train": 64,
    "batch_eval": 64,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_20_neg",
    "embed_dim": 300,
    "embed_finetune": False,
    "embed_noise": 0.05,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.2,
    "encoder_size": 150,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.0,
    "base": 0.7,
    "patience": 10,
    "weight_decay": 0.0,
    "clip_norm": 1,
}
TASK3_B = {
    "name": "TASK3_B",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_20_neg",
    "embed_dim": 300,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.2,
    "encoder_size": 150,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 1,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.0,
    "base": 0.3,
    "patience": 10,
    "weight_decay": 0.0,
    "clip_norm": 1,
}

SEMEVAL_2017 = {
    "name": "SEMEVAL_2017",
    "token_type": "word",
    "batch_train": 32,
    "batch_eval": 32,
   "epochs": 50,
    "embeddings_file": "word2vec_300_6_concatened",
    "embed_dim": 310,
    "embed_finetune": False,
    "embed_noise": 0.2,
    "embed_dropout": 0.1,
    "encoder_dropout": 0.3,
    "encoder_size": 150,
    "encoder_layers": 2,
    "encoder_bidirectional": True,
    "attention": True,
    "attention_layers": 2,
    "attention_context": False,
    "attention_activation": "tanh",
    "attention_dropout": 0.3,
    "base": 0.68,
    "patience": 10,
    "weight_decay": 0.0,
    "clip_norm": 1,
}
