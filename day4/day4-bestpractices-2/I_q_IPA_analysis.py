import numpy as np
from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Load experimental and theoretical data
experimental_data = np.load('I_q_IPA_exp.npy')
theoretical_data = np.load('I_q_IPA_model.npy')


# Remove NaN values from experimental data
experimental_data = experimental_data[~np.isnan(experimental_data).any(axis=1)]

# Define the objective function to minimize
def objective(scale_factor, experimental_data, theoretical_data):
    scaled_theoretical_data = theoretical_data.copy()
    scaled_theoretical_data[:, 1] *= scale_factor
    # Interpolate theoretical data onto the same grid as experimental data
    f = interp1d(scaled_theoretical_data[:, 0], scaled_theoretical_data[:, 1], kind='linear') 
    scaled_theoretical_strength = f(experimental_data[:, 0])
    # Calculate sum of squared differences
    error = np.sum((experimental_data[:, 1] - scaled_theoretical_strength)**2)
    return error

# Find the scale factor that minimizes the objective function
result = minimize_scalar(objective, args=(experimental_data, theoretical_data), bounds=(0.0001, 2.0), method='bounded')

# Get the optimized scale factor
optimal_scale_factor = result.x

# Scale the theoretical data with the optimal scale factor
scaled_theoretical_data = theoretical_data.copy()
scaled_theoretical_data[:, 1] *= optimal_scale_factor

# Plot the experimental and scaled theoretical data
plt.figure()
plt.scatter(experimental_data[:, 0], experimental_data[:, 1], label='Experimental Data')
plt.plot(scaled_theoretical_data[:, 0], scaled_theoretical_data[:, 1], label='Scaled Theoretical Data')
plt.xlabel('Scattering Vector')
plt.ylabel('Scattering Strength')
plt.legend()
plt.title('Experimental Data vs Scaled Theoretical Data')
plt.grid(True)
plt.show()

