from diagrams import Diagram
from diagrams.aws.integration import SQS,SimpleQueueServiceSqsQueue, SimpleQueueServiceSqsMessage
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue, GlueCrawlers, GlueDataCatalog
from diagrams.custom import Custom
from diagrams.programming.language import Python
from pathlib import Path

HOME_PATH = f"{Path(__file__).parent.resolve()}"
CUSTOM_PATH = f"{HOME_PATH}/custom"
print(CUSTOM_PATH)
graph_attrs = {'fontsize': '45', 'bgcolor': '#e6ffff', 'labelfontsize': '20', 'nodesep': '1.0'}

with Diagram(name="Custom Local", show=True,graph_attr=graph_attrs):
    spotify_icon = Custom(label='spotify', icon_path=f'{CUSTOM_PATH}/spotify-200.png')
    sqs = SQS(label='SQS')
    sqs_message = SimpleQueueServiceSqsMessage(label='customer_id, secret_key')
    sqs_queue = SimpleQueueServiceSqsQueue(label='spotify_sqs_message')
    spotify_lambda = Lambda('spotify_lambda')
    spotify_s3 = S3('spotify_s3_storage')
    glue = Glue('Glue Service')
    crawler = GlueCrawlers(label='crawler')
    data_cat = GlueDataCatalog(label='data_catalogue')
    local_process = Python(label='Local Python Process')

    local_process >> sqs_message >> sqs_queue >> sqs >> spotify_lambda >> spotify_icon
    spotify_icon >> spotify_lambda >> spotify_s3
    spotify_s3 >> crawler >> glue >> data_cat




