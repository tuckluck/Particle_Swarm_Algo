import numpy as np
import pytest
from particle_swarm import Particle, PSO  # Replace 'your_module_name' with the actual file name if not in the same file

# Set a seed for reproducibility in tests
np.random.seed(42)

# Define a simple sphere function as objective
def sphere(x):
    return np.sum(x ** 2)

@pytest.fixture
def basic_pso():
    return PSO(func=sphere, dim=2, bounds=(-5, 5), num_particles=5, max_iter=10)

def test_particle_initialization():
    dim = 3
    bounds = (-10, 10)
    particle = Particle(dim, bounds)
    assert len(particle.position) == dim
    assert len(particle.velocity) == dim
    assert np.all(particle.position >= bounds[0]) and np.all(particle.position <= bounds[1])
    assert np.all(particle.velocity >= -1) and np.all(particle.velocity <= 1)

def test_particle_velocity_update():
    dim = 2
    bounds = (-5, 5)
    particle = Particle(dim, bounds)
    old_velocity = particle.velocity.copy()
    global_best_position = np.random.uniform(bounds[0], bounds[1], dim)
    particle.update_velocity(global_best_position, w=0.5, c1=2.0, c2=2.0)
    assert not np.array_equal(old_velocity, particle.velocity), "Velocity should change after update"

def test_particle_position_update():
    dim = 2
    bounds = (-5, 5)
    particle = Particle(dim, bounds)
    particle.velocity = np.array([10.0, 10.0])  # Force position to exceed bounds
    particle.update_position(bounds)
    assert np.all(particle.position <= bounds[1]) and np.all(particle.position >= bounds[0])

def test_pso_optimization_converges(basic_pso):
    best_position, best_score, _, _, _ = basic_pso.optimize()
    # On a sphere function, best score should be close to 0 after a few iterations
    assert best_score < 1.0

def test_pso_output_shapes(basic_pso):
    best_position, best_score, iters, best_list, pos_matrix = basic_pso.optimize()
    assert len(best_position) == basic_pso.dim
    assert isinstance(best_score, float)
    assert len(iters) == basic_pso.max_iter
    assert len(best_list) == basic_pso.max_iter
    assert pos_matrix.shape == (basic_pso.num_particles, basic_pso.dim * basic_pso.max_iter)
