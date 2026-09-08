from PID_class import PIDController

pid = PIDController(
    Kp=2.0,
    Ki=0.1,
    Kd=0.5,
    dt=0.1
)
pid.set_target(10)

pid.set_deadzone(0.01)

current_state = 0.0

for i in range(100):

    # Give PID the current state
    pid.update_feedback(current_state)

    # PID calculates control signal
    output = pid.compute()

    # Simulate physics
    current_state += output * 0.1

    # Calculate error for telemetry
    error = pid.target - current_state

    print(
        f"Step: {i:3d} | "
        f"Error: {error:8.3f} | "
        f"Output: {output:8.3f} | "
        f"State: {current_state:8.3f}"
    )