import boto3
import time

polly_client = boto3.Session(
                aws_access_key_id='xx',
    aws_secret_access_key='11',
    region_name='us-east-1').client('polly')

response = polly_client.start_speech_synthesis_task(VoiceId='Vitoria',
                OutputS3BucketName='synth-books-buckets-fiap',
                OutputS3KeyPrefix='key',
                OutputFormat='mp3', 
                Text = 'Caro Aluno da FIAP! Vou exemplificar como posso me comunicar usando o Amazon Polly!')

taskId = response['SynthesisTask']['TaskId']

print "O Id da Tarefa he {} ".format(taskId)

task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)

print task_status
