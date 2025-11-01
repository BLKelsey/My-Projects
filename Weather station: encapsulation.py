class WeatherStation:
    def __init__(self, name, observations):               # Constructor: takes station name and a list of observations
        self.__name = name                                # Private attribute for station name
        self.__observations = observations                # Private attribute for storing all observations in a list

    def add_observation(self, observation):               # Method to add a new observation
        self.__observations.append(observation)           # Append observation to the list

    @property
    def latest_observation(self):                         # Property (getter) to return the most recent observation
        if self.__observations:                           # If there are observations in the list
            return self.__observations[-1]                # Return the last (latest) one

    @latest_observation.setter
    def latest_observation(self, observation):            # Property (setter) to add an observation
        self.__observations.append(observation)           # Works like add_observation

    @property
    def number_of_observations(self):                     # Property to count how many observations exist
        return len(self.__observations)

    @property
    def all_observations(self):                           # Property to return the entire list of observations
        return self.__observations

    def __str__(self):                                    # String representation of the object
        return f' {self.__name} has {self.number_of_observations} observations (Showers not displayed)'

# --- Main Program ---
station = WeatherStation("Houston", [])  # Create WeatherStation with empty list
station.add_observation("Showers")                        # Add first observation
print()
station.add_observation("Sunny")                          # Add second observation
print('First observation: ', station.latest_observation)  # Print latest (Sunny)

station.add_observation("Thunderstorm")                   # Add third observation
print('Second observation: ', station.latest_observation) # Print latest (Thunderstorm)

print('There are ', station.number_of_observations, ' observations')   # Show count
print('So,', station)                                                  # Uses __str__ method
