class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.roles = {}  # Dictionary to store roles and their messages
        self._lru = {}   # Dictionary to store roles and their last accessed time
        self._tick = 0   # Counter to track the last accessed time

    def get(self, role):
        if role in self.roles:
            self._lru[role] = self._tick  # Update last accessed time for the role
            self._tick += 1  # Increment the tick counter
            return self.roles[role]  # Return the message associated with the role
        return -1  # Return -1 if role not found

    def set(self, role, message):
        if role not in self.roles and len(self.roles) >= self.capacity:
            # If capacity is reached and role not present, find the oldest role based on last accessed time
            cur_oldest_role = min(self._lru, key=self._lru.get)
            self.roles.pop(cur_oldest_role)  # Remove the oldest role from roles dictionary
            self._lru.pop(cur_oldest_role)   # Remove the oldest role from LRU dictionary
        self.roles[role] = message  # Add or update the role with the message
        self._lru[role] = self._tick  # Update last accessed time for the role
        self._tick += 1  # Increment the tick counter

    def _complexity(self):
        return {
            'get': 'O(1)',   # Get operation complexity is constant time
            'set': 'O(N)',   # Set operation complexity is linear time, can be optimized to O(1)
            'space': 'O(N)'  # Space complexity is linear based on the number of roles
        }