From python:3.6
RUN mkdir poll
Add Django_polls poll
Add requirement.txt .
RUN pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR poll
CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]