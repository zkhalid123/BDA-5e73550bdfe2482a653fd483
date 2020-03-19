import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e73550bdfe2482a653fd484','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify')
	BDA_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e73550bdfe2482a653fd484", spark, "{'url': '/Demo/BankDepositTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi44999843da7d3a23cf90fd336c0bc37b', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e73550bdfe2482a653fd484','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e73550bdfe2482a653fd484','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify','http://23.99.85.149:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e73550bdfe2482a653fd485','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify')
	BDA_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e73550bdfe2482a653fd484"],{"5e73550bdfe2482a653fd484": BDA_DBFS}, "5e73550bdfe2482a653fd485", spark,json.dumps( {"FE": [{"transformationsData": {}, "feature": "age", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "40.81", "stddev": "11.84", "min": "19", "max": "93", "missing": "0"}}, {"transformationsData": {"feature_label": "job"}, "feature": "job", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "admin.", "max": "unknown", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "marital"}, "feature": "marital", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "divorced", "max": "single", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "education"}, "feature": "education", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "primary", "max": "unknown", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "default"}, "feature": "default", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "balance", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "1478.14", "stddev": "2876.75", "min": "-1415", "max": "51439", "missing": "0"}}, {"transformationsData": {"feature_label": "housing"}, "feature": "housing", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "loan"}, "feature": "loan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "contact"}, "feature": "contact", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "cellular", "max": "unknown", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "day", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "15.51", "stddev": "8.42", "min": "1", "max": "31", "missing": "0"}}, {"transformationsData": {"feature_label": "month"}, "feature": "month", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "apr", "max": "sep", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "duration", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "374.27", "stddev": "354.81", "min": "3", "max": "3076", "missing": "0"}}, {"transformationsData": {}, "feature": "campaign", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "2.61", "stddev": "2.89", "min": "1", "max": "32", "missing": "0"}}, {"transformationsData": {}, "feature": "pdays", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "53.94", "stddev": "110.21", "min": "-1", "max": "774", "missing": "0"}}, {"transformationsData": {}, "feature": "previous", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1162", "mean": "0.87", "stddev": "2.47", "min": "0", "max": "40", "missing": "0"}}, {"transformationsData": {"feature_label": "poutcome"}, "feature": "poutcome", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "failure", "max": "unknown", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "deposit"}, "feature": "deposit", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "1162", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0"}, "transformation": "String Indexer"}, {"feature": "job_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "1162", "mean": "2.78", "stddev": "2.68", "min": "0.0", "max": "11.0", "missing": "0"}}, {"feature": "marital_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.6", "stddev": "0.72", "min": "0", "max": "2", "missing": "0"}}, {"feature": "education_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.77", "stddev": "0.89", "min": "0", "max": "3", "missing": "0"}}, {"feature": "default_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.02", "stddev": "0.12", "min": "0", "max": "1", "missing": "0"}}, {"feature": "housing_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.48", "stddev": "0.5", "min": "0", "max": "1", "missing": "0"}}, {"feature": "loan_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.14", "stddev": "0.34", "min": "0", "max": "1", "missing": "0"}}, {"feature": "contact_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.34", "stddev": "0.59", "min": "0", "max": "2", "missing": "0"}}, {"feature": "month_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "1162", "mean": "2.99", "stddev": "2.94", "min": "0.0", "max": "11.0", "missing": "0"}}, {"feature": "poutcome_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.46", "stddev": "0.87", "min": "0", "max": "3", "missing": "0"}}, {"feature": "deposit_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "1162", "mean": "0.48", "stddev": "0.5", "min": "0", "max": "1", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e73550bdfe2482a653fd485','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e73550bdfe2482a653fd485','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify','http://23.99.85.149:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e73550bdfe2482a653fd486','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify')
	BDA_AutoML = tpot_execution.Tpot_execution.run(["5e73550bdfe2482a653fd485"],{"5e73550bdfe2482a653fd485": BDA_AutoFE}, "5e73550bdfe2482a653fd486", spark,json.dumps( {"model_type": "classification", "label": "deposit", "features": ["age", "job", "marital", "education", "default", "balance", "housing", "loan", "contact", "day", "month", "duration", "campaign", "pdays", "previous", "poutcome"], "percentage": "10", "executionTime": "5", "sampling": "0", "sampling_value": "none", "run_id": "d0d7f85b31ca45568d34b2fc5d0d5afb", "ProjectName": "ML Scenarios", "PipelineName": "BDA", "pipelineId": "5e73550bdfe2482a653fd483", "userid": "5e58ebb7957f3f13254389b5", "runid": "", "url_ResultView": "http://23.99.85.149:3200", "experiment_id": "2341748169460103"}))

	PipelineNotification.PipelineNotification().completed_notification('5e73550bdfe2482a653fd486','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e73550bdfe2482a653fd486','5e58ebb7957f3f13254389b5','http://23.99.85.149:3200/pipeline/notify','http://23.99.85.149:3200/logs/getProductLogs')
	sys.exit(1)

