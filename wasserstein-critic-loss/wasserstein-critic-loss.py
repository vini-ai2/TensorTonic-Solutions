import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    R = np.asarray(real_scores)
    F = np.asarray(fake_scores)
    meanR = np.mean(R)
    meanF = np.mean(F)
    loss = float(meanF-meanR)

    return loss
    
    pass