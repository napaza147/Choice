# Experimento cigarrillos: Parte II

```python
SESSION_CONFIGS = [
     dict(
        name='Quiz_1',
        display_name="Experimento_1.0",
        num_demo_participants=20,
            app_sequence=['Quiz_1', 'Choices', 'Quiz_2', 'Biases']
     ),
]
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)
PARTICIPANT_FIELDS=['non_smoker','e1','e2','e3','e4']
REAL_WORLD_CURRENCY_CODE = ''
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2
USE_POINTS = False
```
