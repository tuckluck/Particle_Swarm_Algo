import numpy as np



class Particle:
    def __init__(self, dim, bounds):
        # Initialize particle position and velocity
        self.position = np.random.uniform(bounds[0], bounds[1], dim)   	#initialize position randomly within bounds
        self.velocity = np.random.uniform(-1, 1, dim)    				#initialize position randomly within bounds
        self.best_position = np.copy(self.position)						#can update best for each particle
        self.best_score = float('inf')

    def update_velocity(self, global_best_position, w, c1, c2):
        # Update particle velocity based on inertia, cognitive and social components
        r1 = np.random.rand(len(self.position))    #adds randomness to velocity updates
        r2 = np.random.rand(len(self.position))		#adds randomness to velocity updates

        cognitive = c1 * r1 * (self.best_position - self.position)     #amount that velocity tends towards personal best 
        social = c2 * r2 * (global_best_position - self.position)		#amount that velocity tends towards group best
        self.velocity = w * self.velocity + cognitive + social		#total new velocity

    def update_position(self, bounds):
        # Update position and apply bounds
        self.position += self.velocity
        self.position = np.clip(self.position, bounds[0], bounds[1])		#prevents position from exceeding bounds

class PSO:
    def __init__(self, func, dim, bounds, num_particles=30, max_iter=100, w=0.5, c1=2, c2=2):
        """
        Parameters:
        - func: objective function to minimize
        - dim: number of dimensions
        - bounds: tuple (min, max) for search space
        - num_particles: number of particles in the swarm
        - max_iter: number of iterations
        - w: inertia weight
        - c1: cognitive coefficient
        - c2: social coefficient
        """
        self.func = func
        self.dim = dim
        self.bounds = bounds
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.w = w
        self.c1 = c1
        self.c2 = c2

        # Initialize swarm
        self.swarm = [Particle(dim, bounds) for _ in range(num_particles)]   #initializes all particles with starting velocity and position. 
        self.global_best_position = np.random.uniform(bounds[0], bounds[1], dim)    #initializes random global best position
        self.global_best_score = float('inf')  #sets global best score to infinity to initialize
    
    def optimize(self):
        iterate_list = []
        best_list = []


		# Main optimization loop
        for iteration in range(self.max_iter):
            for particle in self.swarm:
                # Evaluate current fitness
                fitness = self.func(particle.position)
                

                # Update personal best
                if fitness < particle.best_score:   #test to see if best position has been achieved for each particle
                    particle.best_score = fitness
                    particle.best_position = np.copy(particle.position)

                # Update global best
                if fitness < self.global_best_score: 	#test to see if best position achieved by any particale has been reached
                    self.global_best_score = fitness
                    self.global_best_position = np.copy(particle.position)

            # Update velocity and position for each particle
            for particle in self.swarm:
                particle.update_velocity(self.global_best_position, self.w, self.c1, self.c2)
                particle.update_position(self.bounds)
            iterate_list.append(iteration+1)
            best_list.append(self.global_best_position)
            
                
				
            print(f"Iteration {iteration+1}/{self.max_iter} - Best Score: {self.global_best_score:.5f}")

        return self.global_best_position, self.global_best_score, iterate_list, best_list
	

