FROM python:3.12-slim
COPY dice_simulator.py dice_simulator.py
ENV TZ="America/La_Paz"
CMD ["python", "dice_simulator.py"]