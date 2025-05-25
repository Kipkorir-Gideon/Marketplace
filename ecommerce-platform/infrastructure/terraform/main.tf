provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "product_images" {
  bucket = "ecommerce-platform-product-images"
  acl    = "private"
}

resource "aws_rds_instance" "postgres" {
  identifier              = "ecommerce-platform-db"
  engine                 = "postgres"
  engine_version         = "13"
  instance_class         = "db.t2.micro"
  allocated_storage       = 20
  username               = "admin"
  password               = "your_password_here"
  db_name                = "ecommerce"
  skip_final_snapshot    = true
}

resource "aws_elasticsearch_domain" "product_search" {
  domain_name = "ecommerce-platform-search"
  elasticsearch_version = "7.10"

  cluster_config {
    instance_type = "t2.small.elasticsearch"
  }
}

resource "aws_sns_topic" "order_notifications" {
  name = "ecommerce-platform-order-notifications"
}

resource "aws_sqs_queue" "order_processing" {
  name = "ecommerce-platform-order-processing"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.product_images.bucket
}

output "rds_endpoint" {
  value = aws_rds_instance.postgres.endpoint
}

output "elasticsearch_endpoint" {
  value = aws_elasticsearch_domain.product_search.endpoint
}

output "sns_topic_arn" {
  value = aws_sns_topic.order_notifications.arn
}

output "sqs_queue_url" {
  value = aws_sqs_queue.order_processing.id
}