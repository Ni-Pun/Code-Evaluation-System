from django.db import models

# Create your models here.


class Problem(models.Model):
    Id = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 50, null = True, blank = True)
    Difficulty = models.CharField(max_length = 15,null = True, blank = True)
    Statement = models.TextField()
    InputDir = models.TextField(null = True, blank = True)
    OutputDir = models.TextField(null = True, blank = True)
    Constraints = models.CharField(max_length=150, null =True, blank = True)
    Example = models.TextField(null = True, blank = True)    
    

    def __str__(self):
        return (str(self.Id) + '.   ' + self.Name)

class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    verdict = models.CharField(max_length = 50)
    submittedAt = models.DateTimeField('Submitted At')
    usercode = models.TextField(null = True, blank = True)

    def __str__(self):
        return (str(self.problem))

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField(max_length = 200) 
    output = models.TextField(max_length = 200) 

    def __str__(self):
        return (str(self.problem))