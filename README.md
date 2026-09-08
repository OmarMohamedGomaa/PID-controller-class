# PID Controller

A simple Python class for implementing a PID controller.

## Initialization

**Syntax:**

```text
PIDController(Kp, Ki, Kd, dt)
```

## Methods

### Set Target

```text
pid.set_target(target)
```

Sets the desired target.

### Update Feedback

```text
pid.update_feedback(feedback)
```

Updates the current feedback value.

### Set Deadzone

```text
pid.set_deadzone(deadzone)
```

Sets the deadzone to ignore small errors.

### Compute

```text
pid.compute()
```

Calculates and returns the control output.

## Example

```python
pid = PIDController(1.0, 0.1, 0.05)

pid.set_target(100)
pid.update_feedback(80)
pid.set_deadzone(0.5)

output = pid.compute()
```
