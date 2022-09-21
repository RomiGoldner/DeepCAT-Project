def split_train_test(healthy_path="TrainingData/healthy_samples.txt", sick_path="TrainingData/brca_samples_pbmc.txt"):
    # Read the files, split to train and test where 10% is test, and save to files with a _test or _train suffix
    with open(healthy_path) as f:
        healthy_samples = f.read().splitlines()
    with open(sick_path) as f:
        sick_samples = f.read().splitlines()

    # Shuffle and split
    import random
    random.shuffle(healthy_samples)
    random.shuffle(sick_samples)
    healthy_train = healthy_samples[:int(len(healthy_samples) * 0.9)]
    sick_train = sick_samples[:int(len(sick_samples) * 0.9)]
    healthy_test = healthy_samples[int(len(healthy_samples) * 0.9):]
    sick_test = sick_samples[int(len(sick_samples) * 0.9):]
    
    # Save to files
    with open("TrainingData/healthy_samples_train.txt", "w") as f:
        for line in healthy_train:
            f.write(line + "\n")
    with open("TrainingData/healthy_samples_test.txt", "w") as f:
        for line in healthy_test:
            f.write(line + "\n")
    with open("TrainingData/brca_samples_pbmc_train.txt", "w") as f:
        for line in sick_train:
            f.write(line + "\n")
    with open("TrainingData/brca_samples_pbmc_test.txt", "w") as f:
        for line in sick_test:
            f.write(line + "\n")
split_train_test()