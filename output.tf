output "first_lambda" {
  value = "${aws_lambda_function.first_lambda.qualified_arn}"
}

output "api_gateway_ern" {
  value = "${aws_api_gateway_rest_api.api.execution_arn}"
}

output "api_gateway_invoke_url" {
  value = "${aws_api_gateway_deployment.MyDemoDeployment.invoke_url}${aws_api_gateway_resource.resource.path}"
}

output "api_gateway_stage_name" {
  value = "${aws_api_gateway_deployment.MyDemoDeployment.stage_name}"
}

output "api_gateway_stage_name_" {
  value = "${aws_api_gateway_resource.resource.path}"
}

